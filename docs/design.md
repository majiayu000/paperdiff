# paperdiff 设计

一句话：`paperdiff check <arXiv ID | paper.pdf | paper.tex 目录> <仓库 URL | 本地路径>`，逐条列出论文声明的实验设置与代码实际设置之间的差异，每条附双侧出处行号；`paperdiff rerun` 在用户显式开启、设好上限后，在用户自己的机器上跑一条命令，把日志里的数和论文里的数对比。

**它报告差异，不判断对错，更不判断作者是否有不端行为。** 调研（research.md 第 3 节）里多数"不一致"最后都有合理解释：论文报的是评测集，代码打印的是校准集加评测集；论文写的是近似形式，代码用的是小批量版本。

## 1. 语言选择：Python（uv）

| 需求 | Python | TS/bun |
|---|---|---|
| 解析目标仓库的代码（argparse、absl flags、hydra） | 标准库 `ast` 能精确解析 Python 源码并给出行号，零依赖 | 需要另找 Python 解析器（tree-sitter 等），行号和字面量求值都得自己处理 |
| YAML / hydra 配置 | PyYAML（带行号的 `compose_node`） | js-yaml 也可以 |
| PDF 文本抽取 | pypdf 纯 Python，按页给文本 | pdf.js 可用但较重 |
| LaTeX | 用正则 + 少量手写清洗即可；需要时有 pylatexenc | 生态较弱 |
| 复跑目标仓库 | 目标仓库几乎都是 Python，复跑本来就要 Python 环境 | 多一层语言 |

决定性的一条是第一行：被检查的代码本身是 Python，用 `ast` 读它比任何外部解析器都准。markitdown-rs 只做 DOCX/PPTX，没有 PDF，所以 PDF 不复用它，改用 pypdf。

依赖只有 `pyyaml` 和 `pypdf`；测试用 `pytest`。不调用任何 LLM API。

## 2. 总体流程

```
arXiv ID ──fetch──▶ LaTeX 源码（优先） / PDF（退路）──▶ paper 抽取 ──▶ Claim[]
repo URL ──git clone --depth 1──▶ 代码树 ──▶ code 抽取 ──▶ Setting[]
                                                    │
                                   align（按规范键对齐、数值归一化）
                                                    ▼
                                     Finding[]（match / conflict / missing / ambiguous）
                                                    ▼
                                         report.md + report.json
```

模块（每个一个文件，不做插件体系）：

| 文件 | 职责 |
|---|---|
| `fetch.py` | 取论文和仓库，本地缓存 |
| `keys.py` | 规范键表：每个键的同义词（论文侧短语、代码侧变量名）和值类型 |
| `values.py` | 数值与字符串归一化：`3e-4`、`$3\times10^{-4}$`、`10^{-5}`、`1k`、`5,000`、`0.1%` |
| `paper.py` | LaTeX/PDF → Claim[] |
| `code.py` | 仓库 → Setting[] |
| `align.py` | Claim[] × Setting[] → Finding[] |
| `report.py` | Markdown + JSON |
| `rerun.py` | 有上限的复跑 |
| `cli.py` | 命令行入口 |

## 3. 论文侧抽取

### 3.1 获取（遵守 arXiv 规则）

- 优先 LaTeX 源码：`https://export.arxiv.org/src/<id>`。arXiv 的 bulk data 说明要求程序化访问走 `export.arxiv.org`；API 使用条款要求"每 3 秒最多一个请求、单连接"，并允许为个人或研究用途获取和存储 e-print 内容。主站 `arxiv.org/robots.txt` 禁止 `/e-print`、`/src`，所以从不访问主站的这两个路径。
- 源码不可用（只有 PDF 的投稿）时，退到 `https://export.arxiv.org/pdf/<id>`。
- 每次运行最多 2 个请求（源码，必要时再取 PDF），两次请求之间至少间隔 3 秒，带上标明工具名和项目地址的 User-Agent；结果缓存在 `~/.cache/paperdiff/arxiv/<id>/`，命中缓存就不再联网。
- 不做批量抓取，不提供"按列表抓一批论文"的功能。
- 用户也可以直接给本地 `.tex` 目录、`.tar.gz` 或 `.pdf`，完全不联网。

### 3.2 LaTeX 处理

1. 找主文件：含 `\documentclass` 的 `.tex`；递归展开 `\input{}` / `\include{}`，但**不拼接**成一个字符串，而是保留每行的 `(文件, 行号)`，报告里的出处指向原始文件。
2. 去掉注释（未转义的 `%` 之后），保留行结构。
3. 两类候选：
   - **正文句子**：在同一段内，规范键的论文侧短语（如 "learning rate"、"batch size"、"warmup"、"weight decay"、"random seed"）后面一定窗口内出现的数值，或者 "Adam with β1 = 0.9" 这类写法。
   - **表格行**：`tabular` 环境里，第一个单元格匹配规范键短语，后续单元格是值。超参表通常是"参数名 & 值"或"参数名 & 任务1 & 任务2"两种形状，两种都拆成 Claim，后者每列一条并记下列头。
4. 附录与正文同等对待，Claim 记录所在的 `\section` 标题，方便人看。

### 3.3 PDF 退路

pypdf 逐页取文本，按行跑同一套短语 + 数值规则，出处记成 `paper.pdf:p<页>:L<行>`。PDF 里的表格会被拆成行，表格识别率明显差于 LaTeX，报告头部会注明"来源为 PDF，表格抽取不可靠"。

### 3.4 Claim

```json
{"key": "learning_rate", "value": 0.0003, "raw": "3\\times10^{-4}",
 "file": "sections/exp.tex", "line": 42, "section": "Experimental Setup",
 "context": "We use Adam with a learning rate of $3\\times10^{-4}$ ..."}
```

## 4. 代码侧抽取

只读，不执行目标代码，不 import 目标模块。

| 来源 | 方法 | 记为 |
|---|---|---|
| argparse `add_argument('--lr', default=...)` | `ast` 找 `add_argument` 调用，取第一个 `--` 选项名和 `default` 字面量 | `argparse_default` |
| absl / tf flags `flags.DEFINE_float('learning_rate', 5e-5, ...)` | `ast` 找 `DEFINE_*` 调用 | `flag_default` |
| 函数签名默认值 `def train(lr=1e-3)`、dataclass 字段 `lr: float = 1e-3` | `ast`，只收名字能映射到规范键的 | `code_default` |
| 直接调用 `torch.optim.Adam(params, lr=1e-3)`、`torch.manual_seed(42)`、`random.seed(0)`、`np.random.seed(0)` | `ast`，关键字参数或第一个位置参数 | `code_literal` |
| YAML（含 hydra 的 `conf/`、`config/`） | PyYAML 带行号展开为点号路径，如 `optimizer.lr`，取最后一段映射规范键 | `config` |
| JSON 配置 | 同上，行号用文本搜索回填 | `config` |
| README 里的代码块、`*.sh` 脚本中的命令 | 解析 `--flag value`、`--flag=value`、hydra 的 `key=value` | `command` |

**生效值优先级**：`command` > `config` > `argparse_default` / `flag_default` > `code_default` / `code_literal`。这是对常见写法的近似：README 命令覆盖 argparse 默认值，hydra 配置覆盖代码默认值。工具不去模拟真正的运行时合并（那需要执行代码），而是把所有候选值都列出来，并标出"按优先级推测生效的那一个"。

跳过目录：`.git`、`node_modules`、`venv`、`.venv`、`site-packages`、`third_party`、`tests`。

## 5. 对齐与差异分类

### 5.1 规范键

`keys.py` 里一张表，覆盖 ML 论文最常写、也最容易对不上的设置：

`learning_rate, batch_size, epochs, train_steps, warmup_steps, weight_decay, dropout, seed, optimizer, momentum, adam_beta1, adam_beta2, adam_epsilon, grad_clip, label_smoothing, max_seq_length, hidden_size, num_layers, num_heads, lr_schedule, num_gpus, dataset, train/val/test split`

每个键有：论文侧短语（正则）、代码侧名字（`lr`、`learning_rate`、`base_lr`、`train_batch_size`、`per_device_train_batch_size` 等）、值类型（float / int / str）。不在表里的设置不报，宁可漏报也不乱配。

### 5.2 值相等

- 数值：相对误差 ≤ 1e-6 视为相等；`1k`=1000，`1M`=1,000,000；百分比和 0～1 小数（dropout 10% 与 0.1）视为相等。
- 字符串（optimizer、schedule、dataset）：小写后去掉非字母数字，`AdamW` = `adamw`，`torch.optim.Adam` 取最后一段。

### 5.3 先定范围：这条声明对应哪些文件

一篇论文常有多个实验，各用各的脚本（Grokfast 有 `main.py`、`main_mnist.py`、`main_imdb.py`、`main_qm9.py`；LoRA 每个 GLUE 任务一个 `.sh`）。不先定范围，MNIST 的学习率就会去和 IMDb 的脚本比，产生大量假冲突。规则：

1. 取 Claim 的层级标题，从粗到细：`\section` → `\subsection` → 表格行组（如 "RoBERTa large LoRA"）→ 表格列头（如 "CoLA"）。
2. 每一层的标题拆成词（去掉 "experiments"、"details" 这类通用词，以及论文标题冒号前的方法名，如 "LoRA"），与仓库里每个"单元"（文件路径 + 命令启动的脚本名）做子串匹配，保留命中词最多的单元。
3. 某一层没有命中任何文件就停止，不再用更细的层（行组对不上时，单靠列头 "SST-2" 去配文件只是猜）。
4. 只命中非代码文件（例如方法同名的 `config/loss/dpo.yaml`）且这些文件里没有该键时，忽略这一层。
5. 没有任何一层命中时，优先比较"没被其他章节认领的文件"；这一兜底的证据较弱，见下表。

### 5.4 分类

对每个论文 Claim，在范围内同一规范键下找代码 Setting，按 §4 的优先级取最高一层的值作为"推测生效值"：

| 类别 | 条件 | 例子 |
|---|---|---|
| **一致 match** | 推测生效值只有一个，且等于论文值 | 论文 lr=1e-3，argparse 默认 1e-3 |
| **冲突 conflict** | 推测生效值只有一个且不等于论文值，范围有正面依据（标题命中，或整个仓库只有这一个值），且这个值不只是函数签名默认值 | DPO：论文 lr=1e-6，`config/config.yaml` 写 5e-7 |
| **模糊 ambiguous** | 以下任一：同一优先级有多个不同值（不论是否有一个等于论文值）；论文在同一处给出多个值（网格、"r=8 和 r=64" 的比较句）；论文值只出现在被覆盖的低优先级来源（例如等于 argparse 默认值，但 README 命令改成了别的）；范围只来自兜底；唯一的值是函数签名默认值 | BERT SQuAD：论文 lr=5e-5，README 命令 `--learning_rate=3e-5` |
| **缺失 missing_in_code** | 范围内找不到该键 | Grokfast QM9 写 50k 次迭代，`main_qm9.py` 用公式算 epoch 数，没有这个参数 |
| **缺失 missing_in_paper** | 代码里有 `seed / learning_rate / batch_size / epochs|train_steps / optimizer` 这几个核心键，论文全文没有提到 | Grokfast、DPO 代码固定了 seed，论文没写种子 |

冲突的门槛刻意定得高：宁可把不确定的情况放进"模糊"，也不让"冲突"一栏出现假阳性。

"缺失"是最常见也最不确定的一类：代码可能用了别的名字，论文可能写在补充材料里。报告里它排在冲突和模糊之后。

每条 Finding 都带：类别、规范键、论文侧 `{值, 原文, 文件:行, 上下文}`、代码侧候选列表 `[{值, 来源类型, 文件:行, 原文行}]`、推测生效值。

## 6. 报告格式

`paperdiff check ... -o out/` 生成：

- `out/report.md`：头部是输入（论文 ID/版本、仓库 URL 和 commit、生成时间、paperdiff 版本）和统计；然后按 冲突 → 模糊 → 缺失 → 一致 的顺序分节，每条一张小表，论文出处和代码出处都写成 `path:line`，仓库出处附 GitHub permalink（`blob/<commit>/path#L<line>`）。末尾固定附免责声明。
- `out/report.json`：同样内容，结构见 `paperdiff/report.py` 中的 `to_json`。顶层有 `schema_version`。

## 7. 按预算复跑

### 7.1 边界

- **默认不跑。** `paperdiff check` 永远不执行目标代码。只有 `paperdiff rerun` 会执行，并且必须同时满足：命令行带 `--allow-run`，且 spec 里有 `budget.timeout_s`。缺任一条直接报错退出。
- **只在用户的机器或用户自己准备的沙箱里跑。** paperdiff 不提供远程执行、不上传代码。想隔离就由用户在容器里运行 paperdiff 本身。
- **上限**：
  - 时间：`timeout_s` 到时间就杀掉整个进程组，结果记为 `timeout`。
  - GPU：`gpus: 0` 时设 `CUDA_VISIBLE_DEVICES=""`；`gpus: N` 时只暴露前 N 张。
  - token：paperdiff 自己不调 LLM。由 agent（例如 Claude Code）来决定"跑哪几个数、命令怎么写"时，token 上限交给 agent 自己的机制（例如 `claude -p --max-budget-usd`），paperdiff 只把这个预算写进复跑记录，便于审计。
- 命令以参数列表执行（不经过 shell），工作目录限定在仓库目录内。

### 7.2 Spec

```yaml
repo: ./grokfast            # 本地仓库路径
command: ["python", "main.py", "--label", "x", "--filter", "ema"]
budget: {timeout_s: 900, gpus: 0, tokens: null}
targets:
  - name: steps_to_95_val_acc
    paper: {value: 400, source: "paper.tex:120"}
    metric: {file: "results/x.log", regex: "val_acc=0\\.95 at step (\\d+)"}  # 或者从 stdout 里匹配
    tolerance: {rel: 0.25}
```

### 7.3 输出

每个 target 一条：`reproduced`（落在容差内）/ `differs` / `not_found`（日志里没有匹配到）/ `timeout` / `failed`（非 0 退出码），附测得值、论文值、相对偏差、耗时、命令、日志尾部 50 行，写成 `rerun.md` / `rerun.json`。

### 7.4 agent 怎么用

仓库自带 `skills/paperdiff/SKILL.md`：agent 先跑 `paperdiff check`，再从报告里挑 1～3 个能在预算内跑完的关键数（优先 CPU、小数据集），写 spec，向用户展示 spec 和预算并取得同意后再运行 `paperdiff rerun --allow-run`。

## 8. 局限声明（报告里固定附上）

1. paperdiff 只报告**差异**。差异可能来自论文笔误、代码在论文发表后更新、配置写在别处、合理的实现近似，或工具自身的抽取错误。它不判定论文对错，更不判定作者是否有学术不端。
2. 只覆盖规范键表里的设置。方法层面的不一致（公式、模块顺序、损失定义）不在范围内，research.md 里一半的真实案例属于这一类。
3. 代码侧的"生效值"是按优先级推测的，不是运行时真实值。
4. PDF 来源的表格抽取不可靠。
5. 复跑结果受硬件、随机种子、依赖版本影响；一次复跑对不上，不能说明论文结果不可复现。
6. 公开使用报告时请只发聚合统计，或先联系作者，不要单凭工具输出点名指责。

## 9. 不做的事

- 不做批量抓取、不做榜单、不点名排行。
- 不用 LLM 生成"结论"。
- v0 不做 claimcheck（引用是否支持论断）和 numtrace（数字溯源），见选题文档。
