以下总结基于论文库中与 AI 辅助写作/人机共写相关的摘要，按主题归纳最值得关注的发现：

1. LLM 文本存在共性缺陷，编辑是有效改进路径。《Can AI writing be salvaged? Mitigating Idiosyncrasies and Improving Human-AI Alignment in the Writing Process through Edits》（DOI: 10.1145/3706598.3713559）将专业编辑认可的 LLM 文本毛病归纳为七类（如陈词滥调、多余铺陈），基于 1,057 段的 LAMP 语料显示 GPT-4o、Claude-3.5-Sonnet、Llama-3.1-70B 各有局限、互不占优，而自动编辑方法在改善 LLM 文本与人类文本的对齐上表现可期。

2. AI 建议会改变写作风格与文化传播。《AI Suggestions Homogenize Writing Toward Western Styles and Diminish Cultural Nuances》（DOI: 10.1145/3706598.3713564）的跨文化实验（美印各半，118 人）发现 AI 对美国参与者效率增益更大，并使印度参与者转向西方写作风格，表明以西方为中心的同质化效应。《Mind the Gap! Choice Independence in Using Multilingual LLMs...》（DOI: 10.1145/3706598.3713201）进一步发现多语种用户违反“选择独立性”——对西班牙语 LLM 的负面体验会降低其后续对英语 LLM 的使用，且人们总体上无法区分人与 AI 生成的广告。

3. 辅助层级决定质量收益与所有权代价。《Shaping Human-AI Collaboration: Varied Scaffolding Levels in Co-writing with Language Models》（DOI: 10.1145/3613904.3642134）发现脚手架层级与质量/产量呈 U 型关系：段落级（高）辅助显著提升质量，尤其惠及低频写作者，但文本所有权感和满意度中等程度下降。《Co-Writing with AI, on Human Terms: Aligning Research with User Demands Across the Writing Process》（DOI: 10.1145/3757566）对 109 篇 HCI 论文的系统综述加 15 位写作者访谈表明，写作者期望的 AI 介入随写作阶段和写作类型变化（内容型写作者重视规划期所有权，形式型写作者重视翻译/审阅期控制），并归纳出结构化引导、引导式探索、主动共写、批判性反馈四类设计策略。

4. 真实性、披露与感知。《It was 80% me, 20% AI: Seeking Authenticity in Co-Writing with Large Language Models》（DOI: 10.1145/3711020）发现写作者更看重面向自身“成长”而非仅文本产出阶段的个性化，而读者对 AI 共写不太担忧、也无法区分 AI 辅助与纯人写的作品。《How Does the Disclosure of AI Assistance Affect the Perceptions of Writing?》（DOI: 10.18653/v1/2024.emnlp-main.279）发现披露 AI 参与（尤其是内容生成类）会降低平均质量评分并增大评分方差。《The Value, Benefits, and Concerns of Generative AI-Powered Assistance in Writing》（DOI: 10.1145/3613904.3642625）则表明人们愿意为 AI 写作辅助付费（高创造性任务尤甚），它提升生产率与信心，但也削弱责任感并降低写作多样性。

5. 研究者的使用方式与工具设计。《Investigating How Computer Science Researchers Design Their Co-Writing Experiences With AI》（DOI: 10.1145/3706598.3713205）识别出教学、抵制、改造、编排、顺从五种“design-in-use”风格，并指出工作流中断与过度依赖 AI 两大问题。界面层面，Script&Shift（DOI: 10.1145/3706598.3714119）提出将写作意图与 LLM 能力对齐的分层接口以保住写作流畅度；《Toward Personalizable AI Node Graph Creative Writing Support...》（DOI: 10.1145/3706598.3713569）显示写作者偏好灵活组合节点图可视化、LLM 受众扮演与图像/音频生成等多样功能。

总体来看，该文献库最一致的关注点是：LLM 文本存在跨模型的共性风格缺陷（编辑与个性化是主要改进方向）；AI 介入的层级、时机与披露方式同时塑造质量收益与所有权/真实性代价；跨文化与多语种部署可能带来风格同质化与用户信任的连锁效应；而写作者真正需要的是随写作过程动态调整的人本化控制。
