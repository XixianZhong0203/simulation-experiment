# Simulation Experiment A

两组都可以检索同一份本地论文库。实验仅替换每轮随附的 5 篇论文。两组的 10 篇从背景库统一排除，模型、任务、排序规则和检索预算在一对内一致。

## OpenCode 接入

1. 在 OpenCode 里接通提供商，拿到完整模型 ID（例如你在 OpenCode 里选中的 provider/model）。连接设置请放在 OpenCode 的用户配置中。实验使用临时目录和独立的 OpenCode 进程，不读取其他项目的配置。
2. 用 OpenCode v2 和带 SQLite FTS5 的 Python 3.11 或更新版本。在本目录运行：

   ```sh
   python3 run.py --check
   python3 run.py --model 'provider/model'
   ```

   可用 `EXPERIMENT_A_MODEL` 环境变量代替 `--model`。如 Excel 移动了，用 `--workbook "/绝对路径/文件.xlsx"`。第二对可用 `--dispersed-first` 交换运行顺序。

   已验证可跑通的接入示例（provider 定义在 OpenCode 用户配置中）：

   ```sh
   python3 run.py --model 'litellm/Qwen3.8-27B-FP8-reasoning'
   ```

模型由 `run.py` 中的 `call_model()` 调用。只需接入 OpenCode 并传入模型 ID，无需改实验代码或把凭证填进本目录。OpenCode 会将模型输入发给你选的模型提供商。

仓库包含两组各 5 篇的实验材料。运行时另需提供原始 Excel 论文库。

## 检索与结果

- 本地索引检索原摘要。模型自行决定是否检索并写出英文查询。默认最多三次、每次最多六个结果。所有索引记录都可以命中。检索用 SQLite FTS5 关键词匹配和 BM25 排序。
- 每一步使用独立的 OpenCode 会话，程序重传同一个任务、当轮 5 篇及已经取得的检索结果。实验专用代理拒绝 OpenCode 工具，检索由程序单独执行。模型自身的已有知识仍可能出现在回答中。
- `runs/` 下每一对保存 `run.json` 和 `comparison.json`，各组保留模型输入、原始事件、检索记录和 `answer.md`。
- `review.json` 自动列出可按 DOI 或完整标题识别的引用。实际使用数由评分者对照摘要填写，引用 ID 和摘要确实支持观点要分别核对。可在 `idea_alignment_notes` 记录是否回应「何时需要帮助」和「能否轻松跳过」、新增观点如何连接原问题，以及是否把猜想写成定论。
