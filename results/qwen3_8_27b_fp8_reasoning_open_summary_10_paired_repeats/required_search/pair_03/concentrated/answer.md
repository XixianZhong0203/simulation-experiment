人机协同写作（Human-AI Co-Writing）文献总结——最值得关注的发现：

1. LLM 文本质量存在共性缺陷：专业编辑对 LLM 生成文本中不想要的“个性化风格”（如陈词滥调、多余解释）形成共识，归纳出七类问题；GPT4o、Claude-3.5、Llama-3.1 之间无质量优劣之分，而自动编辑方法有望改善 LLM 文本与人类写作风格的对齐（Can AI writing be salvaged? DOI: 10.1145/3706598.3713559）。

2. 脚手架水平呈 U 形效应：低脚手架（下句建议）无显著改善；高脚手架（下段建议）显著提升质量与效率，尤其惠及非惯常写作人群，但文本归属感与满意度轻微下降，提示需要个性化脚手架机制（Shaping Human-AI Collaboration: Varied Scaffolding Levels in Co-writing with Language Models, DOI: 10.1145/3613904.3642134）。

3. 真实感与披露效应：写作者更重视创作过程的真实感，期望个性化 AI 支持其成长而非停留在文本生成；读者基本无法识别 AI 辅助作品且态度积极（It was 80% me, 20% AI, DOI: 10.1145/3711020）。但披露 AI 参与（尤其内容生成）会降低质量评分并减少其入选首选作品的比例（How Does the Disclosure of AI Assistance Affect the Perceptions of Writing?, DOI: 10.18653/v1/2024.emnlp-main.279）。

4. 文化与多语言偏差：西方中心的 AI 建议使印度用户转向西方写作风格，削弱文化表达独特性，且效率收益存在文化差异（AI Suggestions Homogenize Writing Toward Western Styles and Diminish Cultural Nuances, DOI: 10.1145/3706598.3713564）；用户对多语言 LLM 存在“选择独立性”违反，先前对某语言表现的不满会外溢影响后续另一种语言的采用（Mind the Gap!, DOI: 10.1145/3706598.3713201）。

5. 价值与风险并存：人们愿意为 AI 写作辅助付费（直接内容生成与高创造性任务尤甚），生产力与信心提升，但直接生成会削弱责任感与写作多样性（The Value, Benefits, and Concerns of Generative AI-Powered Assistance in Writing, DOI: 10.1145/3613904.3642625）。

6. 设计启示：对 109 篇 HCI 论文的系统综述提出四类设计策略（结构化引导、引导式探索、主动共写、批判性反馈），并指出 AI 介入需求随写作阶段（计划、转换、审读、监控）与写作类型变化（Co-Writing with AI, on Human Terms, DOI: 10.1145/3757566）；界面层面，Script&Shift 分层范式可减少写作流被打断（Script&Shift, DOI: 10.1145/3706598.3714119）；对 19 名 CS 研究者的观察归纳出五种“设计在使用中”风格：教学、抵抗、再利用、编排、顺从（Investigating How Computer Science Researchers Design Their Co-Writing Experiences With AI, DOI: 10.1145/3706598.3713205）。

小结：该领域的核心结论是——LLM 写作存在共性短板但可通过编辑缓解；AI 辅助的净收益取决于脚手架水平与用户画像；披露、文化、多语言因素深刻影响感知与采用；按写作阶段个性化、保留作者控制权的 AI 介入是当前最重要的设计方向（Toward Personalizable AI Node Graph Creative Writing Support, DOI: 10.1145/3706598.3713569）。
