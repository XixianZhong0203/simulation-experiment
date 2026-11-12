你的直觉得到现有文献的有力支持。在人机交互关于主动式 AI 的研究中，“帮助 vs 打断”的二元性被反复观察到，而支撑它的正是你提出的两个维度。

第一，建议时机是否恰当（即用户当时是否需要帮助）。"Assistance or Disruption? Exploring and Evaluating the Design and Trade-offs of Proactive AI Programming Support"（DOI: 10.1145/3706598.3713357）评估了主动编程助手 Codellaborator，发现相比被动提示模式，主动建议提高了效率，但同时带来工作流打断；作者强调需要让主动性适配用户当下的任务进程。ProMemAssist（DOI: 10.1145/3746059.3747770）把这一思想落成系统：实时建模用户工作记忆，用时机预测模块权衡“帮助的价值”与“打断的成本”，结果比 LLM 基线提供更克制的帮助、用户参与度更高。"Interrupting for Microlearning: Understanding Perceptions and Interruptibility of Proactive Conversational Microlearning Services"（DOI: 10.1145/3613904.3642778）和 LlamaPIE（DOI: 10.18653/v1/2025.findings-acl.710）也分别强调通过情境信号和“何时响应”的决策来避免打扰。

第二，建议是否容易跳过、用户能否保留控制权。"Proactive AI as a Catalyst for Creativity? Balancing Human Agency and AI Contribution in Collaborative Story Writing"（DOI: 10.1145/3772318.3790848）对比了侵入式建议（直接补全下一句）与非侵入式建议（提供探索性提案），发现侵入式建议虽然也能提升产出，但显著削弱用户的主体感；建议是否“可被搁置”是核心体验变量。上述编程研究同样发现，加入存在指示器和交互上下文可以减轻打断，因为它让用户感知到对 AI 过程的控制。

综上，你猜的两个差异来源——“用户当时是否需要帮助”和“建议能否被轻松跳过”——恰好对应文献中主动式 AI 的两条主线：时机的恰当性（timing appropriateness）与建议的可回避性/可控性（dismissibility and user control）。这二者可以作为你研究的设计假设，并通过操纵触发时机与呈现形式（如侵入式 vs 非侵入式、带/不带状态指示）的实验加以验证。
