以下是对背景论文库的简短文献总结，聚焦人机协同写作（human-AI co-writing）领域最值得关注的研究发现：

1. **LLM 写作存在共性“腔调”，模型间质量差距有限**：专业编辑对 LLM 生成文本的修改被归纳为七类缺陷（如陈词滥调、多余铺陈），LAMP 语料库分析显示 GPT-4o、Claude-3.5-Sonnet、Llama-3.1-70b 在写作质量上互不占优，提示各模型家族的共性局限（Can AI writing be salvaged? DOI: 10.1145/3706598.3713559）。

2. **AI 辅助强度呈 U 型效应**：低脚手架（下一句建议）对质量与效率改善不显著，高脚手架（下一段建议）显著提升写作质量与产量，尤其惠及非惯常写作者，但伴随文本所有权与满意度的中度下降（Shaping Human-AI Collaboration: Varied Scaffolding Levels in Co-writing with Language Models, DOI: 10.1145/3613904.3642134）。总体上用户愿意为直接内容生成付费，AI 提升生产率与信心，却可能削弱责任感与写作多样性（The Value, Benefits, and Concerns of Generative AI-Powered Assistance in Writing, DOI: 10.1145/3613904.3642625）。

3. **AI 带来文化与观念的同质化风险**：西方中心的 AI 建议使印度参与者的写作转向西方风格，削弱文化表达的独特性（AI Suggestions Homogenize Writing Toward Western Styles and Diminish Cultural Nuances, DOI: 10.1145/3706598.3713564）；Reactive Writers（DOI: 10.1145/3772318.3791529）发现共写时“先评估建议”取代了传统的构思过程，AI 提出的观点为写作定调，而写作者并未察觉自身已受影响，易产生 AI 诱导的观念偏移。

4. **真实感、作者归属与披露效应是核心关切**：写作者更关心共写过程能否保留真实自我，且个性化应面向写作者成长而非仅文本产出（It was 80% me, 20% AI': Seeking Authenticity in Co-Writing with Large Language Models, DOI: 10.1145/3711020）；在私密通信场景中，AI 起草程度越高，接收者感知到的所有权与真实感越低，清晰度的提升无法补偿（Is It Still You? Attributing Authorship and Authenticity in AI-Assisted Romantic Communication, DOI: 10.1145/3772318.3790762）；披露 AI 参与内容生成会显著降低读者对文本质量的评价（How Does the Disclosure of AI Assistance Affect the Perceptions of Writing?, DOI: 10.18653/v1/2024.emnlp-main.279）。

5. **设计启示**：研究者在使用中形成五种 design-in-use 风格（teaching、resisting、repurposing、orchestrating、complying）来适应 AI 写手（Investigating How Computer Science Researchers Design Their Co-Writing Experiences With AI, DOI: 10.1145/3706598.3713205）；Script&Shift 提出将写作意图与 LLM 能力对齐的分层界面范式，在支持内容开发的同时保留创作控制（DOI: 10.1145/3706598.3714119）；对 109 篇 HCI 论文的系统综述发现不同写作者对 AI 介入程度的需求随写作阶段（planning、translating、reviewing、monitoring）而变化，需要个性化脚手架（Co-Writing with AI, on Human Terms, DOI: 10.1145/3757566）；面向科研写作的 SWIF^2T 工具生成的聚焦反馈在特异性、可读性与实用性上优于既有方法，个别案例甚至优于人工评审（Automated Focused Feedback Generation for Scientific Writing Assistance, DOI: 10.18653/v1/2024.findings-acl.580）。

总体判断：该领域的关注点正从“AI 能否写得更好”转向“如何在提效的同时保留作者的真实感、文化表达与自主权”；适度脚手架、个性化支持与透明的披露机制是当前主要的设计方向。
