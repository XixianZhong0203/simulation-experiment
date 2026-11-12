你的初步想法——AI 主动建议有时能帮人继续做下去、有时反而打断思路，且差别可能在于"当时是否需要帮助"和"能否轻松跳过建议"——与论文库中几项研究直接呼应，可以沿着两条主线来组织这段讨论。

第一，"何时该给建议"（需求判定/时机）。ProMemAssist（DOI: 10.1145/3746059.3747770）通过实时建模用户的短时记忆来预测介入时机，其核心正是一个在"帮助的价值"与"打断的成本"之间做权衡的 timing predictor，这与你的第一个猜测高度一致。LlamaPIE（DOI: 10.18653/v1/2025.findings-acl.710）则把"何时回应"显式拆成一个独立的小模型问题来解决，追求不打断对话的克制式辅助；用户实验显示人们明显更偏好这种主动但克制的助手，而非无辅助或纯被动基线。

第二，"能否轻松跳过/打断成本是否低"（可弃用性）。Codellaborator 论文（"Assistance or Disruption? Exploring and Evaluating the Design and Trade-offs of Proactive AI Programming Support", DOI: 10.1145/3706598.3713357）的受试者研究发现，主动 agent 虽提升了效率，却也带来 workflow disruption；而加入 presence 指示与交互上下文后，用户掌控感和对 AI 过程的觉察度提高，打断感被缓解——这正指向"建议是否容易被识别为可跳过、可回归原任务"这一点。"Need Help? Designing Proactive AI Assistants for Programming"（DOI: 10.1145/3706598.3714002）进一步指出，编程这一共享工作区让建议更相关，从而影响其采纳与忽略，即可弃用性取决于建议与当前任务的耦合程度。"Interrupting for Microlearning: Understanding Perceptions and Interruptibility of Proactive Conversational Microlearning Services"（DOI: 10.1145/3613904.3642778）则从可打断性（interruptibility）角度，识别出决定数分钟级建议能否被自然接受的关键情境因素，进一步支持你把"跳过成本"作为自变量。

综合来看，你的两个猜测分别对应文献中"时机/需求判定"和"打断成本/可弃用性"两条主线，且已有研究（尤其 ProMemAssist 与 Codellaborator）都把二者作为需要被显式建模或测量的设计变量，说明你的切入点对一个已被初步验证、但尚未系统化的空白是成立的。建议下一步把"建议的可弃用性"操作化为可测量指标（如用户跳过建议所需的时间或注意转移量），再与"用户当时是否处于需求缺口"（可用 ProMemAssist 式的认知负荷/工作记忆信号，或更简单的任务阶段标签）做交叉，验证二者的交互效应。
