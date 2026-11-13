简短文献总结——AI 辅助写作领域最值得关注的发现：

1. 人机共写是主动共建而非被动接受。大规模真实使用分析发现，少数几类原型协作行为（修改意图、探索文本、提问、调整风格、注入新内容）即可解释用户与 LLM 交互的大部分变化，且写作意图与协作行为显著相关（Prototypical Human-AI Collaboration Behaviors from LLM-Assisted Writing in the Wild, DOI: 10.18653/v1/2025.emnlp-main.852）；对 19 名计算机科学研究者的观察进一步识别出教学、抗拒、改造、编排、顺从五种使用风格（Investigating How Computer Science Researchers Design Their Co-Writing Experiences With AI, DOI: 10.1145/3706598.3713205）。

2. LLM 文本存在跨模型的共性缺陷，编辑可部分补救。专业作家对 LLM 文本的不满可归纳为七类问题（如陈词滥调、多余说明）；GPT-4o、Claude-3.5-Sonnet、Llama-3.1-70B 在写作质量上互不占优；自动编辑方法在改善人机文本对齐上显示出前景，但专家仍更偏好专家编辑后的文本（Can AI writing be salvaged? Mitigating Idiosyncrasies and Improving Human-AI Alignment in the Writing Process through Edits, DOI: 10.1145/3706598.3713559）。

3. 过度依赖与真实性构成核心张力。AI 辅助与建议复用模式相关，反思式界面能提高用户对 AI 输出的觉察（Overreliance in Writing Tasks: Exploring Similarity-Based Measures of AI Influence on Writing and Proposing a Reflective Writing Interface Intervention, DOI: 10.1145/3805689.3812389）；作家把真实性理解为创作过程与自我的建构，欢迎面向成长而非仅文本产出的个性化；读者则几乎无法分辨 AI 辅助作品并持积极态度（It was 80% me, 20% AI: Seeking Authenticity in Co-Writing with Large Language Models, DOI: 10.1145/3711020）。

4. AI 正在使写作向西方风格趋同并削弱文化表达。跨文化实验显示，AI 建议带来的效率提升对美国人更大，并促使印度参与者采用西方写作风格（AI Suggestions Homogenize Writing Toward Western Styles and Diminish Cultural Nuances, DOI: 10.1145/3706598.3713564）；针对研究文化的分析同样指出 LLM 缺乏文化胜任力、倾向于同质化写作（Research Borderlands: Analysing Writing Across Research Cultures, DOI: 10.18653/v1/2025.acl-long.1272）。此外，在诗歌细读任务中，单条 AI 解读同时提升表现与愉悦，但重度依赖 AI 的用户表现更好而愉悦更低，提示辅助应遵循“少即是多”（What Does AI Do for Cultural Interpretation? A Randomized Experiment on Close Reading Poems with Exposure to AI Interpretation, DOI: 10.1145/3772318.3791727）。

5. 界面设计是缓解上述问题的可行路径。Script&Shift 的分层界面将写作意图与 LLM 能力对齐，在保留创作控制的同时减少流程中断（Script&Shift: A Layered Interface Paradigm for Integrating Content Development and Rhetorical Strategy with LLM Writing Assistants, DOI: 10.1145/3706598.3714119）；结合节点图可视化、受众模拟与图像/音频生成的原型插件则表明，作家偏好按需组合多种生成式功能来应对写作不同阶段的需求（Toward Personalizable AI Node Graph Creative Writing Support, DOI: 10.1145/3706598.3713569）。
