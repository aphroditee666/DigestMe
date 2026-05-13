# Google DeepMind Blog

> 分类: AI专题
> URL: https://deepmind.com/blog/feed/basic/
> 抓取: 30 篇

---

## 1. AlphaEvolve: How our Gemini-powered coding agent is scaling impact across fields

- 日期: 2026-05-06 10:43
- 链接: https://deepmind.google/blog/alphaevolve-impact/

```
Improving AI infrastructure
AlphaEvolve has graduated from pilot testing to becoming a core component of our infrastructure. AlphaEvolve has been used as a regular tool to optimize the design of the next generation of TPUs. It also helped discover more efficient cache replacement policies, achieving in two days what previously required a concerted, human-intensive effort spanning months.
“AlphaEvolve began optimizing the lowest levels of hardware powering our AI stacks. It proposed a circuit design so counterintuitive yet efficient that it was integrated directly into the silicon of our next-generation TPUs. This is the latest example of TPU brains helping design next-generation TPU bodies.” — Jeff Dean, Chief Scientist, Google DeepMind and Google Research
AlphaEvolve improved the efficiency of Google Spanner by refining its Log-Structured Merge-tree compaction heuristics. This optimization reduced 'write amplification'—the ratio of data written to storage versus the original request—by 20%. It also provided insights for new compiler optimization strategies that reduced the storage footprint of software by nearly 9%.
Scaling commercial applications
Together with Google Cloud, we are now bringing the power of AlphaEvolve to a variety of commercial enterprises across industries.
- In financial services, Klarna used the system to optimize one of its largest transformer models — doubling its training speed whilst improving model quality.
- In semiconductor manufacturing, Substrate applied AlphaEvolve to its computational lithography framework, achieving a multi-fold increase in runtime speed, enabling them to run significantly larger simulations of advanced semiconductors.
- In logistics, FM Logistic used the technology to optimize complex routing challenges like the Traveling Salesman Problem, finding 10.4% improvement in routing efficiency over the previous heavily optimized solutions — saving over 15,000 kilometers of distance travelled annually.
- In advertising and marketing, WPP used AlphaEvolve to refine AI model components, navigating complex, high-dimensional campaign data and achieving 10% accuracy gains over their competitive manual model optimizations.
- In computational material and life sciences, Schrödinger applied AlphaEvolve to achieve a roughly 4x speedup in both Machine Learned Force Fields (MLFF) training and inference.
“AlphaEvolve allows us to explore larger chemical spaces faster and more efficiently than ever before. Faster MLFF inference carries real business impact, shortening R&D cycles in drug discovery, catalyst design, and materials development, and enabling companies to screen molecular candidates in days rather than months.” — Gabriel Marques, Technical Lead of Machine Learning at Schrödinger.
The future of AlphaEvolve
The past year shows how AlphaEvolve is rapidly becoming a versatile, general-purpose system. It is demonstrating that the next breakthroughs will be driven by algorithms that can learn, evolve and optimize themselves. As we look ahead, we are excited to expand these capabilities, and bring the power of this technology to an even broader set of external challenges.
Acknowledgements
AlphaEvolve was developed by Matej Balog, Alexander Novikov, Ngân Vũ, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, Adam Zsolt Wagner, Sergey Shirobokov, Borislav Kozlovskii, Francisco J. R. Ruiz, Abbas Mehrabian, M. Pawan Kumar, Abigail See, Swarat Chaudhuri, George Holland, Alex Davies, Sebastian Nowozin, and Pushmeet Kohli. This research was developed as part of a broader initiative focused on using AI for algorithm discovery. Following the initial development, Aja Huang, Anton Kovsharov, Alexey Cherepanov, Anindya Basu, Becky Evangelakos, Jamie Smith, and Mario Pinto joined the team and contributed to scaling AlphaEvolve’s impact.
Adam Connors, Alex Bäuerle, Anna Trostanetski, Fernanda Viegas, Gabi Cardoso, Jonathan Caton, Lucas Dixon, Mariana Felix, Martin Wattenberg, Matin Akhlaghinia, Richard Green, Yosuke Ushigome, and Yunhan Xu collaborated with our team to develop the AlphaEvolve UI, with support from many others.
Anant Nawalgaria, Diego Ballesteros, Gemma Jennings, Jakob Oesinghaus, Kartik Sanu, Laurynas Tamulevičius, Nicolas Stroppa, Nishta Dhawan, Oliver Hilsenbeck, Puneet Jagralapudi, Reah Miyara, Skander Hannachi, Tom Beyer, and Vishal Agarwal collaborated with our team to develop the AlphaEvolve API and engage with Google Cloud customers, with support from many others.
We gratefully acknowledge our collaborators for leading applications of AlphaEvolve on critical problems and contributing to this report: Aaron Wenger, Abhradeep Guha Thakurta, Akanksha Jain, Alex Vitvitskyi, Amir Yazdan Bakhsh, Andrew Carroll, Aranyak Mehta, Arthur Conmy, Ansh Nagda, Davide Paglieri, Eric Perim Martins, Gabriella Marfani, Hassler Thurston, Hongzheng Chen, Jack Mason, János Kramár, Jasper Xian, Jeremy Ratcliff, Jessica Sapick, Johannes Bausch, Jonathan Katz, Kevin Miller, Kim Stachenfeld, Mark Kurzeja, Mircea Trofin, Myriam Khan, Nero Geng, Pablo Samuel Castro, Petar Veličković, Pi-Chuan Chang, Prabhakar Raghavan, Raghav Gupta, Rohin Shah, Sasha Vezhnevets, Sébastien Lahaie, Sergio Guadarrama, Shravya Shetty, Shruthi Gorantala, Terence Tao, Todd Lipcon, Tom O'Brien, Vinod Nair, Ziyue Wang, Zun Li, among many other users of AlphaEvolve.
Finally, we thank our leadership for their guidance and support: Amin Vahdat, Ankur Jain, Demis Hassabis, Jeff Dean, Parthasarathy Ranganathan, Pushmeet Kohli, Saurabh Tiwary, and Sundar Pichai. We also extend our gratitude to our partner teams across Google DeepMind, Google Cloud, Google Labs, Google Research, and other product areas for enabling the applications and products powered by AlphaEvolve.
```

---

## 2. Enabling a new model for healthcare with AI co-clinician

- 日期: 2026-04-30 12:14
- 链接: https://deepmind.google/blog/ai-co-clinician/

```
Enabling a new model for healthcare with AI co-clinician
Health systems worldwide are striving for better outcomes, lower costs, and an improved experience for both patients and clinicians. However, progress is constrained by a global shortage of clinical experts, with the World Health Organization predicting a shortfall of more than 10 million health workers by 2030.
While AI is often seen as the key to bridging this gap, it has not yet been able to fully meet the needs of clinicians and patients. That's why, today, we are announcing our AI co-clinician research initiative, to explore how AI could better amplify doctors’ expertise and deliver higher quality care to patients.
At Google DeepMind, our journey in medical AI has evolved from mastering examination-style tests of medical knowledge with MedPaLM, to matching physician performance in text-based simulated medical consultations with AMIE, including in real-world feasibility trial settings. We also have a long history of studying how clinicians and AI systems might work together.
We hypothesize that the next evolution of healthcare delivery will entail “triadic care” where AI agents can help patients in their care journeys under the clinical authority of their physician. Medicine has always been a team sport, and AI agents can bring more teammates onto the field: extending clinicians' reach while ensuring they retain judgment and control.
This serves as the foundation of our AI co-clinician research initiative: AI designed to function as a collaborative member of the care team that interacts with patients under expert clinical supervision. We designed and evaluated AI co-clinician in both clinician and patient-facing settings. Addressing both perspectives is key for AI to enhance the quality, cost, availability and experience of care delivery.
Augmenting clinicians with AI co-clinician
For a physician, a tool is useful only if it is trustworthy and factually grounded. We therefore researched how well AI co-clinician might support clinicians by surfacing high-quality evidence.
In collaboration with academic physicians, we adapted the "NOHARM" framework to test our AI for "errors of commission" (incorrect information) and "errors of omission" (failure to surface critical information).
In head-to-head blind evaluations, physicians consistently preferred AI co-clinician’s responses to leading evidence synthesis tools. In objective analysis of 98 realistic primary care queries, our system recorded zero critical errors in 97 cases, improving over two AI systems widely used by physicians.
Beyond reliable synthesis of clinical evidence, AI systems should answer queries about medications and therapeutic interventions with the precision that doctors demand. This is a difficult task for AI yet remains underexplored. To address this gap, we evaluated AI co-clinician on the OpenFDA set of RxQA questions, a challenging benchmark designed to assess complex medication knowledge and reasoning. We saw significant progress in navigating these tests, surpassing other frontier AI systems especially when questions were posed in the open-ended way they’re asked in real care. The findings underscore the potential for advanced AI to provide helpful assistance as clinicians navigate the increasingly data-intensive requirements of care planning and management.
Researching AI co-clinician’s real time multimodal capabilities in telemedical settings
Beyond assistive clinician-facing settings, we are also investigating how AI co-clinician performs within patient-facing research contexts. Expert clinical assessment traditionally includes subtle visual and auditory cues, such as observing a patient’s gait, the nuances of respiratory patterns, or the appearance of skin changes. While prior studies (including our work with Beth Israel Deaconess Medical Center) demonstrated value in AI text-chats before a doctor’s appointment, restricting interactions to text fundamentally constrains the clinical value of AI. Medicine isn’t just text; it requires eyes, ears and a voice.
This is why we are exploring the potential for real-time multimodal AI as an assistive component of the care team. Building on the capabilities of Gemini and Project Astra, we tested the capabilities of AI co-clinician to use live audio and video to engage with patients, simulating telemedical calls where capable AI could one day support better diagnosis and management under expert supervision. Further details regarding our methodology and results are available in our technical report: “Towards Conversational Medical AI with Eyes, Ears and a Voice”
Working with academic physicians at Harvard and Stanford, we designed a randomized simulation study with 20 synthetic clinical scenarios and 10 physician "patient-actors". The agent demonstrated new capabilities beyond text-only systems, such as guiding patients through complex physical examinations in real time. For example, it successfully corrected a patient's inhaler technique and guided shoulder maneuvers to identify a rotator cuff injury.
While there is frequent discussion regarding AI’s potential to match or exceed human clinical performance, these high-fidelity simulations more rigorously evaluate that premise. We assessed over 140 aspects of consultation skill and found that expert physicians performed better than the AI system overall, particularly in identifying "red flags" and guiding critical physical examinations. This finding suggests these systems are currently best used as supportive tools for practitioners rather than replacements for clinical judgment. At the same time, our work highlights the significant progress in AI’s capabilities: AI co-clinician performed at a level comparable to or exceeding primary care physicians (PCPs) in 68 of the 140 assessed areas. The results underscore extensive promise and flag specific areas where further research can most impactfully advance medical AI.
Below you can see the research team role-playing as hypothetical patients in this telemedical setting with the AI co-clinician, highlighting the system’s potential capabilities and limitations.
Engineering trust with safeguards for clinical-grade AI
The transition and deployment of AI into clinical environments requires uncompromising architectural and operational safeguards. In our research on simulations of patient-facing telemedical conversations, AI co-clinician uses a dual-agent architecture: a "Planner" module continuously monitors the conversation, verifying that the "Talker" agent stays within safe clinical boundaries.
Similarly, to meet doctors’ needs AI co-clinician prioritizes clinical-grade evidence, performing verification and citation checking for retrieval. The evaluations we report above were constructed by physicians to mirror a range of their real-world evidence needs, formulating questions from hypothetical scenarios for rigorously evaluating AI’s capabilities.
Research collaborations for rigorous real-world evaluation of AI co-clinician
To further develop and assess AI co-clinician, we are currently advancing a phased approach with academic and research collaborators across globally diverse healthcare settings including in the US, India, Australia, New Zealand, Singapore and UAE.
As we progress through these evaluation phases, we will further our research in more geos including mission-aligned healthcare organizations and academic medical centers. Our goal is to ensure that medical AI is developed and deployed responsibly in line with applicable standards, supporting better health worldwide.
Note: Our research collaborations are not, at this stage, intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease, or to provide medical advice.
Acknowledgements
We are grateful to our research partners at Harvard Medical School and Stanford Medicine and the many medical centers and care organizations engaging in further trusted tester evaluations with our team. This project involved collaborations with many teams at Google DeepMind, Google Research, Google Cloud and Google for Health and we thank our team mates for insightful discussions and contributions.
In particular, AI co-clinician would not have been possible without the core research and engineering efforts of Aniruddh Raghu, Arthur Chen, Charlie Taylor, CJ Park, David Stutz, Devora Berlowitz, Doug Fritz, Dylan Slack, Eliseo Papa, Jack Chen, JD Velasquez, Jing Rong Lim, Katya Tregubova, Kelvin Guu, Meet Shah, Richard Green, Ryutaro Tanno, Sukhdeep Singh, Victoria Johnston, Adam Rodman.
We thank our many collaborators for their invaluable contributions, including Ali Eslami, Aliya Rysbeck, Andy Song, Anil Palepu, Anna Cupani, Bakul Patel, Bibo Xu, Brett Hatfield, David Wu, Ed Chi, Emma Cooney, Erica Oppenheimer, Erwan Rolland, Euan A. Ashley, Francesca Pietra, Rebeca Santamaria-Fernadez, Gordon Turner, Gregory Wayne, Hannah Gladman, Irene Teinemaa, Jack O'Sullivan, Jacob Koshy, Jan Freyberg, Jason Gusdorf, Joelle Wilson, Katherine Tong, Juraj Gottweis, Michael Howell, Mili Sanwalka, Pavel Dubov, Pete Clardy, Peter Brodeur, Rachelle Sico, SiWai Man, Sumanth Dahathri, Taylan Cemgil, Tim Strother, Uchechi Okereke, Valentin Lievin, Vishnu Ravi, Yana Lunts, Yun Liu, Simon Staffell, Rachel Teo, Adriana Fernandez Lara, Armin Senoner, Danielle Breen, Paula Tesch, Leen Verburgh, Dimple Vijaykumar, Juanita Bawagan, Muinat Abdul, Mariana Montes and Rob Ashley. Feature videos were produced by Christopher Godfree, Matt Mager, Emma Moxhay and Simon Waldron.
Thanks to James Manyika and Demis Hassabis for their insightful guidance and support throughout the research process.
```

---

## 3. Announcing our partnership with the Republic of Korea

- 日期: 2026-04-27 07:00
- 链接: https://deepmind.google/blog/announcing-our-partnership-with-the-republic-of-korea/

```
Announcing our partnership with the Republic of Korea
Using frontier AI to accelerate scientific breakthroughs, push the boundaries of innovation and support local talent.
Ten years ago, the historic AlphaGo match in Seoul captured the world's imagination and showcased the profound potential of artificial intelligence. Alongside this milestone anniversary, we are taking a significant step forward by announcing a new partnership between Google DeepMind and the Republic of Korea's Ministry of Science and ICT (MSIT).
We share a vision that AI will play a pivotal role in national economic development. Korea is uniquely positioned for this transformation, reaching a point where AI capabilities are becoming the foundation for future employment and innovation. The nation currently leads the world in AI innovation density and boasts the fastest-growing AI adoption rate among the world's top 30 economies.
Part of Google DeepMind’s National Partnerships for AI initiative, this collaboration is designed to support Korea's AI strategy, cultivate a thriving AI ecosystem, and accelerate groundbreaking discoveries in critical fields like life sciences, weather and climate.
Bringing frontier AI models to Korea’s scientific community
Korea’s Ministry of Science and ICT (MSIT) has recently launched the K-Moonshot Missions, an initiative aimed at unlocking step-change improvements in research productivity and addressing national grand challenges.
Helping make this vision a reality, Google will establish an AI Campus in the Republic of Korea — an AI-focused facility within its Seoul offices.
The AI Campus will be a hub for Korean academia and research institutions to collaborate with Google’s world-leading AI experts to accelerate scientific breakthroughs through research and access to our most advanced AI for Science models, programs and events. We will begin by exploring collaborations with research-oriented institutions including Seoul National University (SNU), Korea Advanced Institute of Science and Technology (KAIST) and the Ministry’s three AI Bio Innovation Hubs, leveraging our models in fields such as life sciences, energy, weather and climate, for example:
- AlphaEvolve - a Gemini-powered coding agent for designing and optimising advanced algorithms. This has shown beneficial impact across many areas in computing and math, and we are seeing similar examples emerge in drug discovery and energy.
- AlphaGenome - an AI model to help scientists better understand how mutations in human DNA sequences impact a wide range of gene functions, speeding up research on genome biology and helping to improve disease understanding.
- AlphaFold - already used by more than 85,000 researchers in Korea, we will explore accelerating AI-enabled predictions for proteins, DNA and RNA.
- AI co-scientist - a multi-agent AI system that acts as a virtual scientific collaborator to help researchers brainstorm and verify hypotheses. This is showing promising benefits in a range of biomedical applications and we look forward to collaborating through joint research exploration and technical advisory to support the Ministry’s AI Scientist Project on ways to best integrate the system.
- WeatherNext - we will explore collaborations to support Korea's energy and sustainability goals in predicting and analyzing the impacts of extreme weather events and optimizing renewable energy on grids.
Cultivating AI talent and partnering on safety
Realizing the full potential of AI requires investing in people and building responsibly. To support the next generation of Korean AI talent, we are opening doors to forge connections with Google DeepMind, including exploring internship opportunities for Korean students. This builds on Google’s broader commitment to the region, including the recent milestone of providing 50,000 AI Essentials scholarships to help job seekers gain foundational skills.
Finally, following our Frontier AI Safety Commitments made at the AI Seoul Summit, we will collaborate with the Korean AI Safety Institute (AISI) on research and best practices.
Building on the AlphaGo legacy
As we look back on the legacy of AlphaGo, we are incredibly excited for what lies ahead. We look forward to collaborating with the government as they invest in important local AI infrastructure, such as a new National AI for Science Center (NAIS), due to open in May.
By combining Google DeepMind's frontier AI models with the brilliant scientific minds in Korea, we believe we can unlock scientific discoveries that will benefit society for generations to come.
```

---

## 4. Decoupled DiLoCo: A new frontier for resilient, distributed AI training

- 日期: 2026-04-22 10:20
- 链接: https://deepmind.google/blog/decoupled-diloco/

```
Decoupled DiLoCo: A new frontier for resilient, distributed AI training
Our new distributed architecture helps to train LLMs across distant data centers - with lower bandwidth and more hardware resiliency.
Training a frontier AI model traditionally depends on a large, tightly coupled system in which identical chips must stay in near-perfect synchronization. This approach is highly effective for today’s state-of-the-art models, but as we look toward future generations of scale, maintaining this level of synchronization across thousands of chips becomes a significant logistical challenge.
Today, in a new paper we are excited to share a new approach to this problem, called Decoupled DiLoCo (Distributed Low-Communication). By dividing large training runs across decoupled “islands” of compute, with asynchronous data flowing between them, this architecture isolates local disruptions so that other parts of the system can keep learning efficiently.
The result is a more resilient and flexible way to train advanced models across globally distributed data centers. And crucially, Decoupled DiLoCo does not suffer the communication delays that made previous distributed methods like Data-Parallel impractical at global scale.
As frontier models continue to grow in scale and complexity, we’re exploring diverse approaches to train models across more compute, locations and varied hardware.
Developing more fault-tolerant asynchronous training at scale
Decoupled DiLoCo builds on two earlier advances: Pathways, which introduced a distributed AI system based on asynchronous data flow, and DiLoCo, which dramatically reduced the bandwidth required between distributed data centers, making it practical to train large language models across distant locations.
Decoupled DiLoCo brings those ideas together to train AI models more flexibly at scale. Built on top of Pathways, it enables asynchronous training across separate islands of compute (known as learner units) so that a chip failure in one area doesn’t interrupt the progress of the others.
This infrastructure is also self-healing. In testing, we used a method called “chaos engineering” to introduce artificial hardware failures during training runs. Decoupled DiLoCo continued the training process after the loss of entire learner units, and then seamlessly reintegrated them when they came back online.
Testing Decoupled DiLoCo with Gemma 4 models demonstrated that, when hardware fails, the system maintains greater availability of learning clusters than more traditional training methods — while ultimately delivering the same benchmarked level of machine learning (ML) performance.
Decoupled DiLoCo is not only more resilient to failures, but is also practical for executing production-level, fully distributed pre-training. We successfully trained a 12 billion parameter model across four separate U.S. regions using 2-5 Gbps of wide-area networking (a level relatively achievable using existing internet connectivity between datacenter facilities, rather than requiring new custom network infrastructure between facilities). Notably, the system achieved this training result more than 20 times faster than conventional synchronization methods. This is because our system incorporates required communication into longer periods of computation, avoiding the "blocking" bottlenecks where one part of the system must wait for another.
Driving the evolution of AI training infrastructure
At Google, we take a full-stack approach to AI training, spanning hardware, software infrastructure and research. Increasingly, gains are coming from rethinking how these layers fit together.
Decoupled DiLoCo is one example. By enabling training jobs at internet-scale bandwidth, it can tap any unused compute wherever it sits, turning stranded resources into useful capacity.
Beyond efficiency and resilience, this training paradigm also unlocks the ability to mix different hardware generations, such as TPU v6e and TPU v5p, in a single training run. This approach not only extends the useful life of existing hardware, but also increases the total compute available for model training. In our experiments, chips from different generations running at different speeds still matched the ML performance of single-chip-type training runs, ensuring that even older hardware can meaningfully accelerate AI training.
What’s more, because new generations of hardware don’t arrive everywhere all at once, being able to train across generations can alleviate recurring logistical and capacity bottlenecks.
As we push the frontiers of AI infrastructure today, we’re continuing to explore approaches to resilient systems needed to unlock the next generation of AI.
Acknowledgements
This work was done by a team of members across Google DeepMind and Google Research.
The leads and core contributors behind Decoupled DiLoCo are Arthur Douillard, Keith Rush, Yani Donchev, Zachary Charles, Ayush Dubey, Blake Woodworth, Ionel Gog, Josef Dean, Nova Fallen, Zachary Garrett. Operational support was done by Nate Keating and Jenny Bishop.
We are also grateful for the additional support and advising from Jeff Dean, Marc’Aurelio Ranzato, Raia Hadsell, Arthur Szlam, Edouard Yvinec, Henry Prior, Paul Barham, Michael Isard, Daniel Ramage, Brendan McMahan, Chase Hensel, and Zoltan Egyed.
```

---

## 5. Partnering with industry leaders to accelerate AI transformation

- 日期: 2026-04-21 14:54
- 链接: https://deepmind.google/blog/partnering-with-industry-leaders-to-accelerate-ai-transformation/

```
Partnering with industry leaders to accelerate AI transformation
We’re joining forces with Accenture, Bain & Company, BCG, Deloitte, and McKinsey to bring the power of frontier AI to organizations around the world.
Artificial intelligence (AI) could contribute up to $15.7 trillion to the global economy by 2030, yet many businesses face a significant adoption gap. To date, only 25% of organizations have successfully moved AI into production at scale.
At Google DeepMind, we believe AI is one of the most transformative technologies of our time, capable of delivering new products and services, and scientific breakthroughs that improve the lives of billions of people. To help businesses harness this potential responsibly, we’re partnering with Accenture, Bain & Company, BCG, Deloitte, and McKinsey to accelerate AI-driven transformation and help industries adopt frontier technology at scale. By combining our advanced research with their strategic expertise, we aim to solve complex challenges across sectors and drive global economic growth.
A new initiative for enterprise transformation
We’re partnering with global enterprise consultancies to help them deliver world-leading agentic transformation for customers at speed and scale. Together we’ll use AI to drive meaningful human impact, empowering workforces with AI tools that provide real-time data for better decision-making and management of complex tasks.
From research labs to real-world impact
This collaboration allows our partners to work directly with Google DeepMind’s world-leading technical talent. Together, we will focus on critical enterprise needs in sectors like finance, manufacturing, retail, media and entertainment.
These partnerships include three key pillars:
- Enabling scaled, industry-specific AI capabilities: We will collaborate on challenging customer use cases, supporting the development of scaled, industry-specific AI solutions.
- Early access to frontier models: Partners will receive early access to our frontier models, including the Gemini family. Their feedback on these will help us further refine these systems to ensure they’re equipped to deliver benefits for customers.
- Access to AI leadership: We will connect our leadership with customer CEOs and boards, helping them navigate the future of frontier AI research and development.
Looking ahead
These efforts build upon Google Cloud’s work supporting global consulting partners, systems integrators, software partners, and specialized services providers as they implement and scale agentic AI.
In the coming years, AI has the potential to solve critical global challenges and amplify human potential. To secure these benefits, AI must be diffused responsibly across industries, remaining guided by human expertise. We are excited to see what we can build and scale together with the world’s leading strategic partners in pursuit of these goals.
```

---

## 6. Gemini 3.1 Flash TTS: the next generation of expressive AI speech

- 日期: 2026-04-15 16:03
- 链接: https://deepmind.google/blog/gemini-3-1-flash-tts-the-next-generation-of-expressive-ai-speech/

```
Gemini 3.1 Flash TTS: the next generation of expressive AI speech
Today, we’re introducing Gemini 3.1 Flash TTS, the latest text-to-speech model that delivers improved controllability, expressivity and quality — empowering developers, enterprises and everyday users to build the next generation of AI-speech applications.
Starting today, 3.1 Flash TTS is rolling out:
- For developers in preview via the Gemini API and Google AI Studio
- For enterprises in preview on Vertex AI
- For Workspace users via Google Vids
Improved speech quality and controllability
We’ve improved the overall speech quality of Gemini 3.1 Flash TTS, making it our most natural and expressive model to date. On the Artificial Analysis TTS leaderboard, a benchmark that captures thousands of blind human preferences, 3.1 Flash TTS achieved an impressive Elo score of 1,211.
Artificial Analysis has also positioned Gemini 3.1 Flash TTS within its “most attractive quadrant” for its ideal blend of high-quality speech generation and low cost. The model stands out further with native multi-speaker dialogue, support for 70+ languages, and granular creative control via natural language.
New audio tags for more expressive speech generation
3.1 Flash TTS also introduces audio tags — an intuitive way to control vocal style, pace and delivery. By embedding natural language commands directly into the text input, you can steer AI-speech output with improved levels of granularity.
You can start experimenting with these audio tags along with other updates to the developer experience in Google AI Studio with configurable controls that place the developer in the “director’s chair”:
- Scene direction: Set the stage by defining the environment and providing specific dialogue instructions. This world-building context helps characters remain “in-character” and react to one another naturally across multiple turns.
- Speaker-level specificity: Cast characters using unique Audio Profiles, then specify Director’s Notes to toggle pace, tone and accent. Using inline tags, speakers can pivot from these high-level settings to change expression mid-sentence.
- Seamless export: Once the performance is perfected, these exact parameters can be exported as Gemini API code to ensure consistent, recognizable voices across various projects and platforms.
With these new configurations, developers can enhance precision for specific scenarios, creating memorable characters and immersive audio experiences.
Get started with high-fidelity speech generation in the Google AI Studio Playground.
Built for global scale
Gemini 3.1 Flash TTS delivers high-fidelity speech and more precise control across more than 70 languages. These core optimizations bring advanced style, pacing and accent control to major markets — helping developers create localized, expressive speech experiences for users at global scale.
Early developer and enterprise testers are already seeing the impact of 3.1 Flash TTS, highlighting its impressive controllability and expressivity. They’ve told us how audio tags provide a new level of creative precision, transforming simple text into a high-fidelity vocal performance.
Watermarked with SynthID
All audio generated by Gemini 3.1 Flash TTS is watermarked with SynthID. This imperceptible watermark is interwoven directly into the audio output, allowing the reliable detection of AI-generated content to help prevent misinformation. For more information on our approach to safety and responsibility, you can review the model card.
```

---

## 7. Gemini Robotics-ER 1.6: Powering real-world robotics tasks through enhanced embodied reasoning

- 日期: 2026-04-13 15:52
- 链接: https://deepmind.google/blog/gemini-robotics-er-1-6/

```
Gemini Robotics-ER 1.6: Powering real-world robotics tasks through enhanced embodied reasoning
For robots to be truly helpful in our daily lives and industries, they must do more than follow instructions, they must reason about the physical world. From navigating a complex facility to interpreting the needle on a pressure gauge, a robot’s “embodied reasoning” is what allows it to bridge the gap between digital intelligence and physical action.
Today, we’re introducing Gemini Robotics-ER 1.6, a significant upgrade to our reasoning-first model that enables robots to understand their environments with unprecedented precision. By enhancing spatial reasoning and multi-view understanding, we are bringing a new level of autonomy to the next generation of physical agents.
This model specializes in reasoning capabilities critical for robotics, including visual and spatial understanding, task planning and success detection. It acts as the high-level reasoning model for a robot, capable of executing tasks by natively calling tools like Google Search to find information, vision-language-action models (VLAs) or any other third-party user-defined functions.
Gemini Robotics-ER 1.6 shows significant improvement over both Gemini Robotics-ER 1.5 and Gemini 3.0 Flash, specifically enhancing spatial and physical reasoning capabilities such as pointing, counting, and success detection. We are also unlocking a new capability: instrument reading, enabling robots to read complex gauges and sight glasses — a use case we discovered through close collaboration with our partner, Boston Dynamics.
Starting today, Gemini Robotics-ER 1.6 is available to developers via the Gemini API and Google AI Studio. To help you get started, we are sharing a developer Colab containing examples of how to configure the model and prompt it for embodied reasoning tasks.
Pointing: The foundation of spatial reasoning
Pointing is a fundamental capability for an embodied reasoning model, evolving with each model generation. Points can be used to express many concepts, including:
- Spatial reasoning: Precision object detection and counting
- Relational logic: Making comparisons, such as identifying the smallest item in a set; defining "from-to" relationships (e.g move X to location Y)
- Motion reasoning: Mapping trajectories and identifying optimal grasp points
- Constraint compliance: Reasoning through complex prompts like "point to every object small enough to fit inside the blue cup"
Gemini Robotics-ER 1.6 can use points as intermediate steps to reason about more complex tasks. For example, it can use points to count items in an image, or to identify salient points on an image to help the model perform mathematical operations to improve its metric estimations.
The example below shows Gemini Robotics-ER 1.6’s strengths in pointing to multiple elements, and knowing when and when not to point.
Success Detection: The engine of autonomy
In robotics, knowing when a task is finished is just as important as knowing how to start it. Success detection is a cornerstone of autonomy, serving as a critical decision-making engine that allows an agent to intelligently choose between retrying a failed attempt or progressing to the next stage of a plan.
Achieving visual understanding in robotics is challenging, requiring sophisticated perception and reasoning capabilities combined with broad world knowledge in order to handle complicating factors such as occlusions, poor lighting and ambiguous instructions. Additionally, most modern robotics setups include multiple camera views such as an overhead and wrist-mounted feed. This means a system needs to understand how different viewpoints combine to form a coherent picture at each moment and across time.
Gemini Robotics-ER 1.6 advances multi-view reasoning, enabling the system to better understand multiple camera streams and the relationship between them, even in dynamic or occluded environments, as demonstrated in the typical multi-view scenario below.
Instrument reading: Real-world visual reasoning
To understand a key strength of Gemini Robotics-ER 1.6, we must look at how it combines capabilities like spatial reasoning and world knowledge to solve complex, real-world problems. A perfect example is instrument reading.
This task stems from facility inspection needs, a critical focus area for our partners at Boston Dynamics. Industrial facilities contain many instruments — thermometers, pressure gauges, chemical sight glasses and more — that require constant monitoring. Spot, a Boston Dynamics robot product, is able to visit the instruments throughout the facility and capture images of them.
Instrument reading requires complex visual reasoning. One must precisely perceive a variety of inputs — including the needles, liquid level, container boundaries, tick marks and more — and understand how they all relate to each other. In the case of sight glasses, this involves estimating how much the liquid fills the sightglass taking into account distortion from the camera perspective. Gauges typically have text describing the unit, which must be read and interpreted, and some have multiple needles referring to different decimal places that need to be combined.
Capabilities like instrument reading and more reliable task reasoning will enable Spot to see, understand, and react to real-world challenges completely autonomously.
Gemini Robotics-ER 1.6 achieves its highly accurate instrument readings by using agentic vision, which combines visual reasoning with code execution. The model takes intermediate steps: first zooming into an image to get a better read of small details in a gauge, then using pointing and code execution to estimate proportions and intervals and get an accurate reading, and ultimately applying its world knowledge to interpret meaning.
Read an analog gauge with accuracy
Our safest robotics model yet
Safety is integrated into every level of our embodied reasoning models. Gemini Robotics-ER 1.6 is our safest robotics model to date, demonstrating superior compliance with Gemini safety policies on adversarial spatial reasoning tasks compared to all previous generations.
The model also shows a substantially improved capacity to adhere to physical safety constraints. For example, it makes safer decisions through spatial outputs like pointing regarding which objects can be safely manipulated under gripper or material constraints (e.g., “don't handle liquids”, “don't pick up objects heavier than 20kg“).
We also tested how well the model identifies safety hazards in text and video scenarios based on real-life injury reports. On these tasks, our Gemini Robotics-ER models improve over baseline Gemini 3.0 Flash performance (+6% in text, +10% in video) in perceiving injury risks accurately.
Collaborate with us to improve embodied reasoning for robotics
We are committed to ensuring Gemini Robotics-ER provides maximum value to the robotics community. If current capabilities are limited for your specialized application, we invite you to submit this form with 10–50 labeled images illustrating specific failure modes to help us build more robust reasoning features. We look forward to collaborating with you to enhance these capabilities in our upcoming releases.
```

---

## 8. Gemma 4: Byte for byte, the most capable open models

- 日期: 2026-04-02 16:00
- 链接: https://deepmind.google/blog/gemma-4-byte-for-byte-the-most-capable-open-models/

```
Gemma 4: Byte for byte, the most capable open models
Today, we are introducing Gemma 4 — our most intelligent open models to date. Purpose-built for advanced reasoning and agentic workflows, Gemma 4 delivers an unprecedented level of intelligence-per-parameter. This breakthrough builds on incredible community momentum: since the launch of our first generation, developers have downloaded Gemma over 400 million times, building a vibrant Gemmaverse of more than 100,000 variants. We listened closely to what innovators need next to push the boundaries of AI, and Gemma 4 is our answer: breakthrough capabilities made widely accessible under an Apache 2.0 license.
Open model performance vs size on Arena.ai’s chat arena as of 4/1.
Built from the same world-class research and technology as Gemini 3, Gemma 4 is the most capable model family you can run on your hardware. They complement our Gemini models, giving developers the industry's most powerful combination of both open and proprietary tools.
Industry-leading capabilities and mobile-first AI
We are releasing Gemma 4 in four versatile sizes: Effective 2B (E2B), Effective 4B (E4B), 26B Mixture of Experts (MoE) and 31B Dense. The entire family moves beyond simple chat to handle complex logic and agentic workflows. Our larger models deliver state-of-the-art performance for their sizes, with the 31B model currently ranking as the #3 open model in the world on the industry-standard Arena AI text leaderboard, and the 26B model securing the #6 spot. There, Gemma 4 outcompetes models 20x its size. For developers, this new level of intelligence-per-parameter means achieving frontier-level capabilities with significantly less hardware overhead.
At the edge, our E2B and E4B models redefine on-device utility, prioritizing multimodal capabilities, low-latency processing and seamless ecosystem integration over raw parameter count.
Powerful, accessible, open
To power the next generation of pioneering research and products, we've sized the Gemma 4 models specifically to run and fine-tune efficiently on hardware — from billions of Android devices worldwide, to laptop GPUs, all the way up to developer workstations and accelerators.
By using these highly optimized models, you can fine-tune Gemma 4 to achieve state-of-the-art performance on your specific tasks. We've already seen incredible success with this approach; for instance, INSAIT created a pioneering Bulgarian-first language model (BgGPT), and we worked with Yale University on Cell2Sentence-Scale to discover new pathways for cancer therapy, among many others.
Here is what makes Gemma 4 our most capable open model family yet:
- Advanced reasoning: Capable of multi-step planning and deep logic, Gemma 4 demonstrates significant improvements in math and instruction-following benchmarks that require it.
- Agentic workflows: Native support for function-calling, structured JSON output, and native system instructions enables you to build autonomous agents that can interact with different tools and APIs and execute workflows reliably.
- Code generation: Gemma 4 supports high-quality offline code, turning your workstation into a local-first AI code assistant.
- Vision and audio: All models natively process video and images, supporting variable resolutions, and excelling at visual tasks like OCR and chart understanding. Additionally, the E2B and E4B models feature native audio input for speech recognition and understanding.
- Longer context: Process long-form content seamlessly. The edge models feature a 128K context window, while the larger models offer up to 256K, allowing you to pass repositories or long documents in a single prompt.
- 140+ languages: Natively trained on over 140 languages, Gemma 4 helps developers build inclusive, high-performance applications for a global audience.
Versatile models for diverse hardware
We are releasing the Gemma 4 model weights in sizes tailored for specific hardware and use cases, ensuring you get frontier-class reasoning wherever you need it:
26B and 31B models: Frontier intelligence, offline on your personal computers
Optimized to provide researchers and developers with state-of-the-art reasoning on accessible hardware, our unquantized bfloat16 weights fit efficiently on a single 80GB NVIDIA H100 GPU. For local setups, quantized versions run natively on consumer GPUs to power your IDEs, coding assistants and agentic workflows. Our 26B Mixture of Experts (MoE) focus on latency, activating only 3.8 billion of its total parameters during inference to deliver exceptionally fast tokens-per-second, while our 31B Dense is maximizing raw quality and provides a powerful foundation for fine-tuning.
These models were evaluated against a large collection of different datasets and metrics to cover different aspects of text generation. See additional benchmarks in our model card.
E2B and E4B models: A new level of intelligence for mobile and IoT devices
Engineered from the ground up for maximum compute and memory efficiency, these models activate an effective 2 billion and 4 billion parameter footprint during inference to preserve RAM and battery life. In close collaboration with our Google Pixel team and mobile hardware leaders like Qualcomm Technologies and MediaTek, these multimodal models run completely offline with near-zero latency across edge devices like phones, Raspberry Pi, and NVIDIA Jetson Orin Nano. Android developers can now prototype agentic flows in the AICore Developer Preview today for forward-compatibility with Gemini Nano 4.
An open-source license
You gave us feedback, and we listened. Building the future of AI requires a collaborative approach, and we believe in empowering the developer ecosystem without restrictive barriers. That's why Gemma 4 is released under a commercially permissive Apache 2.0 license.
This open-source license provides a foundation for complete developer flexibility and digital sovereignty; granting you complete control over your data, infrastructure, and models. It allows you to build freely and deploy securely across any environment, whether on-premises or in the cloud.
Built on a foundation of trust and safety
These models undergo the same rigorous infrastructure security protocols as our proprietary models. By choosing Gemma 4, enterprises and sovereign organizations gain a trusted, transparent foundation that delivers state-of-the-art capabilities while meeting the highest standards for security and reliability.
An ecosystem of choices
- Start experimenting in seconds: Get instant access to Gemma 4 and begin building right away. Explore Gemma 4 in Google AI Studio (31B and 26B MoE) or in Google AI Edge Gallery (E4B and E2B). For Android development, use it to power Agent Mode in Android Studio, and start building apps for production on Android with the ML Kit GenAI Prompt API.
- Use your favorite tools: With day-one support for Hugging Face (Transformers, TRL, Transformers.js, Candle), LiteRT-LM, vLLM, llama.cpp, MLX, Ollama, NVIDIA NIM and NeMo, LM Studio, Unsloth, SGLang, Cactus, Baseten, Docker, MaxText, Tunix, Keras, you have the flexibility to choose the best tools for your project.
- Download the models: Get the model weights from Hugging Face, Kaggle or Ollama.
- Customize Gemma 4 to your specific needs: Train and adapt the model using your preferred platform, like Google Colab, Vertex AI or even your gaming GPU.
- Scale to production on Google Cloud: While local on-device inference is ideal for offline use, Google Cloud removes all compute ceilings. Deploy your way through Vertex AI, Cloud Run, GKE, Sovereign Cloud, TPU-accelerated serving and the highest compliance guarantees for regulated workloads. Learn more about getting started on Google Cloud here.
- Accelerate your AI development across multiple hardware platforms: Gemma 4 is optimized for industry-leading hardware out of the box. Experience maximum performance on NVIDIA AI infrastructure from NVIDIA Jetson Orin Nano to Blackwell GPUs, integrate with AMD GPUs via the open-source ROCm™ stack, or deploy on Trillium and Ironwood TPUs for massive scale and efficiency.
- Compete for impact: Join the Gemma 4 Good Challenge on Kaggle to build products that create meaningful, positive change in the world.
```

---

## 9. Gemini 3.1 Flash Live: Making audio AI more natural and reliable

- 日期: 2026-03-26 15:23
- 链接: https://deepmind.google/blog/gemini-3-1-flash-live-making-audio-ai-more-natural-and-reliable/

```
Gemini 3.1 Flash Live: Making audio AI more natural and reliable
Today, we’re advancing Gemini’s real-time dialogue capabilities with Gemini 3.1 Flash Live, our highest-quality audio and voice model yet. It delivers the speed and natural rhythm needed for the next generation of voice-first AI, offering a more intuitive experience for developers, enterprises and everyday users.
3.1 Flash Live is available across Google products:
- For developers in preview via the Gemini Live API in Google AI Studio
- For enterprises in Gemini Enterprise for Customer Experience
- For everyone via Search Live and Gemini Live
For developers: Robust reasoning and task execution
We’ve improved 3.1 Flash Live’s overall quality, making it more reliable for developers and enterprises to build voice-first agents that can complete complex tasks at scale. On ComplexFuncBench Audio, a benchmark that captures multi-step function calling with various constraints, it leads with a score of 90.8% compared to our previous model.
On Scale AI’s Audio MultiChallenge, Gemini 3.1 Flash Live leads with a score of 36.1% with “thinking” on. The benchmark specifically tests complex instruction following and long-horizon reasoning amidst the interruptions and hesitations typical of real-world audio.
3.1 Flash Live also has improved tonal understanding to deliver more natural dialogue. In Gemini Enterprise for Customer Experience, it’s even more effective at recognizing acoustic nuances like pitch and pace than 2.5 Flash Native Audio. It’s also better at dynamically adjusting its response to users' expressions of frustration or confusion.
3.1 Flash Live lets you build voice-ready agents that handle complex tasks in noisy environments.
Illustrative demonstration built with Gemini 3.1 Pro, powered by Gemini 3.1 Flash Live.
3.1 Flash Live lets you use your voice to vibe code and quickly iterate.
Illustrative demonstration built with Gemini 3.1 Pro, powered by Gemini 3.1 Flash Live.
Companies like Verizon, LiveKit and The Home Depot have given positive feedback on 3.1 Flash Live in their workflows, highlighting its improved, natural conversation.
For everyone: More natural and intuitive interactions
In Gemini Live and Search Live, the 3.1 Flash Live model delivers more helpful and natural responses, whether you’re asking quick daily questions or engaging in more complex conversations.
With the 3.1 Flash Live model under the hood, Gemini Live delivers faster responses compared to the previous model and it can follow the thread of your conversation for twice as long, keeping your train of thought intact during longer brainstorms.
3.1 Flash Live makes Gemini Live faster and more helpful
3.1 Flash Live is also inherently multilingual, which enables this week’s global expansion of Search Live. With this launch, people in more than 200 countries and territories can now have real-time, multimodal conversations with Search in their preferred language.
Get real-time troubleshooting help using 3.1 Flash Live in Search Live
Try Gemini 3.1 Flash Live
All audio generated by 3.1 Flash Live is watermarked with SynthID. This imperceptible watermark is interwoven directly into the audio output, allowing the reliable detection of AI-generated content to help prevent misinformation. For more information on our approach to safety and responsibility, see the model card.
Experience the naturalness and reliability of 3.1 Flash Live, starting today. We look forward to seeing how you interact and build with it.
```

---

## 10. Protecting people from harmful manipulation

- 日期: 2026-03-25 16:46
- 链接: https://deepmind.google/blog/protecting-people-from-harmful-manipulation/

```
Protecting people from harmful manipulation
As AI models get better at holding natural conversations, we must examine how these interactions affect people and society.
Building on a breadth of scientific research, today, we are releasing new findings on the potential for AI to be misused for harmful manipulation*, specifically, its ability to alter human thought and behavior in negative and deceptive ways. With this latest study, we have created the first empirically validated toolkit to measure this kind of AI manipulation in the real world, which we hope will help protect people and advance the field as a whole. We’re publicly releasing all materials necessary to run human participant studies using the same methodology. (Note: The behaviors observed during this study took place in a controlled lab setting, and do not necessarily predict real-world behaviors.)
Why harmful manipulation matters
Consider two scenarios: One AI model gives you facts to make a well-informed healthcare decision that improves your well-being. Another AI model uses fear to pressure you to make an ill-informed decision that harms your health. The first educates and helps you; the second tricks and harms you.
These scenarios highlight the difference between two types of persuasion in human-AI interactions (also defined in earlier research):
- Beneficial (rational) persuasion: Using facts and evidence to help people make choices that align with their own interest
- Harmful manipulation: Exploiting emotional and cognitive vulnerabilities to trick people into making harmful choices
Our latest work helps us and the wider AI community better understand the risk of AI developing capabilities for harmful manipulation and build a scalable evaluation framework to measure this complex area. To do this effectively, we simulated misuse in high-stakes environments, explicitly prompting AI to try to negatively manipulate people's beliefs and behaviours on key topics.
Developing new evaluations for a complex challenge
Testing the outcomes of AI harmful manipulation
Testing for harmful manipulation is inherently difficult because it involves measuring subtle changes in how people think and act, varying heavily by topic, culture and context.
This is what motivated our latest research, which involved conducting nine studies involving over 10,000 participants across the UK, the US, and India. We focused on high-stakes areas such as finance, where we used simulated investment scenarios to test if AI could influence how people would behave in complex decision-making environments, and health, where we tracked if AI could influence which dietary supplements people preferred. Interestingly, the AI was least effective at harmfully manipulating participants on health-related topics.
Our findings show that success in one domain does not predict success in another, validating our targeted approach to testing for harmful manipulation in specific, high-stakes environments where AI could be misused.
How could AI manipulate?
In addition to tracking efficacy (whether the AI successfully changes minds), we also measured its propensity (how often it even tries to use manipulative tactics). We tested propensity in two scenarios: when we explicitly told the model to be manipulative, and when we didn’t.
As detailed in our research, we counted manipulative tactics in experimental transcripts, confirming the AI models were most manipulative when explicitly instructed to be.
Our results also suggest that certain manipulative tactics may be more likely to result in harmful outcomes, though further research is required to understand these mechanisms in detail.
By measuring both efficacy and propensity, we can better understand how AI manipulation works and build more targeted mitigations.
Putting research into practice
As AI becomes a part of our everyday lives, we need to know it can’t be misused to harmfully manipulate people.
Beyond this latest study, we recently introduced an exploratory Harmful Manipulation Critical Capability Level (CCL) within our Frontier Safety Framework to help us track models with capabilities which could be misused to systematically change beliefs and behaviors in direct human-AI interactions in ways which could lead to severe harm.
These evaluations also serve as the foundation for how we test our models, including Gemini 3 Pro, for harmful manipulation. You can read more about this in this safety report. Like all our safety evaluations, this is an ongoing process. We will continue to refine our models and methodologies to keep pace with advancing AI.
Looking ahead
Understanding and mitigating harmful manipulation is a complex challenge. As model capabilities evolve, so too must our evaluation and mitigation techniques. For example, we’re currently exploring how to ethically evaluate the efficacy of harmful manipulation in even higher-stakes situations—like discussions involving deeply held personal beliefs—where users might be more susceptible to influence. Next, we will be expanding our research to investigate how audio, video, and image inputs as well as agentic capabilities, factor into AI manipulation.
We’ll continue to share findings and iterate based on feedback from the Frontier Model Forum and academic community. Our goal is to lead collective progress to prevent harmful manipulation, advancing AI models that prioritize safety and empower people.
*Notes: The scope of this particular research focuses exclusively on demonstrating general manipulation capabilities to help further the scientific study of evaluating harmful manipulation. This does not relate to testing safeguards around model outputs or manipulation in policy-violating and dangerous topics (e.g. terrorism and child safety) as this work is covered elsewhere and tested separately.
You can also read more about our harmful manipulation work in this interview with our researchers and in the Gemini 3 Pro Frontier Safety Report.
Acknowledgments
Canfer Akbulut, Rasmi Elasmar, Abhishek Roy, Anthony Payne, Priyanka Suresh, Lujain Ibrahim, Seliem El-Sayed, Charvi Rastogi, Ashyana Kachra, Will Hawkins, Kristian Lum, Laura Weidinger, William Isaac, Dawn Bloxwich, Lewis Ho, Eva Lu, Jenny Brennan, Mahmoud Hassan, Mark Graham
```

---

## 11. Lyria 3 Pro: Create longer tracks in more

- 日期: 2026-03-25 16:01
- 链接: https://deepmind.google/blog/lyria-3-pro-create-longer-tracks-in-more/

```
Lyria 3 Pro: Create longer tracks in more Google products
Last month, we introduced Lyria 3, featuring custom music generation designed to spark creative expression. Now, we’re bringing our most advanced music generation model to more Google products, and introducing Lyria 3 Pro. This advanced version allows the creation of tracks up to 3 minutes long, with customization and creative control. Lyria 3 Pro better understands musical composition, so you can now prompt for specific elements like intros, verses, choruses and bridges. It’s great for experimenting with different styles or generating songs with complex transitions.
Providing new places to generate music
High-quality music generation should be accessible wherever creativity happens. Whether you are an app developer, a business or music professional, or a creator, these integrations allow you to use Lyria’s advanced musical awareness to scale your production.
Vertex AI: Lyria 3 Pro is now in public preview on Vertex AI for businesses who require on-demand audio at scale. It gives organizations the ability to scale high-fidelity production, from rapidly generating bespoke soundtracks for gaming to integrating into creative tools, music and video platforms.
Google AI Studio and the Gemini API: For developers building the next generation of creative tools, Lyria 3 provides improved musical awareness and structural coherence to offer creative flexibility. Lyria 3 Pro is now available alongside Lyria RealTime in AI Studio.
Google Vids: Vids is an AI-powered video creation app that anyone can use. With Lyria 3 and Lyria 3 Pro in Vids, you can add custom music that matches your style for everything from creative projects to marketing videos. This is rolling out to Google Workspace customers and Google AI Pro & Ultra subscribers starting this week.
Gemini app: Longer generations with Lyria 3 Pro are now available in the Gemini app, starting with paid subscribers. Lyria 3 Pro’s enhanced customization offers more space to experiment and play with longer tracks. So now, you can add more details to bring your full vision to life, or create personalized tracks for vlogs, podcasts or tutorial videos.
ProducerAI: We recently introduced ProducerAI, a collaborative music creation tool, built by musicians looking for new ways to enhance their creative process. With Lyria 3 Pro, ProducerAI offers an agentic experience designed to help artists, producers and songwriters at every level iterate on comprehensive songs. It’s available globally to free and paid subscribers.
Partnering with creatives
We have been developing our music generation tools responsibly and in close partnership with the industry to ensure AI serves as a tool for creative expression.
Through our Music AI Sandbox, we provide musicians, producers and songwriters with a suite of experimental tools designed to expand their creative horizons. The insights from this collaboration helped shape the development of Lyria 3.
We’re inviting artists to integrate AI into their workflows to make sure our technology helps the people who use it. Grammy-winning producer Yung Spielburg used Lyria in his composition and production process for the score of the Google DeepMind short film “Dear Upstairs Neighbors.” And we’re also collaborating with DJ and producer François K, who used Lyria in an iterative process to create a soon-to-be-released song.
Responsibility was foundational, and remains integral in the design and training of Lyria 3, using materials that YouTube and Google has a right to use under our terms of service, partner agreements, and applicable law. To protect original expression, Lyria 3 and Gemini do not mimic artists; if a prompt names a creator, the model takes that as broad inspiration. Additionally, we employ filters to check outputs against existing content and users must adhere to the Terms of Service and Gen AI prohibited use policies, which prohibit violating others' intellectual property and privacy rights. All Lyria 3 and Lyria 3 Pro outputs are embedded with SynthID, our imperceptible watermark for identifying Google AI-generated content.
Lyria 3 Pro is rolling out to professionals, developers, organizations and everyday creators to help craft high quality music generations.
```

---

## 12. Measuring progress toward AGI: A cognitive framework

- 日期: 2026-03-17 16:03
- 链接: https://deepmind.google/blog/measuring-progress-toward-agi-a-cognitive-framework/

```
Measuring progress toward AGI: A cognitive framework
Artificial General Intelligence (AGI) has the potential to accelerate scientific discovery and help solve some of humanity’s most pressing problems. But it can be difficult to know how close we are to this key milestone, because there’s a lack of empirical tools for evaluating systems’ general intelligence. Tracking progress toward AGI will require a wide range of methods and approaches, and we believe cognitive science provides one important piece of the puzzle.
That’s why today, we’re releasing a new paper, “Measuring Progress Toward AGI: A Cognitive Taxonomy,” that presents a scientific foundation for understanding the cognitive capabilities of AI systems.
Alongside the paper, we are partnering with Kaggle to launch a hackathon, inviting the research community to help build the evaluations needed to put this framework into practice.
Deconstructing general intelligence
Our framework draws on decades of research from psychology, neuroscience and cognitive science to develop a cognitive taxonomy. It identifies 10 key cognitive abilities that we hypothesize will be important for general intelligence in AI systems:
- Perception: extracting and processing sensory information from the environment
- Generation: producing outputs such as text, speech and actions
- Attention: focusing cognitive resources on what matters
- Learning: acquiring new knowledge through experience and instruction
- Memory: storing and retrieving information over time
- Reasoning: drawing valid conclusions through logical inference
- Metacognition: knowledge and monitoring of one's own cognitive processes
- Executive functions: planning, inhibition and cognitive flexibility
- Problem solving: finding effective solutions to domain-specific problems
- Social cognition: processing and interpreting social information and responding appropriately in social situations
To understand AI capabilities across these cognitive abilities, we propose a three-stage evaluation protocol that benchmarks system performance in relation to human capabilities:
- Evaluate AI systems across a broad suite of cognitive tasks covering each ability, using held-out test sets to prevent data contamination
- Collect human baselines for the same tasks from a demographically representative sample of adults
- Map each AI system’s performance relative to the distribution of human performance in each ability
Going from theory to practice
Defining these cognitive abilities is a crucial first step, but we need more than a framework to measure progress. To put this theory into practice, we are launching a new Kaggle hackathon — “Measuring progress toward AGI: Cognitive abilities”. The hackathon encourages the community to design evaluations for five cognitive abilities where the evaluation gap is the largest: learning, metacognition, attention, executive functions and social cognition.
Participants can use Kaggle's newly launched Community Benchmarks platform to build and test their evaluations against a lineup of frontier models.
We are offering a total prize pool of $200,000: $10,000 awards for the top two submissions in each of the five tracks, and $25,000 grand prizes for the four absolute best overall submissions. Submissions are open March 17 through April 16, and we’ll announce the results June 1. Head over to the Kaggle website to start building.
```

---

## 13. From games to biology and beyond: 10 years of AlphaGo’s impact

- 日期: 2026-03-09 13:52
- 链接: https://deepmind.google/blog/10-years-of-alphago/

```
From games to biology and beyond: 10 years of AlphaGo’s impact
Ten years ago, our AI system AlphaGo became the first program to defeat a world champion at the complex game of Go – reaching a milestone in the field a decade before many experts thought possible.
The achievement heralded the beginning of what is now recognized as the modern era in artificial intelligence (AI). With a single creative play, the famous ‘Move 37,’ AlphaGo demonstrated the potential of AI and signaled that we now had the techniques to begin tackling real-world scientific problems.
Today, this breakthrough continues to inform our work building systems on the path to artificial general intelligence (AGI). We believe AGI will be the most profound technology ever invented and potentially the ultimate tool to advance science, medicine, and productivity.
A creative spark
In 2016, over 200 million people watched AlphaGo face world-champion Go player Lee Sae Dol in Seoul. The match was defined by ‘Move 37’ in Game 2, a play so unconventional that professional commentators initially thought it was a mistake. But it proved to be decisive. One hundred or so moves later, the stone was in exactly the right position for AlphaGo to win the game. It was a display of incredible foresight and the AI system’s ability to go beyond mimicking human experts and find entirely new strategies.
Go has long been a proving ground for AI research because of the game’s sheer complexity. There are 10170 possible positions on the board—far more than the number of atoms in the observable universe.
To make the game tractable, AlphaGo used deep neural networks combined with advanced search and reinforcement learning – an AI approach DeepMind pioneered.
AlphaGo learned a model of plausible Go moves by first learning from games played by human experts, and then playing hundreds of thousands of games against itself, improving as the strongest winning strategies were reinforced. The system then considered only the most potentially fruitful paths and from that smaller subset of moves, found the one most likely to lead it to win.
After AlphaGo, we built AlphaGo Zero, which learned the game from completely random play and became arguably the strongest player in history. Then we generalized the system further with AlphaZero, which taught itself from scratch to master any 2-player perfect information game, including Go, chess, and shogi. Beginning with no prior knowledge other than the rules of the game, AlphaZero was able to learn to master chess in a matter of hours, and beat not only the top human players but the best specialised chess programs at the time, like Stockfish. And even though chess had been so heavily analysed with the aid of these programs, just as with Go, AlphaZero was still able to come up with interesting new strategies.
It was further proof of what I knew the moment we won the match in Seoul - the technology was ready to be applied to our real goal of accelerating scientific breakthroughs.
I believe the greatest lesson AlphaGo offered was a definitive preview of the AI era—proving it wasn’t some distant, vague future, but a reality arriving on our doorstep. It served as a "roadmap from the future," sending a clear signal to humanity about how the world was about to change.
Catalyzing breakthroughs in science
By proving it could navigate the massive search space of a Go board, AlphaGo demonstrated the potential for AI to help us better understand the vast complexities of the physical world. We started by attempting to solve the protein folding problem, a 50-year grand challenge of predicting the 3D structure of proteins - information that is crucial for understanding diseases and developing new drugs.
In 2020, we finally cracked this longstanding scientific problem with our AlphaFold 2 system. From there, we folded the structures for all 200 million proteins known to science and made them freely available to scientists in an open-source database. Today, over 3 million researchers around the world use the AlphaFold database to accelerate their important work on everything from malaria vaccines to plastic-eating enzymes. And in 2024, it was the honor of a lifetime for John Jumper and I to be awarded the Nobel Prize in Chemistry for leading this project, on behalf of the entire AlphaFold team.
Since AlphaGo’s win, we’ve applied its groundbreaking approach to many other areas of science and mathematics, including:
Mathematical reasoning: The most direct descendant of AlphaGo’s architecture, AlphaProof learned to prove formal mathematical statements using a combination of language models and AlphaZero’s reinforcement learning and search algorithms. Alongside AlphaGeometry 2, it became the first system to achieve a medal-standard (silver) at the International Mathematical Olympiad (IMO), proving AlphaGo's methods could unlock advanced mathematical reasoning and laying the foundation for our most capable general models.
Gemini, our largest and most capable model, recently went even further. An advanced version of its Deep Think mode achieved gold-medal level performance at the 2025 IMO using an approach inspired by AlphaGo. Since then, Deep Think has been applied to even more complex, open-ended challenges across science and engineering.
Algorithm discovery: Just as AlphaGo searched for the best move in a game, our coding agent AlphaEvolve explores the space of computer code to discover more efficient algorithms. It had its own Move 37 moment when it found a novel way to multiply matrices, a fundamental mathematical operation powering nearly all modern neural networks. AlphaEvolve is now being tested on problems ranging from data center optimization to quantum computing.
Scientific collaboration: We are integrating the search and reasoning principles pioneered with AlphaGo into an AI co-scientist. By having agents 'debate' scientific ideas and hypotheses, this system acts as a collaborator capable of performing the rigorous thinking necessary to identify patterns in data and solve sophisticated problems. In validation studies at Imperial College London, it analyzed decades of literature and independently arrived at the same hypothesis about antimicrobial resistance that researchers had spent years developing and validating experimentally.
We’ve also used AI to better understand the genome, advance fusion energy research, improve weather prediction and more.
As impressive as our scientific models are, they are highly specialized. To achieve fundamental breakthroughs like creating limitless clean energy or solving diseases that we don’t understand today, we need general AI systems that can find underlying structure and connections between different subject areas, and help us to come up with new hypotheses like the best scientists do.
Future of intelligence
For an AI to be truly general, it needs to understand the physical world. We built Gemini to be multimodal from the beginning so it could understand not just language, but also audio, video, images and code to build a model of the world.
To think and reason across these modalities, the latest Gemini models use some of the techniques we pioneered with AlphaGo and AlphaZero.
The next generation of AI systems will also need to be able to call upon specialized tools. For example, if a model needed to know the structure of a protein it could use AlphaFold for that.
We think the combination of Gemini’s world models, AlphaGo’s search and planning techniques, and specialized AI tool use will prove to be critical for AGI.
True creativity is a key capability that such an AGI system would need to exhibit. Move 37 was a glimpse of AI’s potential to think outside the box, but true original invention will require something more. It would need to not only come up with a novel Go strategy, as AlphaGo impressively did, but actually invent a game as deep and elegant, and as worthy of study as Go.
Ten years after AlphaGo’s legendary victory, our ultimate goal is on the horizon. The creative spark first seen in Move 37 catalyzed breakthroughs that are now converging to pave the path towards AGI - and usher in a new golden age of scientific discovery.
```

---

## 14. Gemini 3.1 Flash-Lite: Built for intelligence at scale

- 日期: 2026-03-03 16:35
- 链接: https://deepmind.google/blog/gemini-3-1-flash-lite-built-for-intelligence-at-scale/

```
Gemini 3.1 Flash-Lite: Built for intelligence at scale
Today, we're introducing Gemini 3.1 Flash-Lite, our fastest and most cost-efficient Gemini 3 series model. Built for high-volume developer workloads at scale, 3.1 Flash-Lite delivers high quality for its price and model tier.
Starting today, 3.1 Flash-Lite is rolling out in preview to developers via the Gemini API in Google AI Studio and for enterprises via Vertex AI.
Cost-efficiency without compromise
Priced at just $0.25/1M input tokens and $1.50/1M output tokens, 3.1 Flash-Lite delivers enhanced performance at a fraction of the cost of larger models. It outperforms 2.5 Flash with a 2.5X faster Time to First Answer Token and 45% increase in output speed, according to the Artificial Analysis benchmark while maintaining similar or better quality. This low latency is needed for high-frequency workflows, making it an ideal model for developers to build responsive, real-time experiences.
Gemini 3.1 Flash-Lite outperforms 2.5 Flash in speed and quality.
3.1 Flash-Lite achieves an impressive Elo score of 1432 on the Arena.ai Leaderboard and outperforms other models of similar tier across reasoning and multimodal understanding benchmarks, including 86.9% on GPQA Diamond and 76.8% on MMMU Pro–even surpassing larger Gemini models from prior generations like 2.5 Flash.
Adaptive intelligence at scale for developers
Beyond its raw performance, Gemini 3.1 Flash-Lite comes standard with thinking levels in AI Studio and Vertex AI, giving developers the control and flexibility to select how much the model “thinks” for a task, which is critical for managing high-frequency workloads. 3.1 Flash-Lite can tackle tasks at scale, like high-volume translation and content moderation, where cost is a priority. And it can also handle more complex workloads where more in-depth reasoning is needed, like generating user interfaces and dashboards, creating simulations or following instructions.
3.1 Flash-Lite instantly fills an e-commerce wireframe with hundreds of products in different categories.
3.1 Flash-Lite can generate dynamic weather dashboards in real-time, using live forecasts and historical data.
3.1 Flash-Lite creates a SaaS agent capable of executing versatile, multi-step tasks for a business.
3.1 Flash-Lite can analyze and sort large numbers of content like images quickly.
Early-access developers on AI Studio and Vertex AI, and companies like Latitude, Cartwheel and Whering are already using 3.1 Flash-Lite to solve complex problems at scale. Early testers highlighted 3.1 Flash-Lite’s efficiency and reasoning capabilities, saying it can handle complex inputs with the precision of a larger-tier model, plus follow instructions and maintain adherence.
We look forward to seeing what you build with 3.1 Flash-Lite and the rest of the Gemini 3 series models.
```

---

## 15. Nano Banana 2: Combining Pro capabilities with lightning-fast speed

- 日期: 2026-02-26 16:01
- 链接: https://deepmind.google/blog/nano-banana-2-combining-pro-capabilities-with-lightning-fast-speed/

```
Nano Banana 2: Combining Pro capabilities with lightning-fast speed
In August of last year, our Gemini Image model, Nano Banana, became a viral sensation, redefining image generation and editing. Then in November, we released Nano Banana Pro, offering users advanced intelligence and studio-quality creative control. Today, we’re bringing the best of both worlds to users across Google.
Introducing Nano Banana 2 (Gemini 3.1 Flash Image), our latest state-of-the-art image model. Now you can get the advanced world knowledge, quality and reasoning you love in Nano Banana Pro, at lightning-fast speed.
Intelligence and visual quality at Flash speed
Nano Banana 2 brings the high-speed intelligence of Gemini Flash to visual generation, making rapid edits and iteration possible. It makes once-exclusive Pro features accessible to a wider audience, including:
- Advanced world knowledge: The model pulls from Gemini’s real-world knowledge base, and is powered by real-time information and images from web search to more accurately render specific subjects. This deep understanding also helps you create infographics, turn notes into diagrams and generate data visualizations.
- Precision text rendering and translation: Nano Banana 2 allows you to generate accurate, legible text for marketing mockups or greeting cards. You can even translate and localize text within an image to share your ideas globally.
A flat lay infographic depicting the water cycle
Triptych infographic comparing cloud types
Museum Clos Lucé in Synthetic Cubism style
Localized "Native Wildlife" sign
Enhanced creative control
Nano Banana 2 also dramatically closes the gap between speed and visual fidelity, delivering high-quality, photorealistic imagery. Here’s what our newest model offers and has improved on from the original Nano Banana:
- Subject consistency: Maintain character resemblance of up to five characters and the fidelity of up to 14 objects in a single workflow, allowing you to storyboard and build narratives without altering the appearance of your inputs.
- Precise instruction following: With enhanced instruction following, the model adheres more strictly to your complex requests, capturing the specific nuances of your idea so the image you get is the image you asked for.
- Production-ready specs: Make attention grabbing assets with full control of various aspect ratios and resolutions from 512px to 4K, ensuring your visuals stay sharp whether they are for a vertical social post or a wide-screen backdrop.
- Visual fidelity upgrade: Nano Banana 2 delivers vibrant lighting, richer textures and sharper details, maintaining high-quality aesthetics at the speed expected from Flash.
Joyful characters and items at a farm
Fluffy friends building a treehouse
Misty panoramic aerial shot of a verdant valley
Highly stylized pop-art fashion portrait in different aspect ratios
Try Nano Banana 2 today
Whatever your needs, we now offer the perfect tool for every workflow: Nano Banana Pro for high-fidelity tasks requiring maximum factual accuracy, or Nano Banana 2 for rapid generation, precise instruction following and integrated image-search grounding.
Nano Banana 2 is rolling out today across Google products, including:
- Gemini app: Nano Banana 2 will replace Nano Banana Pro across the Fast, Thinking and Pro models. Google AI Pro and Ultra subscribers will keep access to Nano Banana Pro for specialized tasks by regenerating images via the three-dot menu.
- Search: In AI Mode and Lens, through the Google app as well as mobile and desktop browsers. View availability here, including 141 new countries and territories and eight additional languages.
- AI Studio + API: Available in preview in AI Studio and Gemini API. Pricing here. Also available in Google Antigravity.
- Google Cloud: Available in preview with the Gemini API in Vertex AI.
- Flow: Nano Banana 2 is the new default image generation model in Flow, available to all Flow users for zero credits.
- Google Ads: Nano Banana 2 is available now, powering suggestions while creating campaigns in Google Ads.
Try Nano Banana 2 in the Gemini app, using the new templates feature.
World knowledge from Nano Banana 2 in AI Mode in Search.
Subject preservation from Nano Banana 2 in Flow.
Robust provenance: marking and verification
As generative media evolves, so must the tools we use to identify and understand it. We continue to deepen our provenance approach, by coupling our state-of-the-art SynthID technology with interoperable C2PA Content Credentials, we provide users with a more holistic and contextual view of not just if AI was used, but how.
Our provenance tools are already making an impact. Since its launch in November, our SynthID verification feature in Gemini app has been used over 20 million times across various languages, helping people identify Google AI-generated images, video and audio. We’ll soon be bringing C2PA verification to the Gemini app, too.
```

---

## 16. Gemini 3.1 Pro: A smarter model for your most complex tasks

- 日期: 2026-02-19 16:06
- 链接: https://deepmind.google/blog/gemini-3-1-pro-a-smarter-model-for-your-most-complex-tasks/

```
Gemini 3.1 Pro: A smarter model for your most complex tasks
Last week, we released a major update to Gemini 3 Deep Think to solve modern challenges across science, research and engineering. Today, we’re releasing the upgraded core intelligence that makes those breakthroughs possible: Gemini 3.1 Pro. We are shipping 3.1 Pro across our consumer and developer products to bring this progress in intelligence to your everyday applications.
Starting today, 3.1 Pro is rolling out:
- For developers in preview via the Gemini API in Google AI Studio, Gemini CLI, our agentic development platform Google Antigravity and Android Studio
- For enterprises in Vertex AI and Gemini Enterprise
- For consumers via the Gemini app and NotebookLM
Building on the Gemini 3 series, 3.1 Pro represents a step forward in core reasoning. 3.1 Pro is a smarter, more capable baseline for complex problem-solving. This is reflected in our progress on rigorous benchmarks. On ARC-AGI-2, a benchmark that evaluates a model’s ability to solve entirely new logic patterns, 3.1 Pro achieved a verified score of 77.1%. This is more than double the reasoning performance of 3 Pro.
Intelligence applied
3.1 Pro is designed for tasks where a simple answer isn’t enough, taking advanced reasoning and making it useful for your hardest challenges. This improved intelligence can help in practical applications — whether you’re looking for a clear, visual explanation of a complex topic, a way to synthesize data into a single view, or bringing a creative project to life.
Code-based animation: 3.1 Pro can generate website-ready, animated SVGs directly from a text prompt. Because these are built in pure code rather than pixels, they remain crisp at any scale and maintain incredibly small file sizes compared to traditional video.
Complex system synthesis: 3.1 Pro utilizes advanced reasoning to bridge the gap between complex APIs and user-friendly design. In this example, the model built a live aerospace dashboard, successfully configuring a public telemetry stream to visualize the International Space Station’s orbit.
Interactive design: 3.1 Pro codes a complex 3D starling murmuration. It doesn't just generate the visual code; it builds an immersive experience where users can manipulate the flock with hand-tracking and listen to a generative score that shifts based on the birds’ movement. For researchers and designers, this provides a powerful way to prototype sensory-rich interfaces.
Creative coding: 3.1 Pro can translate literary themes into functional code. When prompted to build a modern personal portfolio for Emily Brontë’s "Wuthering Heights," the model didn’t just summarize the text. It reasoned through the novel’s atmospheric tone to design a sleek, contemporary interface, creating a website that captures the essence of the protagonist.
What’s next
Since releasing Gemini 3 Pro in November, your feedback and the pace of progress have driven these rapid improvements. We are releasing 3.1 Pro in preview today to validate these updates and continue to make further advancements in areas such as ambitious agentic workflows before we make it generally available soon.
Starting today, Gemini 3.1 Pro in the Gemini app is rolling out with higher limits for users with the Google AI Pro and Ultra plans. 3.1 Pro is also now available on NotebookLM exclusively for Pro and Ultra users. And developers and enterprises can access 3.1 Pro now in preview in the Gemini API via AI Studio, Antigravity, Vertex AI, Gemini Enterprise, Gemini CLI and Android Studio.
We can’t wait to see what you build and discover with it.
```

---

## 17. A new way to express yourself: Gemini can now create music

- 日期: 2026-02-18 16:01
- 链接: https://deepmind.google/blog/a-new-way-to-express-yourself-gemini-can-now-create-music/

```
A new way to express yourself: Gemini can now create music
Since launching the Gemini app, we've built tools to encourage creative expression through images and video. Today, we're taking the next step: custom music generation. Lyria 3, Google DeepMind’s latest generative music model, is rolling out today in beta in the Gemini app. Just describe an idea or upload a photo, like “a comical R&B slow jam about a sock finding their match" and in a matter of seconds, Gemini will translate it into a high-quality, catchy track. To push the creative envelope further, you can even ask Gemini to take inspiration from something you upload.
Lyria 3 improves on audio generation from our Lyria models in three important ways:
- No need to provide your own lyrics! They'll be generated for you based on your prompt.
- You have more creative control over elements like the style, vocals and tempo you want.
- You can create more realistic and musically complex tracks.
Here’s how you can use it:
- Text to track: Describe a specific genre, mood, inside joke, or memory to create unique tracks with lyrics or instrumental audio that fits your vibe. “I’m feeling nostalgic. Create a track for my mother about the great times we had as kids and the memories of her home cooked plantains. Make it a fun afrobeat track with a true African vibe.”
- From photos and videos to track: Upload a photo or video and watch Gemini use the content to compose a track with lyrics that fit the mood perfectly. “Use these photos to create a track about my dog Duncan on a hike in the woods.”
The Gemini app creates 30-second tracks with custom cover art generated by Nano Banana. This makes it easy to quickly share with friends by downloading or simply clicking the share link. The goal of these tracks isn't to create a musical masterpiece, but rather to give you a fun, unique way to express yourself.
Creators can also explore Lyria 3 on YouTube’s Dream Track. Available in the U.S. and now rolling out to YouTube creators in other countries, Lyria 3 will enhance the quality of each unique Shorts soundtrack. Whether it's creating a lyrical verse or a vibey backing track, being able to better customize the soundtrack will take creators’ Shorts to the next level.
New audio verification capabilities
All tracks generated in the Gemini app are embedded with SynthID, our imperceptible watermark for identifying Google AI-generated content. We are also giving you more tools to help identify AI content, broadening our verification capabilities in the Gemini app to include audio, along with image and video. Simply upload a file and ask if it was generated using Google AI, and Gemini will check for SynthID and use its own reasoning to return a response.
Our commitment to developing generative AI responsibly
Since we first launched Lyria in 2023, we've sought to develop this technology responsibly in collaboration with the music community. We've learned a lot through these collaborations and our experiments, like Music AI Sandbox, and have been very mindful of copyright and partner agreements as we've trained Lyria 3.
Music generation with Lyria 3 is designed for original expression, not for mimicking existing artists. If your prompt names a specific artist, Gemini will take this as broad creative inspiration and create a track that shares a similar style or mood. We also have filters in place to check outputs against existing content. We recognize that our approach might not be foolproof, so you can report content that may violate your rights or the rights of others. Additionally, in order to use our products, users must adhere to our Terms of Service and Gen AI prohibited use policies, which prohibit violations of others’ intellectual property and privacy rights.
Lyria 3 is available in the Gemini app for all users 18+ in English, German, Spanish, French, Hindi, Japanese, Korean and Portuguese, with plans to expand quality and coverage of more languages, rolling out on desktop today and to the mobile app over the next several days. And Google AI Plus, Pro and Ultra subscribers will enjoy higher limits.
Our goal with music generation in the Gemini app is to help you add a fun, custom soundtrack to your daily life. Try it out today at gemini.google.com.
```

---

## 18. Accelerating discovery in India through AI-powered science and education

- 日期: 2026-02-17 13:42
- 链接: https://deepmind.google/blog/accelerating-discovery-in-india-through-ai-powered-science-and-education/

```
Accelerating discovery in India through AI-powered science and education
Introducing our National Partnerships for AI and collaboration in India
We believe AI will be the most transformative technology in human history and that it should be deployed in ways that benefit all of humanity. This requires deep, strategic collaboration between frontier AI labs, governments, academia, and civil society.
To fully realise AI’s potential, Google DeepMind is working with governments through our National Partnerships for AI initiative to broaden access to our frontier AI capabilities, helping ensure they are deployed to serve citizens and meet national priorities in science, education, resilience, and public services.
Building on our collaborations with the US and UK governments, we are establishing a new partnership with Indian government bodies and local institutions. In the global AI transformation, India is showing exceptional leadership in applying the technology to tackle its own biggest challenges. But India is going even further, playing a critical international role by convening this week the fourth global AI summit of governments, companies and civil society. International dialogue and collaboration will guide positive impacts and create the global frameworks required to prepare society for a future with AI.
Partnership in India to broaden AI access
Our partnerships are designed to accelerate the pace of progress across India. Here are a few ways we are working together to unlock new possibilities in science and education.
Advancing scientific breakthroughs
Google DeepMind, Google Research and Google.org are partnering with the Anusandhan National Research Foundation (ANRF) to facilitate the adoption of AI models to advance science. We’re providing access to our frontier AI for Science models, supporting hackathons and community contests, and enabling training and mentorship to students, researchers, and those in the early stages of their careers.
Researchers and engineers in India will be able to use our AI tools, including:
- AlphaGenome: An AI model to help scientists better understand how mutations in human DNA sequences impact a wide range of gene functions
- AI Co-scientist: A multi-agent AI system that acts as a virtual scientific collaborator
- Earth AI: A collection of models built on Gemini’s advanced reasoning that are helping enterprises, nonprofits, and cities with everything from environmental monitoring to disaster response
Scientists around the world are already using AlphaFold - our AI system capable of accurately predicting the structure and interactions of proteins, DNA, RNA, ligands and more - to accelerate discoveries. India stands as the fourth largest adopter of AlphaFold globally, with over 180,000 researchers using it today. We hope to see Indian scientists benefit even more from using AlphaGenome and the other AI systems we are now providing.
We're also working to support AI for science at a global level. This is why, today at the India Summit, we announced the $30 million Google.org Impact Challenge: AI for Science, an open call for researchers, nonprofits, and social enterprises in India, and around the world, using AI to achieve scientific breakthroughs. Selected awardees will also have the opportunity to participate in a Google.org Accelerator, receiving engineering support, expert mentorship, and infrastructure from Google DeepMind and Google Research to turn their concepts into scalable discoveries.
Empowering India’s Students and Teachers with an AI-powered Future
Our recent survey with Ipsos has shown that learning is the top motivation for using AI globally. This is especially true in India, which now leads the world in daily Gemini usage by students. We’re seeing AI can drive profound comprehension and critical thinking when it is purpose-built for learning and implemented as a supportive partner to educators.
At City Montessori School in Lucknow, teachers are integrating Guided Learning into math classes for Grade 8-9 students and seeing a positive response. An early analysis of a randomized control study conducted by Fab AI shows that students are demonstrating a desire for deeper learning, not just quick answers: in almost three out of every four conversations on Gemini, students sought to develop their understanding rather than a quick answer or shortcut.
That’s why we’re expanding efforts with additional partners to supercharge the potential of learning for more Indian students and teachers:
- Powering innovation hubs with GenAI assistants: Together with Atal Tinkering Labs, which serves more than 10,000 Indian schools and 11 million students, we will help incorporate robotics and coding into local curricula, integrate Gemini thoughtfully into teacher workflows, and build a safely guardrailed AI assistant for students grounded in national curriculum standards that can act as an educational partner. Teachers can access real-time tips to help students fix a robot missing a part with readily available materials or mend a broken circuit design by simply pointing a camera to it or asking Gemini in chat.
- Transforming textbooks into interactive digital journeys: In a first-of-its-kind partnership with PM Publishers Pvt. Ltd., a K-12 textbook publisher in India, Gemini will be used to transform two million static textbooks into AI-powered interactive journeys across more than 250 titles and 2,000 schools. Each book features a QR code that can be scanned by students to access a custom Gem (specialized versions of the Gemini AI model), that acts as an expert assistant on the subject, providing summaries and responses on the contents of the respective book.
- Serving India’s linguistic diversity: There is incredible potential for AI to make a positive impact on education when built in close partnership with experts and grounded in local language and culture. Building on Google.org’s recent $2 million founding contribution to establish the new Indic Language Technologies Research Hub at IIT Bombay, we’ll help incorporate India’s linguistic diversity into AI as it advances globally.
These efforts build on the global success of existing AI literacy programs like Experience AI, a joint partnership developed by Google DeepMind with Raspberry Pi Foundation, which has already reached up to 300,000 students and 8,000 teachers in India.
AI solutions for India’s agriculture and energy sectors
Our new partnerships in science and education build on our ongoing collaboration with local Indian organizations to tackle global challenges in agriculture and energy security. Working with Indian startups, institutions like Council on Energy, Environment and Water (CEEW), and Indian state and central government entities are using the APIs of our freely available Agri AI models to enhance agricultural resilience, crop productivity and farmer incomes. TerraStack is also using Google AI to combine satellite, crop, and weather data, into hyper-local insights that help farmers make better agricultural decisions.
We also recently announced a growing collaboration with Open Climate Fix to integrate our WeatherNext AI models into India’s electricity grid operations. We’re aiming to significantly improve the accuracy of renewable energy forecasts in India, help grid operators manage volatility, and support the country’s ambitious clean energy targets. When we tested the integration of WeatherNext into OCF’s wind generation forecast, results showed up to 8% accuracy improvement in forecast performance.
This partnership comes as India rapidly scales its renewable capacity, becoming the third largest generator of solar energy globally in 2023, with an ambitious target of installing 500 GW of renewable capacity by 2030. Working together on energy solutions has never been more important - we remain committed to working with experts in India to progress this effort together to prepare for the future.
Preparing for the future together
AI’s global impact is inevitable, but its success is not. To turn potential into prosperity, we are committing to deep, local collaboration with India's government bodies and institutions to ensure AI delivers tangible results across the subcontinent–and the world.
```

---

## 19. Gemini 3 Deep Think: Advancing science, research and engineering

- 日期: 2026-02-12 16:15
- 链接: https://deepmind.google/blog/gemini-3-deep-think-advancing-science-research-and-engineering/

```
Gemini 3 Deep Think: Advancing science, research and engineering
Today, we’re releasing a major upgrade to Gemini 3 Deep Think, our specialized reasoning mode, built to push the frontier of intelligence and solve modern challenges across science, research, and engineering.
We updated Gemini 3 Deep Think in close partnership with scientists and researchers to tackle tough research challenges — where problems often lack clear guardrails or a single correct solution and data is often messy or incomplete. By blending deep scientific knowledge with everyday engineering utility, Deep Think moves beyond abstract theory to drive practical applications.
The new Deep Think is now available in the Gemini app for Google AI Ultra subscribers and, for the first time, we’re also making Deep Think available via the Gemini API to select researchers, engineers and enterprises. Express interest in early access here.
Here is how our early testers are already using the latest Deep Think:
Lisa Carbone, a mathematician at Rutgers University, works on the mathematical structures required by the high-energy physics community to bridge the gap between Einstein’s theory of gravity and quantum mechanics. In a field with very little existing training data, she used Deep Think to review a highly technical mathematics paper. Deep Think successfully identified a subtle logical flaw that had previously passed through human peer review unnoticed.
At Duke University, the Wang Lab utilized Deep Think to optimize fabrication methods for complex crystal growth for the potential discovery of semiconductor materials. Deep Think successfully designed a recipe for growing thin films larger than 100 μm, meeting a precise target that previous methods had challenges to hit.
Anupam Pathak, an R&D lead in Google’s Platforms and Devices division and former CEO of Liftware, tested the new Deep Think to accelerate the design of physical components.
Elevating reasoning with mathematical and algorithmic rigor
Last year, we showed that specialized versions of Deep Think could successfully navigate some of the toughest challenges in reasoning, achieving gold-medal standards at math and programming world championships. More recently, Deep Think has enabled specialized agents to conduct research-level mathematics exploration.
The updated Deep Think mode continues to push the frontiers of intelligence, reaching new heights across the most rigorous academic benchmarks, including:
- Setting a new standard (48.4%, without tools) on Humanity’s Last Exam, a benchmark designed to test the limits of modern frontier models
- Achieving an unprecedented 84.6% on ARC-AGI-2, verified by the ARC Prize Foundation
- Attaining a staggering Elo of 3455 on Codeforces, a benchmark consisting of competitive programming challenges
- Reaching gold-medal level performance on the International Math Olympiad 2025
Navigating complex scientific domains
Beyond mathematics and competitive coding, Gemini 3 Deep Think now also excels across broad scientific domains such as chemistry and physics. Our updated Deep Think mode demonstrates gold medal-level results on the written sections of the 2025 International Physics Olympiad and Chemistry Olympiad. It also demonstrates proficiency in advanced theoretical physics, achieving a score of 50.5% on CMT-Benchmark.
Accelerating real-world engineering
In addition to its state-of-the-art performance, Deep Think is built to drive practical applications, enabling researchers to interpret complex data, and engineers to model physical systems through code. Most importantly, we are working to bring Deep Think to researchers and practitioners where they need it most — beginning with surfaces such as the Gemini API.
With the updated Deep Think, you can turn a sketch into a 3D-printable reality. Deep Think analyzes the drawing, models the complex shape and generates a file to create the physical object with 3D printing.
Available to Google AI Ultra Subscribers and the Gemini API via our Early Access Program
Google AI Ultra subscribers will be able to access the updated Deep Think mode starting today in the Gemini app. Scientists, engineers and enterprises can also now express interest in our early access program to test Deep Think via the Gemini API.
We can’t wait to see what you discover.
```

---

## 20. Accelerating Mathematical and Scientific Discovery with Gemini Deep Think

- 日期: 2026-02-09 16:12
- 链接: https://deepmind.google/blog/accelerating-mathematical-and-scientific-discovery-with-gemini-deep-think/

```
Accelerating Mathematical and Scientific Discovery with Gemini Deep Think
Under direction from expert mathematicians and scientists, Gemini Deep Think is solving professional research problems across mathematics, physics, and computer science
In the summer of 2025, an advanced version of Gemini Deep Think achieved Gold-medal standard at the International Mathematics Olympiad (IMO) and later, an updated version, obtained similar results at the International Collegiate Programming Contest. These results demonstrated the model could reason through some of the most challenging math and programming problems designed for students. Since then, Gemini Deep Think mode has moved into science, engineering and enterprise workflows to tackle more complex, open-ended challenges.
In the last week, our teams published two papers (1, 2) detailing a cross-disciplinary effort to solve professional research problems using Gemini Deep Think mode. These results stem from deep collaboration between mathematicians, physicists, and computer scientists.
The Frontier of Pure Mathematics
Unlike IMO problems, research-level mathematics requires advanced techniques from vast literature. While foundation models have large knowledge bases, data scarcity often leads to superficial understanding and hallucinations in advanced subjects.
To solve this, we built a math research agent (internally codenamed Aletheia), powered by Gemini Deep Think mode. It features a natural language verifier to identify flaws in candidate solutions and enable an iterative process of generating and revising solutions. Crucially, this agent can admit failure to solve a problem, a key feature that improved the efficiency for researchers.
Additionally, the research agent uses Google Search and web browsing to navigate complex research, preventing spurious citations and computational inaccuracies when synthesizing published literature.
Since achieving IMO Gold-medal standard in July 2025, Gemini Deep Think has progressed rapidly, scoring up to 90% on the IMO-ProofBench Advanced test as inference-time compute scales. We demonstrated that the scaling law continues to hold as we progress beyond Olympiad level into PhD-level exercises (per our internal FutureMath Basic benchmark). Notably, Aletheia demonstrated that higher reasoning quality can be achieved at a lower inference-time compute.
For research-level math, Aletheia has already enabled several advancements, produced via varying levels of autonomous research:
- Reliable autonomous research. A research paper (Feng26) generated by AI without any human intervention, which calculates certain structure constants in arithmetic geometry called eigenweights.
- AI-guided collaboration. A research paper (LeeSeo26) demonstrating human-AI collaboration in proving bounds on systems of interacting particles called independent sets.
- An extensive semi-autonomous evaluation (Feng et al., 2026b) of 700 open problems on Bloom’s Erdős Conjectures database, including autonomous solutions to four open questions listed there. On Erdős-1051, our model autonomously solved and helped lead to a generalization reported in a research paper (BKKKZ26).
The agent also contributed intermediate propositions on two further papers, (FYZ26) and (ACGKMP26). It is also of note that there has been prior work using Gemini for research-level math at a smaller scale in terms of collaborations and the number of problems tackled.
Following extensive discussions with the mathematical community, we suggest a taxonomy to classify AI-assisted mathematics research by significance and degree of AI contribution - contributing to the wider discussion on responsible documentation, evaluation and communication of AI-generated results. Level 2 (“publishable quality”) works have been submitted to reputable journals. Currently, we do not claim any Level 3 (“Major Advance”) and Level 4 (“Landmark Breakthrough”) results.
Prompts and model outputs are available here. For discussions on AI contributions, our “Human-AI Interaction card”, and community impact, see our paper.
Expanding to Physics and Computer Science
Gemini Deep Think mode has also demonstrated promise in computer science and physics. The second paper builds on similar agentic reasoning ideas, and identifies effective "recipes" for collaboration, specifically the "Advisor" model, where humans guide AI through iterative "Vibe-Proving" cycles to validate intuition and refine proofs. We also detail tactical techniques like “balanced prompting” —requesting simultaneous proof or refutation to prevent confirmation bias—and code-assisted verification. These methods, combined with the model's ability to bridge disparate scientific fields through deep structural connections, are transforming how theoretical research is conducted. This work builds upon our successful deployment of an advanced version of Gemini Deep Think to assist in reviewing CS theory papers for STOC’26 conference.
Collaborating with experts on 18 research problems, an advanced version of Gemini Deep Think helped resolve long-standing bottlenecks across algorithms, ML and combinatorial optimization, information theory, and economics. Highlights from our “Accelerating Research with Gemini” paper include (corresponding section numbers in paper):
- Crossing mathematical borders for network puzzles: Progress on classic computer science problems like "Max-Cut" (efficiently splitting networks) and the "Steiner Tree" (connecting high-dimensional points) had slowed down. Gemini broke both deadlocks by thinking outside the box. It solved these discrete algorithmic puzzles by pulling advanced tools—like the Kirszbraun Theorem, measure theory, and the Stone-Weierstrass theorem—from entirely unrelated branches of continuous mathematics. See Sections 4.1 and 4.2.
- Settling a decade-old conjecture in online submodular optimization: A 2015 theory paper proposed a seemingly obvious rule for data streams: making a copy of an arriving item is always less valuable than simply moving the original. Experts struggled for a decade to prove this. Gemini engineered a highly specific three-item combinatorial counterexample, rigorously proving the long-standing human intuition false. See Section 3.1.
- Machine learning optimization: Training AI to filter out noise usually requires engineers to manually tune a mathematical "penalty." Researchers created a new technique that did this automatically, but couldn't mathematically explain why. Gemini analyzed the equations and proved the method succeeds by secretly generating its own "adaptive penalty" on the fly. See Section 8.3.
- Upgrading economic theory for AI: A recent 'Revelation Principle' for auctioning AI generation tokens only worked mathematically when bids were restricted to rational numbers. Extending the domain to continuous real numbers invalidated the original proof. Gemini employed advanced topology and order theory to extend the theorem, accommodating real-world, continuous auction dynamics. See Section 8.4.
- Physics of cosmic strings: Calculating gravitational radiation from cosmic strings requires finding analytical solutions to tricky integrals containing "singularities." Gemini found a novel solution using Gegenbauer polynomials. This naturally absorbed the singularities, collapsing an infinite series into a closed form, finite sum. See Section 6.1.
Spanning diverse fields—from information and complexity theory to cryptography and mechanism design—the results demonstrate how AI is fundamentally shifting research. For details, see our paper.
Given computer science's fluid, conference-driven publication pipeline, we describe these results by academic trajectory rather than a rigid taxonomy. About half target strong conferences—including an ICLR ’26 acceptance—while most remaining findings will form future journal submissions. Even when course-correcting the field by identifying errors (Section 3.2) or refuting conjectures (Section 3.1), these outcomes highlight AI’s value as a high-level scientific collaborator.
The Future of Human-AI Collaboration
Building on Google’s previous breakthroughs (1, 2, 3, 4, 5), this work demonstrates that general foundation models - leveraged with agentic reasoning workflows - can act as a powerful scientific companion.
Under direction from expert mathematicians, physicists, and computer scientists, Gemini Deep Think mode is proving its utility across fields where complex math, logic and reasoning are core.
We are witnessing a fundamental shift in the scientific workflow. As Gemini evolves, it acts as "force multiplier" for human intellect, handling knowledge retrieval and rigorous verification so scientists can focus on conceptual depth and creative direction. Whether refining proofs, hunting for counterexamples, or linking disconnected fields, AI is becoming a valuable collaborator in the next chapter of scientific progress.
Acknowledgements
We thank the community of expert mathematicians, physicists, and computer scientists for their help and advice on this project
This project was a large-scale collaboration across Google and its success is due to the combined efforts of many individuals and teams. Thang Luong and Vahab Mirrokni led the overall research directions with deep technical expertises from Tony Feng and David Woodruff.
Authors of the first paper “Towards Autonomous Mathematics Research” include: Tony Feng, Trieu H. Trinh, Garrett Bingham, Dawsen Hwang, Yuri Chervonyi, Junehyuk Jung, Joonkyung Lee, Carlo Pagano, Sang-hyun Kim, Federico Pasqualotto, Sergei Gukov, Jonathan N. Lee, Junsu Kim, Kaiying Hou, Golnaz Ghiasi, Yi Tay, YaGuang Li, Chenkai Kuang, Yuan Liu, Hanzhao (Maggie) Lin, Evan Zheran Liu, Nigamaa Nayakanti, Xiaomeng Yang, Heng-Tze Cheng, Demis Hassabis, Koray Kavukcuoglu, Quoc V. Le, Thang Luong. We thank the following experts for feedback and discussions on the work: Jarod Alper, Kevin Barreto, Thomas Bloom, Sourav Chatterjee, Otis Chodosh, Michael Hutchings, Seongbin Jeon, Youngbeom Jin, Aiden Yuchan Jung, Jiwon Kang, Jimin Kim, Vjekoslav Kovač, Daniel Litt, Ciprian Manolescu, Mona Merling, Agustin Moreno, Carl Schildkraut, Johannes Schmitt, Insuk Seo, Jaehyeon Seo, Terence Tao, Cheng-Chiang Tsai, Ravi Vakil, Zhiwei Yun, Shengtong Zhang, Wei Zhang, Yufei Zhao.
Authors of the second paper “Accelerating Scientific Research with Gemini: Case Studies and Common Techniques” include David P. Woodruff, Vincent Cohen-Addad, Lalit Jain, Jieming Mao, Song Zuo, MohammadHossein Bateni, Simina Branzei, Michael P. Brenner, Lin Chen, Ying Feng, Lance Fortnow, Gang Fu, Ziyi Guan, Zahra Hadizadeh, Mohammad T. Hajiaghayi, Mahdi JafariRaviz, Adel Javanmard, Karthik C. S., Ken-ichi Kawarabayashi, Ravi Kumar, Silvio Lattanzi, Euiwoong Lee, Yi Li, Ioannis Panageas, Dimitris Paparas, Benjamin Przybocki, Bernardo Subercaseaux, Ola Svensson, Shayan Taherijam, Xuan Wu, Eylon Yogev, Morteza Zadimoghaddam, Samson Zhou, Yossi Matias, Jeff Dean, James Manyika, Vahab Mirrokni. This list includes Google researchers building the agentic reasoning on top of Gemini, and our academic expert collaborators verifying and collaborating with Gemini. We also thank Corinna Cortes for her careful review of the paper.
We are grateful for the foundational support from the rest of the DeepThink team: Anirudh Baddepudi, Michael Brenner, Irene Cai, Kristen Chiafullo, Paul Covington, Rumen Dangovski, Chenjie Gu, Huan Gui, Vihan Jain, Rajesh Jayaram, Melvin Johnson, Rosemary Ke, Maciej Kula, Nate Kushman, Jane Labanowski, Steve Li, Pol Moreno, Sidharth Mudgal, William Nelson, Ada Maksutaj Oflazer, Sahitya Potluri, Navneet Potti, Shubha Raghvendra, James Roggeveen, Siamak Shakeri, Archit Sharma, Xinying Song, Mukund Sundararajan, Qijun Tan, Zak Tsai, Erik Wang, Theophane Weber, Winnie Xu, Zicheng Xu, Junwen Yao, Shunyu Yao, Adams Yu, Lijun Yu, and Honglei Zhuang.
We’d like to thank the Gemini Post-Training team for building the foundational model for Deep Think: Arash Ahmadian, Ankesh Anand, Charles Chen, Yong Cheng, Kedar Dhamdhere, Philipp Fränken, Justin Gilmer, Elena Gribovskaya, Luheng He, Yangsibo Huang, Rishabh Joshi, Ajay Kannan, Arvind Kannan, Guangda Lai, Robert Leland, Hanzhao (Maggie) Lin, Yingjie Miao, Bryce Petrini, Corbin Quick, Vikash Sehwag, Yue Song, Pranav Talluri, Ankur Taly, George Tucker, Michael Voznesensky, Manish Reddy Vuyyuru, Yiming Wang, Jinliang Wei, Qiao Zhang, Yuan Zhang, Zizhao Zhang.
We thank Quoc Le, Koray Kavukcuoglu, Demis Hassabis, James Manyika, Yossi Matias, and Jeff Dean for sponsoring this project.
Last but not least, we thank Divy Thakkar, Adam Brown, Vinay Ramasesh, Alex Davies, Thomas Hubert, Eugénie Rives, Pushmeet Kohli, Benoit Schillings for feedback and support of the project.
```

---

## 21. Project Genie: Experimenting with infinite, interactive worlds

- 日期: 2026-01-29 17:01
- 链接: https://deepmind.google/blog/project-genie-experimenting-with-infinite-interactive-worlds/

```
Project Genie: Experimenting with infinite, interactive worlds
In August, we previewed Genie 3, a general-purpose world model capable of generating diverse, interactive environments. Even in this early form, trusted testers were able to create an impressive range of fascinating worlds and experiences, and uncovered entirely new ways to use it. The next step is to broaden access through a dedicated, interactive prototype focused on immersive world creation.
Starting today, we're rolling out access to Project Genie for Google AI Ultra subscribers in the U.S (18+). This experimental research prototype lets users create, explore and remix their own interactive worlds.
How we’re advancing world models
A world model simulates the dynamics of an environment, predicting how they evolve and how actions affect them. While Google DeepMind has a history of agents for specific environments like Chess or Go, building AGI requires systems that navigate the diversity of the real world.
To meet this challenge and support our AGI mission, we developed Genie 3. Unlike explorable experiences in static 3D snapshots, Genie 3 generates the path ahead in real time as you move and interact with the world. It simulates physics and interactions for dynamic worlds, while its breakthrough consistency enables the simulation of any real-world scenario — from robotics and modelling animation and fiction, to exploring locations and historical settings.
Building on our model research with trusted testers from across industries and domains, we are taking the next step with an experimental research prototype: Project Genie.
How Project Genie works
Project Genie is a prototype web app powered by Genie 3, Nano Banana Pro and Gemini, which allows users to experiment with the immersive experiences of our world model firsthand. The experience is centred on three core capabilities:
1. World sketching
Prompt with text and generated or uploaded images to create a living, expanding environment. Create your character, your world, and define how you want to explore it — from walking to riding, flying to driving, and anything beyond.
For more precise control, we have integrated “World Sketching” with Nano Banana Pro. This allows you to preview what your world will look like and modify your image to fine tune your world prior to jumping in. You can also define your perspective for the character — such as first-person or third-person — giving you control over how you experience the scene before you enter.
2. World exploration
Your world is a navigable environment that’s waiting to be explored. As you move, Project Genie generates the path ahead in real time based on the actions you take. You can also adjust the camera as you traverse through the world.
3. World remixing
Remix existing worlds into new interpretations, by building on top of their prompts. You can also explore curated worlds in the gallery or by selecting the randomizer icon for inspiration, or build on top of them. And once you’re done, you can download videos of your worlds and your explorations.
How we’re building responsibly
Project Genie is an experimental research prototype in Google Labs, powered by Genie 3. As with all our work towards general AI systems, our mission is to build AI responsibly to benefit humanity. Since Genie 3 is an early research model, there are a few known areas for improvement:
- Generated worlds might not look completely true-to-life or always adhere closely to prompts or images, or real-world physics
- Characters can sometimes be less controllable, or experience higher latency in control
- Limitations in generations to 60 seconds
A few of the Genie 3 model capabilities we announced in August, such as promptable events that change the world as you explore it, are not yet included in this prototype. You can find more details on model limitations and future updates on how we’re improving the experience, here.
Building on the work we have been doing with trusted testers, we are excited to share this prototype with users of our most advanced AI to better understand how people will use world models in many areas of both AI research and generative media.
Access to Project Genie begins rolling out today to Google AI Ultra subscribers 1 in the U.S. (18+), expanding to more territories in due course. We look forward to seeing the infinitely diverse worlds they create, and in time, our goal is to make these experiences and technology accessible to more users.
```

---

## 22. D4RT: Teaching AI to see the world in four dimensions

- 日期: 2026-01-16 10:39
- 链接: https://deepmind.google/blog/d4rt-teaching-ai-to-see-the-world-in-four-dimensions/

```
D4RT: Teaching AI to see the world in four dimensions
Introducing D4RT, a unified AI model for 4D scene reconstruction and tracking across space and time.
Anytime we look at the world, we perform an extraordinary feat of memory and prediction. We see and understand things as they are at a given moment in time, as they were a moment ago, and how they are going to be in the moment to follow. Our mental model of the world maintains a persistent representation of reality and we use that model to draw intuitive conclusions about the causal relationship between the past, present and future.
To help machines see the world more like we do, we can equip them with cameras, but that only solves the problem of input. To make sense of this input, computers must solve a complex, inverse problem: taking a video — which is a sequence of flat 2D projections — and recovering or understanding the rich, volumetric 3D world, in motion.
Today, we are introducing D4RT (Dynamic 4D Reconstruction and Tracking), a new AI model that unifies dynamic scene reconstruction into a single, efficient framework, bringing us closer to the next frontier of artificial intelligence: total perception of our dynamic reality.
The Challenge of the Fourth Dimension
In order for it to understand a dynamic scene captured on a 2D video, an AI model must track every pixel of every object as it moves through the three dimensions of space and the fourth dimension of time. In addition, it must disentangle this motion from the motion of the camera, maintaining a coherent representation even when objects move behind one another or leave the frame entirely. Traditionally, capturing this level of geometry and motion from 2D videos requires computationally intensive processes or a patchwork of specialized AI models — some for depth, others for movement or camera angles — resulting in AI reconstructions that are slow and fragmented.
D4RT’s simplified architecture and novel query mechanism place it at the forefront of 4D reconstruction while being up to 300x more efficient than previous methods — fast enough for real-time applications in robotics, augmented reality, and more.
How D4RT Works: A Query-Based Approach
D4RT operates as a unified encoder-decoder Transformer architecture. The encoder first processes the input video into a compressed representation of the scene’s geometry and motion. Unlike older systems that employed separate modules for different tasks, D4RT calculates only what it needs using a flexible querying mechanism centered around a single, fundamental question:
"Where is a given pixel from the video located in 3D space at an arbitrary time, as viewed from a chosen camera?"
Building on our prior work, a lightweight decoder then queries this representation to answer specific instances of the posed question. Because queries are independent, they can be processed in parallel on modern AI hardware. This makes D4RT extremely fast and scalable, whether it’s tracking just a few points or reconstructing an entire scene.
Capabilities: Fast, Accurate 4D Understanding
With this flexible formulation, a wide variety of 4D tasks can now be solved by the model, including:
- Point Tracking: By querying a pixel's location across different time steps, D4RT can predict its 3D trajectory. Importantly, an object need not be visible on other frames of the video for the model to make a prediction.
- Point Cloud Reconstruction: By freezing time and the camera viewpoint, D4RT can directly generate the complete 3D structure of a scene, eliminating extra steps such as separate camera estimation or per-video iterative optimization.
- Camera Pose Estimation: By generating and aligning 3D snapshots of a single moment from different viewpoints, D4RT can easily recover the camera's trajectory.
As detailed in the underlying technical report, D4RT outperforms previous methods across a wide spectrum of 4D reconstruction tasks. Qualitative comparisons show that while other methods struggle with dynamic objects — often duplicating them or failing to reconstruct them entirely — D4RT maintains a solid, continuous understanding of the moving world.
Crucially, D4RT’s precision does not come at the expense of efficiency. In testing, it performed 18x to 300x faster than the previous state of the art. For example, D4RT processed a one-minute video in roughly five seconds on a single TPU chip. Previous state-of-the-art methods could take up to ten minutes for the same task — an improvement of 120x.
Downstream Applications
D4RT demonstrates that we don't need to choose between accuracy and efficiency in 4D reconstruction. Its flexible, query-based system can capture our dynamic world in real-time, paving the way for the next generation of spatial computing. This includes:
- Robotics: Robots need to navigate dynamic environments populated by moving people and objects. D4RT can provide the spatial awareness required for safe navigation and dextrous manipulation.
- Augmented Reality (AR): For AR glasses to overlay digital objects onto the real world, they need an instant, low-latency understanding of a scene’s geometry. D4RT’s efficiency contributes to making on-device deployment a tangible reality.
- World Models: By effectively disentangling camera motion, object motion, and static geometry, D4RT brings us a step closer to AI that possesses a true “world model” of physical reality — a necessary step on the path to AGI.
We're continuing to explore the model’s capabilities and potential for applications across robotics, augmented reality, and beyond.
```

---

## 23. Veo 3.1 Ingredients to Video: More consistency, creativity and control

- 日期: 2026-01-13 17:00
- 链接: https://deepmind.google/blog/veo-3-1-ingredients-to-video-more-consistency-creativity-and-control/

```
Veo 3.1 Ingredients to Video: More consistency, creativity and control
Today, Veo is getting more expressive, with improvements that help you create more fun, creative, high-quality videos based on ingredient images, built directly for the mobile format. We’re excited to bring new creative possibilities for everyone from casual storytellers to professional filmmakers.
We’re releasing:
- Improvements to Veo 3.1 Ingredients to Video, our capability that lets you create videos based on reference images. This update makes videos more expressive and creative, even with simple prompts
- Native vertical outputs for Ingredients to Video (portrait mode) to power mobile-first, short-form video creation
- State-of-the-art upscaling to 1080p and 4K resolution 1 for high-fidelity production workflows
Whether you are looking for livelier movement, better control over visual elements or broadcast-ready resolution, these updates give you the tools to bring your vision to life. These updates are launching in the Gemini app, YouTube, Flow, Google Vids, the Gemini API and Vertex AI.
Improvements to Veo 3.1 Ingredients to Video
Turn ingredient images into fun, shareable clips
Even with short prompts, you can generate dynamic and engaging videos based on ingredient images. You’ll now see richer dialogue and storytelling, making your videos feel more alive and expressive.
Maintain identity consistency for your characters
Identity consistency is better than ever with Veo 3.1 Ingredients to Video. Keep your characters looking the same even as the setting changes, making it easier to tell a full narrative by having the same character appear across multiple scenes.
Achieve background and object consistency
Control the scene by maintaining the integrity of your setting and the objects within it. You can also reuse an object, backgrounds or textures across scenes.
Seamlessly blend textures, characters and objects
Combine disparate elements — like characters, objects, textures and stylized backgrounds — into a cohesive, high-impact clip.
Pro tip: use the new Nano Banana Pro (Gemini 3 Pro Image) in the Gemini app or Flow to create your ingredient images, which you can then use to create stunning videos with Veo 3.1 Ingredients to Video.
Create high-fidelity visuals with upgraded capabilities
With Veo 3.1’s new capabilities, we are introducing mobile-optimized outputs and professional-grade quality options.
Native vertical outputs for Ingredients to Video
For the first time, "Ingredients to Video" supports generating videos in a native 9:16 aspect ratio. Whether you are creating for YouTube Shorts or other platforms, you can now produce high-quality, full-screen vertical storytelling without cropping or quality loss.
State-of-the-art upscaling to 1080p and 4K resolution
Generate videos 1080p and 4K with state-of-the-art upscaling. Our improved 1080p resolution offers a sharper, cleaner video perfect for editing. For even more detail, choose 4K to capture rich textures and stunning clarity — ideal for high-end productions and large screens.
Try these updates today
Across our products and services, you can now access these new capabilities tailored to your workflow:
- Consumers and creators: We are bringing Veo 3.1 Ingredients to Video directly to YouTube Shorts and the YouTube Create app for the first time. You can also try the enhanced Veo 3.1 Ingredients to Video and portrait mode for Veo in the Gemini app starting today.
- Professional and enterprise workflows: The enhanced Veo 3.1 Ingredients to Video and native vertical format support are rolling out to Flow, the Gemini API, Vertex AI, and Google Vids, with 1080p and 4K resolution options also available on Flow, the API, and Vertex AI.
Verify videos in the Gemini app
We’re committed to providing tools to make it easier to determine if content is AI-generated. This is why videos generated by Google’s tools are embedded with our imperceptible SynthID digital watermark.
In December we expanded our powerful verification tool in the Gemini app to include video. You can now upload a video and simply ask if it was generated with Google AI. This builds on our existing image verification tools, helping to foster a more transparent ecosystem for everyone.
You can find out more about how we’re increasing transparency in AI content with SynthID in our blog post.
```

---

## 24. Google's year in review: 8 areas with research breakthroughs in 2025

- 日期: 2025-12-23 17:01
- 链接: https://deepmind.google/blog/googles-year-in-review-8-areas-with-research-breakthroughs-in-2025/

```
Google's year in review: 8 areas with research breakthroughs in 2025
2025 has been a year of extraordinary progress in research. With artificial intelligence, we can see its trajectory shifting from a tool to a utility: from something people use to something they can put to work. If 2024 was about laying the multimodal foundations for this era, 2025 was the year AI began to really think, act and explore the world alongside us. With quantum computing, we made progress towards real-world applications. And across the board, we helped turn research into reality, with more capable and useful products and tools making a positive impact on people's lives today.
Here’s a look back at some of the breakthroughs, products and scientific milestones that defined the work of Google, Google DeepMind and Google Research in a year of relentless progress.
Delivering breakthroughs on world-class models
This year, we significantly advanced our model capabilities with breakthroughs on reasoning, multimodal understanding, model efficiency, and generative capabilities, beginning with the release of Gemini 2.5 in March and culminating in the November launch of Gemini 3 and the December launch of Gemini 3 Flash.
Built on a foundation of state-of-the-art reasoning, Gemini 3 Pro is our most powerful model to date, designed to help you bring any idea to life. It topped the LMArena Leaderboard and redefined multimodal reasoning with breakthrough scores on benchmarks like Humanity’s Last Exam — a fiendishly hard test for AI models to see if AI can truly think and reason like humans — and GPQA Diamond. It also set a new standard for frontier models in mathematics, achieving a new state-of-the-art of 23.4% on MathArena Apex. We followed shortly with Gemini 3 Flash, which combines Gemini 3's Pro-grade reasoning with Flash-level latency, efficiency and cost, making it the most performant model for its size. Gemini 3 Flash's quality surpasses our previous Gemini 2.5 Pro-scale model's capabilities at a fraction of the price and substantially better latency, continuing our Gemini-era trend of 'the next generation's Flash model is better than the previous generation's Pro model'.
Learn more about our progress on our world-class AI models this year:
- Gemini 3 Flash: frontier intelligence built for speed (Dec 2025)
- A new era of intelligence with Gemini 3 (Nov 2025)
- Introducing Nano Banana Pro (Nov 2025)
- Introducing Veo 3.1 and new creative capabilities in the Gemini API (Nov 2025)
- Gemini 2.5: Our most intelligent AI model (March 2025)
Gemini 3 Flash price & benchmark table.
We’re committed to making useful AI technology accessible, with state-of-the-art open models. We built our Gemma family of models to be lightweight and open for public use; this year we were able to introduce multimodal capabilities, significantly increase the context window, expand multilingual capabilities, and improve efficiency and performance.
Learn more about this year’s advances in Gemma models:
Innovating and transforming our products with AI
Throughout 2025, we continued to advance the trajectory of AI from tool to utility, transforming our portfolio of products with new, powerful agentic capabilities. We reimagined software development by moving beyond tools that assist coding to introducing powerful, agentic systems that collaborate with developers. Key advances, such as the impressive coding capabilities in Gemini 3 and the launch of Google Antigravity, mark a new era in AI-assisted software development.
Learn more about this year’s advances building developer tools:
This evolution was also clear across our core products, from AI-enabled features on the Pixel 10 and updates to AI Mode in Search like generative UI, to AI-first innovations like the Gemini app and NotebookLM, which gained advanced features like Deep Research.
Learn more about how we’ve transformed our products with AI:
- 9 ways AI makes Pixel 10 our most helpful phone yet (Aug 2025)
- Expanding AI Overviews and introducing AI Mode (March 2025)
- Gemini 3 brings upgraded smarts and new capabilities to the Gemini app (Nov 2025)
- NotebookLM adds Deep Research and support for more source types (Nov 2025)
- Generative UI: A rich, custom, visual interactive user experience for any prompt (Nov 2025)
Empowering creativity and co-creating with AI
2025 was a transformative year for generative media, giving people new and unprecedented capabilities to realize their creative ambitions. Generative media models and tools for video, images, audio and worlds became more effective and broadly used, with breakouts Nano Banana and Nano Banana Pro offering unprecedented capabilities for native image generation and editing. We worked with people in creative industries to develop tools like Flow and Music AI Sandbox, making them more helpful for creative workflows, and we expanded creative possibilities for people with new, AI-powered experiences in the Google Arts & Culture lab, major upgrades to image editing within the Gemini app, and the introduction of powerful new generative media models like Veo 3.1, Imagen 4 and Flow.
Learn more about how we’re building AI to enhance creativity:
- Art, science, travel: 3 new AI-powered experiences this holiday season (Nov 2025)
- Introducing Veo 3.1 and advanced capabilities in Flow (Oct 2025)
- Nano Banana: Image editing in Gemini just got a major upgrade (Aug 2025)
- Veo 3, Imagen 4, and Flow: Fuel your creativity with new generative media models and tools (May 2025)
- Music AI Sandbox, now with new features and broader access (April 2025)
As research breakthroughs continue to expand AI’s capabilities, Google Labs is where we share AI experiments as we develop them – hearing from users and evolving as we learn. Some of this year’s most engaging experiments from Labs: Pomelli, an AI experiment for on-brand marketing content; Stitch, which introduced a way to turn prompt and image inputs into complex UI designs and frontend code in minutes; Jules, an asynchronous coding agent that acts as a collaborative partner for developers; and Google Beam, a 3D video communications platform that used AI to advance the possibilities of remote presence.
Learn more about how we’re experimenting in Labs:
Advancing science and mathematics
2025 was also a banner year for scientific advances with AI, marked by breakthroughs in life sciences, health, natural sciences, and mathematics.
In the space of a year, we made progress in building AI resources and tools that empower researchers and help them understand, identify, and develop treatments in healthcare. In genomics, where we’ve been applying advanced technology to research for 10 years, we moved beyond sequencing, using AI to interpret the most complex data. We also marked the 5-year anniversary of AlphaFold, the Nobel-winning AI system that solved the 50-year-old protein folding problem. AlphaFold has been used by over 3 million researchers in more than 190 countries, including over 1 million users in low- and middle-income countries.
Learn more about how we’re using AI to advance life sciences and health:
- AlphaFold: Five years of impact (Nov 2025)
- Using AI to identify genetic variants in tumors with DeepSomatic (Oct 2025)
- AI as a research partner: Advancing theoretical computer science with AlphaEvolve (Sept 2025)
- AlphaGenome: AI for better understanding the genome (June 2025)
- Accelerating scientific breakthroughs with an AI co-scientist (Feb 2025)
Gemini’s advanced thinking capabilities, including Deep Think, also enabled historic progress in mathematics and coding. Deep Think was able to solve problems that require deep abstract reasoning – achieving gold medal-standard in two international contests.
Learn more about how we’re advancing natural sciences and mathematics:
Shaping innovations in computing and the physical world
We’re also leading major discoveries and shaping the future of science in areas like quantum computing, energy and moonshots. Research in this area drew new levels of public attention, with progress towards real-world applications of quantum computing as demonstrated by Quantum Echoes and, notably, Googler Michel Devoret becoming a 2025 Physics Nobel Laureate along with former Googler John Martinis and UC Berkeley’s John Clarke, for their foundational 1980s quantum research.
Learn more about our work on space infrastructure and quantum computing:
- Project Suncatcher: Exploring a space-based, scalable AI infrastructure system design (Nov 2025)
- Googler Michel Devoret awarded the Nobel Prize in Physics (Oct 2025)
- Our Quantum Echoes algorithm is a big step toward real-world applications for quantum computing (Oct 2025)
In 2025, we continued to advance the core infrastructure that powers our AI, focusing on breakthroughs in hardware design and improving energy efficiency. This included the introduction of Ironwood, a new TPU built for the age of inference, which was designed using a method called AlphaChip, alongside a commitment to measuring the environmental impact of our technology.
Learn more about how we’re using AI to develop chips, infrastructure and improve energy efficiency:
Our work in robotics and visual understanding brought AI agents into both the physical and virtual worlds, with advancements like the foundational Gemini Robotics models, the more sophisticated Gemini Robotics 1.5, and the introduction of Genie 3 as a new frontier for general-purpose world models.
Learn more about our work with world models and robotics:
Tackling global challenges and opportunities at scale
Our work throughout 2025 demonstrates how AI-enabled scientific progress is being directly applied to address the world's most critical and pervasive challenges. By leveraging state-of-the-art foundational models and agentic reasoning, we are significantly increasing our understanding of the planet and its systems, while also delivering impactful solutions in areas vital to human flourishing, including climate resilience, public health and education.
For example, we are using state-of-the-art foundational models and agentic reasoning to help increase our understanding of the planet, helping enable work that is making a difference in people’s lives now from weather predictions to urban planning to public health. For example, our flood forecasting information now covers more than two billion people in 150 countries for severe riverine floods. And our most advanced and efficient forecasting model, WeatherNext 2 can generate forecasts 8x faster and with resolution up to 1-hour. Using this technology, we’ve supported weather agencies in making decisions based on a range of scenarios through our experimental cyclone predictions.
Learn more about our work in weather, mapping and wildfires:
- WeatherNext 2: Our most advanced weather forecasting model (Nov 2025)
- New updates and more access to Google Earth AI (Oct 2025)
- Google Earth AI: Our state-of-the-art geospatial AI models (July 2025)
- AlphaEarth Foundations helps map our planet in unprecedented detail (July 2025)
- How we're supporting better tropical cyclone prediction with AI (June 2025)
- Inside the launch of FireSat, a system to find wildfires earlier (March 2025)
We are working with partners to apply AI-enabled scientific progress closer to patients, opening up new avenues for disease management and therapeutic discovery.
Learn more about our health-related work:
- Cell2Sentence-Scale 27B: How a Gemma model helped discover a new potential cancer therapy pathway (Oct 2025)
- From diagnosis to treatment: Advancing AMIE for longitudinal disease management (March 2025)
AI is proving to be a powerful tool in education, enabling new forms of understanding and expanding curiosity through initiatives like LearnLM and Guided Learning in Gemini. We brought Gemini’s most powerful translation capabilities to Google Translate, enabling much smarter, more natural and accurate translations and piloting new speech to speech translation capabilities.
Learn more about how we’re using AI to enable learning:
Prioritizing responsibility and safety
We couple our research breakthroughs with rigorous and forward-looking work on responsibility and safety. As our models grow more capable, we’re continuing to advance and evolve our tools, resources and safety frameworks to anticipate and mitigate risk. Gemini 3 demonstrated this approach in action: it's our most secure model yet, and has undergone the most comprehensive set of safety evaluations of any Google AI model to date. And we’re looking further ahead, exploring a responsible path to AGI, prioritizing readiness, proactive risk assessment, and collaboration with the wider AI community.
Learn more about our responsibility and safety work:
- You can now verify Google AI-generated videos in the Gemini app (Dec 2025)
- How we’re bringing AI image verification to the Gemini app (Nov 2025)
- Strengthening our Frontier Safety Framework (September 2025)
- Taking a responsible path to AGI (April 2025)
- Evaluating potential cybersecurity threats of advanced AI (April 2025)
Leading frontier collaborations with industry, academia and civil society
Advancing the frontier of AI responsibly demands collaboration across all parts of society. In 2025, we worked with leading AI labs to help to form the Agentic AI Foundation and support open standards to ensure a responsible and interoperable future for agentic AI. In education, we’ve partnered with school districts like Miami Dade County and education groups like Raspberry Pi to equip students and educators with AI skills. Our research partnerships with universities like UC Berkeley, Yale, the University of Chicago and many more have been instrumental to some of this year’s most exciting frontier research, and we’re working with the US Department of Energy’s 17 national laboratories to transform how scientific research is conducted. And we’re working with filmmakers and other creative visionaries to put the best AI tools in their hands and explore storytelling in the age of AI.
Learn more about our work on frontier collaboration:
- Google DeepMind supports U.S. Department of Energy on Genesis: a national mission to accelerate innovation and scientific discovery (Dec 2025)
- Formation of the Agentic AI Foundation (AAIF), Anchored by New Project Contributions Including Model Context Protocol (MCP), goose and AGENTS.md (Dec 2025)
- Announcing Model Context Protocol (MCP) support for Google services (Dec 2025)
- Our latest commitments in AI and learning (Nov 2025)
- Partnering to power Miami’s AI-ready future (Oct 2025)
- AI on Screen premiere: “Sweetwater” short film explores new AI narratives (Sept 2025)
- Behind “ANCESTRA”: combining Veo with live-action filmmaking (Jun 2025)
- How Indian music legend Shankar Mahadevan experiments with Music AI Sandbox (April 2025)
Looking ahead
As we look towards 2026, we’re looking forward to continuing to advance the frontier, safely and responsibly, for the benefit of humanity.
```

---

## 25. Gemini 3 Flash: frontier intelligence built for speed

- 日期: 2025-12-17 11:58
- 链接: https://deepmind.google/blog/gemini-3-flash-frontier-intelligence-built-for-speed/

```
Gemini 3 Flash: frontier intelligence built for speed
Today, we're expanding the Gemini 3 model family with the release of Gemini 3 Flash, which offers frontier intelligence built for speed at a fraction of the cost. With this release, we’re making Gemini 3’s next-generation intelligence accessible to everyone across Google products.
Last month, we kicked off Gemini 3 with Gemini 3 Pro and Gemini 3 Deep Think mode, and the response has been incredible. Since launch day, we have been processing over 1T tokens per day on our API. We’ve seen you use Gemini 3 to vibe code simulations to learn about complex topics, build and design interactive games and understand all types of multimodal content.
With Gemini 3, we introduced frontier performance across complex reasoning, multimodal and vision understanding and agentic and vibe coding tasks. Gemini 3 Flash retains this foundation, combining Gemini 3's Pro-grade reasoning with Flash-level latency, efficiency and cost. It not only enables everyday tasks with improved reasoning, but also is our most impressive model for agentic workflows.
Starting today, Gemini 3 Flash is rolling out to millions of people globally:
- For developers in the Gemini API in Google AI Studio, Gemini CLI and our new agentic development platform Google Antigravity
- For everyone via the Gemini app and in AI Mode in Search
- For enterprises in Vertex AI and Gemini Enterprise
Gemini 3 Flash: frontier intelligence at scale
Gemini 3 Flash demonstrates that speed and scale don’t have to come at the cost of intelligence. It delivers frontier performance on PhD-level reasoning and knowledge benchmarks like GPQA Diamond (90.4%) and Humanity’s Last Exam (33.7% without tools), rivaling larger frontier models, and significantly outperforming even the best 2.5 model, Gemini 2.5 Pro, across a number of benchmarks. It also reaches state-of-the-art performance with an impressive score of 81.2% on MMMU Pro, comparable to Gemini 3 Pro.
In addition to its frontier-level reasoning and multimodal capabilities, Gemini 3 Flash was built to be highly efficient, pushing the Pareto frontier of quality vs. cost and speed. When processing at the highest thinking level, Gemini 3 Flash is able to modulate how much it thinks. It may think longer for more complex use cases, but it also uses 30% fewer tokens on average than 2.5 Pro, as measured on typical traffic, to accurately complete everyday tasks with higher performance.
Gemini 3 Flash pushes the Pareto frontier on performance vs. cost and speed.
Performance, here, is measured by LMArena Elo Score.
Gemini 3 Flash’s strength lies in its raw speed, building on the Flash series that developers and consumers already love. It outperforms 2.5 Pro while being 3x faster (based on Artificial Analysis benchmarking) at a fraction of the cost. Gemini 3 Flash is priced at $0.50/1M input tokens and $3/1M output tokens (audio input remains at $1/1M input tokens).
Gemini 3 Flash outperforms 2.5 Pro in speed and quality.
For developers: intelligence that keeps up
Gemini 3 Flash is made for iterative development, offering Gemini 3’s Pro-grade coding performance with low latency — it’s able to reason and solve tasks quickly in high-frequency workflows. On SWE-bench Verified, a benchmark for evaluating coding agent capabilities, Gemini 3 Flash achieves a score of 78%, outperforming not only the 2.5 series, but also Gemini 3 Pro. It strikes an ideal balance for agentic coding, production-ready systems and responsive interactive applications.
Gemini 3 Flash’s strong performance in reasoning, tool use and multimodal capabilities is ideal for developers looking to do more complex video analysis, data extraction and visual Q&A, which means it can enable more intelligent applications — like in-game assistants or A/B test experiments — that demand both quick answers and deep reasoning.
Gemini 3 Flash enables multimodal reasoning in a hand-tracked "ball launching puzzle game" game providing near real-time AI assistance.
Gemini 3 Flash builds and A/B tests new loading spinner designs in near real-time, streamlining the design-to-code process.
Gemini 3 Flash uses multimodal reasoning to analyze and caption an image with contextual UI overlays in near real-time, ultimately transforming a static image into an interactive experience.
Gemini 3 Flash takes a single instruction prompt and codes three unique design variations.
We’ve received a tremendous response from companies using Gemini 3 Flash. Companies like JetBrains, Bridgewater Associates, and Figma are already using it to transform their businesses, recognizing how its inference speed, efficiency and reasoning capabilities perform on par with larger models. Gemini 3 Flash is available today to enterprises via Vertex AI and Gemini Enterprise.
For everyone: Gemini 3 Flash is rolling out globally
Gemini 3 Flash is now the default model in the Gemini app, replacing 2.5 Flash. That means all of our Gemini users globally will get access to the Gemini 3 experience at no cost, giving their everyday tasks a major upgrade.
Because of Gemini 3 Flash’s incredible multimodal reasoning capabilities, you can use it to help you see, hear and understand any type of information faster. For example, you can ask Gemini to understand your videos and images and turn that content into a helpful and actionable plan in just a few seconds.
Gemini 3 Flash in the Gemini app can analyze short video content and give you a plan, like how to improve your golf swing.
As Gemini 3 Flash is optimized for speed, it can see and guess what you’re drawing while you’re still sketching it.
You can upload an audio recording and Gemini 3 Flash will identify your knowledge gaps, create a custom quiz, and give you detailed explanations on the answers.
Or you can quickly build fun, useful apps from scratch using your voice without prior coding knowledge. Just dictate to Gemini on the go, and it can transform your unstructured thoughts into a functioning app in minutes.
Gemini 3 Flash is also starting to roll out as the default model for AI Mode in Search with access to everyone around the world.
Building on the reasoning capabilities of Gemini 3 Pro, AI Mode with Gemini 3 Flash is more powerful at parsing the nuances of your question. It considers each aspect of your query to serve thoughtful, comprehensive responses that are visually digestible — pulling real-time local information and helpful links from across the web. The result effectively combines research with immediate action: you get an intelligently organized breakdown alongside specific recommendations — at the speed of Search.
This shines when tackling complex goals with multiple considerations like trying to plan a last-minute trip or learning complex educational concepts quickly.
Try Gemini 3 Flash today
Gemini 3 Flash is available now in preview via the Gemini API in Google AI Studio, Google Antigravity, Vertex AI and Gemini Enterprise. You can also access it through other developer tools like Gemini CLI and Android Studio. It’s also starting to roll out to everyone in the Gemini app and AI Mode in Search, bringing fast access to next-generation intelligence at no cost.
We’re looking forward to seeing what you bring to life with this expanded family of models: Gemini 3 Pro, Gemini 3 Deep Think and now, Gemini 3 Flash.
```

---

## 26. Gemma Scope 2: helping the AI safety community deepen understanding of complex language model behavior

- 日期: 2025-12-16 10:14
- 链接: https://deepmind.google/blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/

```
Gemma Scope 2: helping the AI safety community deepen understanding of complex language model behavior
Announcing a new, open suite of tools for language model interpretability
Large Language Models (LLMs) are capable of incredible feats of reasoning, yet their internal decision-making processes remain largely opaque. Should a system not behave as expected, a lack of visibility into its internal workings can make it difficult to pinpoint the exact reason for its behaviour. Last year, we advanced the science of interpretability with Gemma Scope, a toolkit designed to help researchers understand the inner workings of Gemma 2, our lightweight collection of open models.
Today, we are releasing Gemma Scope 2: a comprehensive, open suite of interpretability tools for all Gemma 3 model sizes, from 270M to 27B parameters. These tools can enable us to trace potential risks across the entire "brain" of the model.
To our knowledge, this is the largest ever open-source release of interpretability tools by an AI lab to date. Producing Gemma Scope 2 involved storing approximately 110 Petabytes of data, as well as training over 1 trillion total parameters.
As AI continues to advance, we look forward to the AI research community using Gemma Scope 2 to debug emergent model behaviors, use these tools to better audit and debug AI agents, and ultimately, accelerate the development of practical and robust safety interventions against issues like jailbreaks, hallucinations and sycophancy.
Our interactive Gemma Scope 2 demo is available to try, courtesy of Neuronpedia.
What’s new in Gemma Scope 2
Interpretability research aims to understand the internal workings and learned algorithms of AI models. As AI becomes increasingly more capable and complex, interpretability is crucial for building AI that is safe and reliable.
Like its predecessor, Gemma Scope 2 acts as a microscope for the Gemma family of language models. By combining sparse autoencoders (SAEs) and transcoders, it allows researchers to look inside models, see what they’re thinking about, and how these thoughts are formed and connect to the model’s behaviour. In turn, this enables the richer study of jailbreaks or other AI behaviours relevant to safety, like discrepancies between a model's communicated reasoning and its internal state.
While the original Gemma Scope enabled research in key areas of safety, such as model hallucination, identifying secrets known by a model, and training safer models, Gemma Scope 2 supports even more ambitious research through significant upgrades:
- Full coverage at scale: We provide a full suite of tools for the entire Gemma 3 family (up to 27B parameters), essential for studying emergent behaviors that only appear at scale, such as those previously uncovered by the 27b-size C2S Scale model that helped discover a new potential cancer therapy pathway. Although Gemma Scope 2 is not trained on this model, this is an example of the kind of emergent behavior that these tools might be able to understand.
- More refined tools to decipher complex internal behaviors: Gemma Scope 2 includes SAEs and transcoders trained on every layer of our Gemma 3 family of models. Skip-transcoders and Cross-layer transcoders make it easier to decipher multi-step computations and algorithms spread throughout the model.
- Advanced training techniques: We use state-of-the-art techniques, notably the Matryoshka training technique, which helps SAEs detect more useful concepts and resolves certain flaws discovered in Gemma Scope.
- Chatbot behavior analysis tools: We also provide interpretability tools targeted at the versions of Gemma 3 tuned for chat use cases. These tools enable analysis of complex, multi-step behaviors, such as jailbreaks, refusal mechanisms, and chain-of-thought faithfulness.
Advancing the field
By releasing Gemma Scope 2, we aim to enable the AI safety research community to push the field forward using a suite of cutting-edge interpretability tools. This new level of access is crucial for tackling real-world safety problems that only arise in larger, modern LLMs.
Learn more about Gemma Scope
```

---

## 27. Improved Gemini audio models for powerful voice experiences

- 日期: 2025-12-12 17:50
- 链接: https://deepmind.google/blog/improved-gemini-audio-models-for-powerful-voice-experiences/

```
Improved Gemini audio models for powerful voice interactions
Earlier this week, we introduced greater control over audio generation with an upgrade to our Gemini 2.5 Pro and Flash Text-to-Speech models.
But generating expressive speech is only one side of the conversation. Today, we’re releasing an updated Gemini 2.5 Flash Native Audio for live voice agents. This update improves the model’s ability to handle complex workflows, navigate user instructions, and hold natural conversations.
Gemini 2.5 Flash Native Audio is now available across Google products including Google AI Studio, Vertex AI, and has also started rolling out in Gemini Live and Search Live, bringing the naturalness of native audio to Search Live for the first time. This means you can more effectively brainstorm live with Gemini, get real-time help in Search Live, or build the next generation of enterprise-ready customer service agents.
Beyond powering helpful agents, native audio unlocks new possibilities for global communication. We’re introducing live speech translation, a capability that enables streaming speech-to-speech translation for headphones. It preserves the speaker’s intonation, pacing and pitch. This beta experience is rolling out in the Google Translate app starting today.
Live Voice Agents
To enable the breadth of use cases across surfaces and products, we have improved Gemini 2.5 Native Audio in three key areas:
- Sharper function calling: We’ve improved the model's reliability when triggering external functions. It can now more accurately identify when to fetch real-time information during a conversation and seamlessly weave that data back into the audio response, without breaking the flow. On ComplexFuncBench Audio, an eval that captures multi-step function calling with various constraints, Gemini 2.5 Native Audio leads with a score of 71.5%.
- Robust instruction following: The model is now better at handling complex instructions resulting in higher user satisfaction on content completeness. With a 90% adherence rate to developer instructions (up from 84%), it delivers more reliable outputs.
- Smoother conversations: We’ve achieved significant gains in multi-turn conversation quality. Gemini 2.5 Flash Native Audio is able to retrieve context from previous turns more effectively, creating more cohesive conversations.
The updated Gemini 2.5 Flash Native Audio’s performance against previous versions and industry competitors on ComplexFuncBench
What customers are saying
Google Cloud customers are already using Gemini’s native audio capabilities to drive real business results, from mortgage processing to customer calls.
- “Users often forget they’re talking to AI within a minute of using Sidekick, and in some cases have thanked the bot after a long chat…New Live API AI capabilities offered through Gemini [2.5 Flash Native Audio] empower our merchants to win.” – David Wurtz, VP of Product, Shopify
- "By integrating the Gemini 2.5 Flash Native Audio model…we've significantly enhanced Mia's capabilities since launching in May 2025. This powerful combination has enabled us to generate over 14,000 loans for our broker partners." – Jason Bressler, Chief Technology Officer, United Wholesale Mortgage (UWM)
- “Working with the Gemini 2.5 Flash Native Audio model through Vertex AI allows Newo.ai AI Receptionists to achieve unmatched conversational intelligence ... .They can identify the main speaker even in noisy settings, switch languages mid-conversation, and sound remarkably natural and emotionally expressive.” – David Yang, Co-founder, Newo.ai
Live Speech Translation
Gemini now natively supports new live speech-to-speech translation capabilities designed to handle both continuous listening and two-way conversation.
With continuous listening, Gemini automatically translates speech in multiple languages into a single target language. This allows you to put headphones in and hear the world around you in your language.
For two-way conversation, Gemini’s live speech translation handles translation between two languages in real-time, automatically switching the output language based on who is speaking. For example, if you speak English and want to chat with a Hindi speaker, you’ll hear English translations in real-time in your headphones, while your phone broadcasts Hindi when you’re done speaking.
Gemini’s live speech translation has a number of key capabilities that help in the real world:
- Language coverage: Translates speech in over 70 languages and 2000 language pairs by combining Gemini model’s world knowledge and multilingual capabilities with its native audio capabilities
- Style transfer: Captures the nuance of human speech, preserving the speaker’s intonation, pacing and pitch so the translation sounds natural.
- Multilingual input: Understands multiple languages simultaneously in a single session, helping you follow multilingual conversations without needing to fiddle around with language settings.
- Auto detection: Identifies the spoken language and begins translation, so you don’t even need to know what language is being spoken to start translating.
- Noise robustness: Filters out ambient noise so you can converse comfortably even in loud, outdoor environments.
Starting today, you can try it in a new beta experience in the Google Translate app for real-time translation in your headphones by connecting them to your device and tapping “Live translate.” This experience is rolling out to all Android devices in the US, Mexico and India with support for iOS and more regions coming soon.
Based on feedback, we will continue to iterate on this experience and bring it to more Google products including the Gemini API in 2026.
Get started today
Start building voice agents today with Gemini 2.5 Flash Native Audio, now generally available on Vertex AI and as preview in the Gemini API. Try it out in Google AI Studio.
Gemini 2.5 Flash and 2.5 Pro text-to-speech models are also available via the Gemini API in Google AI Studio. Get started with the speech generation docs, explore the prompting guide, or check out the Gemini API Cookbook to get started.
```

---

## 28. Deepening our partnership with the UK AI Security Institute

- 日期: 2025-12-11 00:06
- 链接: https://deepmind.google/blog/deepening-our-partnership-with-the-uk-ai-security-institute/

```
Deepening our partnership with the UK AI Security Institute
Today, we're announcing an expanded partnership with the UK AI Security Institute (AISI) through a new Memorandum of Understanding focused on foundational security and safety research, to help ensure artificial intelligence is developed safely and benefits everyone.
The research partnership with AISI is an important part of our broader collaboration with the UK government on accelerating safe and beneficial AI progress.
Building on a foundation of collaboration
AI holds immense potential to benefit humanity by helping treat disease, accelerate scientific discovery, create economic prosperity and tackle climate change. For these benefits to be realised, we must put safety and responsibility at the heart of development. Evaluating our models against a broad spectrum of potential risks remains a critical part of our safety strategy, and external partnerships are an important element of this work.
This is why we have partnered with the UK AISI since its inception in November 2023 to test our most capable models. We are deeply committed to the UK AISI’s goal to equip governments, industry and wider society with a scientific understanding of the potential risks posed by advanced AI as well as potential solutions and mitigations.
We are actively working with AISI to build more robust evaluations for AI models, and our teams have collaborated on safety research to move the field forward, including recent work on Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety. Building on this success, today we are broadening our partnership from testing to include wider, more foundational, research in a variety of areas.
What the partnership involves
Under this new research partnership, we're broadening our collaboration to include:
- Sharing access to our proprietary models, data and ideas to accelerate research progress
- Joint reports and publications sharing findings with the research community
- More collaborative security and safety research combining our teams' expertise
- Technical discussions to tackle complex safety challenges
Key research areas
Our joint research with AISI focuses on critical areas where Google DeepMind's expertise, interdisciplinary teams, and years of pioneering responsible research can help make AI systems more safe and secure:
Monitoring AI reasoning processes
We will work on techniques to monitor an AI system’s “thinking”, also commonly referred to as its chain-of-thought (CoT). This work builds on previous Google DeepMind research as well, and our recent collaboration on this topic with AISI, OpenAI, Anthropic and other partners. CoT monitoring helps us understand how an AI system produces its answers, complementing interpretability research.
Understanding social and emotional impacts
We will work together to investigate the ethical implications of socioaffective misalignment; that is, the potential for AI models to behave in ways which do not align with human wellbeing, even when they’re technically following instructions correctly. This research will build on existing Google DeepMind work that has helped define this critical area of AI safety.
Evaluating economic systems
We will explore the potential impact of AI on economic systems by simulating real-world tasks across different environments. Experts will score and validate these tasks, after which they will be categorised along dimensions like complexity or representativeness, to help predict factors like long-term labour market impact.
Working together to realise the benefits of AI
Our partnership with AISI is one element of how we aim to realise the benefits of AI for humanity while mitigating potential risks. Our wider strategy includes foresight research, extensive safety training that goes hand-in-hand with capability development, rigorous testing of our models, and the development of better tools and frameworks to understand and mitigate risk.
Strong internal governance processes are also essential for safe and responsible AI development, as is collaborating with independent external experts who bring fresh perspectives and diverse expertise to our work. Google DeepMind’s Responsibility and Safety Council works across teams to monitor emerging risk, review ethics and safety assessments and implement relevant technical and policy mitigations. We also partner with other external experts like Apollo Research, Vaultis, Dreadnode and more, to conduct extensive testing and evaluation of our models, including Gemini 3, our most intelligent and secure model to date.
Additionally, Google DeepMind is a proud founding member of the Frontier Model Forum, as well as the Partnership on AI, where we focus on ensuring safe and responsible development of frontier AI models and increasing collaboration on important safety issues.
We hope our expanded partnership with AISI will allow us to build more robust approaches to AI safety for the benefit not just of our own organisations, but also the wider industry and everyone who interacts with AI systems.
```

---

## 29. Strengthening our partnership with the UK government to support prosperity and security in the AI era

- 日期: 2025-12-10 14:59
- 链接: https://deepmind.google/blog/strengthening-our-partnership-with-the-uk-government-to-support-prosperity-and-security-in-the-ai-era/

```
Strengthening our partnership with the UK government to support prosperity and security in the AI era
AI presents an opportunity to build a more prosperous and secure world.
The UK has already laid a strong foundation to seize this moment and is uniquely positioned to translate AI innovation into public benefit. That’s why we are excited to deepen our collaboration with the UK government to accelerate this work and offer a blueprint for other countries.
Together we will focus on using AI to speed up progress in science and education, modernize public services and advance national security and resilience.
Accelerating access to frontier AI in key sectors: Science & Education
Our partnership will center on providing access to frontier AI in two areas foundational to the UK’s long-term success: scientific discovery and education.
The UK has a rich history of applying new technologies to drive scientific progress, from Hooke’s microscope to Faraday’s electrical experiments. We aim to build on this heritage, and empower the next generation of scientists with AI tools that can unlock breakthroughs, transform the economy, and solve some of the major challenges facing humanity. We will provide priority access to our “AI for Science” models to UK scientists, including:
- AlphaEvolve - a Gemini-powered coding agent for designing advanced algorithms
- AlphaGenome - an AI model to help scientists better understand our DNA
- AI co-scientist - a multi-agent AI system that acts as a virtual scientific collaborator
- WeatherNext - a family of state-of-the-art weather forecasting models
Like the microscope or telescope, these AI tools are designed to enhance scientific capacity, enabling researchers to tackle problems of unprecedented complexity and scale. For example, AlphaFold - our AI system for predicting protein structures - has already enabled almost 190,000 researchers in the UK alone to deepen their understanding of areas such as crop resilience, antimicrobial resistance and other critical biological challenges.
Establishing Google DeepMind’s first automated science laboratory in the UK
To help turbocharge scientific discovery, we will establish Google DeepMind’s first automated laboratory in the UK in 2026, specifically focused on materials science research. A multidisciplinary team of researchers will oversee research in the lab, which will be built from the ground up to be fully integrated with Gemini. By directing world-class robotics to synthesize and characterize hundreds of materials per day, the team intends to significantly shorten the timeline for identifying transformative new materials.
Discovering new materials is one of the most important pursuits in science, offering the potential to reduce costs and enable entirely new technologies. For example, superconductors that operate at ambient temperature and pressure could allow for low cost medical imaging and reduce power loss in electrical grids. Other novel materials could help us tackle critical energy challenges by unlocking advanced batteries, next-generation solar cells and more efficient computer chips.
Enhancing teaching and learning
AI can augment the classroom experience, especially when grounded in learning science.
This impact was made clear in a successful pilot program in Northern Ireland, where Gemini helped save teachers an average of 10 hours per week by streamlining administrative work and brainstorming engaging lesson content.
Beyond time savings, Eedi's recent exploratory randomized controlled trial (RCT) with UK students indicates that AI can help drive effective student learning. Students who received short AI tutoring sessions (under supervision by teachers) were 5.5 percentage points more likely to solve novel problems on subsequent topics than students who worked with human tutors alone.
To help scale this impact further across the UK, we are supporting research to understand how AI tools impact teaching and learning through a rigorous scientific approach, and exploring how to tailor our Gemini model - leveraging our longstanding commitment to pedagogy, including our LearnLM efforts - to complement England’s national curriculum. Our goal is to deliver state of the art educational experiences while also helping reduce educator workloads, freeing them to reclaim more time to focus on what they do best: helping every learner thrive.
Modernizing public services
AI also has tremendous potential to help build more effective and efficient public services. We are working directly with government teams to ensure they have the technical expertise and access to frontier models required to reimagine these services to better serve citizens. The UK Government’s AI Incubator team (i.AI) is currently trialling Extract - a tool for council planners that uses Gemini to transform old planning documents into clear, digital data. Currently, converting a single planning document takes up to 2 hours. Extract will transform these into digital data in just 40 seconds, significantly speeding up decision-making timelines.
Advancing national security and resilience
Our partnership will involve deeper collaboration with the UK AI Security Institute on critical safety research in explainability, alignment and societal impact, so these risks may be better understood and mitigated. Read more about this work here.
AI can also be a powerful defender against security risks. We will work with the UK government to advance AI-enhanced approaches to national cyber resilience, exploring using tools like Big Sleep and CodeMender to identify vulnerabilities and automatically fix code, enabling a more secure future.
National partnerships on AI
We believe AI will be humanity's most transformational technology, and we are committed to partnering with governments globally to turn its potential into real progress for people everywhere. By building on our collaboration with the UK government and important initiatives like the US-UK Tech Prosperity Deal, we aim to advance innovation, scientific discovery, and security for all.
```

---

## 30. FACTS Benchmark Suite: Systematically evaluating the factuality of large language models

- 日期: 2025-12-09 11:29
- 链接: https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/

```
FACTS Benchmark Suite: Systematically evaluating the factuality of large language models
Large language models (LLMs) are increasingly becoming a primary source for information delivery across diverse use cases, so it’s important that their responses are factually accurate.
In order to continue improving their performance on this industry-wide challenge, we have to better understand the types of use cases where models struggle to provide an accurate response and better measure factuality performance in those areas.
The FACTS Benchmark Suite
Today, we’re teaming up with Kaggle to introduce the FACTS Benchmark Suite. It extends our previous work developing the FACTS Grounding Benchmark, with three additional factuality benchmarks, including:
- A Parametric Benchmark that measures the model’s ability to access its internal knowledge accurately in factoid question use-cases.
- A Search Benchmark that tests a model’s ability to use Search as a tool to retrieve information and synthesize it correctly.
- A Multimodal Benchmark that tests a model’s ability to answer prompts related to input images in a factually correct manner.
We are also updating the original FACTS grounding benchmark with Grounding Benchmark - v2, an extended benchmark to test a model’s ability to provide answers grounded in the context of a given prompt.
Each benchmark was carefully curated to produce a total of 3,513 examples, which we are making publicly available today. Similar to our previous release, we are following standard industry practice and keeping an evaluation set held-out as a private set. The FACTS Benchmark Suite Score (or FACTS Score) is calculated as the average accuracy of both public and private sets across the four benchmarks. Kaggle will oversee the management of the FACTS Benchmark Suite. This includes owning the private held-out sets, testing the leading LLMs on the benchmarks, and hosting the results on a public leaderboard. More details about the FACTS evaluation methodology can be found in our tech report.
Benchmark overview
Parametric Benchmark
The FACTS Parametric benchmark assesses the ability of models to accurately answer factual questions, without the aid of external tools like web search. All the questions in the benchmark are “trivia style” questions driven by user interest that can be answered via Wikipedia (a standard source for LLM pretraining). The resulting benchmark consists of a 1052-item public set and a 1052-item private set.
A typical prompt from the public set would require the model to answer a simple question on a niche topic, e.g., “Who played harmonica on ‘The Rockford Files’ theme song?”
Search Benchmark
By contrast, the FACTS Search benchmark evaluates a model’s ability to use a web search tool for answering questions. This benchmark was designed to be challenging for LLMs even with access to the web, often requiring the retrieval of multiple facts sequentially to answer a single query. The same web search tool is being made available to all models, ensuring the model capabilities are tested in isolation without the confounding factor of custom web retrieval settings. FACTS Search consists of a 890-item public set and a 994-item private set.
The following example from the public set was included because it requires retrieving information from several web pages, “What is the sum of the birth years of the British boxer who defeated Vazik Kazarian at the 1960 Summer Olympics, the Moroccan boxer who also competed in the men’s light welterweight event at those same Olympics, and the Danish boxer who competed in both the 1960 and 1964 Summer Olympics?”
Multimodal Benchmark
The FACTS Multimodal benchmark evaluates the ability of models to generate factually accurate text in response to image-based questions, which is a critical capability for modern multimodal systems.
This task requires the integration of visual grounding, i.e. its ability to accurately interpret and connect information from visual input, using its internal or “parametric” world knowledge. The evaluation framework is designed to ensure that a response is both correct and provides all necessary information to be complete. The benchmark consists of a 711-item public set and a 811-item private set.
For example, the following image from the public set of the Multimodal benchmark appeared with the prompt: “What genus does this animal belong to?”
Results
We evaluated leading LLMs on the FACTS Benchmark Suite, which includes the updated FACTS Grounding v2.
The table below lists 15 leading models and their overall FACTS score (followed by the breakdown to the scores across the four individual benchmarks: Grounding, Multimodal, Parametric and Search).
Gemini 3 Pro leads in overall performance, with a FACTS Score of 68.8%. In particular, we saw significant improvements from Gemini 2.5 Pro to Gemini 3 Pro in Search & Parametric slices, where the error rate was reduced by 55% on FACTS Search and 35% for FACTS Parametric. FACTS Multimodal saw the lowest scores, generally. All evaluated models achieved an overall accuracy below 70%, leaving considerable headroom for future progress.
Beyond the FACTS Benchmark Suite, Gemini’s improvement in factuality is also reflected in another factuality benchmark, SimpleQA Verified, going from 54.5% accuracy on Gemini 2.5 Pro to 72.1% accuracy on Gemini 3 Pro. SimpleQA Verified tests LLMs’ parametric knowledge on short-form responses.
Looking Ahead
While LLM factuality is still an area of ongoing research, the FACTS Benchmark Suite and Gemini 3 Pro results are representative of Google’s long-term commitment towards making information universally accessible and useful. We hope this work encourages deeper research into LLM factuality, leading to better and more accurate models and products for the people that rely on them.
```

---
