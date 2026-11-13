以下是对背景论文库的简要文献总结（按主题归纳，每条结论标注支持论文的标题与DOI）：

1. 信任是动态、情境依赖的，且容易被系统不一致打断
- 物流领域与AI规划系统协作多年的专家，即便明确指出系统不完美，也会随时间发展出信任；但系统的不一致和频繁改进迭代会破坏信任发展，并削弱控制感、透明度与系统理解（"Good Performance Isn't Enough to Trust AI: Lessons from Logistics Experts on their Long-Term Collaboration with an AI Planning System", 10.1145/3706598.3713099）。
- 协作前的初始信任源于对AI能力、正直、善意与适应性的期望；协作过程中受AI沟通行为影响的"情境信任"会维持或修正初始信任，并反哺后续对AI的预期（"Understanding the Evolvement of Trust Over Time within Human-AI Teams", 10.1145/3687060）。
- 在个人健康决策中，信任取决于AI推荐的个性化程度与个体决策风格的匹配程度（"Selective Trust: Understanding Human-AI Partnerships in Personal Health Decision-Making Process", 10.1145/3706598.3713462）。

2. 控制权应被视为可调节的"轨迹"，而非固定设置
- 专家将人机共创中的控制理解为随共创阶段、领域和信任水平变化的动态、情境依赖构念（"\"Control Is a Trajectory, Not a Point\": Conceptualizing Control in Human-AI Co-Creativity", 10.1145/3772318.3790861）。
- 一项N=18的受试内研究发现：主动式AI编程代理比纯提示方式更高效，但会造成工作流干扰；存在感指示与交互上下文能减轻干扰、提升用户对AI过程的感知，同时也凸显了用户控制、代码所有权与代码理解之间的权衡（"Assistance or Disruption? Exploring and Evaluating the Design and Trade-offs of Proactive AI Programming Support", 10.1145/3706598.3713357）。
- 一项覆盖近20年顶级HCI/CSCW文献（134篇）的范围综述，提供了组织代理模式、控制机制与交互情境的整合框架及操作化目录（"Exploring Collaboration Patterns and Strategies in Human-AI Co-creation through the Lens of Agency", 10.1145/3757594）。

3. 用户以批判性策略应对AI输出的不确定性
- 视障屏幕阅读器用户面对GenAI信息时采取"日常不确定性"（everyday uncertainty）心态：不期待信息正确完整，而是从含错来源中提取线索、将信息视为临时性的、承认信息的主观性，并持续调整期望与策略（"Everyday Uncertainty: How Blind People Use GenAI Tools for Information Access", 10.1145/3706598.3713433）。

4. 团队与界面层面：AI重塑协作动态与学习体验
- 搜救团队引入分布式AI后比对照组更快达成共识，但也面临信息过载与冲突检测带来的困难（"The Influence of Distributed AI in Trust and Collaboration for Search-and-Rescue Teams", 10.1145/3772318.3791523）。
- 基于"促进信任的语言风格"对讨论伙伴进行算法化配对，可提升人际信任，且效果独立于观点相似度（"Making Pairs That Cooperate: AI Evaluation of Trust in Human Conversations", 10.1145/3711027）。
- AI聊天导师的化身（avatar）表征对学习体验的影响因人而异，取决于学习习惯与任务类型，并会诱发特定的提示行为（"Exploring the Impact of Avatar Representations in AI Chatbot Tutors on Learning Experiences", 10.1145/3706598.3713456）。
- UI/UX设计师在发散思维阶段更看重能给予控制、促进协作、提升效率以释放创造力、并与自身视觉习惯对齐的AI工具（"Beyond Automation: How Designers Perceive AI as a Creative Partner in the Divergent Thinking Stages of UI/UX Design", 10.1145/3706598.3713500）。

核心启示：人机协作中的信任与控制都不是静态属性，而是随时间、情境与交互持续演化的动态过程。最值得关注的研究发现是——AI系统的不一致与频繁迭代会实质性破坏信任（10.1145/3706598.3713099），主动性与控制的设计需要"轨迹化"地随阶段与信任水平调节（10.1145/3772318.3790861, 10.1145/3706598.3713357），并且应把可解释的AI过程、与用户决策风格及习惯对齐的推荐（10.1145/3706598.3713462, 10.1145/3706598.3713500）作为设计核心目标。
