# 发布与推广计划（草案，等用户确认后执行）

当前状态：本地 git 仓库，未建远程、未 push、未发布任何内容。下面每一步都需要用户确认。

## 1. 发布前需要用户决定的事

| # | 事项 | 当前默认 | 说明 |
|---|---|---|---|
| 1 | 仓库名与可见性 | `majiayu000/paperdiff`，public | 2026-10-22 实查：`majiayu000/paperdiff` 不存在；GitHub 上同名项目 4 个均 0★（manyapn/paperdiff 做的是"研究论断是否冲突"，Obsessus/PaperDiff 做论文并排对比，都不涉及代码）；PyPI `paperdiff` 返回 404，可用 |
| 2 | 许可证 | MIT（已加 LICENSE） | 依赖 pypdf（BSD）、PyYAML（MIT），无冲突 |
| 3 | 是否发 PyPI | 暂不发，README 写的是 `uv tool install git+https://github.com/majiayu000/paperdiff` | 发的话 `uv build && uv publish`，需要 PyPI token（用户自己操作） |
| 4 | 示例里点名的 4 篇论文 | 保留（都是 2018–2024 年的经典论文，差异已人工核实，并标注了 README 自己承认的差异和误配） | 若希望更保守，可只保留统计、去掉具体条目 |
| 5 | 是否去 microsoft/LoRA#37、ironjr/grokfast#16 留言补充证据 | 不留言 | 留言属于外部发布动作；如果要留，只陈述"paper 表格第 X 行 vs 脚本第 Y 行"，不带评价 |
| 6 | README 语言 | 英文 | 中文圈推广可另写一篇文章，不改 README |

## 2. 发布步骤（用户已批准公开；自动执行被权限策略拦下，需用户本人运行或放行）

```bash
cd paperdiff
gh repo create majiayu000/paperdiff --public --source . --push \
  --description "Paper vs code consistency checker for ML reproducibility: compare hyperparameters, data splits and seeds in an arXiv paper with its GitHub code, line by line."
gh repo edit majiayu000/paperdiff --homepage https://majiayu000.github.io/paperdiff/ \
  --add-topic reproducibility --add-topic machine-learning --add-topic ml-research --add-topic arxiv \
  --add-topic hyperparameters --add-topic research-tools --add-topic peer-review --add-topic replication \
  --add-topic latex --add-topic deep-learning --add-topic code-review --add-topic static-analysis \
  --add-topic python --add-topic cli --add-topic paper-implementation --add-topic open-science
gh api -X POST repos/majiayu000/paperdiff/pages -f 'source[branch]=main' -f 'source[path]=/docs'
gh run watch --repo majiayu000/paperdiff --exit-status $(gh run list --repo majiayu000/paperdiff -L1 --json databaseId -q '.[0].databaseId')
git tag -s v0.1.0 -m "paperdiff 0.1.0" || git tag -a v0.1.0 -m "paperdiff 0.1.0"
git push origin v0.1.0
gh release create v0.1.0 --repo majiayu000/paperdiff --title "paperdiff 0.1.0" --notes-file docs/release-notes-0.1.0.md
```

社交预览图（docs/social-preview.png，1280×640）只能在网页上传：仓库 Settings → General → Social preview → Edit → Upload。

PyPI（不在本次范围，2026-10-23 实查 `https://pypi.org/simple/paperdiff/` 返回 404，名字可用）：

```bash
uv build && uv publish   # 需要用户本人的 PyPI token
```

## 3. 借 ICLR 2027 讨论期推广（11-05～11-18）

日期依据：ICLR 2027 官方日期页，审稿 11-05 放出，作者讨论期 11-05～11-18（选题文档信号 #8）。

原则：只发工具和聚合统计；不点名任何在审论文；不在 OpenReview 上发表任何内容；不替任何人写审稿意见或 rebuttal。

| 时间 | 动作 | 产出 |
|---|---|---|
| 10-23～11-01 | 用户确认后发布仓库；补 2～3 篇近年热门论文的示例（同样只用已发表论文） | 仓库 + examples |
| 11-02～11-04 | 写一篇"复现前先跑 paperdiff"的短文：以 LoRA α 8 vs 16（issue #37 已公开讨论 3 年）为例，讲清"差异 ≠ 错误"，附 BERT README 自己承认差异的反例 | 博客 / 知乎 / 小红书草稿，发前给用户过目 |
| 11-05～11-18 | 面向作者（rebuttal 期间自查 camera-ready 的代码是否和论文一致）和审稿人（核对作者提供的代码）推广；渠道：HN Show HN、r/MachineLearning、X、中文社区 | 帖子文字发前给用户确认 |
| 讨论期内（可选） | 对一批**已公开到 arXiv 且附代码**的 ICLR 2027 投稿跑静态检查，只发聚合统计（例如"N 篇里 X% 至少有一处学习率与代码不同"），不列论文名；arXiv 抓取遵守每 3 秒 1 次、单连接，规模控制在几十篇 | 统计图 + 方法说明 |

风险与对策：

- **误报伤口碑**：所有公开示例都人工核对过；"冲突"门槛设得高（见 design.md §5.4），帖子里明确写出已知误配（DPO 的 reward model epochs）。
- **被当成"打假工具"**：帖子和 README 第一屏都写"只报差异，不下结论"；不提供批量排名功能。
- **竞品**：最接近的是 SciCoQA（数据集，7★）和 asech109/claimcheck（0★）。宣传点是"单命令、arXiv 直取、双侧行号、复跑默认关闭"。
