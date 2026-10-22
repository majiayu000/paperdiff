# paperdiff 调研（2026-10-22）

结论先行：**"论文写的设置"和"代码实际生效的设置"之间的逐条比对，目前没有可直接用的开源工具。** 最接近的三样东西是：

- 学术数据集 SciCoQA（ACL 2026，UKPLab，7★）：证明了问题真实存在，并测出最好的 LLM 也只能找出 46.7% 的真实差异；但它是数据集和评测代码，不是给人用的工具。
- asech109/claimcheck（0★，2026-05 后无更新）：核对**作者自己的** LaTeX 和自己的 config/日志，不处理 arXiv 下载、argparse 默认值和 README 命令，也不跑代码。
- 各种 "paper → code" agent（Paper2Code 4,996★、PrathamLearnsToCode/paper2code 1,536★）和 PaperBench：方向相反，是从论文**生成**代码，或评测 agent 复现论文的能力，不核对作者已经发布的代码。

审稿现场的需求是真实的：下文列出 10 条 ICLR/NeurIPS 公开评审里审稿人亲手比对代码、发现不一致的记录。

所有数字均为 2026-10-22 实查。GitHub 数字来自 `gh api search/repositories`，OpenReview 案例来自 `api2.openreview.net/notes/search` 的全文检索。

## 1. 查重：拆词搜索

| 关键词组 | GitHub total | 相关结果 |
|---|---|---|
| `paper code consistency` | 233 | 只有 2 个相关：asech109/claimcheck 0★、Dhanu577/rpapercodeaudit 0★（R/Bioconductor 标注助手）；其余是各论文的官方仓库 |
| `paper code alignment` | 580 | UKPLab/scicoqa 7★，其余无关 |
| `paper code mismatch hyperparameter` | 0 | — |
| `paper vs code audit` | 4 | 均 0★ |
| `reproducibility check paper repository` | 5 | 均无关或 0★ |
| `hyperparameter extraction paper latex` | 0 | — |
| `arxiv latex hyperparameter extraction` | 0 | — |
| `paper config diff` | 3 | 无相关 |
| `paper reproducibility audit hyperparameters` | 0 | — |
| `ml reproducibility checker` | 2 | midnightoatmeal/42-ML_reproducibility_checker 0★（Streamlit，NLP 实体比对，只看"数据集链接"和"方法名"） |
| `reproduce paper agent` | 231 | 前几名均 0★ 的个人练习 |
| `paper2code` | 155 | going-doer/Paper2Code 4,996★、PrathamLearnsToCode/paper2code 1,536★、issol14/paper2code-skill 42★ |
| `research code audit llm` | 60 | kennethkhoocy/applied-micro-skills 22★（经济学复现审计 skill）、LARi-UQAC/ResearchTools 14★ |
| `paper implementation discrepancy` | 20 | 全部是"discrepancy"作为数学概念的论文实现，无关 |

## 2. 功能矩阵

图例：✅ 有；◐ 部分；✗ 无。

| 工具 | 类型 | 输入 arXiv/PDF | 读 LaTeX 源码 | 读代码 config/argparse/yaml | 逐条差异 + 出处行号 | 按预算实跑 | 开源 CLI | 备注 |
|---|---|---|---|---|---|---|---|---|
| **paperdiff（本项目）** | CLI | ✅ | ✅ 优先 | ✅ | ✅ | ✅ 默认关闭，需显式开启 | ✅ | 只报差异，不下结论 |
| [UKPLab/SciCoQA](https://github.com/UKPLab/scicoqa)（ACL 2026） | 数据集 + LLM 评测 | ✅ PDF | ✗ | ◐ 把整个仓库塞给 LLM | ◐ 自由文本描述 | ✗ | ✗（研究代码） | 92 条真实 + 543 条合成差异；22 个模型最好只找出 46.7% 的真实差异（[arXiv 2601.12910](https://arxiv.org/abs/2601.12910)）。可以当 paperdiff 的评测集 |
| [asech109/claimcheck](https://github.com/asech109/claimcheck) 0★ | CLI | ✗ 本地 .tex | ✅ | ◐ 读 config 和日志里的数 | ✅ file:line | ✗（明确不执行代码） | ✅ | 面向作者自查；不追 argparse 默认值 |
| [42-ML_reproducibility_checker](https://github.com/midnightoatmeal/42-ML_reproducibility_checker) 0★ | Streamlit | ✅ PDF | ✗ | ◐ 只找数据集链接、方法名 | ✗ | ✗ | ◐ | 无超参层面比对 |
| [Dhanu577/rpapercodeaudit](https://github.com/Dhanu577/rpapercodeaudit) 0★ | 标注助手 | 纯文本 | ✗ | ◐ R 包 | ◐ 草稿，需人工勾选 | ✗ | ✅ | 仅 R/Bioconductor |
| [Paper2Code / PaperCoder](https://github.com/going-doer/Paper2Code) 4,996★（ICLR 2026） | 多 agent 代码生成 | ✅ | ✅ | ✗（生成新代码） | ✗ | ✗ | ✅ | 方向相反 |
| [PrathamLearnsToCode/paper2code](https://github.com/PrathamLearnsToCode/paper2code) 1,536★ | agent skill | ✅ arXiv | ◐ | ✗（生成新代码） | ◐ 生成代码里标注 §出处 | ✗ | ✅ | README 有"ambiguity audit"一步，但审的是论文本身的含糊处 |
| [PaperBench](https://github.com/openai/preparedness)（OpenAI） | 评测基准 | — | — | — | — | agent 从零复现 | ✅ | 20 篇 ICML 2024 论文、8,316 个评分项，最好的 Claude 3.5 Sonnet (New) 平均复现分 21.0%（[arXiv 2504.01848](https://arxiv.org/abs/2504.01848)） |
| [CORE-Bench](https://arxiv.org/abs/2409.11363) | 评测基准 | — | — | — | — | agent 跑作者代码 | ✅ | 指出 MLRC 2022 中 28 篇附代码和数据的论文只有 18 篇能完整复现 |
| [MLReplicate](https://arxiv.org/abs/2605.16616) | 评测基准 | — | — | — | — | 自主科研系统复现 | — | ICML 2025 杰出论文，6 个系统 |
| [paperswithcode.co](https://paperswithcode.co/)（HF 于 2026 年复活） | 网站 | ✅ | ✗ | ✗ | ✗ | ✗ | ✗ | 首页实查：趋势论文、任务、方法、数据集浏览；没有任何复现或一致性检查 |
| [ML Reproducibility Challenge](https://blog.neurips.cc/2026/05/04/mlrc-2026-reproducibility-as-an-official-track-at-neurips/) | 社区活动 | — | — | — | — | 人工复现 | — | 2026 年起成为 NeurIPS 官方 track；未找到官方推荐的自动化工具 |
| [tjhavranek/paper-workshop (CRUCIBLE)](https://github.com/tjhavranek/paper-workshop) 11★ | Claude Code skill | ✅ | ◐ | ◐ | ◐ 审稿意见带引文 | ✅ 重跑作者代码 | ✅ | 定位是"对抗式审稿 + 改稿"，范围宽，经济学取向 |
| [Agentic Reproducibility Assessment](https://arxiv.org/abs/2605.02651) | 研究原型 | ✅ | — | — | ◐ 工作流图 | ◐ | — | 在 213 篇 ReScience C 文章上约 61% 准确率（据 StartupHub 二手报道） |
| ["Review the Code, Not the Story"](https://arxiv.org/abs/2606.07683) | 立场论文 | — | — | — | — | 提议 | — | 提议由会议控制的 AI 构建环境、跑实验、把论断连到证据；只是提案 |
| AAAI 2026 AI 审稿试点 | 会议试点 | — | — | — | — | — | — | 通用 AI 审稿，不针对代码 |

**空白**：没有一个工具同时做到 (a) 直接吃 arXiv ID 拿 LaTeX 源码，(b) 把 argparse/yaml/hydra/README 命令解析成"实际生效值"，(c) 逐条给出双侧出处行号，(d) 复跑默认关闭、带硬上限。SciCoQA 的结论（LLM 整体检出率低，最难的是"论文省略了细节"）说明：把整篇论文加整个仓库直接丢给 LLM 效果不好；先做确定性的结构化抽取，再把 LLM 用在窄处，更可能做得准。

## 3. OpenReview 上审稿人抱怨"论文与代码不一致"的真实案例

检索方式：`api2.openreview.net/notes/search`，type=terms，词组包括 "inconsistent with the code"、"paper and the code"、"in the provided code"、"in the released code"、"code is inconsistent"，只保留 ICLR/NeurIPS 的记录。下表为人工逐条读过的命中，按差异类型归类（对应 paperdiff 的检查项）。

| # | 会议 | 记录 | 差异类型 | 审稿人指出的问题（转述） |
|---|---|---|---|---|
| 1 | ICLR 2025 | [Sub4973 评论](https://openreview.net/forum?id=o0DQDGaVIY&noteId=ef6pbQnW5q) | 训练设置 | 论文写 8 卡分布式训练，提供的入口脚本却是 `--gpu_id 0` 单卡，`--local_rank` 参数被注释掉；审稿人称这种不一致让复现白费时间 |
| 2 | ICLR 2026 | [Sub11231 评审](https://openreview.net/forum?id=YDl4vqQqGP&noteId=pog7d1pEPA) | 数据划分 | 指出 `exp/exp_classification.py` 第 22–25 行把测试集当验证集用，构成测试集泄漏 |
| 3 | ICLR 2026 | [Sub21616 评审](https://openreview.net/forum?id=LlhiiTg9ux&noteId=wf01SA8CHN) | 方法/公式 | 专设一节"论文与代码不一致"，逐条对比论文 3.2 节的 lambda 权重定义与代码实现 |
| 4 | ICLR 2026 | [Sub16019 评审](https://openreview.net/forum?id=6c2h6mZVfu&noteId=WRJ91II74S) | 方法/顺序 | 论文说 RoPE 在脉冲之前施加，发布的代码里 Q/K 先过 LIF 再做 RoPE |
| 5 | ICLR 2026 | [Sub20582 评论](https://openreview.net/forum?id=Ys2OgNLNV7&noteId=hJ46isLnY4) | 结果数字 + 提示词 | 代码 notebook 输出的数字和表 2 对不上；图 1 写的提示词前缀在代码里没有。作者回复：代码输出的是校准集加评测集，论文只报评测集 |
| 6 | ICLR 2026 | [Sub14216 评审](https://openreview.net/forum?id=kdAFb1lljm&noteId=GwAN18Nxux) | 整体 | 补充材料代码与正文不一致且不完整，无法复现 |
| 7 | ICLR 2026 | [Sub11576 评审](https://openreview.net/forum?id=SdLqXlO2Ur&noteId=YtFRJ3lX45) | 超参缺失（模糊） | 式 4、9、10 的多个超参论文没给，代码里也很难找到 |
| 8 | ICLR 2025 | [Sub13743 Meta-review](https://openreview.net/forum?id=f6GMwpxXHG&noteId=dcQhbPG1Km) | 方法 | AC 在拒稿理由中列出"论文方法与所给代码不一致" |
| 9 | ICLR 2024 | [Sub3768 评审](https://openreview.net/forum?id=ztuCObOc2i&noteId=OPYpDioiBD) | 方法/优化 | 附录 A 说用随机优化求熵势，代码实际做法不同；作者在[回复](https://openreview.net/forum?id=ztuCObOc2i&noteId=7eIr01E8xJ)中解释为小批量近似 |
| 10 | NeurIPS 2025 | [Sub26011 Decision](https://openreview.net/forum?id=IUYAqr7qDA&noteId=QciHg8aqbL) | 方法图 | AC 总结里提到图 3 与代码不一致（dummy/text token、k/v 的用法），rebuttal 后已解决 |

补充观察：

- 第 5、9 条里，作者都给出了合理解释。所以工具只能报"差异"，不能报"错误"；这一点写进了 design.md 的局限声明。
- 第 1、2 条（GPU 数、数据划分）和第 7 条（超参缺失）是可以用结构化抽取自动发现的；第 3、4、8、9、10 条属于"方法语义不一致"，需要读懂代码逻辑，静态规则做不到，这是 paperdiff 第一版明确不做的范围。
- ICLR 2026 在 2025 年底出过 OpenReview 安全事件并回滚过部分评审（[ICLR 官方说明](https://blog.iclr.cc/2025/12/03/iclr-2026-response-to-security-incident/)），上表链接 2026-10-22 均可访问。

## 4. 对设计的影响

1. **先确定性抽取，后 LLM**。SciCoQA 显示整篇丢给 LLM 的检出率不到一半；paperdiff v0 只做确定性抽取（LaTeX 表格/段落正则 + Python AST + YAML），所有结论都有字面出处，不需要 API key 也能跑。
2. **"代码侧实际生效值"是核心难点**。案例 1 的问题出在启动脚本参数覆盖默认值，所以要同时解析 argparse 默认值、yaml、README 里的命令行和 shell 脚本里的 `--flag value`，并按优先级标出"哪个值最终生效"。
3. **三类差异**：冲突（双方都有且不同）、缺失（论文写了代码找不到，或代码关键参数论文没写）、模糊（同名参数在代码里有多个不同值，无法判断哪个生效）。案例 7 就是"模糊/缺失"。
4. **复跑默认关闭**。CORE-Bench 和 PaperBench 都说明 agent 复现成本高、成功率低；paperdiff 只在用户机器上、显式开启、带时间上限时跑用户指定的命令，然后把日志里的数字和论文对比。

## 5. 局限

- OpenReview 全文检索只按词组命中，未覆盖中文或换一种说法的评审；案例是"存在性证据"，不代表比例。
- paperswithcode.co 的功能只看了首页（WebFetch），HF 官方博客原文未找到。
- ARA 的 61% 准确率来自二手报道，未读原论文全文。
