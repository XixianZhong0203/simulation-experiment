文献总结（基于背景论文库）

这批研究围绕"人—AI 协作"展开，最值得关注的是几条反复出现的发现：

1. 主动式 AI 提升效率与创造力，但伴随工作流中断与自主性损失。在编程场景中，主动式 AI 智能体比纯提示范式更高效，但会造成工作流中断；加入"在场"指示器与交互上下文可减轻中断、提升用户对 AI 过程的觉察（"Assistance or Disruption? Exploring and Evaluating the Design and Trade-offs of Proactive AI Programming Support"，DOI: 10.1145/3706598.3713357）。在协作写作中，主动式 AI 能增强创造力并加快写作，但 AI 参与度与人类代理感（agency）之间存在权衡；若 AI 能激发出更强的灵感，用户即使在高 AI 参与下也能维持较高的代理感（"Proactive AI as a Catalyst for Creativity? Balancing Human Agency and AI Contribution in Collaborative Story Writing"，DOI: 10.1145/3772318.3790848）。

2. 透明化设计本身也有副作用。协同写作系统 Plotania 发现：虚拟读者反馈提升了受众意识却降低了创作代理感；透明归属层虽让用户更清楚 AI 的贡献，却引发身份焦虑并减少了 AI 使用；作者据此提出"保留代理感的透明"（agency-preserving transparency）设计原则（"Plotania: Exploring Transparency Trade-offs in AI Co-Writing Through Virtual Readers and Transparent Attribution"，DOI: 10.1145/3772318.3790926）。

3. 信任是动态、情境化的，不能仅靠系统性能获得。个人健康决策中，信任受推荐个性化程度与个体决策风格共同塑造（"Selective Trust: Understanding Human-AI Partnerships in Personal Health Decision-Making Process"，DOI: 10.1145/3706598.3713462）；人—AI 团队中，初始信任会随协作中情境信任的建立而维持或被修正（"Understanding the Evolvement of Trust Over Time within Human-AI Teams"，DOI: 10.1145/3687060）；物流领域的真实长期案例显示，系统不一致与频繁迭代会破坏信任发展，专家即使信任系统也会出于人际因素推翻正确的 AI 决策（"Good Performance Isn't Enough to Trust AI: Lessons from Logistics Experts on their Long-Term Collaboration with an AI Planning System"，DOI: 10.1145/3706598.3713099）。

4. 面对不可靠的 AI 输出，用户会形成批判性的应对策略：视信息为暂定、从错误中提取线索、持续调整期望与策略，这一"日常不确定性"心态尤其体现在盲人用户借助 GenAI 获取信息的过程中（"Everyday Uncertainty: How Blind People Use GenAI Tools for Information Access"，DOI: 10.1145/3706598.3713433）。

5. 界面与沟通设计显著影响体验：avatar 表征会影响提示行为与学习体验（"Exploring the Impact of Avatar Representations in AI Chatbot Tutors on Learning Experiences"，DOI: 10.1145/3706598.3713456）；AI 的口头与视觉沟通模态各有取舍，需按团队构成加以设计（"Verbal vs. Visual: How Humans Perceive and Collaborate with AI Teammates Using Different Communication Modalities in Various Human-AI Team Compositions"，DOI: 10.1145/3686976）；室内设计协同共创中，问卷数据最易被信任且能激发创造力，AI 预测叠加层需经自然语言中介才能建立信任，凸显"真实性—可解释性"权衡（"AIDED: Augmenting Interior Design with Human Experience Data for Designer-AI Co-Design"，DOI: 10.1145/3772318.3791378）。

6. 在 UI/UX 的发散性思维阶段，设计师看重可控性、协作性与效率；AI 主要扮演研究辅助、创意启动、方案生成与原型探索四种角色（"Beyond Automation: How Designers Perceive AI as a Creative Partner in the Divergent Thinking Stages of UI/UX Design"，DOI: 10.1145/3706598.3713500）。

一句话概括：AI 的价值不在于替代，而在于与用户保留控制权、自主性与信任相匹配的支持；设计重点应放在可调节的主动性、保留代理感的透明化，以及随时间动态演化的信任管理上。
