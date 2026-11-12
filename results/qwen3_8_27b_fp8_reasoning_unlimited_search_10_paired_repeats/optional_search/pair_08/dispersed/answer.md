你的直觉其实可以形式化成一个「时机匹配 × 中断成本」的调节模型：主动式 AI 建议是帮助还是干扰，取决于两个变量——建议出现的时刻是否与用户当下的任务需求匹配（需要帮助 vs. 正沉浸在自己的流程里），以及建议带来的中断成本是否足够低（能否轻松跳过、稍后回来、或保持原有上下文）。这个框架在现有文献里都有对应的支撑证据。

第一，主动支持确实有「帮」与「扰」两面。在 Assistance or Disruption? Exploring and Evaluating the Design and Trade-offs of Proactive AI Programming Support（DOI: 10.1145/3706598.3713357）中，作者用 Codellaborator 这个基于编辑器和任务上下文主动发起协助的 LLM 智能体做对比实验，发现主动智能体比纯提示（prompt-only）模式更高效，但会引发工作流中断；加入「存在指示器」和交互上下文后，中断被缓解、用户对 AI 过程的感知也更好。该文还指出了用户控制权、归属感和代码理解上的权衡，并明确主张「让主动性适应编程过程」——这几乎就是你要检验的「用户当时需不需要帮助」假设。

第二，可控性（可退出性）是关键的设计变量。Beyond Automation: How Designers Perceive AI as a Creative Partner in the Divergent Thinking Stages of UI/UX Design（DOI: 10.1145/3706598.3713500）发现，设计师看重的是对构思过程的控制权、协作感和效率提升，只有当用户能随时接管时，AI 才被视为「伙伴」而不是干扰源。这与你的第二个猜想一致：能不能轻松跳过建议，决定它被体验为帮助还是打断。

第三，「需不需要帮助」不是客观状态，而是个体差异下的主观判断。Selective Trust: Understanding Human-AI Partnerships in Personal Health Decision-Making Process（DOI: 10.1145/3706598.3713462）发现，信任受个体决策风格和个性化推荐程度的调节，AI 建议需要与个人的决策偏好对齐才有效。类似的，Everyday Uncertainty: How Blind People Use GenAI Tools for Information Access（DOI: 10.1145/3706598.3713433）显示用户会带着怀疑态度、把 AI 输出当作「暂定信息」来主动筛选——说明用户必须保有过滤和主导权，建议才能被吸收而非造成混乱。

落到研究设计上，你可以把「主动性时机」和「建议显著度/可忽略成本」作为自变量，设计不同界面变体（如高显著推送 vs. 低显著、一键忽略、带存在指示），在任务流程的不同阶段测量建议接受率、任务绩效、中断恢复时间和主观打扰感，检验「需要 × 可退出性」的交互效应。Codellaborator 中「上下文与存在指示缓解中断」的发现，以及 UI/UX 设计师研究中「控制权决定 AI 是否被视为伙伴」的结论，都可以直接作为你的设计假设和评估维度。
