以下是一份简短的文献总结，概括本次 AI 辅助写作（human-AI co-writing）文献中最值得关注的研究发现。每条发现后标注支持它的论文标题或 DOI。

一、AI 改变了写作的过程本身，而非仅仅改变产物
1. 出现“Reactive Writing（反应式写作）”：与 AI 建议的互动（阅读并决定是否接受）成为核心活动，挤占了传统的构思与语言生成；作者往往未察觉 AI 的影响并自以为在掌控，因而极易受 AI 诱导的偏见与观点偏移影响。（Reactive Writers: How Co-Writing with AI Changes How We Engage with Ideas, DOI 10.1145/3772318.3791529）
2. 支架（scaffolding）强度呈 U 型影响：低支架（下一句）无显著提升，高支架（下一段）显著改善质量与效率、尤其帮助非惯用写作与低技术用户，但会降低文本所有权感与满意度。（Shaping Human-AI Collaboration: Varied Scaffolding Levels in Co-writing with Language Models, DOI 10.1145/3613904.3642134）
3. 使用时机关键：在构思一开始就调用 LLM 会降低原创想法数量、削弱创造性自我效能与自我归属，效应受自主性与所有权中介。（Timing Matters: How Using LLMs at Different Timings Influences Writers' Perceptions and Ideation Outcomes, DOI 10.1145/3706598.3713146）

二、文本质量与文化层面的系统性风险
4. LLM 文本存在跨模型家族的共性缺陷：专业写作者对 LLM 生成文本的不当特性高度一致（如陈词滥调、多余铺陈），GPT4o、Claude-3.5-Sonnet、Llama-3.1-70b 在质量上并无互相超越，自动编辑方法有望改善人机对齐。（Can AI writing be salvaged? Mitigating Idiosyncrasies and Improving Human-AI Alignment in the Writing Process through Edits, DOI 10.1145/3706598.3713559）
5. 文化同质化：西方中心的 AI 建议使印度参与者转向西方写作风格，不仅改变“写什么”也改变“怎么写”，削弱了区分文化表达的细微差异，且 AI 给美国人带来的效率增益更大。（AI Suggestions Homogenize Writing Toward Western Styles and Diminish Cultural Nuances, DOI 10.1145/3706598.3713564）
6. 披露效应：披露 AI 辅助、尤其是 AI 参与内容生成时，会降低议论文与创意故事的平均质量评分，且个体间评分分歧增大；披露还会降低 AI 生成内容作品在“最高排名”中的占比。（How Does the Disclosure of AI Assistance Affect the Perceptions of Writing?, DOI 10.18653/v1/2024.emnlp-main.279）

三、能动性、所有权与个性化的悖论
7. 界面隐喻塑造能动性认知：在功能相近但隐喻不同（能动型/工具型/魔法型）的共创系统中，写作者的控制感与作者身份感出现可分类的亚型，隐喻本身即影响创作实践。（Where Do I 'Add the Egg'?: Exploring Agency and Ownership in AI Creative Co-Writing Systems, DOI 10.1145/3772318.3791952）
8. 个性化悖论：以阅读高亮驱动的个性化能提升参与度，但高亮从“理解策略”退化为“喂给 AI 的工具行为”，导致对 AI 的显著依赖及自主性、所有权、自我归属下降。（AI Personalization Paradox: Reading Highlights for Personalized AI-Assisted Writing Increases Engagement but Undermines Autonomy and Ownership, DOI 10.1145/3772318.3791502）
9. 需求随写作过程与作者类型变化：以内容为中心的作者（如学术研究者）在意规划阶段的所有权，以形式为中心的作者（如创意写作者）在意翻译与审阅阶段的控制；作者偏好受情境目标、价值观与原创/作者身份观念塑造。（Co-Writing with AI, on Human Terms: Aligning Research with User Demands Across the Writing Process, DOI 10.1145/3757566）

四、研究者如何在“使用中设计”写作助手
10. 19 名计算机科学研究员与写作助手协作呈现五种“design-in-use”风格——teaching（教导）、resisting（抵抗）、repurposing（改造用途）、orchestrating（编排）、complying（顺从），并暴露出工作流中断与过度依赖 AI 等问题，为更有效的助手设计提供依据。（Investigating How Computer Science Researchers Design Their Co-Writing Experiences With AI, DOI 10.1145/3706598.3713205）
11. 分层界面范式（Script&Shift）通过将写作意图与 LLM 能力对齐，支持内容开发（scripting）与面向不同受众的组织策略调整（shifting），在保持创作控制的同时保留写作的自然流程。（Script&Shift: A Layered Interface Paradigm for Integrating Content Development and Rhetorical Strategy with LLM Writing Assistants, DOI 10.1145/3706598.3714119）

总体结论：现有证据一致表明，AI 写作助手不仅改变文本，更系统性地重塑写作过程（反应式、支架与时间效应）、带来质量与文化同质化风险，并在个性化与隐喻设计上反复考验作者的所有权与能动性。设计方向应围绕“保留人类控制权”展开——按写作阶段与作者类型做个性化支架、延后用于构思、提供透明度与来源记录、并避免以个性化之名诱导依赖。
