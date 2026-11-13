这组文献围绕"人机协作写作"展开，共同刻画了当前 AI 写作助手的收益与局限。最值得关注的发现如下：

1) 研究者的实际使用方式高度分化。一项对 19 名计算机科学研究者（观察+回顾性访谈、design-in-use 视角）的研究发现，协作中会出现工作流中断和过度依赖 AI 等问题，并归纳出五种 design-in-use 风格：teaching、resisting、repurposing、orchestrating、complying（Investigating How Computer Science Researchers Design Their Co-Writing Experiences With AI, DOI: 10.1145/3706598.3713205）。

2) LLM 生成的文本存在共性缺陷且各模型间无显著质量差异。专业编辑总结出七类"AI 腔"特征（如陈词滥调、不必要的陈述），并构建了 1,057 段经编辑的 LAMP 语料；GPT4o、Claude-3.5-Sonnet、Llama-3.1-70b 在写作质量上互不占优，而基于自动编辑的方法在改善 LLM 文本与人类文本对齐方面显示出潜力（Can AI writing be salvaged? Mitigating Idiosyncrasies and Improving Human-AI Alignment in the Writing Process through Edits, DOI: 10.1145/3706598.3713559）。

3) AI 建议会带来文化同质化。一项 118 人（印度与美国）的跨文化对照实验表明，西方中心的 AI 模型给美国参与者带来更大的效率提升，并促使印度参与者转向西方写作风格，既改变"写什么"也改变"怎么写"，削弱了文化表达的差异（AI Suggestions Homogenize Writing Toward Western Styles and Diminish Cultural Nuances, DOI: 10.1145/3706598.3713564）。

4) 交互设计能缓解上述问题。Script&Shift 提出分层界面范式，将写作意图与 LLM 能力对齐，区分"内容生成（scripting）"与"面向不同受众的组织/修辞调整（shifting）"，在保持创作控制权与自然写作流的同时支持多样化内容开发（Script&Shift: A Layered Interface Paradigm for Integrating Content Development and Rhetorical Strategy with LLM Writing Assistants, DOI: 10.1145/3706598.3714119）；另一项面向创意写作（故事/道德反思）的工作则发现，用户偏好组合使用节点图结构可视化、LLM 读者模拟、图像与音频生成等多元功能，以覆盖写作过程中变化的需求（Toward Personalizable AI Node Graph Creative Writing Support, DOI: 10.1145/3706598.3713569）。

综合来看：AI 写作助手的价值不仅取决于模型质量，更取决于交互设计与文化适配——共性缺陷（AI 腔、同质化）提示我们需要更好的编辑方法与跨文化设计，而分层/个性化交互范式（如 Script&Shift、节点图支持）则为保留人的创作控制提供了可行路径。
