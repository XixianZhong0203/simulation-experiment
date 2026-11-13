文献总结：AI 写作协作（human-AI co-writing）的关键研究发现

现有研究可归纳为四个最值得关注的方向：

1. 用户与 AI 协作的方式高度多样且“以使用为设计”：对 19 名计算机科学研究者观察与回顾式访谈发现，研究者会在使用中主动改造写作助手以克服挑战，呈现出五种 design-in-use 风格——教学（teaching）、抵抗（resisting）、改造用途（repurposing）、编排（orchestrating）与顺从（complying），同时暴露出工作流被打断、过度依赖 AI 等问题（Investigating How Computer Science Researchers Design Their Co-Writing Experiences With AI, 10.1145/3706598.3713205）。大规模“真实使用”分析也发现用户并非被动接受输出，而是会修正意图、探索文本、提问、调整风格或注入新内容，少数典型协作行为（PATHs）即可解释用户—LLM 交互的大部分变异，且特定写作意图与这些行为显著相关（Prototypical Human-AI Collaboration Behaviors from LLM-Assisted Writing in the Wild, 10.18653/v1/2025.emnlp-main.852）。

2. 代理感与所有权是核心矛盾，且随写作阶段变化：对 109 篇 HCI 论文的 PRISMA 系统综述识别出四类 AI 写作支持设计策略（结构化引导、引导式探索、主动共写、批判性反馈），并将其映射到写作规划、转译、审校、监控四个认知过程；访谈显示内容导向型作者（如学者）在规划阶段最看重所有权，形式导向型作者（如创意写作者）则更重视对转译与审校的控制（Co-Writing with AI, on Human Terms, 10.1145/3757566）。支架水平的实地实验（N=131）进一步揭示“U 型”效应：低支架对质量与效率无显著改善，高支架显著提升写作质量与产出（尤其惠及非经常写作者和科技经验较少的用户），但会带来文本所有权和满意度的中度下降，提示需要个性化支架机制（Shaping Human-AI Collaboration: Varied Scaffolding Levels in Co-writing with Language Models, 10.1145/3613904.3642134）。在“真实性”层面，19 名职业作者的访谈表明作者对“保持真实声音”的关切更多落在创作过程与自我建构上，他们欢迎个性化支持但希望个性化服务于作者成长而非仅仅文本生产；而 30 名读者对 AI 共写作品几乎不敏感、无法区分并态度积极（It was 80% me, 20% AI': Seeking Authenticity in Co-Writing with Large Language Models, 10.1145/3711020）。

3. LLM 文本质量存在可识别的“共性局限”，且伴随文化同质化风险：专业编辑对 LLM 生成文本的缺陷达成一致，形成七类“怪癖”分类法（如陈词滥调、不必要的铺陈），并构建了 LAMP 语料（1,057 段经专业编辑的 LLM 文本）；分析显示 GPT-4o、Claude-3.5-Sonnet、Llama-3.1-70b 在写作质量上互不占优，说明跨模型家族的共性局限；偏好标注证实专家更偏好专家编辑后的文本，自动编辑方法在改善 LLM 文本与人类文本对齐方面前景可观（Can AI writing be salvaged?, 10.1145/3706598.3713559）。跨文化受控实验（118 名印度与美国被试）则发现西方中心模型带来的效率增益对美国人更大，并促使印度参与者转向西方写作风格，削弱了文化表达的细微差异（AI Suggestions Homogenize Writing Toward Western Styles and Diminish Cultural Nuances, 10.1145/3706598.3713564）。

4. AI 写作辅助的价值与代价并存，多语言场景还有“选择独立性”问题：实验表明人们愿意为 AI 写作辅助（尤其是直接内容生成且任务高度创意时）放弃经济支付，AI 提升了生产力与自信，但直接内容生成也会降低问责感并削弱写作多样性（The Value, Benefits, and Concerns of Generative AI-Powered Assistance in Writing, 10.1145/3613904.3642625）；多语言说服性共写任务中，先接触西语 LLM 会降低后续对英语 LLM 的使用（违反选择独立性），且人们对广告来源（人写 vs AI）的信念会改变捐助行为，人们总体难以区分人类与 LLM 生成文本（Mind the Gap! Choice Independence in Using Multilingual LLMs for Persuasive Co-Writing Tasks in Different Languages, 10.1145/3706598.3713201）。

5. 系统设计方向：分层、可个性化的接口能保住写作流的自然性。Script&Shift 通过把写作意图与 LLM 能力对齐（内容开发 scripting + 面向受众的 shifting），让作者可在规划、转译、审校中保持创意控制并鼓励发散式迭代写作，评估显示其能兼顾效率与流畅（Script&Shift: A Layered Interface Paradigm for Integrating Content Development and Rhetorical Strategy with LLM Writing Assistants, 10.1145/3706598.3714119）；针对故事写作，原型（FigJam 插件）显示作者偏好在不同写作阶段灵活组合节点图结构可视化、LLM 受众扮演、图像/音频生成等能力，包括对“道德/主题”的反思支持（Toward Personalizable AI Node Graph Creative Writing Support, 10.1145/3706598.3713569）。

总体来看，最值得关注的共识是：AI 共写的收益（效率、信心、生产力）与代价（所有权、真实性、多样性、文化同质化）同时存在；未来设计应从“统一辅助”转向按写作阶段、用户目标与文化背景进行个性化、可调节介入（scaffolding），并让作者保有对过程与自我表达的掌控。
