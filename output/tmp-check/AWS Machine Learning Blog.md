# AWS Machine Learning Blog

> 分类: 大厂技术博客
> URL: https://aws.amazon.com/blogs/amazon-ai/feed/
> 抓取: 20 篇

---

## 1. Halliburton enhances seismic workflow creation with Amazon Bedrock and Generative AI

- 日期: 2026-05-08 13:20
- 链接: https://aws.amazon.com/blogs/machine-learning/halliburton-enhances-seismic-workflow-creation-with-amazon-bedrock-and-generative-ai/

```
Seismic data analysis is an essential component of energy exploration, but configuring complex processing workflows has traditionally been a time-consuming and error-prone challenge. Halliburton’s Seismic Engine, a cloud-native application for seismic data processing, is a powerful tool that previously required manual configuration of approximately 100 specialized tools to create workflows. This process was not only time-consuming but also required deep expertise, potentially limiting the accessibility and efficiency of the software. 
 To address this challenge, Halliburton partnered with the AWS Generative AI Innovation Center to develop an AI-powered assistant for Seismic Engine. The solution uses Amazon Bedrock , Amazon Bedrock Knowledge Bases , Amazon Nova , and Amazon DynamoDB to transform complex workflow creation into conversations. Geoscientists and data scientists can configure processing tools through natural language interaction instead of manual configuration. 
 In this post, we’ll explore how we built a proof-of-concept that converts natural language queries into executable seismic workflows while providing a question-answering capability for Seismic Engine tools and documentation. We’ll cover the technical details of the solution, share evaluation results showing workflow acceleration of up to 95%, and discuss key learnings that can help other organizations enhance their complex technical workflows with generative AI. 
 Our collaboration with AWS has been instrumental in accelerating subsurface interpretation workflows. By integrating Amazon Bedrock services with Halliburton Landmark’s DS365 Seismic Engine, we were able to reduce traditionally time‑consuming workflow‑building tasks by an order of magnitude. This generative AI–powered workflow assistant not only improves efficiency and accuracy but also makes our advanced geophysical tools more accessible to a broader range of users. The scalable cloud‑native architecture on AWS has enabled us to deliver a seamless, conversational experience that fundamentally improves productivity across subsurface workflows. 
 — Phillip Norlund, Manager of Subsurface Technologies, Halliburton Landmark 
 — Slim Bouchrara, Senior Product Owner of Subsurface R&D, Halliburton Landmark 
 Solution overview 
 Our project aimed to address two key objectives: transforming natural language queries into executable seismic workflows, and providing an intelligent question and answer (Q&A) system for Seismic Engine documentation. To achieve this, we developed a solution using Amazon Bedrock that enables geoscientists to interact with complex seismic tools through natural conversation.The backbone of our system is a FastAPI application deployed on AWS App Runner, which handles user queries through a streaming interface. When a user submits a query, an intent router powered by Amazon Nova Lite analyzes the request to determine whether it’s seeking workflow generation or technical information. For Q&A requests, the system uses Amazon Bedrock Knowledge Bases with Amazon OpenSearch Serverless to provide relevant answers from indexed documentation. For workflow requests, a generation agent using Anthropic’s Claude on Amazon Bedrock creates YAML workflows by selecting from 82 available Seismic Engine tools. 
 To maintain context and enable multi-turn conversations, we integrated Amazon DynamoDB for chat history and interaction logging. The system supports streaming responses for both Q&A and workflow generation, providing immediate feedback to users as the system processes their requests. This architecture allows complex technical workflows to be created and modified through natural conversation, while maintaining the precise control required for seismic data processing. The following diagram illustrates the solution architecture. 
 Query routing and intent classification 
 After the user’s query is provided to the system, the Intent Router classifies the intent label of the given query by calling Amazon Nova Lite via the Amazon Bedrock API. The large language model (LLM) is given a prompt to produce one of three intent labels: “Workflow_Generation”, “QnA”, and “General_Question”.The “Workflow_Generation” label is used to route queries related to workflow generation, including reading/loading datasets, data processing operations, and various requests involving manipulating specific datasets. The “QnA” intent label is used for questions related to specific tools, requests for sample workflows, or questions about Seismic Engine documentation. The “General_Question” label is reserved for queries unrelated to Seismic Engine operations or workflows.In our implementation, Amazon Nova Lite performed the routing task efficiently, offering a good balance between accuracy and latency. 
 Question answering implementation 
 The Q&A component handles Seismic Engine-related queries by using Amazon Bedrock Knowledge Bases, a fully managed service for end-to-end Retrieval Augmented Generation (RAG) workflow. We chose Bedrock Knowledge Bases because it alleviates the operational overhead of managing vector databases, chunking strategies, and embedding pipelines. As a fully managed service, it handles infrastructure scaling, security, and maintenance automatically, so that our team could focus on solution development rather than RAG infrastructure operations. The service provides native support for multiple chunking strategies including hierarchical chunking, which maintains parent-child relationships to balance granular retrieval with broader document context.The data sources include tool documentation markdown files and Seismic Engine manuals stored in S3. We kept tool documentation files unchunked since they’re relatively short, preserving complete context for individual tools. For longer documents like Seismic Engine manuals, we used hierarchical chunking with default settings. We use Amazon Titan Text Embeddings V2 for embedding generation and OpenSearch Serverless as the vector database. The system also stores metadata such as file names, URLs, and document types for each indexed item for downstream use.For both retrieval and response generation, we use Amazon Bedrock Knowledge Bases’ retrieve_and_generate API with Claude 3.5 Haiku as the model. The system supports multi-turn conversations by maintaining session context, and responses are formatted with inline citations for enhanced traceability. 
 Note: This solution was developed and evaluated using Claude 3.5 Sonnet V2 and Claude 3.5 Haiku. Since then, these models have been succeeded by Claude Sonnet 4.5 and most recently Claude Sonnet 4.6, as well as Claude Haiku 4.5, all available through Amazon Bedrock. The solution architecture supports model upgrades without code changes, so that you can use the latest model capabilities. 
 This approach enables our system to provide context-aware, relevant answers to user queries about Seismic Engine tools and workflows. 
 Workflow generation 
 For queries classified as “Workflow_Generation”, our solution uses LLM agents to convert natural language into executable YAML workflows. The agent is bound with 82 tools available on Seismic Engine. Based on the user’s query and tool specifications that define inputs, parameters, and outputs, the agent selects appropriate tools, determines their correct execution order, and generates a YAML workflow that addresses the user’s requirements. The following figure illustrates the workflow generation process. 
 We used both Claude 3.5 Sonnet V2 and Claude 3.5 Haiku in our implementation, orchestrated through the LangChain framework for agent management and tool binding. The models are provided with detailed tool descriptions and specifications, so that they can understand each tool’s capabilities and requirements. When generating workflows, the system considers not only the explicit requirements in the user’s query but also includes necessary default parameters when specific values aren’t provided.The workflow generation process supports multi-turn conversations, so that users can modify previously generated workflows through natural language requests. By using conversation history stored in Amazon DynamoDB, the LLM can either generate new workflows or modify existing ones according to the user’s current query. 
 Evaluation 
 To evaluate our solution’s effectiveness, we created a comprehensive test dataset of query-workflow pairs, consisting of both low and medium complexity workflows. These were derived from real historical workflows and validated by subject matter experts to verify they accurately represent typical user requests. 
 Workflow generation results 
 Model Complexity Success Rate Mean Generation Time (s) Median Generation Time (s) 
 Claude Haiku 3.5 simple 84% 8.3 5.9 
 medium 90% 12.4 9.1 
 Claude Sonnet 3.5 V2 simple 86% 11.2 11.5 
 medium 97% 15.8 16.6 
 Both models demonstrated strong performance, with Claude Sonnet 3.5 V2 showing superior success rates, particularly for medium complexity workflows. The system delivers responses through streaming, providing users with immediate feedback as the workflow is generated, with complete workflows delivered within 5.9-16.6 seconds. Claude Haiku 3.5 offers faster generation times, providing a trade-off option between speed and accuracy. 
 Comparison to baseline performance 
 User Type % Success % Failure Time to Build Simple Flow (min) Time to Build Complex Flow (min) 
 New User 70% 20% 4 20 
 Experienced User 85% 10% 2 5 
 Our Solution 84-97% 3-16% 0.13-0.26 0.21-0.28 
 Our generative AI solution demonstrates the following improvements: 
 Success rates of 84-97% surpass both new and experienced users. 
 Workflow creation time is reduced from minutes to seconds, representing over a 95% time reduction. 
 These results demonstrate that users across experience levels can enhance productivity by over 95%, while maintaining or exceeding the accuracy of manual workflow creation. 
 Conclusion 
 In this post, we showed how we used Amazon Bedrock to transform complex technical processes into natural conversations. By implementing an AI-powered assistant with integrated Q&A capabilities, we achieved workflow generation success rates of 84-97% while reducing creation time by over 95% compared to manual processes. The system’s ability to handle both low and medium complexity workflows, combined with its contextual understanding of Seismic Engine tools, demonstrates how generative AI can improve industrial software usability without compromising accuracy. 
 This approach also generalizes well to other domains with complex, multi-step agentic workflows requiring specialized tool knowledge and configuration. As next steps, consider exploring multi-agent architectures using frameworks like Strands Agents SDK with Amazon Bedrock AgentCore for improved accuracy through specialized sub-agents. 
 About the authors 
 Yuan Tian 
 Yuan is an Applied Scientist at the AWS Generative AI Innovation Center, where he architects and implements generative AI solutions such as agentic systems for customers across healthcare, life sciences, finance, and energy. He brings an interdisciplinary background combining machine learning with computational biology, and holds a Ph.D. in Immunology from the University of Alabama at Birmingham. 
 Di Wu 
 Di is a Deep Learning Architect at AWS Generative AI Innovation Center, specializing in GenAI, AI agents, and model customization. He works with enterprise customers across diverse industries to architect and deliver production-ready AI solutions, including healthcare data analyst agents, travel booking voice agents, and database deep research agents. Outside of work, Di enjoys reading and writing. 
 Gan Luan 
 Gan is an Applied Scientist on the AWS Generative AI Innovation and Delivery team. He is passionate about leveraging generative AI techniques to help customers solve real-world business problems. 
 Haochen Xie 
 Haochen is a Senior Data Scientist at AWS Generative AI Innovation Center. He is an ordinary person. 
 Hayley Park 
 Hayley is an Applied Scientist at the AWS Generative AI Innovation Center, where she helps companies tackle real business problems by building generative AI applications. Before joining AWS GenAI, she worked on voice and language experiences across the Alexa Kids and Fire TV SLU teams. She holds a Ph.D. in Computational Linguistics from the University of Illinois at Urbana-Champaign, where her research focused on computational methods for low-resource languages, as well as an M.S. in Statistics. 
 Baishali Chaudhury 
 Baishali is an Applied Scientist at the Generative AI Innovation Center at AWS, where she focuses on advancing Generative AI solutions for real-world applications. She has a strong background in computer vision, machine learning, and AI for healthcare. Baishali holds a PhD in Computer Science from University of South Florida and PostDoc from Moffitt Cancer Centre. 
 Jared Kramer 
 Jared is an Applied Science Manager at AWS Generative AI Innovation Center. 
 Arun Ramanathan 
 Arun is a Senior Generative AI Strategist at AWS Generative AI Innovation Center.
```

---

## 2. Secure short-term GPU capacity for ML workloads with EC2 Capacity Blocks for ML and SageMaker training plans

- 日期: 2026-05-07 15:59
- 链接: https://aws.amazon.com/blogs/machine-learning/secure-short-term-gpu-capacity-for-ml-workloads-with-ec2-capacity-blocks-for-ml-and-sagemaker-training-plans/

```
As companies of various sizes adopt graphic processing units (GPU)-based machine learning (ML) training, fine-tuning and inference workloads, the demand for GPU capacity has outpaced industry-wide supply . This imbalance has made GPUs a scarce resource , creating a challenge for customers who need reliable access to GPU compute resources for their ML workloads. 
 When you encounter GPU capacity limitations, you might consider creating on-demand capacity reservations (ODCRs) . ODCRs apply to planned, steady-state workloads with well-understood usage patterns. Short-term ODCR availability for GPU instances, particularly P-type instances, is often limited. Additionally, without a long-term contract, ODCRs are billed at on-demand rates, offering no cost advantage. This makes ODCRs unsuitable for short or exploratory workloads such as testing, evaluations, or events. A guided approach to secure short-term GPU capacity becomes necessary. 
 In this post, you will learn how to secure reserved GPU capacity for short-term workloads using Amazon Elastic Compute Cloud (Amazon EC2) Capacity Blocks for ML and Amazon SageMaker training plans . These solutions can address GPU availability challenges when you need short-term capacity for load testing, model validation, time-bound workshops, or preparing inference capacity ahead of a release. 
 Solution overview and short-term GPU options 
 There are several ways to access GPU capacity on AWS for short-term workloads: 
 On-demand GPU instances 
 On-demand instances are usually the first option for short-term GPU usage. If capacity is available at launch time, you can start using GPU instances immediately without prior commitment. This works well for ad hoc experiments, short tests and development tasks. 
 On-demand GPU capacity depends on regional supply and current demand, and availability can change quickly. If you stop or scale down an instance, you might not be able to reacquire the same capacity when needed again. This uncertainty often leads to keeping GPU instances running longer than needed, which can increase cost. Choose on-demand instances when your workload can tolerate potential launch delays or when timing is flexible. 
 Spot GPU instances 
 Spot instances can reduce your GPU compute costs by up to 90% , but they trade cost saving for availability certainty. Spot capacity depends on unused capacity in the AWS Region. Instances can be interrupted when Amazon EC2 needs the capacity back, thus spot instances are suitable only for workloads that can handle interruption. 
 For ML workloads, spot instances work well when you can checkpoint progress and restart. Recommended use cases include distributed training jobs with periodic checkpoints, batch inference workloads that can be retried, and workshop environments that are designed to tolerate partial capacity. 
 Amazon EC2 Capacity Blocks for ML 
 Amazon EC2 Capacity Blocks for ML reserves GPU capacity for a specific time window so that the requested instances will be available when you launch them during the reserved period. Unlike ODCRs, Capacity Blocks are fully self-service and offer better short-term availability for GPU instances with a 40-50% discounted rate. Each Capacity Block represents a reservation of a specific number of a selected instance type for a defined duration. You can: 
 Reserve a start time up to eight weeks in advance. 
 Choose a duration from 1–14 days (in 1-day increments) or 15–182 days (in 7-day increments). 
 Configure up to 64 instances per Capacity Block. 
 Configure up to 256 instances across multiple Capacity Blocks across accounts in your AWS Organizations on a particular date (minimum of four blocks needed to reach this limit; blocks can run concurrently). 
 Organizations can purchase Capacity Blocks and provision them across multiple accounts , allowing different workloads to access a pool of reserved capacity at no additional cost. 
 Capacity Blocks apply to workloads that run directly on Amazon EC2, where you manage the operating system, networking, and orchestration layers yourself. 
 Service level agreement (SLA) and hardware failures: If hardware fails during your reservation, you can terminate the affected instance and manually launch a replacement into the same Capacity Blocks reservation. The system returns the reserved capacity slot to your reservation after approximately 10 minutes of cleanup. Amazon EC2 maintains a buffer within each Capacity Block to support relaunching instances in case of hardware degradation, at no additional cost. 
 Note: Capacity Blocks have the following limitations: 
 Support only selected Amazon EC2 instance families , such as P5, Trn1 and Trn2, and do not cover every GPU instance type. 
 Can’t reserve capacity for Amazon SageMaker-managed instance types such as ml.p4dn or ml.p5. 
 Can’t be shared and used with Amazon SageMaker. 
 Can’t be moved or split. 
 UltraServer Capacity Blocks are scoped to the AWS account where purchased and can’t be shared across accounts or within AWS Organization . 
 Amazon SageMaker training plans 
 Amazon SageMaker training plans provide access to reserve GPU capacity for ML workloads in the Amazon SageMaker AI managed environment, such as training jobs, Amazon SageMaker HyperPod clusters and inference. SageMaker training plans aren’t interchangeable with EC2 Capacity Blocks. With SageMaker training plans, you can: 
 Schedule reservations for specific GPU-based instances and durations. 
 Access your capacity without managing underlying infrastructure. 
 Use a range of accelerated computing options, including the latest NVIDIA GPUs and AWS Trainium accelerators. 
 Note that G-type instances (except G6 instances) aren’t currently supported by SageMaker training plans. If you need G6 instances, contact your AWS account team. For detailed information about the supported instance types in a given AWS Region, duration, and quantity options, see Supported instance types, AWS Regions, and pricing . 
 Amazon SageMaker training plans apply to: 
 SageMaker training jobs 
 SageMaker HyperPod clusters 
 SageMaker Inference workloads 
 Choose this option when you want Amazon SageMaker AI to manage instance provisioning, scaling, and lifecycle while still securing reserved capacity during a defined window. 
 Decision framework: choosing the right option 
 When planning your short-term GPU strategy, you should evaluate options based on three key factors: 
 Availability: From on-demand to reserved capacity. 
 Cost model: On-demand pricing or upfront commitments with lower than on-demand pricing . 
 Workload environment: Amazon EC2 direct access compared to Amazon SageMaker-managed workloads. 
 From short-term to long-term capacity planning: While this post focuses on securing short-term GPU capacity, you might need to plan for longer-term or recurring workloads. You can run assessments based on historical data; or use short-term GPU resources to load test your workload and gain better understanding of the instance number and type needed for production. For production deployments or large-scale events requiring significant GPU capacity, start planning at least three weeks in advance. Work with your AWS account team to assess your requirements and develop a capacity strategy that meets your timeline. 
 Cost consideration 
 Capacity Blocks for ML require upfront payment and offer 40-50% lower hourly rates compared to on-demand pricing. For example in US East (N. Virginia), p5.48xlarge costs $34.608/hour with Capacity Blocks versus $55.04/hour on-demand . 
 SageMaker training plans are priced 70-75% below on-demand rates . You pay the price up front at the time you schedule the reservation. AWS regularly updates prices based on trends in supply and demand. You pay the rate that’s current at the time that you make the reservation, even if the training plan starts later after the price changes. 
 If your instances don’t run continuously throughout the reservation period, the total cost of making reservations might exceed on-demand cost. Evaluate based on your workload’s actual runtime needs. 
 Disclaimer: All pricing figures referenced in this section are based on publicly available AWS pricing as of the date of publication and are subject to change. For the most current pricing, refer to Amazon EC2 pricing and SageMaker AI pricing . 
 Decision process 
 Start with the least restrictive option and move toward reserved capacity when availability or timing becomes critical. 
 Decision tree to choose the right option for securing GPU capacity. 
 Step 1: Determine your infrastructure management model 
 If you need full control over the operating system, networking, and orchestration, use Amazon EC2 and use on-demand instances, spot instances, or Capacity Blocks. 
 If you want a managed service that handles infrastructure provisioning and operations for you, use Amazon SageMaker AI and use SageMaker on-demand or SageMaker training plans for ml.* instance types. 
 Step 2: Try on-demand capacity first 
 For both Amazon EC2 and Amazon SageMaker AI workloads, start with on-demand capacity. This approach: 
 Requires no prior commitment. 
 Allows immediate start if capacity is available. 
 If an initial launch fails, try these flexibility options: 
 Try a different AWS Region where capacity might be available. 
 Adjust the start time to off-hours when demand is typically lower. 
 Use spot instances as a supplement on workloads that can tolerate interruption. 
 Step 3: Use reserved capacity when certainty is required 
 If your workload must start at a specific time or your delivery timeline depends on reserved GPU access, reserving capacity becomes the appropriate choice: 
 For Amazon EC2 workloads, use Capacity Blocks for ML. 
 For Amazon SageMaker AI workloads, use Amazon SageMaker training plans for either training jobs, HyperPod clusters, or inference workloads. 
 Technical implementation: Reserving GPU capacity for inference with SageMaker training plans 
 This section shows you how to reserve and use GPU capacity for inference workloads managed by Amazon SageMaker training plans. Note that SageMaker training plans reservations are specific to the selected target resource. A plan purchased for inference can’t be used for Training Jobs or HyperPod clusters, or the reverse. 
 For other scenarios: 
 If you’re reserving capacity for SageMaker training jobs or SageMaker HyperPod clusters, refer to create training plans for training jobs or HyperPod clusters . 
 If your workload runs directly on Amazon EC2 and requires reserved capacity for a fixed window, refer to Capacity Blocks for ML . 
 Prerequisites 
 Before you begin, confirm that you have: 
 An AWS account with appropriate AWS Identity and Access Management (IAM) permissions . For creating training plans, use AmazonSageMakerTrainingPlanCreateAccess managed policy. 
 For creating, describing, and deleting inference endpoints, use the following policy: 
 {
 "Version": "2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateEndpointConfig",
 "sagemaker:CreateEndpoint",
 "sagemaker:DescribeEndpoint",
 "sagemaker:DeleteEndpoint",
 "sagemaker:DeleteEndpointConfig"
 ],
 "Resource": [
 "arn:aws:sagemaker:*:*:endpoint/*",
 "arn:aws:sagemaker:*:*:endpoint-config/*"
 ]
 }
 ]
} A SageMaker AI model resource created and ready for deployment. For instructions, see create a model . 
 The AWS Command Line Interface (AWS CLI) version 2.0 or later. 
 Create a training plan 
 To get started, go to the Amazon SageMaker AI console , choose Training plans in the left navigation pane, and choose Create training plan . 
 The Training plans page in the Amazon SageMaker AI console. 
 For example, choose your preferred training date and duration (1 day), instance type and count (1 ml.trn1.32xlarge) for Inference Endpoint, and choose Find training plan . 
 Configure your training plan by selecting the instance type, instance count, date and duration for your inference workload. 
 The console displays available plans with the total price. 
 Review the suggested plans with upfront pricing before accepting the reservation. 
 If you accept this training plan, add your training details in the next step and choose Create your plan . 
 Note: SageMaker training plans can’t be canceled after purchase. The reservation will expire automatically at the end of the reserved period. 
 To monitor training plan status 
 Review your training plan status in the console. 
 After creating your training plan, you can see the list of training plans. The plan initially enters a Pending state, awaiting payment. You pay the full price of a training plan up front. After AWS completes payment processing, the plan will transition to the Scheduled state. On the plan’s start date, it becomes Active , and the system allocates resources for your use. 
 To verify training plan status with AWS CLI 
 Use the following command to check the training plan status: 
 aws sagemaker describe-training-plan \
--training-plan-name your-training-plan-name \
--region your-region When the response shows "Status": "Active" , you can start running your inference tasks. Verify that the TargetResources field shows endpoint to confirm the plan is configured for inference workloads. 
 To create endpoint configuration 
 Use the following command to generate an endpoint configuration that uses the training plan resources: 
 aws sagemaker create-endpoint-config \
--endpoint-config-name your-endpoint-config-name \
--production-variants '[ 
 {
 "VariantName": "your-variant-name",
 "ModelName": "your-model-name",
 "InitialInstanceCount": 1,
 "InstanceType": "ml.trn1.32xlarge",
 "CapacityReservationConfig": {
 "MlReservationArn": "your-training-plan-arn",
 "CapacityReservationPreference": "capacity-reservations-only"
 }
 }
]' To deploy the endpoint 
 Create your endpoint resource by specifying the endpoint configuration from the previous step: 
 aws sagemaker create-endpoint \
--endpoint-name your-endpoint-name \
--endpoint-config-name your-endpoint-config-name To verify endpoint status 
 Check your endpoint status and training plan capacity reservation status: 
 aws sagemaker describe-endpoint \
--endpoint-name your-endpoint-name \
--region your-region Clean up resources 
 To avoid incurring ongoing charges, delete the resources that you created: 
 Delete the endpoint: 
 aws sagemaker delete-endpoint --endpoint-name your-endpoint-name Delete the endpoint configuration: 
 aws sagemaker delete-endpoint-config --endpoint-config-name your-endpoint-config-name Conclusion 
 Securing GPU capacity for transient workloads requires a different approach than planning long-term, steady-state usage. In this post, you learned how to approach short-term GPU capacity planning by: 
 Starting with on-demand capacity and increasing flexibility when possible. 
 Distinguishing between Amazon EC2–based workloads and Amazon SageMaker AI managed workloads. 
 Reserving capacity using Capacity Blocks or SageMaker training plans when availability and certainty are required. 
 You also learned how to use SageMaker training plans to reserve GPU capacity ahead of time. This capability helps reduce operational friction when preparing inference capacity for planned evaluations, releases, or expected traffic increases. 
 To learn more, refer to the following resources: 
 Capacity Blocks for ML 
 Reserve training plans for your training jobs or HyperPod clusters 
 Amazon SageMaker AI now supports Flexible Training Plans capacity for Inference 
 Amazon SageMaker AI Pricing 
 Reserve compute capacity with EC2 On-Demand Capacity Reservations 
 About the authors 
 Vanessa Ji 
 Vanessa Ji is an Associate Solutions Architect at Amazon Web Services. She partners with Independent Software Vendors (ISVs) to design scalable cloud architectures and drive solution adoptions. With a background in mechanical engineering and applied research, Vanessa focuses on generative AI, life science and manufacturing use cases. 
 Alvaro Sanchez Martin 
 Alvaro Sanchez Martin is a Senior Solutions Architect at Amazon Web Services, specializing in AI/ML and cloud engineering. He accelerates customers’ journeys from ideation to production, with deep expertise in generative AI and machine learning solutions. Alvaro leads business strategic discussions with senior leadership on technical and architectural trade-offs, best practices, and risk mitigation strategies. 
 Yati Agarwal 
 Yati Agarwal is a Senior Product Manager at Amazon Web Services (AI Platform). She owns the end-to-end capacity strategy for AI workloads, ensuring that the infrastructure powering the most demanding machine learning use cases is available, scalable, and reliable. Her scope spans the full AI development lifecycle – from foundation model training and fine-tuning at large scale, to inference serving real-time and batch customer workloads, to interactive ML development environments where data scientists and engineers iterate and experiment. She is passionate about understanding customer capacity requirements across each of these dimensions and translating them into actionable plans that bridge engineering, product, and operations – ensuring AI workloads run at scale, without disruption.
```

---

## 3. Overcoming reward signal challenges: Verifiable rewards-based reinforcement learning with GRPO on SageMaker AI

- 日期: 2026-05-07 15:53
- 链接: https://aws.amazon.com/blogs/machine-learning/overcoming-reward-signal-challenges-verifiable-rewards-based-reinforcement-learning-with-grpo-on-sagemaker-ai/

```
Training large language models requires accurate feedback signals, but traditional reinforcement learning (RL) often struggles with reward signal reliability. The quality of these signals directly influences how models learn and make decisions. However, creating robust feedback mechanisms can be complex and error prone. Real-world training scenarios often introduce hidden biases, unintended incentives, and ambiguous success criteria that can derail the learning process, leading to models that behave unpredictably or fail to meet desired objectives. 
 In this post, you will learn how to implement reinforcement learning with verifiable rewards (RLVR) to introduce verification and transparency into reward signals to improve training performance. This approach works best when outputs can be objectively verified for correctness, such as in mathematical reasoning, code generation, or symbolic manipulation tasks. You will also learn how to layer techniques like Group Relative Policy Optimization (GRPO) and few-shot examples to further improve results. You’ll use the GSM8K dataset (Grade School Math 8K: a collection of grade school math problems) to improve math problem solving accuracy, but the techniques used here can be adapted to a wide variety of other use cases. 
 Technical overview 
 Before diving into implementation, it’s helpful to understand the RL concepts that underpin this approach. RL addresses challenges in model training by establishing a structured feedback system through reward signals. This paradigm enables models to learn through interaction, receiving feedback that guides them toward optimal behavior. RL provides a framework for models to iteratively improve their responses based on clearly defined signals about the quality of their outputs, making it highly effective for training models that interact with users and must adapt their behavior based on outcomes. Traditional RL has highlighted an important consideration: the quality of the reward signal matters significantly. When reward functions are imprecise or incomplete, models can engage in “reward hacking,” finding unintended ways to maximize scores without achieving the desired behavior. Recognizing this limitation has led to the development of more rigorous approaches that focus on creating reliable, well-defined reward functions. 
 RLVR addresses reward hacking through rule-based feedback defined by the model tuner. It uses programmatic reward functions that automatically score outputs against specific criteria, enabling rapid iteration without the bottleneck of collecting human ratings. These “verifiable” rewards come from objective, reproducible rules, making RLVR ideal for evolving requirements because it learns general optimization strategies and adapts quickly to new scenarios. GRPO is a reinforcement learning algorithm that improves AI model learning by comparing performance within groups rather than across all data at once. It organizes training data into meaningful groups and optimizes performance relative to each group’s baseline, giving appropriate attention to each category. This group-aware optimization reduces training variance, accelerates convergence, and can produce models that perform consistently across various categories. Combining RLVR with GRPO creates a framework where automated rewards guide learning while group-relative optimization helps drive balanced performance. 
 You define reward functions for different task aspects, and GRPO treats these as distinct groups during training, facilitating simultaneous improvement across dimensions. This combination delivers rapid adaptation and robust performance, ideal for dynamic environments requiring generalization beyond training distribution. Adding few-shot learning enhances this framework in three ways. First, few-shot examples provide templates that show the model what good outputs look like, narrowing the search space for exploration. Second, GRPO leverages these examples by generating multiple candidate responses per prompt and learning from their relative performance within each group. Third, verifiable rewards immediately confirm which approaches succeed. This combination accelerates learning: the model starts with concrete examples of the desired format, explores variations efficiently through group-based comparison, and receives definitive feedback on correctness. 
 Solution overview 
 In this section, you will walk through how to fine-tune a Qwen2.5-0.5B model on SageMaker AI using Amazon Amazon SageMaker Training Jobs . Amazon SageMaker Training jobs support distributed multi-GPU and multi-node configurations, so you can spin up high-performance clusters on demand, train billion-parameter models faster, and automatically shut down resources when the job finishes. 
 Note: While Qwen2.5-0.5B was selected for this use case, others like code generation will require a larger model (e.g. Qwen2.5-Coder-7B) and subsequently larger training instances. 
 Prerequisites 
 To run the example from this post on Amazon SageMaker AI, you must fulfill the following prerequisites: 
 An AWS account that will contain your AWS resources. 
 An AWS Identity and Access Management (IAM) role to access SageMaker AI. To learn more about how IAM works with SageMaker AI, see AWS Identity and Access Management for Amazon SageMaker AI . 
 You can run the notebook provided in this post from your preferred development environment, including interactive development environments (IDEs) such as PyCharm or Visual Studio Code, provided your AWS credentials are properly set up and configured to access your AWS account. To set up your local environment, refer to Configuring settings for the AWS CLI . Optionally, you can use Amazon SageMaker Studio for straightforward development process on SageMaker AI. 
 If you’re following along with this post, you will need a ml.p4d.24xlarge instance training. You will need access to these SageMaker training instances to run the example training code. If you’re unsure, you can review the AWS service quotas on the AWS Management Console : Choose Amazon SageMaker as the AWS service under Manage Quotas. 
 Select ml.p4d.24xlarge for training job usage and request an increase at account level. 
 Access to the GitHub repo: https://github.com/aws-samples/amazon-sagemaker-generativeai 
 Environment set up 
 You can use your preferred IDE, such as VS Code or PyCharm, but make sure your local environment is configured to work with AWS, as discussed in the prerequisites. 
 To use SageMaker Studio JupyterLab spaces complete the following steps: 
 On the Amazon SageMaker AI console, choose Domains in the navigation pane, then open your domain. 
 In the navigation pane under Applications and IDEs , choose Studio . 
 On the User profiles tab, locate your user profile, then choose Launch and Studio . 
 In Amazon SageMaker Studio, launch an ml.t3.medium JupyterLab notebook instance with at least 50 GB of storage. 
 A large notebook instance isn’t required, because the fine-tuning job will run on a separate ephemeral training instance with GPU acceleration. 
 To begin fine-tuning, start by cloning the GitHub repo and navigating to 3_distributed_training/reinforcement-learning/grpo-with-verifiable-reward directory, then launch the model-finetuning-grpo-rlvr.ipynb 
 Notebook with a Python 3.12 or higher version kernel 
 Prepare the dataset for fine-tuning 
 Running GRPO with RLVR requires you to have the final answer to each question to calculate reward. First, prepare the data by extracting the final answer for each question. 
 dataset = GSM8K(split='train', include_answer=False, include_reasoning=True, few_shot=True, num_shots=8, seed=None, cot=True).dataset.shuffle(seed=42)
Dataset({
    features: ['question', 'answer', 'prompt', 'final_answer'],
    num_rows: 7473
}) 
 In addition, this example uses few-shot examples (8 shots) to improve model training performance. For more information on few-shot examples in reinforcement learning, refer to the paper “Reinforcement Learning for Reasoning in Large Language Models with One Training Example” . While the research paper focuses on single-shot examples, this post will show you both single and multi-shot performance. 
 Each input will contain 8 examples, followed by the problem to be solved: 
 "Question: Mark has $50 and buys a toy that costs $35. How much money does he have left?
Solution: Let's think step by step. To find out how much money Mark has left, subtract the cost of the toy from the total amount of money Mark has. So, $50 - $35 = $15.
#### The final answer is 15

Question: Emily has 3 times as many pencils as Alice. If Alice has 15 pencils, how many pencils does Emily have?
Solution: Let's think step by step. To find out how many pencils Emily has, we multiply the number of pencils Alice has by 3. Alice has 15 pencils, so Emily has 15 * 3 = 45 pencils.
#### The final answer is 45

Question: Jack has collected 12 more marbles than Kevin. If Kevin has 27 marbles, how many marbles does Jack have?
Solution: Let's think step by step. To find how many marbles Jack has, we add 12 to the number of marbles Kevin has. So, Jack has 27 + 12 = 39 marbles.
#### The final answer is 39

Question: There are 24 students in a classroom. If each group must have 4 students, how many groups can be formed?
Solution: Let's think step by step. To find how many groups can be formed, we divide the number of students by the number of students per group. So, 24 / 4 = 6 groups can be formed.
#### The final answer is 6

Question: Samantha baked 40 cookies and wants to divide them equally into bags, with each bag containing 5 cookies. How many bags will Samantha need?
Solution: Let's think step by step. To find the number of bags needed, divide the total number of cookies by the number of cookies per bag. Thus, 40 divided by 5 equals 8.
#### The final answer is 8

Question: A pack of pencils costs $4. If you buy 7 packs, how much will you spend in total?
Solution: Let's think step by step. The total cost is found by multiplying the cost per pack by the number of packs. Hence, you spend 7 * $4 = $28.
#### The final answer is 28

Question: A book has 240 pages, and Sarah reads 20 pages each day. How many days will it take her to finish the book?
Solution: Let's think step by step. Sarah reads 20 pages per day, so we divide the total pages by the number of pages she reads per day. Therefore, it takes her 240 / 20 = 12 days to finish the book.
#### The final answer is 12

Question: A farmer has a total of 80 apples and oranges. If he has 30 apples, how many oranges does he have?
Solution: Let's think step by step. To determine the number of oranges, we subtract the number of apples from the total number of fruits. So, the number of oranges is 80 - 30 = 50.\n
#### The final answer is 50

Question: Mimi picked up 2 dozen seashells on the beach.  Kyle found twice as many shells as Mimi and put them in his pocket. Leigh grabbed one-third of the shells that Kyle found.  How many seashells did Leigh have?
Solution: Let's think step by step. 
 After the data has been prepared, keep 10 percent of the data as a validation set and push both training and validation set to S3. 
 The Verifiable Reward Function 
 This GRPO implementation for mathematical reasoning employs a dual-reward system that provides objective, verifiable feedback during training. This approach leverages the inherent verifiability of mathematical problems to create reliable training signals without requiring human annotation or subjective evaluation.You will implement two complementary reward functions that work together to guide the model toward both correct response formatting and mathematical accuracy of the result: 
 Format Reward Function 
 This function helps verify the model learns to structure its responses correctly by: 
 Pattern Matching : Searches for the specific format #### The final answer is [number] 
 Consistent Scoring : Awards 0.5 points for proper formatting, 0.0 for incorrect format 
 Training Signal : Encourages the model to follow the expected answer structure 
 #Format reward function

def format_reward_func_qa(completions, **kwargs):
    pattern = r"\n#### The final answer is \d+"    
    completion_contents = [completion for completion in completions]    
    matches = [re.search(pattern, content) for content in completion_contents]
    return [0.5 if match else 0.0 for match in matches] 
 Correctness Reward Function 
 This function provides the core mathematical verification by: 
 Answer Extraction : Uses regex to extract numerical answers from formatted responses 
 Normalization : Removes common formatting characters (commas, currency symbols, units) 
 Precision Comparison : Uses a tolerance of 1e-3 to handle floating-point precision 
 Binary Scoring : Awards 1.0 for correct answers, 0.0 for incorrect ones 
 #Correctness reward function

def correctness_reward_func_qa(completions, final_answer, **kwargs):
    rewards = []
    
    for completion, ground_truth in zip(completions, final_answer):
        try:
            match = re.search(r'####.*?([\d,]+(?:\.\d+)?)', completion)
            if match:
                answer = match.group(1)
                
                for remove_char in [',', '$', '%', 'g']:
                    answer = answer.replace(remove_char, '')
                    
                if abs(float(answer)-float(ground_truth)) < 1e-3:
                    rewards.append(1.0)
                else:
                    rewards.append(0.0)
            else:
                rewards.append(0.0)
        except ValueError:
            rewards.append(0.0)
            
    return rewards 
 Integrating RLVR with GRPO 
 The reward functions are integrated into the GRPO training pipeline through the GRPOTrainer: 
 rewards_funcs = [format_reward_func_qa, correctness_reward_func_qa]

trainer = GRPOTrainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    processing_class=tokenizer,
    peft_config=peft_config,
    reward_funcs=rewards_funcs,
) 
 During training, GRPO uses these reward functions to compute policy gradients. First the model generates multiple completions for each mathematical problem. Next, the reward for each response is computed for both reward functions. The format reward function will grant up to 0.5 for proper response structure, and the correctness reward function will grant up to 1.0 for the mathematical accuracy of the answer for a maximum combined reward of 1.5 per completion. Then GRPO compares the completions within groups to identify the best responses. Finally, in the policy update step, the loss function uses reward differences to update model parameters. Higher-rewarded completions increase their probability, while lower-rewarded completions decrease their probability. This relative ranking drives the optimization process.The following example demonstrates how to fine-tune Qwen2.5-0.5B. The recipe is provided in the scripts folder, allowing you to customize it or change the base model. Here you will use GRPO with verifiable rewards using Quantized Low-Rank Adaptation (QLoRA). QLoRA is used here as a technique to reduce training resource requirements and speed up the training process, with a small trade off in accuracy. 
 # Model arguments
model_name_or_path: Qwen/Qwen2.5-0.5B
tokenizer_name_or_path: Qwen/Qwen2.5-0.5B
model_revision: main
torch_dtype: bfloat16
attn_implementation: flash_attention_2
bf16: true
tf32: true
output_dir: /opt/ml/model/Qwen2.5-0.5B-RL-VR-GRPO

# Dataset arguments
train_dataset_id_or_path: /opt/ml/input/data/train/dataset.json
test_dataset_id_or_path: /opt/ml/input/data/val/dataset.json
dataset_splits: 'train'
max_seq_length: 2048
packing: true

# LoRA arguments
use_peft: true
load_in_4bit: true
lora_target_modules: ["q_proj", "k_proj", "v_proj", "o_proj", "up_proj", "down_proj", "gate_proj"]
lora_modules_to_save: ["lm_head", "embed_tokens"] 
lora_r: 16
lora_alpha: 16

# Training arguments
num_train_epochs: 2
per_device_train_batch_size: 16
gradient_accumulation_steps: 2
gradient_checkpointing: true
gradient_checkpointing_kwargs:
  use_reentrant: True
learning_rate: 1.84e-4
lr_scheduler_type: cosine
warmup_ratio: 0.1

# Logging arguments
logging_strategy: steps
logging_steps: 5
report_to:
- mlflow
save_strategy: "no"
seed: 42 
 Recipe overview 
 This recipe implements Group Relative Policy Optimization (GRPO) with verifiable rewards for fine-tuning the Qwen2.5-0.5B model on mathematical reasoning tasks. The recipe uses a dual-reward system that objectively evaluates both answer formatting and mathematical correctness without requiring human annotation. 
 Important Hyperparameters: 
 learning_rate : 1.84e-4 – Learning rate optimized for GRPO training 
 num_train_epochs : 2 – Training epochs to avoid overfitting 
 per_device_train_batch_size : 16 with gradient_accumulation_steps: 2 – Effective batch size of 32 
 max_seq_length : 2048 – Context window for 8-shot prompting 
 lora_r : 16 and lora_alpha : 16 – LoRA rank and scaling parameters 
 warmup_ratio : 0.1 with cosine scheduler – Learning rate scheduling 
 lora_target_modules – Targets attention and MLP layers for adaptation 
 As a next step, you will use a SageMaker AI training job to spin up a training cluster and run the model fine-tuning. The SageMaker AI Model Trainer . ModelTrainer runs training jobs on fully managed infrastructure; handling environment setup, scaling, and artifact management. It also allows you to specify training scripts, input data, and compute resources without manually provisioning servers. Library dependencies can be managed through the requirements.txt file in scripts folder. ModelTrainer will automatically detect this file and install the listed dependencies at runtime. 
 First, set up your environment. Here you’ll specify the instance type and number of instances for training and the location of the training container. 
 from sagemaker.core import image_uris
from sagemaker.core.helper.session_helper import Session
sagemaker_session = Session()

bucket_name = sagemaker_session.default_bucket()
default_prefix = sagemaker_session.default_bucket_prefix
configs = load_sagemaker_config()

instance_type = "ml.g6.48xlarge"
instance_count = 1
config_filename = "Qwen2.5-0.5B.yaml" 

image_uri = image_uris.retrieve(
    framework="pytorch",
    region=sagemaker_session.boto_session.region_name,
    version="2.7.1",
    instance_type=instance_type,
    image_scope="training"
) 
 Next, configure the environment variables, code locations, and data paths: 
 from sagemaker.train.configs import (
 CheckpointConfig,
 Compute,
 OutputDataConfig,
 SourceCode,
 StoppingCondition,
)
from sagemaker.train.distributed import Torchrun
from sagemaker.train.model_trainer import ModelTrainer

env = {}
env["FI_PROVIDER"] = "efa"
env["NCCL_PROTO"] = "simple"
env["NCCL_SOCKET_IFNAME"] = "eth0"
env["NCCL_IB_DISABLE"] = "1"
env["NCCL_DEBUG"] = "WARN"
env["HF_token"] = os.environ['hf_token']
env["CONFIG_PATH"] = f"recipes/{config_filename}"
env["MLFLOW_EXPERIMENT_NAME"]= "grpo-rlvr"
env["MLFLOW_TAGS"] =  '{"source.job": "sm-training-jobs", "source.type": "grpo-rlvr", "source.framework": "pytorch"}'
env["MLFLOW_TRACKING_URI"] =  MLFLOW_TRACKING_SERVER_ARN

# Define the script to be run
source_code = SourceCode(
    source_dir="./scripts",
    requirements="requirements.txt",
    entry_script="run_finetuning.sh",
)

# Define the compute
compute_configs = Compute(
    instance_type=instance_type,
    instance_count=instance_count,
    keep_alive_period_in_seconds=3600,
)

# define Training Job Name
job_name = f"train-{config_filename.split('/')[-1].replace('.', '-').replace('yaml', 'rlvr')}"

# define OutputDataConfig path
output_path = f"s3://{bucket_name}/{job_name}"
# Define the ModelTrainer
model_trainer = ModelTrainer(
    training_image=image_uri,
    environment=env,
    source_code=source_code,
    base_job_name=job_name,
    compute=compute_configs,
 stopping_condition=StoppingCondition(max_runtime_in_seconds=18000),
    output_data_config=OutputDataConfig(s3_output_path=output_path),
    checkpoint_config=CheckpointConfig(
        s3_uri=output_path + "/checkpoint", local_path="/opt/ml/checkpoints"
    ),
) 
 Set up the channels for training and validation data: 
 from sagemaker.train.configs import InputData

# Pass the input data
train_input = InputData(
    channel_name="train",
    data_source=train_dataset_s3_path, # S3 path where training data is stored
)

val_input = InputData(
    channel_name="val",
    data_source=val_dataset_s3_path, # S3 path where training data is stored
)

# Check input channels configured
data = [train_input, val_input] 
 Then begin training: model_trainer.train(input_data_config=data) The following is the directory structure for source code of this example: 
 scripts/
├── accelerate_configs/                       # Accelerate configuration files
├── run_finetuning.sh      # Launch script for distributed training with Accelerate on SageMaker training jobs
├── run_grpo.py               # Main training script for GRPO
├── utils/                   # utilities to load data and create prompt
├── recipes/                           # Predefined training configuration recipes (YAML)
└── requirements.txt                   # Python dependencies installed at runtime 
 To fine-tune across multiple GPUs, the example training script uses Huggingface Accelerate and DeepSpeed ZeRO-3, which work together to train large models more efficiently. Huggingface Accelerate simplifies launching distributed training by automatically handling device placement, process management, and mixed precision settings. DeepSpeed ZeRO-3 reduces memory usage by partitioning optimizer states, gradients, and parameters across GPUs—allowing billion-parameter models to fit and train faster.You can run your GRPO trainer script with Huggingface Accelerate using a simple command like the following: 
 NUM_GPUS=$(nvidia-smi --list-gpus | wc -l)
echo "Detected ${NUM_GPUS} GPUs on the machine"

# Launch fine-tuning with Accelerate + DeepSpeed (Zero3)
accelerate launch \
  --config_file accelerate_configs/deepspeed_zero3.yaml \
  --num_processes ${NUM_GPUS} \
  run_grpo.py \
  --config $CONFIG_PATH 
 Results 
 After evaluating the models on 100 test samples, the 8-shot GRPO-trained model achieved 41% accuracy compared to the base model’s 11%, demonstrating a 3.7x improvement in chain-of-thought mathematical reasoning. 
 The following chart shows a distinct threshold related to context length, revealing an optimal range of samples for reasoning activation. While 0-shot (6%) and 2-shot (3%) configurations performed poorly – even worse than the base model – performance dramatically improved at 4-shot prompting (33%), then peaked at 8-shot context (41%). This non-linear scaling pattern suggests that GRPO training creates reasoning patterns that require a certain number of examples to activate effectively. The model appears to have learned to leverage group comparisons from multiple examples, consistent with GRPO’s group-based policy optimization approach where the model learns to compare and select optimal reasoning paths from multiple generated solutions. 
 Extending RLVR to other domains 
 While this post focused on mathematical reasoning with GSM8K, the RLVR approach generalizes to domains with objectively verifiable outputs. Two promising directions demonstrate this versatility: 
 Code generation with execution-based rewards 
 Code generation provides natural verification through execution. Partial rewards can be awarded when code compiles and runs without errors, while full rewards are achieved when outputs pass comprehensive unit tests. Domain experts specify requirements using natural language prompts, while the reward model automatically evaluates correctness through code execution—alleviating subjective human evaluation. 
 Domain-specific text generation with semantic validation 
 For specialized domains like medical or technical writing, keyword-based rewards can guide models toward appropriate terminology. Partial rewards encourage inclusion of required terms, while full rewards require complete keyword sets in semantically appropriate contexts. For instance, medical text generation can reward outputs that combine diagnostic keywords (“symptoms,” “diagnosis”) with treatment keywords (“therapy,” “medication”) in clinically valid patterns, teaching domain vocabulary through measurable targets. These examples illustrate how verifiable rewards extend beyond mathematical reasoning to tasks where correctness can be programmatically validated, setting up the foundation for broader applications of this training approach. 
 Cleaning Up 
 To clean up your resources to avoid incurring more charges, follow these steps: 
 Delete any unused SageMaker Studio resources . 
 Optionally, delete the SageMaker Studio domain . 
 Delete any S3 buckets created 
 Verify that your training job isn’t running anymore! To do so, on your SageMaker console, choose Training and check Training jobs. 
 To learn more about cleaning up your resources provisioned, check out Clean up . 
 Conclusion 
 In this example you trained a Qwen2.5-0.5B model using GRPO (Group Relative Policy Optimization) on GSM8K: a dataset of 8,500 grade school math word problems that require multi-step arithmetic reasoning and natural language understanding. Each problem includes a question like “ Janet’s ducks lay 16 eggs per day… ” with step-by-step solutions ending in numerical answers, making it ideal for verifiable reward training. 
 This implementation demonstrates the effectiveness of Reinforcement Learning with Verifiable Rewards (RLVR) for mathematical reasoning tasks. The GRPO-trained Qwen2.5-0.5B model achieved a 3.7x improvement over the base model, reaching 41% accuracy on GSM8K compared to the baseline 11%.The evaluation results validate RLVR as a promising approach for domains with objectively verifiable outcomes, offering an alternative to preference-based training methods. The threshold behavior suggests GRPO learns to leverage group comparisons from multiple examples, consistent with its group-based optimization approach. This work establishes a foundation for applying verifiable reward systems to other domains requiring logical rigor and mathematical accuracy. 
 For more information on Amazon SageMaker AI fully managed training, refer to the training section of the SageMaker AI documentation . The supporting code for this post can be found in GitHub. 
 About the authors 
 Surya Kari is a Senior Generative AI Data Scientist at AWS, specializing in developing solutions leveraging state-of-the-art foundation models. He has extensive experience working with advanced language models including DeepSeek-R1, the Llama family, and Qwen, focusing on their fine-tuning and optimization for specific scientific applications. His expertise extends to implementing efficient training pipelines and deployment strategies using AWS SageMaker, enabling the scaling of foundation models from development to production. He collaborates with customers to design and implement generative AI solutions, helping them navigate model selection, fine-tuning approaches, and deployment strategies to achieve optimal performance for their specific use cases. 
 Giuseppe Zappia is a Principal AI/ML Specialist Solutions Architect at AWS, focused on helping large enterprises design and deploy ML solutions on AWS. He has over 20 years of experience as a full stack software engineer, and has spent the past 6 years at AWS focused on the field of machine learning. 
 Amin Dashti is a Senior Data Scientist and researcher at AWS who bridges deep theoretical insight with practical machine learning expertise. With a background in theoretical physics and over seven years of experience, he has designed and deployed scalable models across domains — from predictive analytics and statistical inference in financial systems to cutting-edge applications in computer vision (CV) and natural language processing (NLP).
```

---

## 4. Agents that transact: Introducing Amazon Bedrock AgentCore payments, built with Coinbase and Stripe

- 日期: 2026-05-07 12:55
- 链接: https://aws.amazon.com/blogs/machine-learning/agents-that-transact-introducing-amazon-bedrock-agentcore-payments-built-with-coinbase-and-stripe/

```
We’re in the midst of a fundamental shift in how software gets built and used. AI agents are moving beyond assistants that wait for instructions. They call APIs, access MCP servers, coordinate with other agents, and complete complex multi-step tasks on behalf of users. As agents take on increasingly diverse tasks, the ecosystem around them is expanding just as fast to meet that demand. 
 Looking further ahead, services, tools, and content must be designed for humans and agents. Agents will discover, evaluate, and pay for resources when they need, all within a single execution loop. The services that support them must be priced and consumed in that way: fractions of a cent per call, billed in real time. Early protocols like x402, ACP, MPP, and AP2 are pioneering what this looks like, and teams are experimenting with payment-enabled agents. The building blocks are emerging, but the agentic economy is still in its earliest days, and the infrastructure to support it at scale doesn’t exist yet. For developers who want to get ahead of this, the path has been hard. You’d wire up bespoke billing relationships with every service provider, manage credentials securely, enforce spending governance, navigate compliance requirements, and write orchestration logic across a fragmented landscape. That’s months of engineering effort, and the stakes are high: a misconfigured payment flow doesn’t just produce a bad answer, it moves real money. 
 Today, we’re announcing Amazon Bedrock AgentCore payments (preview), a new set of features in Amazon Bedrock AgentCore, enabling AI agents to instantly access and pay for what they use, such as web content, APIs, MCP servers, and other agents. We’ve built these capabilities in partnership with Coinbase and Stripe, who are providing the wallet infrastructure and payment rails that power the first set of capabilities. 
 AgentCore is the platform to build, connect, and optimize agents at scale, with security enforced at the infrastructure layer that agents can’t bypass. Developers from companies like Cox Automotive, Thomson Reuters, and PGA TOUR already use AgentCore to build agents that reason, plan, and act across complex workflows. With today’s announcement, those agents can also transact, using the same identity system, agent gateway, and observability they already rely on. Amazon Bedrock AgentCore Payment isn’t a bolted-on module, it’s native to the platform that the agent is built on, governed by the same controls as every other action the agent takes. 
 The first managed end-to-end payment capabilities for agents 
 This marks the first managed payment capabilities purpose-built for autonomous agents, spanning the full lifecycle from wallet authentication through transaction execution to spending governance and observability, so developers can focus on what their agents do, not on how they pay. 
 With these capabilities, developers can build agents that can reach any resource that they need, paid or at no cost, without wiring up each billing relationship by hand. A financial research agent can dynamically access real-time market data feeds and paywalled publications, paying for the articles and data points it uses on behalf of the end user. A coding agent can call specialized APIs and paid MCP servers as it needs them, whether that’s a private package registry, a sandboxed execution environment, or a niche third-party agent that handles one thing well. As the market matures, agents can handle commercial transactions: book flights, reserve hotels, and complete purchases on behalf of users across merchant platforms. 
 To get started, developers connect their agent to a wallet or payment service provider, register a funded payment source, and set spending limits per session. AgentCore manages all credential authentication and token lifecycle. When the agent encounters a paid resource during execution, AgentCore handles protocol negotiation, retries, and payment, routing the transaction through the appropriate provider without interrupting the agent’s reasoning loop. Every transaction is observable through the same logs, metrics, and traces that developers already use to monitor agent behavior. 
 AgentCore is designed to work with any framework and any protocol. We’ve carried that same flexibility into Amazon Bedrock AgentCore payments. Developers don’t have to track the evolving payment protocol landscape or lock into a single standard. At preview, we support the x402 protocol, with additional protocols on the roadmap. As new protocols emerge, we add support at the platform level so developers don’t have to rebuild their agents. 
 “At Warner Bros. Discovery, we’re actively exploring more flexible and scalable approaches to payments as we evolve beyond direct API integrations with third-party processors. AgentCore payments represents a promising direction, enabling our teams to experiment with possible agent-driven experiences where premium content, like live sports and tentpole releases, could be surfaced and transacted on seamlessly in the moment of interest. We’re particularly interested in evaluating its potential to reduce engineering overhead, streamline payment orchestration, and introduce governed, traceable transactions as we look at potential next-generation commerce experiences.” – Mit Majithia, Executive Vice President, Warner Brothers Discovery Inc. 
 Micropayment in preview: Unlocking paid data, APIs, and content for agent workflows 
 The first use case that we’re enabling in preview is where agents make instant micropayments to access APIs, MCP servers, web content, and other agents. Services are rapidly shifting to pay-per-use models, AI agent web crawling surged rapidly in the past year, and these transactions are typically under $1 or fractions of a cent. 
 Developers enable Amazon Bedrock AgentCore payments on their existing agent using the AgentCore SDK or console. You choose between a Coinbase wallet or a Stripe Privy wallet as your payment connection. With both options, end users can fund wallets through stablecoin or fiat using a debit card. Guardrails are enforced at multiple layers. Before an agent can transact, the end user must explicitly authorize the agent to access and use their wallet. At runtime, spending limits are enforced per session, keeping the agent within the budget set for each execution. The agent never has open-ended access to funds. It operates only with explicit permission and within defined limits. 
 Under the hood, the payment flow is built around the x402 protocol, an open HTTP-native payment standard that enables instant stablecoin micropayments. When an agent sends a request to a paid endpoint and receives an HTTP 402 “Payment Required” response, payment processing authenticates with the configured wallet, executes the stablecoin payment, attaches payment proof, and delivers the content back to the agent, all within the execution loop. The payment manager orchestrates the flow while payment limits track spend against session budgets throughout. After enabled, the agent begins orchestrating payments during execution, with full traceability available in the AgentCore console. 
 To help agents find merchants on their own, we’re making the Coinbase x402 Bazaar MCP server available through AgentCore gateway. The bazaar provides a curated list of x402 endpoints that agents can search, discover, and pay for when relevant to their task, turning paid services into something agents can find and use on their own rather than requiring developers to hardcode each integration. 
 Heurist AI, which offers full-stack infrastructure for the AI economy, is building a research agent that performs financial analysis on behalf of end users, using payments capabilities in AgentCore. “Heurist is using AgentCore payments for our research agent which helps end customers to perform financial and crypto analysis and investment advice”, said JW Wang, Founder at Heurist AI. “End customers can set a budget for the research and the agent uses AgentCore payments to get accurate real-time data, commonly around markets, social sentiment, and news. We were able to integrate payments quickly to our agent with low effort and few lines of code.” 
 Built with an ecosystem of partners 
 Coinbase developed the x402 protocol, the open standard that’s quickly gaining traction for machine-to-machine payments, and they built the CDP wallet infrastructure and facilitation that power the micropayment flows in preview. Coinbase has been innovating on AWS for years, serving millions of customers in cryptocurrency exchange and developer platform. We’re now working together as members of the x402 Foundation to establish open standards for the agent economy. 
 “There will soon be more AI agents transacting than humans, and they need money that’s built for the internet – programmable, always on, and global. By bringing Coinbase’s stablecoin infrastructure and x402 into AWS AgentCore, we’re giving developers the full stack to build agents that move money at software speed, with the trust and compliance enterprises expect.” – Brian Foster, Head of Infrastructure Growth and Strategy, Coinbase. 
 Stripe is helping define how commerce works in the agent era, building tools that enable AI agents to discover, negotiate, and complete transactions on behalf of businesses and consumers. With the launch of new payment capabilities, AgentCore is integrating Stripe’s wallet infrastructure, powered by Privy, as a payment connection at preview, giving developers direct access to Stripe’s payment infrastructure from day one. Together, AWS and Stripe are working toward a shared path to fiat payment support as we expand beyond micropayments, combining Stripe’s global payments reach with the agent platform where developers are already building. 
 “Stripe is building the economic infrastructure for AI. For agents to become meaningful economic actors, they need a way to hold and spend money. That’s why we’re excited to partner with AWS to make stablecoin wallets for agents readily available to AgentCore developers.” – Henri Stern, CEO of Privy, a Stripe company. 
 Where we’re headed 
 Micropayments are the first step, addressing the early agent-to-agent commerce patterns where we see the most immediate pull. Beyond micropayments, we see a natural expansion into broader commerce flows where agents act on behalf of buyers, not just other agents. An agent booking flights, reserving hotels, or completing purchases across merchant platforms on behalf of a customer. Getting there will require deeper integration with payment ecosystems, support for additional protocols, stronger buyer intent verification, and end-to-end observability across the full transaction lifecycle. That’s the road ahead, and we’re building for it. 
 The developer experience stays consistent across each phase. Configure your wallet, set your policies, and your agent transacts. What changes is the breadth of what agents can pay for and how. We’re excited about what’s to come. 
 Get started 
 Amazon Bedrock AgentCore payments are available in preview today in US East (N. Virginia), US West (Oregon), Europe (Frankfurt), and Asia Pacific (Sydney). Get started in the AgentCore console. Learn more by reading the documentation . 
 About the author 
 Preethi CN 
 Preethi is Director of AgentCore in the Agentic AI organization, with over 20 years of expertise in embedded and cloud software development. In her 14 years at Amazon, she has architected large-scale distributed systems and driven AI innovations across Retail, Alexa, and AWS, delivering breakthroughs in multimodal AI. She led speech recognition for Alexa, Computer Vision services at AWS, and generative AI transformation that revolutionized how organizations extract insights from unstructured content at scale. As a technical advisor to the Agentic AI Organization, she has provided strategic oversight across Amazon Quick, Kiro, and AWS Transform. Most recently, she crafted the vision and led the launch of AgentCore, the platform for building, connecting, and optimizing production-ready AI agents at scale.
```

---

## 5. Cost effective deployment of vision-language models for pet behavior detection on AWS Inferentia2

- 日期: 2026-05-06 15:37
- 链接: https://aws.amazon.com/blogs/machine-learning/cost-effective-deployment-of-vision-language-models-for-pet-behavior-detection-on-aws-inferentia2/

```
Tomofun , the Taiwan-headquartered pet-tech startup behind the Furbo Pet Camera, is redefining how pet owners interact with their pets remotely. Furbo combines smart cameras with AI to detect behaviors such as barking, running, or unusual activity, and alerts owners in real time. At the core of this capability are computer vision and vision-language models that interpret pet actions from the video streams. 
 Originally, Furbo’s inference workloads were hosted on GPU-based Amazon Elastic Compute Cloud (Amazon EC2) instances. While GPUs provided high throughput, they were also costly because the always-on inference needed to support real-time pet activity alerts at scale. To reduce costs and maintain accuracy, Tomofun turned to EC2 Inf2 instances powered by AWS Inferentia2, the Amazon purpose-built AI chips. In this post, we walk through the following sections in detail. 
 Challenge: Reducing GPU inference cost for real-time vision-language models at scale 
 Running advanced vision-language models like Bootstrapping Language-image Pre-Training (BLIP) , detailed in the original paper , were hosted on GPU instances and proved less cost-effective for always-on, real-time inference workloads at scale. The challenge was twofold: Tomofun needed to sustain cost efficiency for nearly continuous pet behavior monitoring across hundreds of thousands of devices, while also maintaining model fidelity and throughput. Tomofun needed to do this without rewriting large portions of the BLIP code base already optimized for PyTorch. 
 Solution overview 
 Before diving into the architecture, the following diagram provides a high-level view of how the system processes pet behavior detection at scale across AWS services. 
 Webcam interaction – Furbo’s API sits at the center of Tomofun’s pet-behavior detection service, orchestrating image streams from customer’s pet cameras to inference endpoints in AWS. The diagram shows the architecture of Elastic Load Balancing (ELB) and Amazon EC2 Auto Scaling group implemented using EC2 Inf2 instances providing scaling as the inference volume grows in real-time. When a camera captures a frame, the data is routed through Amazon CloudFront and an ELB to the first layer of the EC2 Auto Scaling group that hosts the pet-behavior detection API servers. After the API layer processes each request, it forwards the image to a second-layer Auto Scaling group dedicated to running model inference. 
 Model inference – After processing, the images are forwarded to a second layer EC2 Auto Scaling group containing inference instances. Inside this group, containers host the BLIP model, which can run on Inferentia2-based EC2 Inf2 instances. The BLIP model components compiled using the Neuron SDK are loaded into containers on Inf2 instances. In the early implementation, Furbo’s API routed inference calls exclusively to GPU containers, but now it can also direct requests to Inf2-based containers without changing the upstream API or downstream alert logic. This architecture allows Tomofun to direct inference requests to and switch between GPU and Inferentia2 backends in real-time. This maintains high availability and gives them the flexibility to scale cost-efficient inference while preserving the same API surface for Furbo users. 
 Metrics collection – Amazon CloudWatch monitors key operational metrics across the inference fleet, including latency, throughput, and error rates. These signals provide the observability needed to detect performance degradation early and ensure that service-level objectives are met as traffic patterns shift throughout the day. 
 Scaling with Demand – The ELB dispatches requests to the available instances within the Auto Scaling group, which manages the size of the instance pool size based on the incoming request count as the CloudWatch metric. This metric-driven approach is adopted because the throughput benchmarks for each instance type have already been established through stress testing, so scaling decisions can be driven directly by the volume of image requests. The result is an architecture that scales cost-efficient inference capacity in real time, maintaining high availability as demand grows. 
 Improving BLIP on Inferentia2 
 Before diving into the model details, the following diagram provides a high-level overview of the BLIP architecture and how its core components interact. 
 Source: BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation, 2022 https://arxiv.org/pdf/2201.12086 
 BLIP is composed of three components—the Image Encoder, Text Encoder, and Text Decoder, as shown in the image. For support on Inferentia2, models can be broken into components and wrapped to fit input and output shapes. Tomofun applied this method to BLIP, creating lightweight wrappers for each of the three components of the BLIP model so the original architecture remained unchanged. Each component was compiled independently with torch_neuronx and then combined into the inference pipeline, allowing inputs to flow sequentially. This modular approach maintained compatibility with Inferentia2 without altering BLIP’s pretrained logic. 
 Original model code 
 The first step is to isolate the original BLIP Text Encoder so it can be compiled without modifying its internal logic. The TextEncoder class is a thin wrapper around the original submodule ( model.text_encoder.model ) that standardizes the forward output by returning only the primary tensor. This makes the component straightforward to trace and compile with Neuron while preserving the original architecture. 
 class TextEncoder(torch.nn.Module):
    def __init__(self, model):
        super().__init__()
        self.model = model

    def forward(self, input_ids, attention_mask, encoder_hidden_states, encoder_attention_mask):
        output = self.model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            encoder_hidden_states=encoder_hidden_states,
            encoder_attention_mask=encoder_attention_mask,
            return_dict=False,
        )
        return output[0] 
 During the compilation phase , the original model ( model.text_encoder.model ) is passed directly into torch_neuronx.trace() and compiled into a Neuron-optimized TorchScript artifact, without modifying the pretrained BLIP logic. 
 Wrapper code 
 A wrapper is needed because the torch_neuronx.trace() API expects a tensor tuple of tensors as input and output. To avoid rewriting the model, lightweight wrappers act as an adapter layer that reformats inputs and outputs while keeping the original architecture unchanged. This approach minimizes code changes and allows the compiled components to integrate seamlessly into the existing inference pipeline. 
 class TextEncoderWrapper(torch.nn.Module):
    def __init__(self, model):
        super().__init__()
        self.model = TextEncoder(model)

    @classmethod
    def from_model(cls, model):
        wrapper = cls(model)
        wrapper.model = model
        return wrapper

    def forward(self, input_ids, attention_mask, encoder_hidden_states, encoder_attention_mask, return_dict):
        output = self.model(input_ids, attention_mask, encoder_hidden_states, encoder_attention_mask)
        return (output,) 
 The wrapper is used only at deployment to load the compiled model and format I/O, so it fits the existing BLIP pipeline. 
 Compile : use the original model ( model.text_encoder.model ) 
 Deploy : use TextEncoderWrapper to run the compiled model 
 This keeps the original code unchanged while making the compiled model easy to plug into production. 
 Model compilation for Inferentia2 
 In the following code snippet, model.text_encoder.model represents the unmodified Text Encoder submodule, which is compiled into a Neuron-optimized TorchScript format. 
 def trace_model(model, directory, compiler_args=f"--auto-cast-type fp16 --logfile {LOG_DIR}/log-neuron-cc.txt"):
    if os.path.isfile(directory):
        print(f"Provided path ({directory}) should be a directory, not a file")
        return

    os.makedirs(directory, exist_ok=True)
    os.makedirs(LOG_DIR, exist_ok=True)
    
    # Skip trace if the model is already traced
    if not os.path.isfile(os.path.join(directory, 'text_encoder.pt')):
        print("Tracing text_encoder")
        
        # Step 1: Provide pseudo input data with expected shapes and dtypes
        inputs = (
            torch.ones((1, 8), dtype=torch.int64),
            torch.ones((1, 8), dtype=torch.int64),
            torch.ones((1, 577, 768), dtype=torch.float32),
            torch.ones((1, 577), dtype=torch.int64),
        )
        
        # Step 2: Use torch_neuronx.trace() to compile the model for Inferentia
        encoder = torch_neuronx.trace(model.text_encoder.model,
            inputs,
            compiler_args=compiler_args)
        
        # Step 3: Save the compiled model as TorchScript artifact
        torch.jit.save(encoder, os.path.join(directory, 'text_encoder.pt'))
    else:
        print('Skipping text_encoder.pt') 
 To compile BLIP components for Inferentia2, Tomofun defined a trace function that automates the conversion of GPU-trained PyTorch models into Inferentia-optimized artifacts. The process begins by preparing pseudo input tensors that represent the expected shapes and data types of the model’s inputs, which guides the tracing process. After the inputs are defined, the function calls torch_neuronx.trace() to compile the BLIP sub-model for Inferentia execution, producing a Neuron-optimized version of the original code. Finally, the compiled artifact is saved with torch.jit.save , making it ready for deployment on Inf2 instances. This three-step flow—loading the wrapper, providing pseudo input data, and compiling with Neuron—makes sure that Tomofun can migrate BLIP’s TextDecoder and other components without changing the original model code. 
 Model deployment on Inferentia2 
 In the deployment phase, the compiled submodules are loaded through wrapper classes to assemble the final BLIP inference pipeline. This separation creates a clear workflow where the original model components are used directly for Neuron improvement during compilation, while the wrapper classes handle input and output formatting during inference to ensure compatibility with Inferentia2. The deployment phase code is as following: 
 models.text_encoder = TextEncoderWrapper.from_model( 
 torch.jit.load(os.path.join(directory, 'text_encoder.pt'))) 
 This design preserved the original BLIP architecture without modification while meeting the Neuron SDK’s I/O interface requirements through lightweight wrapper classes. It also enabled a modular, component-level workflow for both compilation and deployment, allowing each BLIP submodule to be compiled and managed independently. As a result, the use of model.text_encoder.model is essential during the compilation phase for direct Neuron optimization, whereas the wrapper classes handle input and output formatting during inference to ensure smooth execution on Inferentia2. 
 Stress testing 
 To validate performance at scale, Tomofun conducted stress tests simulating real-world Furbo camera workloads. Each video stream triggered action detection queries such as “Is the dog barking?”, “Is the dog playing?”, or “Is the dog chewing furniture?”. These tests confirmed that Inf2 instances (one Inferentia2 chip, 32 GB memory) could sustain the required throughput while maintaining low latency. In addition to accuracy, the tests highlighted that the Inf2 deployment could handle simultaneous requests across hundreds of thousands of devices, making it well-suited for Furbo’s always-on global customer base. Importantly, the comparison baseline was running GPU-based instances with an on-demand pricing model, which reflected the cost Tomofun was paying before migration to Inf2. By migrating from those GPU on-demand deployments to Inf2.xlarge instances with Inferentia2, Tomofun achieved 83% cost reduction without compromising performance. 
 The chart illustrates how inference latency changes as server and client concurrency increase. The X-axis represents combinations of the labels represent #server threads – #client threads to simulate performance under different load scenarios. When only a few server threads are available, adding more client threads causes latency to rise quickly. Increasing the number of server threads helps absorb this load and keeps latency lower. At higher concurrency levels, latency increases and gains level off, indicating saturation. This experiment shows that teams should use load testing to identify the right balance between client concurrency and server capacity, and then limit concurrency to that range to achieve the right latency–cost tradeoff in production. 
 Conclusion 
 By migrating BLIP inference on AWS Inferentia-based EC2 Inf2 instances , Tomofun reduced their Furbo application deployment costs by 83%. The transition from GPU to Inferentia2 was seamless, as the migration required only lightweight wrapper classes and left BLIP’s core logic untouched. Testing confirmed that using Inferentia2 not only reduced the deployment costs, but also maintained high throughput for real-time inference at scale. Tomofun plans to migrate more workloads to Inferentia2 as it supports workloads beyond vision-language models, such as audio event detection for barking recognition and potential future integration with large language models to enhance pet-owner interactions. Additionally, the adoption of AWS Deep Learning Containers (DLCs) has been scheduled into the roadmap as a next step, using pre-built, improved container images to simplify dependency management and streamline inference workflows. 
 To learn how to implement similar improvements, explore the AWS Neuron documentation and examples you can reference AWS Neuron Document . You can also visit Furbo website to explore Furbo’s AI-powered features and see how the Furbo ecosystem keeps your pets safe. 
 About the authors 
 Chen-Hsin Ding is a Staff Machine Learning Engineer at Tomofun, with over 10 years of software development experience. He leads Generative AI projects and works closely with backend teams to design practical AI system architectures, focusing on bringing MLOps best practices into the AI team and delivering production-ready LLM and RAG applications. Outside of work, Chen-Hsin enjoys brewing coffee and listening to movie soundtracks and jazz on his hi-fi audio system. 
 Ray Wang is a Senior Solutions Architect at AWS. With 15 years of experience in the IT industry, Ray is dedicated to building modern solutions on the cloud, especially in NoSQL, big data, machine learning, and Generative AI. As a hungry go-getter, he passed all 12 AWS certificates to make his technical field not only deep but wide. He loves to read and watch sci-fi movies in his spare time. 
 Howard Su is a Solutions Architect at AWS. With extensive experience in software development and system operations, he has served in various roles including RD, QA, and SRE. Howard has been responsible for the architectural design of numerous large-scale systems and has led several cloud migrations. Following years of deep technical accumulation, he is now dedicated to advocating for DevOps by leveraging Generative AI to build self-healing, “AI-Native” infrastructures, transitioning the SDLC from traditional orchestration to a truly intelligent, predictive ecosystem.
```

---

## 6. How Hapag-Lloyd uses Amazon Bedrock to transform customer feedback into actionable insights

- 日期: 2026-05-05 16:55
- 链接: https://aws.amazon.com/blogs/machine-learning/how-hapag-lloyd-uses-amazon-bedrock-to-transform-customer-feedback-into-actionable-insights/

```
Hapag-Lloyd stands as one of the world’s leading liner shipping companies, operating a modern fleet of 313 container ships with a total transport capacity of 2.5 million TEU (Twenty-foot Equivalent Unit—a standard unit of measurement for cargo capacity in container shipping). The company maintains a container capacity of 3.7 million TEU, which includes one of the industry’s largest and most modern fleets of reefer containers. With approximately 14,000 employees in the Liner Shipping Segment and more than 400 offices spread across 140 countries, Hapag-Lloyd maintains a robust global presence. Through 133 liner services worldwide, we facilitate reliable connections between more than 600 ports across the continents. 
 The company’s Digital Customer Experience and Engineering team, distributed between Hamburg and Gdańsk, drives digital innovation by developing and maintaining customer-facing web and mobile products. 
 Over the past years, the Digital Customer Experience and Engineering team has evolved from a delivery-focused channel into a true digital product driver, with strong customer focus, engineering excellence, and measurable business impact. We take end-to-end ownership of our digital products, combining customer-centric innovation with engineering craft to directly support growth and business outcomes. Building on a modern, independently owned tech stack and a high level of engineering maturity, we are committed to staying at the forefront of technology. Now, we are taking the next step by moving toward becoming AI-native, investing heavily in artificial intelligence as a core capability. This journey is about amplifying powerful engineering with AI to build smarter products, faster innovation, and greater customer value. 
 Understanding user impact. 
 So far, our customer feedback analysis process had largely been manual and reactive. Especially ahead of review ceremonies, manually analyzing customer feedback could take hours, sometimes days, when hundreds of ratings and comments needed to be reviewed. Every two weeks, Product Managers exported customer feedback data as CSV files, read through large volumes of comments, and manually categorized sentiment and themes. Although this work was valuable and deeply connected to product decisions, it was also repetitive, time-consuming, and difficult to scale, limiting flexibility whenever faster or deeper insights were needed. 
 With our generative AI solution, we fundamentally changed this approach. Instead of manually aggregating and interpreting feedback, we now automate the entire workflow: collecting customer comments, extracting sentiment, identifying themes, and surfacing actionable insights. Product Managers and teams can focus less on operational analysis and more on strategy, innovation, and creating exceptional user experiences. 
 In this post, we walk you through our generative AI–powered feedback analysis solution built using Amazon Bedrock, Elasticsearch , and open-source frameworks like LangChain and LangGraph . Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models from leading AI companies such as AI21 Labs, Anthropic, Cohere, DeepSeek, Luma, Meta, Mistral AI and Amazon through a single API, along with a broad set of capabilities you need to build generative AI applications with security, privacy, and responsible AI. With this solution, you can automatically ingest customer comments, generate rich summaries, and deliver targeted insights. This allows our product teams to make faster, smarter decisions and drive continuous improvement. 
 We walk you through the architecture and implementation of this solution, demonstrating how using generative AI foundations, such as orchestration, data management, security, and privacy, allowed us to rapidly build a scalable, production-ready feedback processing pipeline. 
 Solution overview 
 AWS architecture for automated feedback processing and analysis, utilizing Lambda functions for data ingestion from Amazon S3, Amazon Bedrock for AI-powered insights accessed by stakeholders via Amazon ECS, and Elasticsearch for indexing and querying feedback data with email notifications via SES. 
 The solution is built on AWS architecture designed to address these challenges through scalability, maintainability, and security. It is deployed by using AWS CloudFormation . 
 Continuous & Quarterly Feedback Collection Our web and mobile applications serve hundreds of thousands of customers each month. 
 Users can leave a rating plus text comments, helping us understand user experience and improve services. 
 Daily Feedback Ingestion & Processing A AWS Lambda function runs once per day to fetch the new feedback entries. 
 We use Amazon Bedrock to c lassify sentiment (positive, negative, mixed, or neutral) for each open comment, streamlining downstream analysis. 
 Processed records are indexed in Amazon OpenSearch Service, serving both as our full-text search engine and vector database. 
 Interactive feedback exploration via OpenSearch Service Stakeholders can access real-time feedback insights through OpenSearch Dashboards, giving them a bird’s-eye view of user sentiment, ratings, and trends over time. 
 Starting with high-level visualizations, such as sentiment distribution, rating scores, and feedback volume, users can drill down into specific applications, features, or even individual comments. 
 Dashboards support filtering by time period, comment sentiment, product version, and more, enabling targeted root cause analysis. 
 For example, a Product Manager can visualize how sentiment around a recent app update changed week over week, or zoom into negative comments mentioning a specific feature. 
 AI-Powered Internal Chatbot Our stakeholder-facing chatbot queries the OpenSearch index as its knowledge base. 
 We use Bedrock Guardrails , to enforce safety and reliability and make sure responses align with our brand and compliance standards. 
 Product managers and support teams can ask natural-language questions, for example, “What pain points do customers mention most often?” and receive instant, context-rich answers. 
 Biweekly Insights Report Every two weeks, a second Lambda function aggregates and analyzes the latest feedback trends. 
 It generates a concise report with key metrics, highlights, and sentiment breakdowns. 
 The report is automatically delivered to our Product Managers and Product Owners, feeding directly into sprint planning and roadmap discussions. 
 Generative AI Orchestration 
 Orchestration is a core foundation of our solution, because generative AI workflows typically involve multiple steps that need to be coordinated. In our pipeline, data ingestion and processing steps, such as sentiment analysis, embedding generation, and indexing, are orchestrated using LangChain, which provides modular, reusable components for calling models, transforming data, and integrating with external systems like Amazon OpenSearch Service. For our internal chatbot, we rely on LangGraph to implement a multi-agent architecture. Each assistant is defined declaratively in LangGraph, encapsulating its own logic and tools. This design makes assistants flexible and composable: instead of rigid step-by-step flows, we use an agent-based approach where an LLM selects the right tools and actions dynamically to answer user queries. This gives product managers and support teams a natural, interactive way to explore feedback and related operational insights. 
 Integration with Amazon Bedrock models is straightforward using LangChain’s native support. For example, our AI-powered internal chatbot uses the Claude Sonnet 4.6 model via Amazon Bedrock. We chose Claude Sonnet 4.6 because it offers frontier performance across coding and agentic workflows. The model excels in multi-turn conversational exchanges and agentic workflows, making it ideal for our internal chatbot that requires reliable performance across single and multi-turn interactions with stakeholders. With its precise workflow management capabilities and ability to serve in both lead agent and subagent roles, Claude Sonnet 4.6 delivers the consistent conversational quality our product managers and support teams need when exploring feedback insights at scale. Additionally, we leverage geographic Cross-Region Inference Service (CRIS) endpoint to seamlessly manage unplanned traffic bursts by distributing compute across multiple EU AWS Regions. This cross-region capability ensures our feedback processing pipeline remains resilient during peak usage periods while maintaining consistent performance for our global stakeholder base. The model is configured with guardrails applied directly through LangChain configuration: 
 from langchain_aws import ChatBedrockConverse

def get_chatbot_model():
 return ChatBedrockConverse(
 client=session.client("bedrock-runtime", region_name="eu-central-1", config=config),
 model="eu.anthropic.claude-sonnet-4-6", guardrail_config={
 "guardrailIdentifier": settings.GUARDRAIL_ID,
 "guardrailVersion": "DRAFT",
 "trace": "enabled"
 }
 ) 
 Data Management 
 An AWS Lambda function runs once per day to fetch the new feedback entries from the feedback repository into Amazon S3 , after which the data is categorized with semantic detection through Amazon Bedrock. The data is then indexed in Amazon OpenSearch Service, serving both as our full-text search engine and vector database. 
 Responsible AI 
 To responsibly use the solution, we implement safeguards using Amazon Bedrock Guardrails. This allows us to attach Amazon Bedrock Guardrails to an AI interaction and enforce content moderation policies and make sure responses align with our brand and compliance standards. 
 Using AWS CloudFormation, we define guardrail policies as infrastructure-as-code, providing examples of configurations to help block harmful content. 
 Guardrails as Code: CloudFormation 
 ChatbotGuardrail:
 Type: AWS::Bedrock::Guardrail
 Properties:
 Name: guardrail
 Description: Basic guardrail to block violence and harmful content.
 BlockedInputMessaging: "Input blocked by safety policy."
 BlockedOutputsMessaging: "Response blocked by safety policy."
 WordPolicyConfig:
 ManagedWordListsConfig:
 - Type: PROFANITY
 ContentPolicyConfig:
 FiltersConfig:
 - Type: HATE
 InputStrength: HIGH
 OutputStrength: HIGH
 OutputAction: BLOCK
 - Type: INSULTS
 InputStrength: HIGH
 OutputStrength: HIGH
 OutputAction: BLOCK
 - Type: SEXUAL
 InputStrength: HIGH
 OutputStrength: HIGH
 OutputAction: BLOCK
 - Type: VIOLENCE
 InputStrength: HIGH
 OutputStrength: HIGH
 OutputAction: BLOCK
 - Type: MISCONDUCT
 InputStrength: HIGH
 OutputStrength: HIGH
 OutputAction: BLOCK
 - Type: PROMPT_ATTACK
 InputStrength: NONE
 OutputStrength: NONE
 OutputAction: BLOCK 
 Programmatic Input Validation 
 We also use Amazon Bedrock Guardrails independently to validate raw user input before passing it to the LLM, helping prevent prompt injection and other misuse: 
 def validate_question_with_guardrail(question: str, user_data: UserData) -> bool:
 client = boto3.client('bedrock-runtime')
 response = client.apply_guardrail(
 guardrailIdentifier=settings.GUARDRAIL_ID,
 guardrailVersion='DRAFT',
 source='INPUT',
 content=[{'text': {'text': question}}]
 )

 if response.get("action") == "GUARDRAIL_INTERVENED":
 print(json.dumps(response, indent=4))
 print(
 f"Prompt was blocked. user_id=[{user_data.user_id}] question=[{question}]"
 )
 return False
 return True 
 With this setup, we have created a more secure, scalable, and explainable pipeline that puts Generative AI to work, responsibly and effectively, across our product feedback lifecycle. 
 Monitoring 
 We monitor the parts of the application using Amazon CloudWatch, which collects raw data and processes it into readable, near real-time metrics. We enabled model invocation logging to collect invocation logs, model input data, and model output data for the invocations, enabling collection of full request data, response data, and metadata associated with the calls. Amazon Bedrock also integrates with AWS CloudTrail, which captures API calls for Amazon Bedrock as events. This generates insights that you can use to optimize the applications further like improving response latency or reducing costs. 
 Next Steps 
 The solution processes over 15,000 feedback items per month with an accuracy of 95% for sentiment classification on a labeled test dataset. Instead of spending hours reviewing raw feedback, teams can now receive clear, structured summaries in seconds that highlight the most important topics and recurring signals. This helps them move from information to action much faster, making decisions within days rather than weeks. Over time, the reports helped us understand not only when sentiment improved, but also why it didn’t. By continuously monitoring customer feedback, we can react quickly to early signals, adjust decisions, and correct course when needed. In several areas, actions taken based on these insights have already resulted in more positive comments and a noticeable reduction in negative feedback. A strong example is the “Preview” functionality in Shipping Instructions. This feature was prioritized directly in response to a high volume of negative user feedback highlighting the lack of a preview capability. After its release, AI-driven reports allowed us to track user reactions in detail. Feedback related specifically to this feature showed that the previously frequent requests for preview capability were effectively resolved, demonstrating that the core user need had been successfully addressed. At the same time, broader feedback continued to surface other areas for improvement across the application. AI insights also guided future feature planning and prioritization. Based on user comments, we created new OpenSearch Service-based dashboards that help teams quickly verify and analyze issues reported by users. Another example is the ability to upload cargo data via Excel files, a repeatedly requested feature highlighted by AI recommendations. This functionality is now fully available and is expected to significantly reduce manual effort, particularly for large shipments. During review sessions, the stakeholders can now see top positive and negative comments in real time, alongside AI-generated recommendations, creating a far more informed and productive discussion. 
 This feedback analysis solution is one example of how we are applying generative AI across our processes, and it marks the beginning, not the end, of our AI-native journey. Under our AI-Native Umbrella Program , which serves as a single source of truth for AI adoption, our next focus is to establish a shared, robust AI foundation with Amazon Bedrock. By providing standardized infrastructure, security, and guardrails, we aim to enable every role in the department, engineering, product and delivery (PM, PO, SM), UX/design, and operations/support, to create their own AI “spaces” safely and independently while having access to the best in-class foundation models. This setup is designed to lower the barrier to experimentation, streamline discovery, and encourage hands-on exploration of generative AI use cases in day-to-day work. In doing so, we help teams move faster from ideas to impact, while maintaining consistency, responsibility, and scalability across the AI initiatives. 
 If you want to scale your generative AI applications, you can get started by reading this Architect a mature generative AI foundation on AWS that dives deeper on the various foundational components that help accelerate the end-to-end generative AI application lifecycle. 
 About the authors 
 Aamna Najmi 
 Aamna is a Senior Specialist Solutions Architect for Generative AI focusing on Anthropic models and operationalizing and governing generative AI systems at scale on Amazon Bedrock. She helps ISVs solve their challenges, embrace innovation, and create new business opportunities with Amazon Bedrock. In her spare time, she pursues her passion of experimenting with food and discovering new places. 
 Anna Rysicka 
 Anna is a Software Engineer Team Leader at Hapag-Lloyd with over 10 years of experience in the technology industry. She works with the Documentation & Customs Team, focusing on shipment documentation systems including Shipping Instructions and Bill of Lading solutions. She specializes in modern frontend architectures, TypeScript/Vue.js, and user experience design, with a passion for problem-solving and leveraging AI as a collaborative tool for task management and productivity. As part of the DXE AI Native initiative, Anna guides teams into the AI era with tools and motivation to enhance productivity. In her spare time, she experiments with AI projects, enjoys painting, and loves traveling. 
 Grzegorz Kaczor 
 Grzegorz is a Cloud Architect at Hapag-Lloyd and a technology enthusiast with over 18 years of experience in the tech industry. He specializes in leveraging advanced technologies to deliver innovative solutions for organizations. His background spans serverless architectures, security, observability, and compliance posture management. He is currently exploring generative AI and its practical applications in enterprise environments. In his spare time, he enjoys learning, staying active, and spending time with his daughters.
```

---

## 7. Streamlining generative AI development with MLflow v3.10 on Amazon SageMaker AI

- 日期: 2026-05-05 16:55
- 链接: https://aws.amazon.com/blogs/machine-learning/streamlining-generative-ai-development-with-mlflow-v3-10-on-amazon-sagemaker-ai/

```
Today, we’re excited to announce that Amazon SageMaker AI MLflow Apps now support MLflow version 3.10, bringing enhanced capabilities for generative AI development and streamlined experiment tracking to your generative AI workflows. Building on the foundations established with Amazon SageMaker AI MLflow Apps , this latest version introduces powerful new features for observability, evaluation, and generative AI development that help data scientists and ML engineers accelerate their AI initiatives from experimentation to production. 
 In this post, we’ll explore what’s new in MLflow v3.10, walk you through getting started with SageMaker AI MLflow Apps, and how to leverage these enhancements to build generative AI applications. 
 What’s new in MLflow v3.10 
 MLflow 3.10 introduces a set of targeted improvements to the MLflow ecosystem that extend the tracing and observability capabilities established in MLflow 3.0, with a particular focus on generative AI application development and agentic workflows. On the generative AI front, this release delivers improved tracing for complex multi-turn workflows, tighter integration with popular LLM frameworks and libraries, and streamlined logging for generative AI interactions and invocations. Evaluation receives a substantial upgrade through the mlflow.genai.evaluation() API, which provides a programmatic interface for systematically measuring and maintaining generative AI quality across the development-to-production lifecycle with built-in metrics covering relevance, faithfulness, correctness, and safety—all of which integrate seamlessly with SageMaker AI workflows. 
 Observability improvements include more granular trace filtering and search, richer metadata capture for debugging and root-cause analysis, and pre-built performance dashboards that surface workload level metrics—latency distributions, request counts, quality scores, and token usage —at a glance without manual chart configuration, giving teams running production workloads clear visibility into operational costs while MLflow workspaces provide a structured way to organize MLflow artifacts across teams and projects, as shown below. 
 These improvements coupled with SageMaker AI provide an enterprise-grade generative AI infrastructure, making it straightforward to track experiments, monitor generative AI performance, and maintain governance across AI applications at scale. 
 Getting started with SageMaker AI MLflow App v3.10 
 For new users, creating a SageMaker AI MLflow App is straightforward through the SageMaker Studio console , AWS CLI, or API. The default configuration automatically provisions MLflow 3.10, giving you immediate access to all the latest capabilities. 
 You can get started with fully managed MLflow 3.10 on Amazon SageMaker AI MLflow Apps through the AWS Management Console , AWS Command Line Interface (AWS CLI), or API . 
 Prerequisites 
 To get started, you need: 
 An AWS account with billing enabled 
 An Amazon SageMaker Studio AI domain. To create a domain, refer to Guide to getting set up with Amazon SageMaker AI . 
 Next, navigate to Amazon SageMaker AI Studio console and select the MLflow application. 
 Choose Create MLflow App and enter a name. Here, we have both an AWS Identity and Access Management (IAM) role and Amazon Simple Service (Amazon S3) bucket already configured for you using the SageMaker AI Studio domain’s defaults. And you only need to modify them in the Advanced settings if needed, as shown below. 
 Once created, you receive an MLflow Amazon Resource Name (ARN) for connecting and you can immediately start using the newly created SageMaker AI MLflow App with MLflow v3.10 along with your existing code or you can follow along below to connect your code with SageMaker AI MLflow Apps. 
 To begin tracking your experiments with your newly created SageMaker AI MLflow App, you need to install both MLflow and the AWS SageMaker MLflow plugin in your environment. You can use SageMaker Studio managed Jupyter Lab , SageMaker Studio Code Editor , a local integrated development environment (IDE), or other supported environment where your AI workloads operate with SageMaker AI MLFlow Apps. 
 To install both the Python packages using pip: 
 pip install mlflow==3.10.1 sagemaker-mlflow==0.3.0 
 To connect and start logging your AI experiments, parameters, and models directly to SageMaker AI MLflow Apps, see the code snippet below to get started with your workload. Note, replace the Amazon Resource Name (ARN) with your SageMaker AI MLflow App ARN below. 
 import mlflow
# Connect to your SageMaker MLflow App
mlflow_app_arn = "<your-mlflow-app-arn>"
mlflow.set_tracking_uri(mlflow_app_arn)
# Set your experiment
mlflow.set_experiment("your_genai_experiment")
# Your existing code continues to work with enhanced capabilities
# New features are automatically available 
 Migration 
 If you have an existing MLflow Tracking Server or App hosted on SageMaker or elsewhere you can migrate to a new 3.10 app by following the instructions in the blog post Migrate MLflow tracking servers to Amazon SageMaker AI with serverless MLflow . 
 Conclusion 
 The introduction of MLflow v3.10 in Amazon SageMaker AI MLflow Apps represents a significant step forward in making enterprise AI development more efficient, observable, and manageable. Get started with by Amazon SageMaker AI MLflow Apps by visiting Amazon SageMaker AI Studio and creating your first MLflow App. 
 The new MLflow v3.10 is also supported in Amazon SageMaker AI serverless model customization and SageMaker Unified Studio , and for additional workflow flexibility. 
 Share your feedback with us through AWS re:Post for SageMaker or your usual AWS Support contacts. 
 About the authors 
 Sandeep Raveesh 
 Sandeep Raveesh is a GenAI GTM Specialist Solutions Architect at AWS. He works with customers through their LLM training, inference, and observability. He focuses on product development helping AWS build and solve industry challenges in the generative AI space. You can connect with Sandeep on LinkedIn to learn about generative AI solutions. 
 Dana Benson 
 Dana Benson is a Software Development Manager working in SageMaker AI ML and LLM observability. Prior to joining AWS, Dana developed Smart Home behaviors for Alexa. 
 Ruidi Peng 
 Ruidi Peng is a Software Development Engineer at AWS. He works on the Amazon SageMaker MLflow team, focusing on AI/ML and LLM observability. Ruidi is passionate about building scalable infrastructure that helps customers monitor and gain insights into their machine learning workloads. In his free time, he enjoys going for hikes and exploring the outdoors.
```

---

## 8. Introducing OS Level Actions in Amazon Bedrock AgentCore Browser

- 日期: 2026-05-05 16:54
- 链接: https://aws.amazon.com/blogs/machine-learning/introducing-os-level-actions-in-amazon-bedrock-agentcore-browser/

```
AI agents that automate web workflows operate within the browser’s web layer, the DOM that Playwright and the Chrome DevTools Protocol (CDP) expose. AgentCore Browser provides a secure, isolated browser environment for this, and it works well for the vast majority of automation: navigating pages, filling forms, clicking elements, extracting content. But the web layer has a hard boundary. Anything that the operating system renders (native dialogs, security prompts, certificate choosers, context menus, even Chrome settings) sits outside the DOM entirely. CDP can’t see it, and Playwright can’t interact with it. 
 When a web application calls window.print() and a system print dialog appears, Playwright has no DOM to interact with. When a workflow requires a keyboard shortcut or a right-click context menu, CDP has no mechanism to issue those commands at the OS level. When a browser session encounters a macOS privacy dialog, a Windows Security prompt, or a certificate chooser, they’re invisible to the web automation layer. These scenarios tend to surface in production. They’re triggered by specific application states, OS configurations, or user permissions, not in testing, where web content is predictable enough to validate against. 
 The challenge compounds for vision-enabled agents. A common architecture is to capture a screenshot, send it to a model, receive back coordinates or instructions, and execute. This loop works well for web content, but breaks the moment that native UI appears. The screenshot captures it, the model reasons about it, and then there’s nothing to act with. CDP can’t reach what the OS rendered. The agent sees exactly what to do and has no way to do it. 
 We’re announcing OS Level Actions for AgentCore Browser. This new capability unblocks these scenarios by exposing direct OS control through the InvokeBrowser API, so agents can interact with content visible on the screen, not only what’s accessible through the browser’s web layer. By combining full-desktop screenshots with mouse and keyboard control at the OS level, agents can observe native UI, reason about it, and act on it within the same session. This post walks through how OS Level Actions work, what actions are supported, and how to get started. 
 How OS Level Actions work 
 OS Level Actions are available for new and existing browser configurations without further setup. After a session is active, you dispatch actions through the InvokeBrowser API. Each call carries exactly one action, identified by its type and arguments, and returns a SUCCESS or FAILED status. The active session is identified using the x-amzn-browser-session-id header, which ties each OS-level action to the correct browser session. 
 The expected interaction pattern is an action-screenshot-reaction loop. The agent takes an action (click, type, shortcut), captures a screenshot to observe the current state of the screen, and then decides the next action based on what it sees. This loop allows the agent to react to dynamic UI. This includes native dialogs and OS prompts that might appear mid-workflow. 
 Agent sends an action . This can be a mouse click, key press, or shortcut using InvokeBrowser . 
 AgentCore executes the action on the full OS desktop and returns SUCCESS or FAILED . 
 Agent requests a screenshot to observe the current screen state. 
 AgentCore captures the full desktop , including native dialogs, OS modals, and UI outside the browser window, and returns a base64-encoded PNG. 
 Agent reasons about the screenshot sending it to a vision model to determine what happened and what to do next. 
 Agent sends the next action based on what it observed, continuing the loop. 
 Supported actions 
 OS Level Actions are organized into three categories: mouse control, keyboard input, and visual capture. The following table summarizes eight actions with their fields and constraints. 
 Action Required fields Optional fields Notes 
 mouseClick — x, y, button, clickCount Defaults to current position, LEFT, single click. clickCount: 1–10. 
 mouseMove x, y — Moves cursor to coordinates. 
 mouseDrag endX, endY startX, startY, button Drags from start to end. button defaults to LEFT. 
 mouseScroll — x, y, deltaX, deltaY deltaY negative = scroll down. Range: -1000 to 1000. 
 keyType text — Types a string. Max 10,000 characters. 
 keyPress key presses Presses a key N times. presses: 1–100, defaults to 1. 
 keyShortcut keys — Key combination array. Up to five keys, for example, [“ctrl”, “a”]. 
 screenshot — format Captures full OS desktop. Returns base64-encoded PNG. 
 Mouse actions 
 Mouse actions cover the full range of pointer interactions: clicking, moving, dragging, and scrolling. Coordinate fields are optional for mouseClick . If omitted, the click lands at the current cursor position with a left button single click. This is useful when a prior mouseMove has already positioned the cursor. mouseDrag requires the four coordinates, start and end positions. mouseScroll accepts a position and delta values for both axes—negative deltaY scrolls down, positive scrolls up. A right-click context menu, for example, is a single mouseClick with button set to RIGHT at the target coordinates. Note that some context menu items might not function as expected because of the virtualized environment in which the browser session runs. 
 Keyboard actions 
 The three keyboard actions cover different levels of input. keyType is for typing text. It sends characters directly and handles strings up to 10,000 characters. keyPress is for individual keys that must be pressed repeatedly, such as tab to advance through form fields or escape to dismiss a modal. keyShortcut is for combinations—pass an array of key names and AgentCore presses them simultaneously. 
 Key names for keyPress and keyShortcut must be lowercase. Supported keys include single characters (a–z, 0–9) and named keys such as enter, tab, space, backspace, delete, escape, ctrl, alt, and shift. 
 To select the entire text, for example, you would use keyShortcut with ["ctrl", "a"] . 
 {
 "action": {
 "keyShortcut": {
 "keys": ["ctrl", "a"]
 }
 }
} Screenshot 
 The screenshot action captures the full OS desktop and returns a base64-encoded PNG in the response. It’s the only action that returns data. The other actions return only a status (SUCCESS or FAILED) and an error field on failure. 
 {
 "action":{
 "screenshot":{
 "format":"PNG"
 }
 }
} Getting started 
 The following examples walk through the action-screenshot-reaction loop, matching the companion notebook . For the full working notebook with eight actions demonstrated end to end, start there. 
 Set up clients and create a browser 
 You need two clients: a control plane client ( bedrock-agentcore-control ) for managing browser resources, and a data plane client ( bedrock-agentcore ) for dispatching actions during a session. 
 import boto3
import time

browser_boto3 = boto3.client('bedrock-agentcore-control', region_name='us-west-2')

BROWSER_NAME = "browser_with_os_actions" Before starting a session, you need an AWS Identity and Access Management (IAM) execution role and a browser resource. The execution role requires bedrock-agentcore:InvokeBrowser , bedrock-agentcore:StartBrowserSession , and bedrock-agentcore:StopBrowserSession permissions. The companion notebook includes a helper that creates this role for you: 
 from helpers.utils import create_agentcore_execution_role, SAMPLE_ROLE_NAME

execution_role_arn = create_agentcore_execution_role(SAMPLE_ROLE_NAME) With the role created, create a custom browser: 
 created_browser = browser_boto3.create_browser(
 name=BROWSER_NAME,
 executionRoleArn=execution_role_arn,
 networkConfiguration={
 'networkMode': 'PUBLIC'
 }
)

browser_id = created_browser['browserId']
print(f"Browser ID: {browser_id}") Start a browser session 
 With the browser resource created, start a session. The viewPort sets the screen resolution. This determines the coordinate space for mouse actions and the dimensions of captured screenshots. The sessionTimeoutSeconds controls how long the session stays alive before it’s automatically terminated. 
 # These helpers are included in the companion notebook repository
from helpers.browser import get_credentials, invoke, start_session, stop_session

creds, default_region = get_credentials()
BEDROCK_AGENTCORE_DP_ENDPOINT = f"https://bedrock-agentcore.{default_region}.amazonaws.com/"

sid = start_session(BEDROCK_AGENTCORE_DP_ENDPOINT, browser_id, region=default_region, credentials=creds)

# Wait for session to initialize — adjust if needed for your environment
time.sleep(3) The start_session helper sends a SigV4-signed PUT request to create the session and returns the sessionId. The invoke helper handles signing and dispatching individual actions. 
 Invoke an OS-level action 
 With the session running, you can dispatch OS-level actions through the invoke helper. Each call takes a single action — in this case, a left click at coordinates (600, 370) on the screen: 
 r = invoke(
 BEDROCK_AGENTCORE_DP_ENDPOINT, sid,
 {"mouseClick": {"x": 600, "y": 370, "button": "LEFT"}},
 region=default_region, credentials=creds, browser_id=browser_id
)

print(f"Mouse click status: {r.status_code}, action: {r.json()['result']}") The response tells you whether the action succeeded or failed. Coordinates map to screen pixels, if the session viewport is 1920×1080, valid x values range from 0 to 1919 and y from 0 to 1079. Coordinates outside the screen dimensions return a ValidationException . 
 Capture a screenshot 
 After each action, the agent must observe what happened. The screenshot action captures the full desktop and returns the image as a base64-encoded PNG: 
 import base64
from IPython.display import Image, display

r = invoke(
 BEDROCK_AGENTCORE_DP_ENDPOINT, sid,
 {"screenshot": {"format": "PNG"}},
 region=default_region, credentials=creds, browser_id=browser_id
)

img_bytes = base64.b64decode(r.json()['result']['screenshot']['data'])
display(Image(img_bytes)) This is the observation step in the loop. The agent sends the screenshot to a vision model, which reasons about what’s on screen and returns the next action to take. The cycle repeats until the workflow is complete. 
 Putting it together: dismissing a print dialog 
 Here is the action-screenshot-reaction loop in practice. Suppose the agent navigates to a page that triggers window.print() , and a native print dialog appears. The agent can’t interact with it through CDP, but it can with OS Level Actions.First, the agent captures a screenshot to see the current state of the screen: 
 r = invoke(
 BEDROCK_AGENTCORE_DP_ENDPOINT, sid,
 {"screenshot": {"format": "PNG"}},
 region=default_region, credentials=creds, browser_id=browser_id
)

# Send the screenshot to a vision model to identify the dialog and locate the Cancel button.
# The vision model integration depends on your agent architecture — see the Bedrock
# InvokeModel API for how to send images to Claude or other models.
# The model returns coordinates, e.g.: {"x": 410, "y": 535} The vision model identifies the print dialog and returns the coordinates of the Cancel button. The agent selects it: 
 r = invoke(
 BEDROCK_AGENTCORE_DP_ENDPOINT, sid,
 {"mouseClick": {"x": 410, "y": 535, "button": "LEFT"}},
 region=default_region, credentials=creds, browser_id=browser_id
)

print(f"Click status: {r.status_code}, action: {r.json()['result']}") The agent takes another screenshot to confirm that the dialog was dismissed, and the workflow continues. 
 Stop the session and clean up 
 When the workflow is done, stop the session and clean up resources: 
 stop_session(BEDROCK_AGENTCORE_DP_ENDPOINT, sid, browser_id, region=default_region, credentials=creds) To delete the browser resource and IAM role: 
 browser_boto3.delete_browser(browserId=browser_id)
print(f"Browser {browser_id} deleted")

from helpers.utils import delete_agentcore_execution_role, SAMPLE_ROLE_NAME
delete_agentcore_execution_role(SAMPLE_ROLE_NAME) These steps, act, observe, decide, form the core of the action-screenshot-reaction pattern. The companion notebook walks through eight supported actions with a live browser session, including mouse drag, scroll, keyboard input, and shortcut combinations. 
 Conclusion 
 When we launched Amazon Bedrock AgentCore Browser , it gave AI agents a fully managed, cloud-based browser environment to interact with websites. It navigated pages, extracted content, and automated workflows at scale through Playwright and CDP. OS Level Actions extend that capability beyond the web layer to UI elements visible on the screen. Native dialogs, security prompts, keyboard shortcuts, and browser chrome are no longer blockers. Agents can now observe, reason about, and act on the full OS desktop within the same session. 
 Combined with AgentCore Browser’s existing capabilities like visual understanding and framework integration with Playwright and Amazon Nova Act, OS Level Actions close the last gap in browser automation coverage. 
 To start building: 
 Follow the Amazon Bedrock AgentCore Developer Guide 
 Try the companion notebook for a hands-on walkthrough 
 For broader context on browser automation, see the Amazon Bedrock AgentCore Browser documentation 
 About the authors 
 Evandro Franco 
 Evandro Franco is a Sr. Data Scientist working on Amazon Web Services. He is part of the Global GTM team that helps AWS customers overcome business challenges related to AI/ML on top of AWS, mainly on Amazon Bedrock AgentCore and Strands Agents. He has more than 18 years of experience working with technology, from software development, infrastructure, serverless, to machine learning. In his free time, Evandro enjoys playing with his son, mainly building some funny Lego bricks. 
 Phelipe Fabres 
 Phelipe Fabres is a Sr. Solutions Architect for Generative AI at AWS for Startups. He is part of a global Frontier AI team with a focus on costumers that are building Foundation Models/LLMs/SLMs. Has extended work on Agentic systems and Software driven AI systems. He has more than 10 years of working with software development, from monolith to event-driven architectures with a Ph.D. in Graph Theory. In his free time, Phelipe enjoys playing with his daughter, mainly board games and drawing princess. 
 Saurav Das 
 Saurav Das is part of the Amazon Bedrock AgentCore Product Management team. He has more than 15 years of experience in working with cloud, data and infrastructure technologies. He has a deep interest in solving customer challenges centered around data and AI infrastructure. 
 Yanda Hu 
 Yanda Hu is a software engineer on the Amazon Bedrock AgentCore Engineering team with 5+ years of experience building machine learning and AI solutions at scale. He specializes in designing and delivering scalable agentic systems. He is passionate about the emerging agentic AI landscape, focusing on helping customers overcome real-world challenges in agentic workflows. 
 Cristiano Scandura 
 Cristiano has been in the IT industry since 1998. He joined Amazon Web Services (AWS) in 2018, where he worked on projects for enterprise clients. Currently, he specializes in GenAI and machine learning (ML) projects for all industries in AWS Worldwide Public Sector. 
 Joshua Samuel 
 Joshua Samuel is a Senior AI/ML Specialist Solutions Architect at AWS who accelerates enterprise transformation through AI/ML, and generative AI solutions, based in Melbourne, Australia. A passionate disrupter, he specializes in agentic AI and coding techniques – Anything that makes builders faster and happier. Outside work, he tinkers with home automation and AI coding projects, and enjoys life with his wife, kids and dog.
```

---

## 9. Secure AI agents with Amazon Bedrock AgentCore Identity on Amazon ECS

- 日期: 2026-05-05 15:27
- 链接: https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-amazon-bedrock-agentcore-identity-on-amazon-ecs/

```
AI agents in production require secure access to external services. Amazon Bedrock AgentCore Identity, available as a standalone service, secures how your AI agents access external services whether they run on compute platforms like Amazon ECS, Amazon EKS , AWS Lambda , or on-premises. 
 An earlier post covered AgentCore Identity credential management for AI agents. Running agents on compute environments like ECS raises two questions: How to build an application-owned Session Binding endpoint, and how to manage workload access token lifecycle? 
 This post implements Authorization Code Grant (3-legged OAuth) on Amazon ECS with secure session binding and scoped tokens. This post provides a working implementation with: 
 Secure session binding that prevents CSRF and browser-swapping attacks 
 Auth tokens scoped to each user session, following least-privilege principles 
 Separation of concerns between the agent workload and session binding service 
 Authentication and authorization with OAuth 2.0 and OIDC 
 This solution uses OAuth 2.0 ( RFC 6749) and OpenID Connect (OIDC). OIDC authenticates users (who they are), and OAuth 2.0 authorizes their actions (what they can do). 
 We focus on the Authorization Code Grant for user-delegated access. The user authenticates with an identity provider and grants consent. The application then exchanges an authorization code for an access token, which creates an audit trail.In this flow, the user authenticates with an identity provider and grants consent for the agent to access specific resources on their behalf. The application exchanges the resulting authorization code for a scoped access token which Amazon Bedrock AgentCore Identity secures in its token vault. Because each token is bound to a specific user identity with explicit consent, the solution maintains an auditable chain from user authentication through to agent action. 
 The Authorization Code Grant is suited for agentic workloads that act on behalf of users because it provides user consent before the agent can act, session binding that verifies the user who initiated the authorization request is the same user who granted consent, and scoped delegation that limits the agent to only the permissions the user approved. 
 Callback URL vs. session binding URL 
 In this context, the Authorization Code Grant flow uses two URLs that are often confused: 
 Callback URL: Automatically generated when creating an OAuth client in AgentCore Identity. It points to AgentCore Identity and must be registered with the Authorization Server as the redirect target where the authorization code is sent after user authentication. 
 Session Binding URL: The URL pointing back to a customer-managed service that completes the session binding between the authenticated user and the OAuth flow. This endpoint is implemented and hosted by the customer. 
 Solution overview 
 This architecture diagram shows how AgentCore Identity secures a self-hosted AI agent on Amazon ECS. This walkthrough uses Microsoft Entra ID as the identity provider, but other OIDC-compliant providers are supported. The complete source code and prerequisites for this walkthrough are available in the accompanying GitHub repository. 
 The solution deploys two services on Amazon ECS behind an Application Load Balancer. The Agentic Workload runs the AI agent and handles user requests. The Session Binding Service processes OAuth callbacks to link user sessions with third-party access tokens. Both services use Amazon Bedrock AgentCore Identity to authenticate users inbound via OIDC and authorize outbound actions on their behalf. The numbered annotations in the diagram correspond to the following descriptions. 
 Inbound authentication and traffic routing: Requests arrive at an Amazon Application Load Balancer (ALB), which authenticates the user through the ALB’s built-in OIDC authentication flow. Traffic is encrypted with HTTPS using a certificate from AWS Certificate Manager, and an alias A record in an Amazon Route 53 public hosted zone routes traffic to the load balancer. After authenticating the user through OIDC, the ALB forwards the request to the Amazon ECS cluster. The ALB injects an x-amzn-oidc-data header containing the user’s claims in JWT format, with the sub field uniquely identifying the user. 
 Agentic workload: The Agentic Workload exposes a FastAPI server with an /invocations endpoint that accepts a sessionId and message. The FastAPI server passes these to an agent built with Strands Agents . You can also use LangChain or other agent SDKs since the server handles requests independently of the agent framework. The agent calls a large language model (LLM) on Amazon Bedrock, but other model providers work, too. The agent stores session state in an Amazon S3 bucket and it uses the user’s sub claim as a key prefix to isolate sessions between users. The agent also has tools to perform actions on the user’s behalf in GitHub, which requires the user’s OAuth access token. 
 Outbound authentication with AgentCore Identity: When the agent needs to act on the user’s behalf in a third-party service like GitHub, it requests an OAuth access token through AgentCore Identity. If no valid token exists, AgentCore Identity initiates an Authorization Code Grant flow, prompting the user to authorize access. 
 OAuth callback processing: After the user authorizes access, the Session Binding Service completes the OAuth flow by binding the authorization to the correct user session via AgentCore Identity. 
 User interface: The FastAPI server that hosts the agentic workload exposes a /docs endpoint, which renders the OpenAPI specification as an interactive HTML page. The end user interacts with the agent through this page, which provides a minimal UI for demonstration 
 Amazon CloudWatch captures logs, and a dedicated S3 bucket stores access logs for both the load balancer and the data bucket. ECS pulls container images from Amazon ECR. A set of basic AWS WAF rules is attached to the load balancer to provide baseline protection against common web exploits. An Amazon KMS customer managed key (CMK) encrypts data, except for the access logs bucket, which requires Amazon S3 managed encryption (SSE-S3). 
 Amazon Bedrock AgentCore Identity: Authorization Code Grant 
 This walkthrough adapts the general AgentCore Identity session binding flow for a self-hosted architecture using ALB for authentication, a dedicated Session Binding Service, and direct API calls instead of the AgentCore SDK and Runtime. 
 The sequence diagram shows how AgentCore Identity’s workload identity , workload access tokens , and OAuth 2.0 credential provider work together to securely provide OAuth tokens to the agent on behalf of a user. This flow assumes the authenticated user has not yet authorized the agent to access their resources, meaning no valid token exists in the AgentCore Identity Token Vault . 
 An authenticated user sends a request to the agentic workload. The agentic workload extracts the user ID from the sub claim in the ALB-signed JWT ( x-amzn-oidc-data header) to identify the user. 
 The agentic workload calls the GetWorkloadAccessTokenForUserId API, passing the userId and workloadName , to obtain a workload access token that represents the agent’s identity scoped to this user. 
 AgentCore Identity returns the workload access token to the agentic workload. 
 The agentic workload calls the GetResourceOauth2Token API, passing the workload access token, the provider name of the configured OAuth 2.0 credential provider, a session binding URL (see callbackUrl parameter ), and the required scopes, for instance the read:user scope of GitHub. This requests an OAuth token for the third-party service (in this case, GitHub). 
 Because no valid token exists for this user, AgentCore Identity creates a sessionURI that tracks the authorization flow state across the subsequent requests and responses during the OAuth 2.0 authentication process. 
 AgentCore Identity returns an authorization URL and session URI to the workload 
 The agentic workload returns the authorization URL to the user, prompting them to authorize access. 
 The user clicks the authorization URL and grants the agent permission in the third-party provider’s consent screen. 
 The Authorization Server sends the authorization code to AgentCore Identity. 
 AgentCore Identity redirects the user to the Session Binding URL with the session URI appended, routing them to the Session Binding Service. 
 The user’s browser follows the redirect to the Session Binding Service via the Session Binding URL. The ALB injects the JWT in the x-amzn-oidc-data header. 
 The Session Binding Service calls the CompleteResourceTokenAuth API with the session URI and user ID (extracted from the JWT), binding the completed authorization to the correct user session. On success, it returns a static application owned HTML page confirming the authorization was successful. 
 AgentCore Identity exchanges the authorization code with the Authorization Server for an OAuth2 access token. 
 The Authorization Server returns the OAuth2 access token. 
 AgentCore Identity stores the token in the Token Vault. 
 AgentCore Identity returns success to the Session Binding Service. 
 The Session Binding Service displays “Authorization complete” to the user. 
 On subsequent requests, whether the user needs to re-authorize depends on the credentials the authorization server issued. AgentCore Identity stores both access tokens and refresh tokens (when available) in the Token Vault. When a refresh token is present — as with GitHub when User-to-server token expiration is enabled — AgentCore Identity automatically uses it to obtain a new access token once the original expires, without prompting the user again. If no refresh token was issued and the access token expires, the user will be prompted to re-authorize. Note that tokens can also be revoked on the provider side; in such cases, setting forceAuthentication: true forces a fresh authentication flow. 
 Session binding: 
 Session binding protects against two security threats: 
 Cross-Site Request Forgery (CSRF): An attacker attempts to bind their own OAuth token to the victim’s identity, causing the victim’s agent to unknowingly access the attacker’s resources, enabling data exfiltration and injection. 
 Browser Swapping Attack: An attacker tricks the victim into consenting on their behalf, binding the victim’s OAuth token to the attacker’s identity, granting the attacker direct access to the victim’s resources. 
 Session binding prevents both attacks by ensuring that the user ID at the agent workload matches the user ID at the Session Binding Service, with both identities cryptographically verified through the authentication chain. 
 AgentCore Identity also supports an optional customState parameter in the GetResourceOauth2Token API that can be used to pass a cryptographically random nonce to protect your callback endpoint against CSRF attacks, as recommended by the OAuth 2.0 specification. 
 Why we use GetWorkloadAccessTokenForUserId with AWS ALB and Microsoft Entra ID 
 The recommended API for obtaining a workload access token is GetWorkloadAccessTokenForJWT . This solution uses GetWorkloadAccessTokenForUserId instead. 
 GetWorkloadAccessTokenForJWT requires a dynamically validatable JWT whose signature can be verified at runtime against the issuer’s published signing keys, and whose aud claim matches your application. To obtain such a token from Microsoft Entra ID, you must include your Application ID in the scope of the OIDC authorization request, see the AgentCore Microsoft Inbound documentation for details. 
 However, this is incompatible with the AWS ALB OIDC flow. 
 As part of its OIDC handshake (see ALB OIDC documentation ), the ALB sends the access token to Entra’s UserInfo endpoint to retrieve the authenticated user’s claims which is a mandatory step in the ALB’s authentication flow. This UserInfo endpoint is hosted on Microsoft Graph ( https://graph.microsoft.com/oidc/userinfo ), and it only accepts tokens scoped to Microsoft Graph. When you include your Application ID in the scope, the resulting access token has your application as the audience, the UserInfo endpoint rejects it with a 401 and the ALB returns a 561. 
 If you remove your Application ID from the scope, Entra defaults the access token audience to Microsoft Graph ( 00000003-0000-0000-c000-000000000000 ). The ALB handshake succeeds but the resulting JWT cannot be dynamically validated by AgentCore. It is unusable with GetWorkloadAccessTokenForJWT . 
 This solution: The ALB completes its handshake using the Graph-scoped token. The ALB forwards an ALB-signed JWT in the x-amzn-oidc-data header containing the user’s claims from the UserInfo endpoint, including a sub claim that uniquely identifies the authenticated user. We validate this ALB-signed JWT using AWS’s published signing keys, extract the sub , and pass it to GetWorkloadAccessTokenForUserId . 
 Implementation 
 View the complete code GitHub repository . 
 Obtaining the Workload Access Token 
 The server extracts the user ID from the JWT’s sub claim and requests a workload access token from AgentCore Identity. The server then uses this token, the session ID, and the message to invoke the agent on behalf of the user. Note that session ID here refers to the agent’s conversation session, not the OAuth session URI from the authorization flow. 
 @router.post("/invocations")
async def invoke_agent(
 request: InvocationRequest,
 user_id: str = Depends(get_current_user),
 settings: Settings = Depends(get_settings),
 agent_service: AgentService = Depends(get_agent_service),
) -> StreamingResponse:
 """Invoke agent with streaming response."""
 try:
 agentcore = boto3.client("bedrock-agentcore", region_name=settings.identity_aws_region)
 response = agentcore.get_workload_access_token_for_user_id(
 workloadName=settings.workload_identity_name, userId=user_id
 )
 workload_access_token = response["workloadAccessToken"] 
return StreamingResponse(
 content=agent_service.stream_response(
 user_message=request.user_message,
 session_id=request.session_id,
 user_id=user_id,
 workload_access_token=workload_access_token,
 ),
 media_type="text/event-stream",
 ) 
 Requesting the access token 
 The server uses the require_access_token decorator from AgentCore SDK to retrieve OAuth 2.0 access token, see Obtain OAuth 2.0 access token . We modify the decorator to accept the workload access token as an explicit parameter rather than resolving it internally, giving direct control over token lifecycle management while preserving the SDK’s token retrieval and error-handling logic 
 def requires_access_token(
 *,
 provider_name: str,
 scopes: list[str],
 auth_flow: Literal["M2M", "USER_FEDERATION"],
 workload_access_token: str | None = None,
 session_binding_url: str | None = None,
 on_auth_url: Callable[[str], Any] | None = None,
 force_authentication: bool = False,
 token_poller: TokenPoller | None = None,
 custom_state: str | None = None,
 custom_parameters: dict[str, str] | None = None,
 into: str = "access_token",
 region: str | None = None,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
 """Fetch OAuth2 access token with explicit workload token.

 Args:
 provider_name: The credential provider name
 scopes: OAuth2 scopes to request
 auth_flow: Authentication flow type ("M2M" or "USER_FEDERATION")
 workload_access_token: The workload access token (explicit, not from context)
 session_binding_url: Session Binding URL pointing to the customer-managed service that completes the session binding
 on_auth_url: Handler invoked with the authorization URL when user authorization is required
 force_authentication: Force re-authentication
 token_poller: Custom token poller implementation
 custom_state: State for callback verification
 custom_parameters: Additional OAuth parameters
 into: Parameter name to inject the token into
 region: AWS region

 Returns:
 Decorator function

 """

def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
 client = IdentityClient(region)

 @wraps(func)
 async def wrapper(*args: Any, **kwargs: Any) -> Any:
 try:
 if not workload_access_token:
 raise ValueError("workload_access_token is required")
 token = await client.get_token(
 provider_name=provider_name,
 agent_identity_token=workload_access_token,
 scopes=scopes,
 auth_flow=auth_flow,
 callback_url=session_binding_url,
 on_auth_url=on_auth_url,
 force_authentication=force_authentication,
 token_poller=token_poller,
 custom_state=custom_state,
 custom_parameters=custom_parameters,
 )
 kwargs[into] = token
 return await func(*args, **kwargs)
 except Exception:
 logger.exception("Error in requires_access_token decorator")
 raise

 return wrapper

return decorator 
 Our tool class uses this decorator to supply the access token when calling the GitHub API. 
 class GitHubTools:
 """Tools for interacting with GitHub using OAuth authentication."""

def _on_auth_url(self, url: str) -> None:
 """Handle authorization URL by raising AuthorizationRequiredError.

 This URL must be presented to the user to grant access.
 """
 raise AuthorizationRequiredError(provider="GitHub", auth_url=url)

async def _call_github_api(
 self, endpoint: str, scopes: list[str], params: dict | None = None
) -> Any:
 """Make authenticated GitHub API call.

 Raises:
 ApiError: When API call fails

 """

 @requires_access_token(
 provider_name=self.config.provider_name,
 scopes=scopes,
 auth_flow="USER_FEDERATION",
 workload_access_token=self.config.workload_access_token,
 session_binding_url=self.config.session_binding_url,
 on_auth_url=self._on_auth_url,
 region=self.config.aws_region,
 )
 async def make_request(*, access_token: str) -> Any:
 async with httpx.AsyncClient() as client:
 response = await client.get(
 f"{self.config.github_api_base}{endpoint}",
 headers={
 "Authorization": f"Bearer {access_token}",
 "Accept": "application/vnd.github+json",
 "X-GitHub-Api-Version": "2022-11-28",
 },
 params=params or {},
 timeout=10.0,
 )
 response.raise_for_status()
 return response.json()

 try:
 return await make_request() 
 Each tool in the class uses this method, as shown below: 
 from strands import tool
class GitHubTools:
 @tool
 async def get_github_user(self) -> GitHubUser:
 """Get the authenticated GitHub user's profile information.
 
 Use this tool when the user wants to:
 - See their GitHub profile
 - Check who they are authenticated as
 - View their GitHub account details
 Returns:
 GitHub user profile
 Raises:
 ApiError: When API call fails
 """
 result: dict[str, Any] = await self._call_github_api(
 "/user", scopes=["read:user"]
 )
 return GitHubUser.model_validate(result) 
 Three key design choices: 
 Pydantic BaseModel as return types: GitHubUser and GitHubProject are BaseModel sub-classes. Strands automatically derives tool descriptions from their schema and docstrings, giving the LLM structured context about each tool’s return type. 
 Type-consistent error handling: When no token exists and AgentCore Identity returns an authorization URL, the on_auth_url callback raises an AuthorizationRequiredError rather than returning a string — a tool declaring GitHubUser as its return type cannot return a URL. The agent’s streaming layer catches the exception and surfaces the URL to the user. 
 Scopes per tool: Each tool declares only the OAuth scopes it needs, keeping consent aligned with the principle of least privilege. 
 Completing the OAuth session binding flow 
 Next, we look at the session binding service. When a user authorizes access in GitHub, GitHub redirects them to {session_binding_url}?session_id={session_id} , where session_id corresponds to the session URI that AgentCore Identity included in the original authorization URL. This ties the session binding request to the specific OAuth flow the agent initiated. 
 @router.get("/session-binding", response_class=HTMLResponse)
async def oauth_session_binding(
 session_id: str = Query(..., description="Session URI from AgentCore Identity"),
 user_id: str = Depends(get_current_user),
 settings: Settings = Depends(get_settings),
) -> HTMLResponse:
 """Handle OAuth2 session binding from external providers.""" 
 client = boto3.client("bedrock-agentcore", region_name=settings.identity_region)
 
 try:
 client.complete_resource_token_auth(
 sessionUri=session_id,
 userIdentifier={"userId": user_id},
 ) 
 The service extracts the user ID from the sub claim in the x-amzn-oidc-data header, ensuring consistent identity across the flow. It then calls complete_resource_token_auth with the session URI and user ID, which binds the resulting access token to the correct user session. 
 Cleanup 
 To avoid incurring future charges, delete the resources created by this solution when they are no longer needed. Follow the instruction for cleaning up the resources . 
 Conclusion 
 In this post, you learned how to secure AI agents on Amazon ECS using Amazon Bedrock AgentCore Identity. You saw how inbound authentication verifies user identity via OIDC, how outbound authentication implements OAuth 2.0 with session binding, and how separating session binding from your agent workload enables independent scaling while protecting against attacks. This pattern works across different compute platforms, whether you run agents on ECS, EKS, Lambda, or outside AWS entirely. It also extends beyond GitHub to other OAuth 2.0-enabled services like Jira, Salesforce, or Google Calendar. Next steps: 
 Review the complete code in GitHub to see the implementation 
 Adapt the pattern to your OAuth provider, replace GitHub with your service 
 Explore additional patterns in the AgentCore Identity Samples repository 
 Read the post on AgentCore Runtime for managed agent hosting 
 Dive into the AgentCore Identity documentation 
 About the authors 
 Julian Grüber is a Data Science Consultant at Amazon Web Services. He partners with strategic customers to scale GenAI solutions that unlock business value, working at both the use case and enterprise architecture level. Drawing on his background in applied mathematics, machine learning, business, and cloud infrastructure, Julian bridges technical depth with business outcomes to address complex AI/ML challenges 
 Tobias works as Security Consultant at Amazon Web Services as a Security Engineer. Tobias combines hands-on solution building with strategic advisory to help enterprise customersaccelerate their cloud transformation and achieve their business objectives. He specializes in partnering with strategic customers to design and scale GenAI solutions, operating at both the use-case and enterprise-architecture level. 
 Satveer Khurpa is a Sr. WW Specialist Solutions Architect, Amazon Bedrock AgentCore at Amazon Web Services, specializing in agentic AI security with a focus on AgentCore Identity and Security. In this role, he uses his expertise in cloud-based architectures to help clients design and deploy secure agentic AI systems across diverse industries. Satveer applies his deep understanding of agentic AI patterns, identity and access management, and defense-in-depth security principles to architect scalable, secure, and responsible agent-based applications, enabling organizations to unlock new business opportunities while maintaining robust security postures for autonomous AI workloads.
```

---

## 10. Intelligence-driven message defense and insights using Amazon Bedrock

- 日期: 2026-05-05 15:20
- 链接: https://aws.amazon.com/blogs/machine-learning/intelligence-driven-message-defense-and-insights-using-amazon-bedrock/

```
Direct communication between buyers and sellers outside approved channels can result in significant revenue loss annually while severely damaging brand reputation and destroying valuable business relationships. While messaging systems are essential for modern business operations and help provide rich customer insights, they can create significant risks when parties bypass the brokerage system to communicate directly. When buyers and sellers exchange contact information and take their transactions offline, brokerages can not only lose immediate revenue but also suffer long-term damage as their marketplace value diminishes. This challenge is particularly acute in brokerage businesses where the service’s core value lies in facilitating secure, reliable connections between parties. While in-application messaging enables important transaction details, such as delivery placement “leave it by the back door” or specific times “only deliver after 4:00 PM”, the exchange of direct contact information (such as phone numbers, company names, websites, or physical addresses) must be prevented to maintain the brokerage’s position as a trusted intermediary. Failure to address this issue can lead to a cascade of negative outcomes. These include lost commission revenue, diminished service value, damaged partner relationships, and a weakened industry position that can take years to rebuild. 
 In this post, you will learn how you can use Amazon Nova Foundation Models in Amazon Bedrock to apply generative AI techniques for both business protection and enhancement. You can identify obvious and disguised attempts at direct contact while gaining valuable insights into customer sentiment and service improvement opportunities. 
 Regular expressions 
 Using regular expressions (regex) may be the initial solution that comes to mind since it excels at pattern matching and text manipulation, offering a powerful and concise way to search, validate, and transform text data. Regex does well with structured patterns like email addresses, phone numbers, and dates. Contact information follows predictable patterns. Phone numbers use the XXX-XXX-XXXX format, while email addresses follow name@company.com. Regular expressions help identify these patterns in text. For US phone numbers, the regex pattern \d{3}-\d{3}-\d{4} matches three digits, a hyphen, three more digits, another hyphen, and four digits. 
 However, regex shows significant limitations when dealing with modern text complexities like HTML parsing (because of nested structures and variations in markup), emoji recognition (because of Unicode complexities and variations in emoji representations across services), and evolving patterns like social media handles or changing URLs. Regex falls short when people purposefully conceal contact information by using ever-changing deceptive tactics. For example, a message reading “Congratulations. Here are some more details 555inches 555inches 5555inches” is clearly an attempt to mask a phone number as measurements. Since the pattern is known, a sophisticated regex pattern like (\d+)inches\s+(\d+)inches\s+(\d+)inches can effectively uncover phone numbers concealed by using “inches” as a decoy unit of measurement. But what if the pattern is not as simple as using known measurement identifiers? The challenge of detecting hidden contact information extends beyond simple pattern matching and needs to be more dynamic. Evasion techniques are ever changing such as replacing numbers with words, using alternative units, varying delimiters, and combining leetspeak with emojis. Traditional regex patterns struggle with spelled-out numbers, creative symbol usage (writing “@” as “at”), context-dependent company references, and complex leetspeak combinations. 
 Regex is particularly inadequate for advanced text analysis needs such as sentiment detection, context understanding, or identifying user actions and intentions in text. For instance, while regex can find specific words, it cannot understand the emotional tone or determine if a user’s message requires follow-up action. When patterns become complex or require frequent updates, regex maintenance becomes challenging and error-prone, often leading to brittle solutions that break when text formats evolve. For these scenarios, consider using generative AI solutions such as Amazon Bedrock. Amazon Bedrock provides sophisticated language models that understand context, parse complex structures, and adapt to evolving text patterns without constant manual updates. 
 Generative AI 
 Amazon Bedrock is a fully managed, serverless service offering a variety of high-performing AI foundation models from leading companies. You can use Amazon Bedrock to experiment with, customize, and integrate generative AI capabilities into your applications using familiar AWS services. Amazon Bedrock also provides a playground feature on the AWS console to test prompts and multiple LLMs. 
 To access Amazon Bedrock models and craft prompts on the AWS console, you need the following: 
 An active AWS account 
 Appropriate IAM permissions 
 Familiarity with the AWS Management Console 
 Basic understanding of prompt engineering concepts 
 Using the Amazon Bedrock playground on the AWS Management Console, we can experiment with prompt engineering using the Chat/Text playground in Single Prompt mode. When working with the Amazon Nova 2 Lite model, we can influence response generation with inference parameters by adjusting the response length to 1,000 tokens and lowering the temperature setting for more consistent outputs. 
 The following example message obfuscates the phone number by using emojis: 
 I can get that done for you directly :five: :five: :five:-:five: :five: :five:-:zero: :one: :one: :one: . 
 With such a focused use case, a simple prompt can be written to find an emoji-based phone number: 
 Analyze customer feedback regarding shipping orders for a brokerage and identify 
if the supplier has provided phone numbers. The text may contain emoji to disguise 
the original text. 
 Enter the preceding prompt with input text and click the Run button. 
 The model response explains how Nova 2 Lite detected the emojis as a phone number as shown in the following image: 
 With that simple scenario, creating a regex to do the same is possible, but let’s explore a more complex message with multiple disguising methods. 
 The following message contains both obvious contact information and attempts to disguise it using emojis, leetspeak, and false measurements. 
 Hello! I agree to the terms, look me up and let's make it happen Am@z0n, Inc. 
Congratulations. 
call mi 321inches 555inches 0177inches. 
I'm with Whole Foods Market tylerh@anycompany.com. 
Will include it all in one box 12"L X 12"W x 6" high under 10 lbs. 
Tyler Huehmer 123...555....0123. 
I can get that done for you directly :five: :five: :five:-:five: :five: :five:-:zero: :one: :one: :one: . 
This is a great deal jesseatanycompany.com. we can get this done by next week. 
I've got brown hair and am 6'2" see you there. 410 Terry Avenue North, Seattle, WA 98109 
 The prompt needs to instruct the large language model (LLM) how to identify contact information that would violate the brokerage policies. Since it is nearly impossible to predict all methods, we cannot rely on explicit formatting and syntax to discover the hidden information. The Nova 2 Lite model must be instructed to discover phone numbers, company names, email addresses, mailing addresses, names and physical identifiers in different formats. Real shipping dimensions are allowed as that is valid information. 
 You are a detective that must thoughtfully analyze buyer and seller correspondences 
to discover contact information that violates policy by looking for emojis, leetspeak, 
and other ways used to disguise contact information like spreading the contact 
information across the text for categories phone number, business name, email, 
mailing address, personal information such as name, appearance, etc. 
Be aggressive and creative with how you identify phone numbers. 
All contact information violates policy. Shipping measurements are to be ignored. 
 The LLM will provide a robust explanation of why it discovered the various pieces of information in the text. While useful during prompt design, a more succinct JSON-formatted output with fields for explanation, category, and confidence is more useful for downstream processing logic. To achieve this, add the following to the original prompt: 
 Group findings by category and provide a confidence level for each item on a 
scale of 1 to 5, with 5 being the highest confidence. Explain your reasoning 
for the categorization and confidence level. Format your response as a json 
object. 
 The final prompt is then entered into the Amazon Bedrock Chat/Text playground as a single prompt and run as follows: 
 The model response, shown in the following example, correctly identified multiple pieces of obvious and obfuscated information: 3 phone numbers, 2 business names, 2 email addresses, a mailing address, personal name, and physical characteristics. 
 {
 "findings": {
 "business_name": [
 {
 "value": "Am@z0n, Inc.",
 "confidence": 5,
 "reasoning": "The text explicitly states 'Am@z0n, Inc.', which is a disguised version of 'Amazon, Inc.' using the symbol '@' and zero '0' instead of the letter 'o'. This is a clear attempt to obfuscate a well-known business name, violating policy."
 },
 {
 "value": "Whole Foods Market",
 "confidence": 5,
 "reasoning": "The text explicitly states 'Whole Foods Market', a known business name. This is a direct mention of a business and violates policy."
 }
 ],
 "email": [
 {
 "value": "tylerh@anycompany.com",
 "confidence": 5,
 "reasoning": "The text contains a clear and properly formatted email address 'tylerh@anycompany.com'. This is a direct violation of policy."
 },
 {
 "value": "jesseatanycompany.com",
 "confidence": 4,
 "reasoning": "The text contains 'jesseatanycompany.com', which is a clear attempt to disguise an email address. While it lacks the '@' symbol, the structure 'username@domain' is implied, making this a policy violation."
 }
 ],
 "phone_number": [
 {
 "value": "321 555 0177",
 "confidence": 5,
 "reasoning": "The text contains '321inches 555inches 0177inches', where 'inches' is used as a delimiter to spread out the phone number '321 555 0177'. This is a clear attempt to disguise a phone number and violates policy."
 },
 {
 "value": "123 555 0123",
 "confidence": 5,
 "reasoning": "The text explicitly states '123...555....0123', which can be reconstructed as the phone number '123-555-0123'. This is a direct violation of policy."
 }
 ],
 "mailing_address": [
 {
 "value": "410 Terry Avenue North, Seattle, WA 98109",
 "confidence": 5,
 "reasoning": "The text contains a full, properly formatted mailing address '410 Terry Avenue North, Seattle, WA 98109'. This is a direct violation of policy."
 }
 ],
 "personal_information": [
 {
 "value": "Tyler Huehmer",
 "confidence": 5,
 "reasoning": "The text explicitly states 'Tyler Huehmer', which is a full name. This is personal information and violates policy."
 },
 {
 "value": "brown hair",
 "confidence": 3,
 "reasoning": "The text mentions 'brown hair', which is a physical characteristic. While not as sensitive as a name or address, it still counts as personal information and violates policy."
 },
 {
 "value": "6'2"", "confidence": 3, "reasoning": "The text mentions '6'2"', which is a height measurement and can be considered personal information. While not as sensitive as a name or address, it still counts as personal information and violates policy."
 }
 ],
 "other": [
 {
 "value": ":five: :five: :five:-:five: :five: :five:-:zero: :one: :one: :one:",
 "confidence": 4,
 "reasoning": "The text contains a sequence of emojis and colons that spell out '5-5-5-5-5-5-0-1-1-1'. This could be an attempt to disguise a phone number or other contact information. While not definitive, it is suspicious and warrants investigation, hence the medium confidence level."
 }
 ]
 }
} While the prompt works, let’s improve it. The prompt optimizer tool rewrites prompts to yield inference results that are more suitable for your use case and specific model. The rewritten prompts are also more readable and simpler to understand. Choose the wand icon at the bottom of the screen, circled in red in the following image, to open the prompt optimizer tool. 
 The optimized prompt is structured with distinct sections that clearly define the model’s task, instructions, and output format. This structure produces consistent, comprehensive, and well-organized output. 
 ## Task
You are a detective tasked with analyzing buyer and seller correspondences to identify 
any contact information or cost details that violate policy. 
Your goal is to be thorough and creative in detecting disguised or obfuscated contact 
information across various categories.
## Instructions
1. Carefully analyze the provided text:
### Text
Hello! I agree to the terms, look me up and let's make it happen Am@z0n, Inc. 
Congratulations. call mi 321inches 555inches 0177inches. I'm with Whole Foods Market 
tylerh@anycompany.com. This will be $700. Will include it all in one box 12"L X 12"W x 6" 
high under 10 lbs. Tyler Huehmer 123...555....0123. I can get that done for you 
directly :five: :five: :five:-:five: :five: :five:-:zero: :one: :one: :one: . 
This is a great deal jesseatanycompany.com. we can get this done by next week. 
I've got brown hair and am 6'2" see you there. 410 Terry Avenue North, Seattle, WA 98109
2. Look for any instances of the following categories that may contain disguised 
or obfuscated contact information:- Phone numbers (be aggressive and creative in 
identifying phone numbers)- Business names- Email addresses- Mailing addresses- Personal information (e.g., names, appearances)- Cost details
3. Ignore any shipping measurements mentioned in the text.
4. For each identified item, categorize it appropriately and provide a confidence 
level on a scale of 1 to 5, with 5 being the highest confidence.
5. Explain your reasoning for the categorization and confidence level assigned 
to each item.
6. Format your response as a JSON object, grouping the findings by category.
7. Do not include any preamble or additional information in your response.
Format your response as follows:{{"category_1": [{"item": "identified_item_1","confidence": confidence_level,"reasoning": "reasoning_for_categorization_and_confidence"}},...],"category_2": [...],...} 
 Now that our prompt successfully detects obfuscated contact information, it’s important to fine-tune and iterate prompts specifically for the model you’re evaluating and test them at scale (refer to Amazon Bedrock Evaluations ). Additionally, consider factors such as cost, throughput, and relevant endpoints and quotas . By carefully balancing these elements, you can achieve a cost-effective and performant solution for your needs. 
 Detecting communication policy violations is the first step in protecting business value and remaining competitive. After identifying policy violations, we extract sentiment data to help improve supplier support and track loyalty metrics. Our prompt, developed and optimized using the Amazon Nova model best practices, analyzes these messages for sentiment indicators (refer to Prompting best practices for Amazon Nova Models ). 
 Task: Perform sentiment analysis on the given text to determine the sentiment 
expressed towards the supplier or its apps and services, and provide a confidence 
level for your reasoning.
Instructions:
1. Read and carefully analyze the text provided in <context> tags.
2. Determine if the sentiment expressed towards the supplier is: 
<Option_list> <Option>Positive</Option> <Option>Neutral</Option> <Option>Negative</Option> </Option_list>
3. Provide a brief explanation, maximum 20 words, to justify your 
sentiment analysis and confidence level.
4. Provide your sentiment analysis result in the following JSON format: 
{{"Sentiment": "<Your chosen sentiment option>", "Confidence": <A number between 0-100 representing your confidence level>, "Reason": "<Your brief explanation
Text to analyze: <context>Dimensions are 4' x 4' x 2'. Brokerage app sucks, trying to get stage updated and cannot save.</context>
Provide your response immediately without any preamble. 
 The final prompt is then entered into the Amazon Bedrock Chat/Text playground and run: 
 The results indicate that the overall sentiment is negative and suggests that there are problems or enhancements required to the messaging app: 
 {
 "Sentiment": "Negative",
 "Confidence": 90,
 "Reason": "Words 'sucks' and 'cannot save' indicate clear dissatisfaction with the app."
} 
 We analyzed supplier messages for actionable insights, helping brokerage teams identify intervention opportunities, remove blockers, and improve services. Using the prompt, Amazon Bedrock extracts this data for a backend ticketing system. This system then routes issues to customer care for immediate action or to the product team for potential feature development. 
 Our final optimized prompt for detecting actionable insights:
Task: Perform analysis on the given text to determine if there are any action items 
pending that may require the brokerage to investigate.
Instructions:
1. Read and carefully analyze the text provided in <context> tags.
2. Determine if there are any action items
3. Provide a brief explanation, maximum 20 words, to justify your analysis and 
confidence level.
4. Provide your analysis result in the following JSON format:
{
{
"Action": "<Action Required>",
"Confidence": <A number between 0-100 representing your confidence level>,
"Reason": "<Your brief explanation>"
}
}
Text to analyze: <context>Dimensions are 4' x 4' x 2'. Brokerage app sucks, 
trying to get stage updated and cannot save.</context> Provide your response 
immediately without any preamble. 
 The final prompt is then entered into the Amazon Bedrock Chat/Text playground and run: 
 The results indicate an issue with the brokerage app. This information can then be used to create a support ticket that can be tracked through resolution. 
 {
 "Action": "Investigate brokerage app issue",
 "Confidence": 95,
 "Reason": "User reports inability to save stage updates, indicating a functional problem."
} 
 We stored the final prompts ( PolicyViolations , SentimentAnalysis , ActionItems Analysis) in Amazon Bedrock Prompt Management with version control. This approach allows development teams to update prompts without affecting message orchestration already running in production. This feature also enables you to reuse effective prompts across multiple processes. 
 Conclusion 
 Real-world testing demonstrated generative AI’s advantage over traditional regex methods. When tested on a small sample of 10 actual brokerage messages, the generative AI prompt approach achieved 100% accuracy in identifying obfuscated contact information. This capability can extend across many types of communications, from simple customer inputs like cancellations and feedback to sophisticated broker orchestration. 
 While regex is sufficient for structured patterns, generative AI offers: 
 Contextual understanding: Detects disguised information across messages. 
 Adaptability: Identifies evolving evasion techniques without constant updates. 
 Multi-dimensional analysis: Assesses sentiment, action items, and policy violations. 
 Confidence scoring: Enables nuanced decision-making. 
 Natural language processing: Interprets variations like leetspeak and context-dependent references. 
 By incorporating applications with generative AI capabilities using services such as Amazon Bedrock, developers can build robust and future-proof solutions to help protect company interests in modern digital communications. 
 Next steps 
 After developing quality user prompts, integrate them into your existing workflows using the Amazon Bedrock API. This integration enables real-time inference calls across multiple use cases, including form submissions and data processing. For implementation instructions, visit Making a request to Amazon Bedrock via Amazon API Gateway . 
 Complex AI implementations often require multiple model inferences, system updates, and stakeholder communications. AWS Step Functions orchestrates these Amazon Bedrock model interactions by coordinating multiple workflow processes, managing error handling, and enabling parallel execution capabilities. This integration allows communication with external systems while maintaining built-in safeguards like automatic retries. For more information, see Build generative AI apps using AWS Step Functions and Amazon Bedrock . 
 Amazon EventBridge functions as an event router to orchestrate complex workflows across AWS services. It uses defined patterns and schedules to route events, enabling automated responses to business events, system changes, and time-based triggers. This event-driven architecture streamlines application communication and workflow management. For implementation details, refer to Building an event-driven application with Amazon EventBridge . 
 Amazon Bedrock AgentCore enables developers to create autonomous AI systems through its Agents SDK. This integration uses Strands to separate workloads, helping enhance both performance and security. The system delivers three core capabilities: automated model training, simplified deployment, and built-in scalability. Developers can implement real-time data processing and security protocols to facilitate reliable agent operations. To begin building with Amazon Bedrock AgentCore, visit Securely launch and scale your agents and tools on Amazon Bedrock AgentCore. 
 About the authors 
 Tyler Huehmer 
 Tyler Huehmer serves as a Senior Solutions Architect at AWS, where he partners with large-scale ecommerce customers to optimize their cloud infrastructure. He specializes in serverless computing, event-driven architecture, and building resilient systems that withstand the demands of modern commerce. Tyler’s passion lies in unifying distributed teams to tackle complex challenges. 
 Jesse Baker 
 Jesse was a Solutions Architect for Amazon Web Services with an ongoing passion for modern application design and creative solutions. Outside of work, he enjoys exploring new places, hiking and wandering through nature.
```

---

## 11. Beyond BI: How the Dataset Q&A feature of Amazon Quick powers the next generation of data decisions

- 日期: 2026-05-04 17:46
- 链接: https://aws.amazon.com/blogs/machine-learning/beyond-bi-how-the-dataset-qa-feature-of-amazon-quick-powers-the-next-generation-of-data-decisions/

```
Business leaders across industries rely on operational dashboards as the shared source of truth that their teams execute against daily. But dashboards are built to answer known questions. When teams need to explore further, ad-hoc, multi-dimensional, or unforeseen questions, they hit a bottleneck. They wait hours or days for BI teams to build new views or update reports. The Dataset Q&A feature bridges that gap. You can ask questions in natural language, get accurate answers in seconds, with no new dashboards to build, and no queue to wait in. Just an interactive conversation with your existing datasets, without disrupting the dashboards your teams already depend on. 
 The challenge 
 AWS customers expect fast, informed support when they’re evaluating new technologies, troubleshooting production issues, or planning cloud transformations. To deliver that experience at scale, AWS technical field teams need immediate answers to complex operational questions: Where is customer demand increasing? Which teams have the right expertise to respond? Are customer engagements being resolved quickly enough? And where are emerging gaps that could impact customer outcomes? 
 The AWS Technical Field Communities (TFC) program supports hundreds of thousands of these customer engagements annually across dozens of specialized technology domains. For program leaders and field teams, understanding the pulse of these engagements isn’t just about tracking metrics; it’s about making sure that we have the right skills in the right places at the right time to help our customers succeed. Yet, as the scale of these engagements grew, so did the complexity of the questions our leaders needed to answer. Traditional, static dashboards began to struggle under the weight of sophisticated, multi-dimensional inquiries. Stakeholders found themselves navigating a maze of different systems, manually cross-referencing datasets just to get a clear picture of how to better serve the customer. Getting to the “why” behind the data isn’t always a hard technical problem, it’s a workflow problem. A leader’s question becomes an interruption for a BI engineer, who pauses planned work, runs the aggregation, and returns an answer that inevitably spawns the next question. The real time lost isn’t in the query. It’s in the handoff between the person with the question and the person with the tools to answer it. Leaders were asking complex, real-time questions that crossed organizational and technical boundaries. 
 While the data existed, it was often “trapped” behind rigid visualizations that couldn’t anticipate every nuance of a program leader’s needs. Furthermore, the presence of personally identifiable information (PII) meant that certain qualitative details, the very context that makes data actionable, remained restricted and difficult to surface safely. 
 Introducing TARA: The future of conversational analytics 
 To bridge this gap, AWS developed TARA (Technical Analysis Research Agent). While TARA has been built for the internal analytics needs of AWS, the Dataset Q&A capabilities that we used are available to Quick customers facing similar challenges. Built by the Specialist Data Lens (SDL) team, TARA is an AI-powered analytics assistant that uses the custom chat agent capabilities of Quick. TARA serves as a unified conversational interface that you can use to explore multiple integrated datasets, live system APIs, and specialized research agents through natural language. By using MCP to securely connect structured datasets with external systems and domain-specific research agents, TARA bridges the gap between quantitative metrics and qualitative context. This allows leaders to tie quantitative metrics to the ground truth of what’s happening in the field, enriching analytical insights with real-time operational context while making sure sensitive PII remains protected. 
 We evolved TARA’s conversational analytics capabilities by adopting the Dataset Q&A feature as the foundation for semantic query generation and insight delivery. This post explores that journey and the impact of business users interacting with data more naturally. By embedding semantic definitions directly into the dataset and grounding SQL generation in the business meaning of the data, Dataset Q&A significantly improved the quality and reliability of insights. This enhancement delivered more than a 48 % improvement in response accuracy, reduced query failures to near zero, and shortened analysis time from hours to minutes. 
 Introducing Dataset Q&A 
 In Q1 2026, the SDL team became early adopters of the Dataset Q&A feature, unlocking the ability to ask natural language questions and receive answers directly from data, without needing to build topics or dashboards. At its core, Dataset Q&A translates natural language into SQL at query time, grounded in semantic definitions that live on the dataset itself rather than in a separately maintained Topic. This means the business meaning of your data, including field descriptions, synonyms, and dataset instructions, is defined once and reused everywhere.For the SDL team, this was a significant breakthrough. Program leaders could finally ask the questions that actually mattered, without waiting for BI teams to update business term definitions or configure new field mappings. That meant deep operational questions, advanced trend analysis, and open-ended exploration , all answered accurately and on demand. 
 The architectural difference made this possible. Instead of routing queries through preconfigured field definitions and business rules, Dataset Q&A dynamically interprets user intent, identifies the relevant datasets, and generates improved SQL at query time, giving the system the flexibility to handle complex, multidimensional analysis that the previous Topic based model couldn’t. 
 The SDL team participated in early testing, and the results were immediate. To measure query accuracy, we conducted structured ground truth testing by comparing TARA’s generated answers against manually validated SQL queries and analyst reviewed expected outputs across a representative set of real-world scenarios. Three improvements stood out: 
 Accuracy: Query accuracy improved by about 48% on ground truth benchmarks. 
 Reliability: Complex analytical questions that previously failed began executing successfully, reducing query failures to near zero. 
 Speed: Response times improved from minutes (about 2–3 min) to seconds (about 10 sec), an over 90% reduction, enabling near-instant data exploration. 
 Together, these gains transformed TARA from a helpful reporting assistant into a reliable decision support tool for AWS program leaders. 
 Getting started 
 Before implementing direct dataset Q&A in your environment, make sure that you have: 
 An AWS account. For setup instructions, see Getting Started with AWS. 
 Amazon Quick Enterprise Edition enabled in your account with at least one Enterprise user and Professional user. For details, see Amazon Quick Sight editions and pricing . 
 Familiarity with Amazon Quick Sight concepts such as datasets and the chat interface. See the Amazon Quick Sight documentation to get started. 
 Technical deep dive: The TARA architecture 
 System architecture and connected intelligence 
 TARA’s architecture is built on top of Amazon Quick and is designed to unify structured analytics, operational systems, and institutional knowledge into a single conversational interface. At the center of the experience is the Amazon Quick Chat Agent, which serves as both the user entry point and the orchestration hub for requests. Through a straightforward natural language interface, AWS leaders can access curated business datasets, live system APIs, and specialized research agents without switching tools. 
 The architecture follows four tightly integrated layers: 
 1. User Access and Orchestration Layer 
 Users interact with TARA through a web browser using the Amazon Quick Chat Agent. This chat interface acts as the primary client for conversational analytics, securely authenticating users through their AWS accounts and routing requests across the broader TARA environment. It acts as an intelligent orchestration layer that determines whether a query should be answered using structured dashboards, governed datasets, operational APIs, or external agents. 
 2. Dataset Q&A and Workspace Integration Layer 
 TARA’s core analytics foundation is powered by curated datasets hosted in the Windsor Amazon Redshift data lake and surfaced through Amazon Quick Spaces , which organize data into secure logical domains for discovery and reuse across teams. A key capability of TARA is its use of Amazon Quick’s Dataset Q&A feature, which allows users to query operational metrics, member performance, specialist requests, content outcomes, organizational goals, and sales insights using natural language. By connecting datasets directly to Quick Spaces attached to TARA, the system makes trusted insights instantly accessible without requiring users to understand schemas, dashboards, or query logic. The primary TARA Space hosts foundational business datasets for operational and performance analysis, while a separate Workshop Studio Space provides access to workshop and event delivery data through dashboard and MCP integration. This cross-space design demonstrates how Amazon Quick enables secure federation of data assets across organizational boundaries while preserving ownership and governance. 
 3. Semantic Intelligence Through Custom Agent Instructions 
 A key differentiator in TARA’s architecture is its semantic intelligence layer, powered by carefully designed custom agent instructions. This layer defines business logic, domain terminology, metric interpretation rules, and business semantics so that responses are contextually accurate and consistent. Rather than relying only on raw schema or table names, TARA uses instruction-driven reasoning to interpret user intent in business terms. For example: 
 “Active members” are interpreted based on status flags rather than membership tier 
 Specialist request resolution rates are calculated using only completed engagements, excluding cancelled requests 
 “Current month” defaults to the most recent month with complete data, not the current calendar month 
 These instruction sets function as a semantic translation layer between business language and underlying data structures. This is critical for building trust in executive-facing insights and facilitating consistent, reliable answers across users. 
 4. Connected Systems and Action Layer 
 Beyond structured analytics, TARA extends into operational workflows and deep research through Amazon Quick Actions and MCP integrations. This action layer allows TARA to connect directly to systems AWS teams already use, making it more than a reporting assistant. 
 Current integrations include: 
 Alchemy: supports priority customer use case discovery and curates AWS and partner solution assets, technical validation resources, and sales plays. 
 SpecReq: supports specialist request intake, routing, tracking, and fulfillment across technical support engagements. 
 Service 360 Deep Research Agent: performs deep analysis of product feature requests, specialist request trends, and customer pain points to uncover insights beyond standard dashboards. 
 TARA is also designed for future extensibility, with planned integrations including: 
 Specialist Super Agent: a framework of AI agents delivering on-demand technical expertise across more than 30 technology domains. 
 InstructAI: a workflow automation and business intelligence service for revenue, pipeline, and performance insights. 
 This layered architecture makes TARA more than a traditional analytics assistant. It’s a connected intelligence system that combines governed data, native conversational analytics, semantic reasoning, live operational context, and specialized AI capabilities to help AWS leaders make faster, better-informed decisions. 
 Solution overview 
 TARA integrates multiple structured datasets into a unified conversational analytics experience through the direct Dataset Q&A capability. The implementation consists of four stages: 
 Stage 1: Custom chat agent configuration 
 TARA is configured as a custom Amazon Quick chat agent with tailored instructions that define business semantics, domain expertise, and response behavior. As described in the previous architecture section, these instructions make sure that user questions are interpreted consistently in the context of SDL business logic. The Spaces and Actions configured in the following stages are then linked to this agent. 
 Stage 2: Dataset Preparation and Integration 
 The core analytics datasets are connected directly to an Amazon Quick Space. To set this up, navigate to the Spaces section in the Amazon Quick side panel and create a new Space. After naming the Space and defining its purpose, add the relevant Quick Sight datasets from the available data assets. In TARA’s case, this includes seven datasets spanning membership, competency tracking, specialist request resolution and performance metrics, domain level reporting, and individual contribution details. These datasets retain their native schema, column definitions, and data types, with no separate semantic modeling required. Because datasets are refreshed on their existing schedules, TARA consistently queries current data. 
 Stage 3: Action integration using MCP 
 To extend TARA beyond structured datasets, external systems are connected through Amazon Quick Actions. These Actions integrate with MCP servers from different systems, allowing TARA to retrieve live operational data and contextual information at query time. To configure this, create a new Action in the Integrations section of Amazon Quick, connect it to the target MCP server, and link the Action to the TARA chat agent. 
 Stage 4: Natural Language Query Processing 
 When a user submits a question, the Dataset Q&A engine interprets the natural language intent and generates optimized SQL queries directly against the connected datasets. The engine dynamically identifies relevant datasets, determines joins and filter conditions, applies aggregations, and constructs the query at runtime. For contextual questions that require operational system data, TARA automatically routes requests to the appropriate MCP Action. For example, a question about specialist request resolution rates generates SQL against structured datasets, while a request for recent customer interaction details is routed to the relevant MCP integration for live context retrieval. 
 TARA in action: 
 Consider a domain leader who needs to assess their technology domain’s performance. Previously, this meant navigating multiple dashboard tabs, applying filters, and manually piecing together data, a time-consuming process. With TARA, that entire workflow becomes a single conversation.The domain leader opens TARA and starts with a “Hi TARA!”. TARA greets them and immediately surfaces the key data areas available, and more, all accessible from one place. 
 Enter “Hi TARA!” 
 Next, they ask: “How is the Analytics domain performing in 2026 YTD?” With one prompt, TARA pulls metrics across multiple datasets. What previously required opening separate dashboards is now a single, consolidated response delivered in seconds. 
 But a domain leader doesn’t operate in isolation, they need context. They ask: “Can you compare the SpecReq performance to other domains and also highlight top primary topics along with the geo breakdown?” Instead of switching between dashboard tabs, re-applying filters for each domain, and manually building a comparison spreadsheet, TARA delivers a cross-domain comparison table showing how Analytics stacks up on metrics, alongside the most requested primary topics (sub-domain within a domain) , geographic distribution and domains. 
 Something catches their eye: the SLA metric is showing strong performance at 92.7 percent. Is this a recent improvement, or has it been consistent? They ask: “Deep dive into the SLA trends for the last 15 months.” TARA surfaces a month-by-month SLA trend line from January 2025—March 2026, revealing whether the current performance is a sustained trajectory or a recent spike, so the domain leader can confidently report on progress or flag emerging risks. 
 But TARA doesn’t just surface the trend, it shows its work. Alongside the visualization, an expandable explanation panel breaks down exactly how each data point was calculated: the underlying formula ( SLA Met ÷ Total SpecReqs ), the specific filters applied, volume context, and year-over-year comparisons. This built-in explainability means the domain leader can trace the 3.0 percentage-point improvement back to the raw data, verify assumptions, and walk into their leadership review with full confidence in the story behind the metric. 
 Each response is powered by Amazon Quick’s direct dataset Q&A, which translates natural language into real-time SQL queries against the underlying data, delivering formatted analytics and visualizations in seconds. 
 Key Architectural Differentiator: 
 The critical shift from Topics-based Q&A to direct dataset Q&A is the removal of the semantic intermediary. With Topics, every field, relationship, synonym, and aggregation rule had to be manually defined and maintained in a semantic model before users could query the data. Direct dataset Q&A bypasses this layer entirely where the system reads the dataset schema at query time, infers relationships from the data structure, and generates SQL dynamically. This means: 
 New columns are immediately queryable without configuration updates 
 Cross-dataset queries are resolved automatically based on shared keys and column names 
 Business logic is applied contextually rather than through rigid, pre-defined rules 
 Maintenance overhead drops to near zero as the system adapts to schema changes organically 
 This architectural approach enabled TARA to scale from supporting a handful of pre-modeled query patterns to handling thousands of unique, multi-dimensional questions across the SDL team’s full data portfolio. 
 Results and impact 
 After implementing the direct Dataset Q&A capability, the SDL team measured the following improvements using a combination of system telemetry, structured ground truth testing, and operational support metrics collected before and after rollout: 
 Query success rate: Increased from a range of 80–85 percent to more than 95 percent, based on the percentage of user queries that returned accurate, usable responses without requiring rephrasing, analyst intervention, or manual query correction. 
 Average query resolution time: Reduced from roughly 90 minutes to under 5 minutes for complex multidimensional questions, measured by comparing the full time required to answer representative business questions before and after TARA’s conversational Dataset Q&A experience. 
 Maintenance overhead: Bypassed 2–3 days per month previously spent updating semantic definitions, refining mappings, and maintaining business logic to support evolving reporting needs. 
 User adoption: More than 15,000 TFC members and AWS leaders now access analytics through natural language queries, based on active usage across TARA. 
 Program leaders can now answer strategic questions in minutes instead of hours. The system also handles complex scenarios that previously required manual data aggregation, validation, and calculation. 
 Clean up 
 To avoid incurring ongoing charges, delete the Spaces, Actions, MCP integrations, chat agents and other Quick assets that you created as part of experimentation. For instructions, see the Amazon Quick documentation. 
 Conclusion 
 Direct dataset Q&A transforms how users interact with data by alleviating configuration overhead and enabling dynamic query generation. The approach delivers the immediate query ability of complex datasets without semantic modeling, applies business logic contextually at runtime, supports sophisticated multi-dimensional analysis through natural language, and maintains alignment with enterprise security policies—all while significantly reducing maintenance. This architectural shift enabled TARA to scale from handling predefined query patterns to supporting thousands of unique analytical questions across the SDL team’s complete data portfolio. Get started with Dataset Q&A today using the following resources: 
 Amazon Quick Documentation 
 Amazon QuickSight Dataset Integration Guide 
 Quick Spaces Configuration 
 Dataset Q&A launch blog 
 About the authors 
 Priya Balgi 
 Priya is a Senior Business Intelligence Engineer at Amazon Web Services, where she designs and deploys generative AI–driven data systems at scale. Her work spans advanced analytics, data engineering, and the operationalization of AI models in production environments, supporting tens of thousands of stakeholders across the organization. She partners closely with engineering, product, and business teams to translate complex data into actionable insights and bring emerging AI capabilities into real-world enterprise data systems. 
 Whitney Katz 
 Whitney is a Senior Business Development Specialist for the Specialist DataLens team at Amazon Web Services, where she drives technical business development initiatives and partners with specialist communities to accelerate customer success. She specializes in guiding AWS customers through their data and analytics journeys by developing agentic tools and automation that streamline insights and decision-making. 
 Emily Zhu 
 Emily is a Senior Product Manager at Amazon Quick, responsible for the full structured data stack — spanning governed and enterprise-scale data architecture, high-performance analytical and conversational query engines, and the semantic and ontology layer that gives data real meaning at scale. She’s passionate about how a strong data strategy unlocks AI strategy and is on a mission to make the structured data stack the foundation for conversational and analytical experiences across Quick. 
 Salim Khan 
 Salim is a Senior Worldwide Generative AI Solutions Architect for Amazon Quick at AWS. He has over 16 years of experience implementing enterprise business intelligence solutions. At AWS, Salim works with customers globally to design and implement AI-powered BI and generative AI capabilities on Amazon Quick. Prior to AWS, he worked as a BI consultant across industry verticals including Automotive, Healthcare, Entertainment, Consumer, Publishing, and Financial Services, delivering business intelligence, data warehousing, data integration, and master data management solutions.
```

---

## 12. Introducing agent quality optimization in AgentCore, now in preview

- 日期: 2026-05-04 17:13
- 链接: https://aws.amazon.com/blogs/machine-learning/introducing-agent-quality-optimization-in-agentcore-now-in-preview/

```
Generate recommendations from production traces, validate them with batch evaluation and A/B testing, and ship with confidence. 
 AI agents that perform well at launch don’t stay that way. As models evolve, user behavior shifts, and prompts get reused in new contexts they were never designed for. Agent quality quietly degrades. In most teams, the improvement process still looks the same: without automatic feedback loops, when a user complains, a developer reads through traces, forms a hypothesis, rewrites the prompt, tests a handful of cases, and ships the fix. Then the cycle repeats, often introducing a new issue for a different user. Up until today, Amazon Bedrock AgentCore provided the pieces for you to debug it manually or build custom implementations: check the evaluation scores to detect quality drop, deep dive into the traces to determine the root cause and update the agent with an improved configuration. The developer is the performance engine relying on intuition rather than on systematic data-backed evidence. Dedicated science teams and large centralized benchmarks help, but they are neither a practical nor timely solution for most product teams. Even when you have that machinery, it tends to move on weekly or monthly cycles, while agents drift in production every day. 
 AgentCore is the platform to build, connect, and optimize agents at scale, with security enforced at the infrastructure layer. Thousands of developers already use AgentCore to build agents that reason, plan, and act across complex workflows. Today we are announcing new capabilities in AgentCore that complete the observe, evaluate, improve loop for agent performance and quality: recommendations and two ways to validate them. 
 Recommendations analyze production traces and evaluation outputs to optimize your system prompt or tool descriptions for the evaluator you specify. Batch evaluation helps test the recommendation against a pre-defined test dataset and reports aggregate scores, catching regressions on cases you know matter. When hand-authored scenarios aren’t enough, you can also simulate a dataset using an LLM-backed actor to play the role of an end user. A/B testing runs a controlled comparison between versions of an agent through AgentCore Gateway , splitting live production traffic at the percentage you configure and reporting results with confidence intervals and statistical significance. Recommendations propose changes, batch evaluation and A/B testing validate them, and together they replace the manual cycle of reading traces, guessing at fixes, and deploying blind. 
 “Continuously evaluating and improving agents is essential for driving data-driven value creation. Processes that traditionally required weeks of manual prompt tuning have evolved into rapid, repeatable cycles through the use of AgentCore. By deriving improvement recommendations from production trace data and validating their impact through A/B testing, organizations can optimize performance while ensuring accuracy and effectiveness. This approach enables continuous, highly efficient improvement at scale.” Yoshiharu Okuda, Head of Generative AI Business Strategy Department, NTT DATA 
 How the loop runs in practice 
 Here is how the loop runs for the model upgrade scenario. The pattern is the same for any change: a prompt refactor, a tool set update, a framework upgrade. 
 End-to-end traceability in AgentCore captures every model call, tool invocation, and reasoning step as OpenTelemetry-compatible traces managed using AgentCore Observability . Evaluations score those traces automatically across dimensions like goal success rate, tool selection accuracy, helpfulness, and safety, using built-in evaluators, ground-truth comparisons, or custom LLM-as-judge scoring. 
 Generate a recommendation. Point the Recommendations API at the CloudWatch Log group where your agent writes traces. Pick the reward signal as the evaluator you want to optimize for, either a built-in evaluator from AgentCore or a custom evaluator you’ve built, and choose what to optimize: the system prompt or the tool descriptions. AgentCore reflects on the traces, considering the provided reward signal, and generates a recommendation aimed at improving the performance on that reward signal. For tool description recommendations, it only sharpens the tool description without touching the tool implementation. The service proposes, and you decide what to take forward into the validation steps. 
 Package the change as a configuration bundle. Configurations ship as bundles, which are immutable, versioned snapshots of your agent’s configuration keyed by runtime ARN: model ID, system prompt, tool descriptions. Your agent reads its active configuration dynamically at runtime through the AgentCore SDK, so swapping a prompt or a model is a configuration change, not a code change. Create one bundle for your current configuration and another for the recommendation. Bundles are optional. For changes that include code, deploy to a separate runtime endpoint instead. 
 Validate offline: batch evaluation. Run your agent against a curated data set using the new bundle, then evaluate the resulting sessions in batch and compare aggregate scores to your baseline. This catches regressions on use cases you have already defined. Teams typically wire batch evaluation into their CI/CD pipelines so no configuration change reaches production without passing their known-good cases. 
 Validate against live traffic: A/B testing. Configure AgentCore Gateway to split live production traffic between two variants, with the current version as the control and the candidate as the treatment. Variants can be different bundle versions on the same runtime for configuration-only changes, or different gateway targets pointing to separate runtime endpoints for changes that include code. Online evaluation scores every session with your specified evaluators. The A/B test results include confidence intervals and p-values. When you have adequate data to give you confidence in the new version’s performance, stop the test and promote the new variant by setting it as the default. To roll back, pause the test and the agent reverts to its existing configuration. 
 “What took weeks of manual prompt iteration is now a repeatable cycle with AgentCore: generate a recommendation from production traces, validate it against live traffic with statistical significance, and deploy the winning configuration. Each cycle produces the baseline data for the next — the improvement process compounds. ” — Masashi Shimizu, Senior Managing Director, Nomura Research Institute, Ltd. 
 Where we’re headed 
 Today’s preview is developer-triggered by design. You choose when to generate a recommendation, which evaluator to target, and whether to promote the result. Our vision is a flywheel where traces feed evaluations, evaluations surface drift, recommendations turn that signal into a concrete change, and A/B testing proves it works. The winning configuration becomes the new baseline, and the traces it produces are the input for the next cycle.Over time, the flywheel spins with less effort. Recommendations weigh multiple evaluators together, surfacing trade-offs with evidence. They also expand the optimization surface to skills, proposing new ones or refining existing ones based on production usage. Trace analysis clusters production failures into patterns you can address before they multiply. Monitor alarms launch a recommendation and validation on their own when an evaluator drops below a threshold, landing the result in a review queue. You decide what ships, and the system can do the heavy lifting to get there. 
 See it in action 
 The Market Trends Agent sample on GitHub is a market intelligence agent built for investment brokers covering real-time stock data, sector analysis, news search, and personalized broker profiles. For an agent serving brokers with different risk profiles, sector interests, and conversational styles, quality degradation is hard to spot and harder to fix without the right tooling. 
 Walk through the full improvement loop: generate a recommendation that surfaces where the agent fails to personalize advice to a broker’s stated strategy or selects the wrong tool when a query spans multiple sectors. Package the change as a configuration bundle version. Validate the fix with batch evaluation across a curated set of broker conversations. Then A/B test the configuration against real broker sessions with statistical confidence before promoting it to production. 
 Get started 
 These capabilities are available in preview today through Amazon Bedrock AgentCore in AWS Regions where AgentCore Evaluations is available. During preview, AgentCore Optimization targets system prompts and tool descriptions for agents deployed on AgentCore Runtime and using AgentCore Observability and Evaluations. 
 Get started through the AgentCore Console or CLI. Read the documentation and follow step by step tutorials here. 
 About the authors 
 Amandeep Khurana 
 Amandeep Khurana is a Principal Product Manager, working on Amazon Bedrock AgentCore, focusing on agent operations and performance tooling. He’s passionate about building products at the cutting edge of technology and helping customers adopt them to solve their business problems. 
 Nikhil Kandoi 
 Nikhil Kandoi is a Principal Engineer on the AgentCore team. Nikhil brings deep expertise in building and scaling intelligent systems spanning multiple AI services like AWS Lex, Panorama and Amazon Q. Today, he focuses on the challenges of deploying and managing AI agents at enterprise scale that make large-scale agent deployments reliable and secure. 
 Bharathi Srinivasan 
 Bharathi Srinivasan is a Senior Generative AI Data Scientist at AWS. Bharathi works with enterprise customers on large‑scale generative AI challenges, including robustness and verification of non‑deterministic systems, governance of GenAI and agentic AI platforms, and the quality of dynamic agentic AI systems.
```

---

## 13. Agent-guided workflows to accelerate model customization in Amazon SageMaker AI

- 日期: 2026-05-04 17:10
- 链接: https://aws.amazon.com/blogs/machine-learning/agent-guided-workflows-to-accelerate-model-customization-in-amazon-sagemaker-ai/

```
Every organization has access to the same foundation models. The real competitive advantage comes from customizing them with your proprietary data and domain expertise. But getting there is complex, even for experienced teams. It requires mastering fine-tuning techniques like Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), and Reinforcement Learning Verifiable Rewards (RLVR), navigating fragmented APIs and model-specific data formats, designing rigorous evaluations, and managing months-long experiment cycles. 
 Amazon SageMaker AI now offers an agentic experience that changes this. Developers describe their use case using natural language, and the AI coding agent streamlines the entire journey, from use case definition and data preparation through technique selection, evaluation, and deployment. Purpose-built agent skills deliver specialized expertise on fine-tuning applied to your specific use case, data transformation to required formats, quality evaluation using LLM-as-a-Judge metrics, and flexible deployment to Amazon Bedrock or SageMaker AI endpoints. Agent skills for model customization not only boost productivity but also decrease token usage. All generated code is fully editable, producing reusable artifacts that integrate seamlessly into existing workflows. 
 What makes this experience truly powerful is agent Skills for model customization . They are pre-built, modular instruction sets that encode deep AWS and data science expertise across the entire customization lifecycle. When you describe your use case, the AI coding agent activates the relevant skills, guiding it through data preparation and validation, technique selection, hyperparameter configuration, model evaluation, and deployment. Skills provide specialized knowledge about SageMaker AI APIs, ML workflows, best practices, and common patterns, enabling your coding agent to provide more accurate, SageMaker AI-specific guidance, generating ready-to-run notebooks at each step. Skills are fully customizable, so you can modify them to match your team’s workflows, governance standards, and tooling preferences, enabling reproducible organizational best practices, a common challenge with general-purpose coding assistants. 
 Amazon Kiro in SageMaker AI Studio JupyterLab 
 JupyterLab in SageMaker AI includes an integrated agentic development environment support through ACP. By default, Kiro, Amazon’s AI software development agent, is pre-configured in the chat panel , providing AI-powered code completion, debugging assistance, and interactive coding support directly within your JupyterLab environment. When you use coding agents in SageMaker AI JupyterLab, the space automatically loads relevant SageMaker AI model customization Skills into your agent’s context. 
 Additionally, you can configure other Agent Communication Protocol (ACP) compatible coding agents of your choice, such as Claude Code , giving you flexibility to work with the tools that best fit your workflow. ACP-compatible agents can benefit from the same SageMaker AI Skills integration when used within SageMaker AI JupyterLab. While this example shows the integration with JupyterLab, you can also use remote access to your own IDE outside of JupyterLab. 
 Prerequisites 
 Before starting this tutorial, you must have the following prerequisites: 
 An AWS account 
 The ability to access or create a SageMaker AI domain. If you don’t have a SageMaker AI domain, you can create one using the quick setup or manual setup options 
 An AWS IAM role with the required permissions 
 An Amazon Simple Storage Service (Amazon S3) bucket 
 Access to or can create a SageMakerAI Studio JupyterLab compute space . There is no minimum instance type requirement to use the new features. 
 As of this publication, SageMaker AI Distribution image version 4.1 or higher is required on your SageMakerAI Studio JupyterLab. 
 Verify or Attach AmazonSageMakerFullAccess managed policy to your domain’s execution role. Attach the additional inline policy for Lambda, S3 and Bedrock access to the same execution role 
 Your SageMakerAI Studio execution role’s trust policy must allow these three services to assume the role: sagemaker.amazonaws.com, lambda.amazonaws.com, bedrock.amazonaws.com. 
 Skills overview 
 The SageMaker AI agent skills are built conforming with the Agent Skills open format . The agent-guided model customization workflows are powered by nine modular skills that cover the full customization lifecycle: 
 Skill Name Phase Description 
 Use Case Specification Configuration Structured discovery to define business problem, users, and success criteria 
 Planning Discovery Generates a dynamic, multi-step customization plan tailored to your use case 
 Fine-tuning Setup Configuration, Training Selects base model from SageMaker AI Hub and recommends technique (SFT, DPO, or RLVR) 
 Dataset Evaluation Evaluation, Training Validates dataset format and schema before training 
 Dataset Transformation Data Engineering Converts between ML data formats (OpenAI chat, SageMaker AI, Hugging Face, Amazon Nova) 
 Fine-tuning Training Generates training notebooks for SageMaker AI serverless fine-tuning 
 Model Evaluation Evaluation Configures LLM-as-Judge evaluation with built-in and custom metrics 
 Model Deployment Deployment Determines deployment pathway (SageMaker AI endpoint or Bedrock) and generates code 
 The coding agent (Kiro, Claude Code, Cursor, etc.) provides the conversational interface while the SageMaker AI Skills orchestrate the workflow. When you interact with your coding agent, it activates the relevant skills. This allows you to call SageMaker AI APIs, access S3 data sources, and interact with model registries through AWS-provided MCP servers. Jupyter notebooks are generated for you that execute each step of the process into existing ML pipelines. 
 Supported Fine-Tuning Techniques 
 The model customization skills currently support three fine-tuning techniques and recommend the right one during the planning phase based on your use case. 
 Technique Description Best For 
 SFT (Supervised Fine-Tuning) Trains on input/output pairs Task-specific behavior: instruction following, format compliance, domain-adapted responses 
 DPO (Direct Preference Optimization) Trains on preferred vs. rejected outputs Aligning tone, style, and subjective preferences to match human judgement 
 RLVR (Reinforcement Learning with Verifiable Rewards) Trains using code-based reward functions Tasks where correctness can be programmatically verified 
 Solution implementation 
 For this solution, you’ll fine-tune a small language model (SLM) on the FreedomIntelligence/medical-o1-reasoning-SFT dataset to build a clinical reasoning model that walks through medical cases step-by-step before providing a diagnosis. This demonstrates how fine-tuning can specialize a general-purpose model for domain-specific reasoning tasks. If you’d like to try a different use case, SageMaker AI provides a library of sample datasets across techniques like SFT, DPO, and RLVR that you can use as a starting point. 
 Getting started 
 Open or Create a SageMaker AI Space with JupyterLab 
 Navigate to SageMaker AI Studio 
 Go to Spaces in the left navigation panel or click “Customize with agent” from the model hub 
 Either: Click Create Space and select JupyterLab as your application 
 Open an existing Space that includes JupyterLab 
 In this post, we’ll start with using Kiro and switch to Claude Code as our coding agent. To keep using Kiro, move to the Planning Phase section, or move to the next section to see how to use Claude Code in JupyterLab. 
 Start Using Kiro in the Chat Panel: 
 Kiro requires authentication before you can use it. The chat panel will guide you through the authentication process. 
 In JupyterLab, open the chat panel by clicking the chat icon in the right sidebar 
 Type @ to see your available agents 
 Select @Kiro from the agent dropdown. Start asking questions or requesting code assistance. 
 The first time you use Kiro in a space, it will ask you to login. To login, follow the instructions provided by the chat, or follow here: 
 In JupyterLab, open a new terminal: File > New > Terminal 
 Run the following command kiro-cli login --use-device-flow 
 Select one of the 3 login options in the terminal: 
 Use for Free with Builder ID 
 Use for Free with Google or GitHub 
 Use with Pro license 
 Enter a prompt: “I want to customize a model” 
 Configuring Claude Code in JupyterLab 
 SageMaker AI Studio supports implementing additional coding agents using Agent Client Protocol (ACP). Example agents that support ACP include: 
 Claude (via claude-agent-acp) 
 OpenCode (via opencode CLI >= 1.0.0) 
 Gemini (via gemini CLI >= 0.34.0) 
 Codex (via codex-acp) 
 View the JupyterLab user guide for more information on installation steps. 
 To use Claude Code: 
 Install the CLI tool in your SageMaker AI Studio JupyterLab terminal: 
 npm install -g @zed-industries/claude-agent-acp 
 Restart the space by running the command restart-jupyter-server or by restarting the space via the Studio UI. Please note, this will result in any unsaved work or in memory state (like active kernels) being lost. 
 Authenticate with the agent following its specific authentication process 
 Select the agent from the persona dropdown in the JupyterLab chat panel ( @Claude ) 
 Claude Code can be used with most Anthropic subscriptions including configuring Claude Code with Amazon Bedrock on Amazon SageMaker AI Studio. To configure Claude Code to use Claude through Amazon Bedrock follow the prerequisites in the Claude code guide, enabling Bedrock model access and providing your execution role access to bedrock:InvokeModel and bedrock:InvokeModelWithResponseStream . Then, create the following file to configure Claude Code to use Bedrock. 
 ~/.claude/settings.json:
{ 
 "env": { 

 "CLAUDE_CODE_USE_BEDROCK": "1" 
 } 
} 
 Planning phase 
 Upon receiving the user prompt, the coding agent doesn’t immediately begin executing tasks. It enters a planning phase where it identifies and activates the skills necessary to complete the job. In the process, the agent generates a workflow which users can review and modify. From the initial prompt, the agent recognizes two relevant skill domains and activates both the planning skill for structuring the overall workflow and the finetuning-setup skill for configuring the training job. Before generating any code, the agent asks targeted questions about dataset readiness and use case details to inform its technique and evaluation metrics recommendations. 
 Fine-tune in SageMaker AI 
 With multiple model families and fine-tuning techniques available, choosing the right approach for your specific use case can be challenging. The agent analyzes your dataset structure and task requirements to provide tailored model and technique recommendations, helping you avoid costly trial-and-error cycles. SageMaker AI supports serverless customization across Amazon Nova, GPT-OSS, Llama, Qwen, and DeepSeek family of models. For this use case, we chose Qwen3-0.6B because it is cost-effective to train and deploy while being sufficient for domain-specific tasks like medical reasoning. 
 In the chat panel, prompt the agent: “ I want to fine-tune a model for clinical reasoning that walks through medical cases step-by-step before providing a diagnosis. ” 
 Confirm the plan and answer the agent’s follow-up questions. The agent generates a training notebook that will use a SageMaker AI serverless training job with training and validation metrics tracked through integrated SageMakerAI MLflow Apps. 
 Open the notebook, verify the code and run the notebook cells to submit the training job. 
 Monitor the job within your SageMaker AI Studio. 
 The model’s loss will show a steady decrease during training, showing it successfully learned to provide step-by-step clinical reasoning before reaching diagnoses. For a deeper look at the full metric set and per-step breakdowns, we can view more in the MLflow app. 
 Evaluation 
 Once training completes, we need to measure how well the fine-tuned model performs compared to the base model. The agent recommends an evaluation approach based on our use case, or we can specify the metrics we care about, such as accuracy on held-out medical reasoning questions or reward score improvement over the base model. It then generates a notebook in SageMaker AI Studio JupyterLab that runs the evaluation against an evaluation dataset and reports the results, so we can validate the model’s performance. Evaluation results are also distributed to MLflow for comparisons before moving to deployment. 
 Deployment 
 With evaluation complete, the final step is deploying the fine-tuned model for inference. The agent walks us through deployment options across SageMaker AI and Bedrock through Bedrock Custom Model Import , depending on our latency, scaling, and integration requirements. It then generates a notebook in JupyterLab that provisions the endpoint and runs a sample inference request, so we can validate whether the deployed model is ready to serve predictions. 
 Customize skills 
 The skills included with SageMaker AI cover common fine-tuning workflows, but you can also customize existing skills or author new ones to match your organization’s standards and tooling. For example, you might extend the model-evaluation skill to include domain-specific metrics or add a new skill for a custom deployment target. Skills are defined in simple markdown files in the ~/.kiro/skills directory, making them easy to author, version-control, and share across your organization. 
 Conclusion 
 In this post, we walked through the model customization lifecycle using SageMaker AI agent skills. Starting from a single natural language prompt, the agent planned the workflow, configured and ran a SFT fine-tuning job on Qwen3-0.6B, evaluated the results with metrics tailored to our use case, and deployed the fine-tuned model. The agentic model customization experience in Amazon SageMaker AI is available today. You can get started in minutes. Simply launch a JupyterLab space in SageMaker Studio with Kiro and Agent Skills pre-configured, or bring the same Skills into your preferred IDE from GitHub. Describe your use case in natural language, and let the agent guide you from data preparation through evaluation and deployment. 
 What once required months of specialized ML work and deep knowledge can now be completed in days. The expertise is encoded. The workflow is guided. And the code is yours. Get started today by visiting the GitHub repository for the SageMaker AI agent skills plugin and step-by-step guide. Review the documentation to see how SageMaker AI serverless model customization with agent skills can accelerate your path from idea to production models. 
 About the authors 
 Lauren Mullennex 
 Lauren is a Senior GenAI Specialist Solutions Architect at AWS. She has over a decade of experience in ML, DevOps, and infrastructure. She is a published author of a book on computer vision. Outside of work, you can find her traveling and hiking with her two dogs. 
 Sandeep Raveesh 
 Sandeep is a Generative AI Specialist Solutions Architect at AWS. He works with customer through their AIOps journey across model training, generative AI applications like agents, and scaling generative AI use-cases. He also focuses on go-to-market strategies helping AWS build and align products to solve industry challenges in the generative AI space. You can connect with Sandeep on LinkedIn to learn about generative AI solutions. 
 Mike Diamond 
 Mike is a Principal Product Manager for Amazon SageMaker AI. With two decades of experience applying AI to high-stakes domains, Mike is passionate about responsible AI and making machine learning more accessible through agentic workflows and developer-friendly tooling. 
 Joshua Towner 
 Joshua Towner is a Senior Software Engineer at AWS. 
 Bobby Lindsey 
 Bobby Lindsey is a Machine Learning Specialist at Amazon Web Services. He’s been in technology for over a decade, spanning various technologies and multiple roles. He is currently focused on combining his background in software engineering, DevOps, and machine learning to help customers deliver machine learning workflows at scale. In his spare time, he enjoys reading, research, hiking, biking, and trail running. 
 Emily Moeng 
 Emily Moeng is a Language Data Science Manager at AWS with a background in theoretical and experimental linguistics. She specializes in distilling AI/ML objectives into robust, execution-ready pipelines for data curation, annotation, and model evaluation. 
 Vineet Sharma 
 Vineet is a Senior Product Marketing Manager, Tech at AWS, focused on Amazon SageMaker AI. He specializes in go-to-market strategy, product launches, and translating complex AI and ML services into compelling customer value. He is passionate about creating great customer experiences through clear, impactful messaging. Connect with him on LinkedIn .
```

---

## 14. Generate dashboards from natural language prompts in Amazon Quick

- 日期: 2026-05-04 16:51
- 链接: https://aws.amazon.com/blogs/machine-learning/generate-dashboards-from-natural-language-prompts-in-amazon-quick/

```
Building meaningful dashboards demands hours of manual setup, even for experienced BI professionals. Amazon Quick now generates complete multi-sheet dashboards from natural language prompts, taking you from one or more datasets to a production-ready analysis in minutes. Data analysts building recurring operations reports, program managers preparing a leadership review, or engineers exploring a new dataset can describe what they want, and Amazon Quick produces multiple organized sheets with visuals selected for your data, filter controls for stakeholders to explore by different dimensions, and calculated fields such as year-over-year growth and month-over-month comparisons. Before generating, you review and edit an interactive plan of the proposed structure, keeping you in control of the final output. 
 In Amazon Quick, Analysis is the authoring surface where you build and arrange visuals, filters, and calculated fields across multiple sheets. When you’re ready to share, you publish the analysis as a dashboard. This new generative AI capability creates the analysis and you refine and publish it as a dashboard with a single click. 
 In this post, we walk through generating an analysis from a prompt, reviewing the plan, and exploring the completed output. 
 Prerequisites 
 You need the following prerequisites: 
 An AWS account 
 An Amazon Quick Enterprise Edition subscription 
 How it works 
 To generate an analysis, start by selecting the data that you want to analyze. In Amazon Quick, your data is stored in datasets , which connect to sources such as Amazon Redshift, Amazon Simple Storage Service (Amazon S3), or uploaded files. With your dataset ready, you describe what you want to see, review a plan, and generate. 
 Select your datasets 
 Open a dataset in Amazon Quick and choose Generate analysis . You can also start from the Analyses page. Select 1–3 datasets for the analysis. If your data spans multiple tables—orders in one dataset and products in another—you can select them together. 
 Choose Add data to add more datasets if required. 
 Describe what you want in the analysis / dashboard 
 Write a natural language prompt describing the insights you want to author in the Analysis. Describe the business questions, the metrics that you care about, and how you want the information organized across sheets. For example: “Create an operations dashboard showing order volume trends, revenue KPIs, delivery performance comparing estimated vs actual delivery dates, and product category breakdown by revenue and order count. Include calculated fields for total revenue, average order value, and month-over-month order growth.” 
 Amazon Quick analyzes your data 
 Amazon Quick examines your dataset structure and column statistics. You see real-time progress updates as it works: analyzing dataset columns, analyzing column statistics, creating the analysis plan. 
 If you navigate away, use the Analyses → Generations tab to check status and return to the progress screen. 
 Review and edit the plan 
 Amazon Quick presents the Analysis outline in a two-pane view. The left pane shows your initial prompt and a summary of the selected datasets. The right pane shows the proposed structure: filter controls, sheets, and the visuals planned for each sheet. You can generate immediately or choose Edit to refine the plan first — adjusting sheet names, adding or removing visuals, or reorganizing the layout. 
 Generate the analysis 
 Choose Generate . Real-time progress updates show each component being created: calculated fields, filters, and each sheet sequentially. 
 Early access authors across operations, engineering, and data science found this capability a significant time saver, turning what previously took hours of manual configuration into minutes of guided generation. 
 During early access, an author who had never used AI analytics before tested the feature with his first dataset: “The results are awesome and there is no comparison in the time it takes AI to perform analysis and create dashboards vs. a human being.” — Jeff Sondic, Pre-Construction Manager, GES Ops Construction, Amazon, Ontario Canada 
 The output is a native Quick analysis. It works with existing publishing workflows, embedding patterns, continuous integration and continuous delivery (CI/CD) pipelines, and point-and-click editing in the Analysis surface. You can refine every visual after generation. This isn’t a static image. It’s a live, interactive analysis connected to your data. 
 Publish and share as a dashboard 
 When you’re satisfied with the analysis, choose Publish to create a dashboard. You can share the dashboard with other users, embed it in applications within minutes with features like 1-click embedding, or schedule email deliveries. The published dashboard retains all the sheets, visuals, filter controls, and calculated fields from the generated analysis. Recipients interact with the dashboard without access to the underlying analysis. 
 Getting started 
 At launch, Generate Analysis is available to Enterprise subscription/Author Pro users. Authors also have promotional access to this capability through December 2026 as part of Amazon Quick Enterprise, provided their organization has not restricted access. Available in the following AWS Regions: US East (N. Virginia), US West (Oregon), Asia Pacific (Sydney), Asia Pacific (Tokyo), Europe (Frankfurt), Europe (Ireland), and Europe (London). 
 Conclusion 
 Generate Analysis in Amazon Quick creates complete multi-sheet analyses from natural language prompts, reducing dashboard creation from hours to minutes. During early access, authors across operations, engineering, and data science reported reducing their dashboard creation time by 90% or more. 
 One author said: “As a new user, creating this dashboard would have taken at least a full day. It took 5 minutes.” — Prabhakant Rasal, SDE-III, PXT DLS Tech, Amazon, Dallas TX 
 AI builds your starting point. You refine and publish it as a dashboard. Dashboards encode the questions your team needs to answer repeatedly. For the follow-up explorations and one-off questions that arise in between, try Dataset Q&A to query your data directly in natural language. 
 About the authors 
 Sindhu Chandra 
 Sindhu Chandra is a Senior Tech Product Marketing Manager at AWS, leading go-to-market strategy for Amazon Quick. With 15+ years across Amazon, Uber, and Google, she’s passionate about making tech marketing relatable, inclusive, and grounded in real customer value. Outside work, she enjoys playing with her dog, and brewing coffee from different origins. 
 Rushabh Vora 
 Rushabh Vora is a Principal Product Manager for Amazon Quick at Amazon Web Services, where he leads generative AI capabilities for data analysis and visualization. Rushabh focuses on enabling organizations to transform raw datasets into actionable insights through natural language, reducing the time from data to decision from hours to minutes. He is passionate about making data exploration and dashboard creation accessible to every business user, regardless of technical expertise. 
 Salim Khan 
 Salim Khan is a Senior Worldwide Generative AI Solutions Architect for Amazon Quick at AWS. He has over 16 years of experience implementing enterprise business intelligence solutions. At AWS, Salim works with customers globally to design and implement AI-powered BI and generative AI capabilities on Amazon Quick. Prior to AWS, he worked as a BI consultant across industry verticals including Automotive, Healthcare, Entertainment, Consumer, Publishing, and Financial Services, delivering business intelligence, data warehousing, data integration, and master data management solutions.
```

---

## 15. From data lake to AI-ready analytics: Introducing new data source with S3 Tables in Amazon Quick

- 日期: 2026-05-04 16:12
- 链接: https://aws.amazon.com/blogs/machine-learning/from-data-lake-to-ai-ready-analytics-introducing-direct-query-with-s3-tables-in-amazon-quick/

```
Organizations today are increasingly looking to combine analytics and AI to accelerate insights and decision-making. Amazon Quick , a unified agentic AI-powered analytics and decision intelligence service, brings together data visualization, natural language interaction, and agent-driven automation in a single, governed experience. With this, business users can explore data, generate insights, and take action without requiring specialized machine learning (ML) expertise. 
 At the same time, modern data architectures are evolving toward scalable data lakes built on open table formats such as Apache Iceberg, which offer improved performance, cost efficiency, and governance. However, analyzing large-scale data often requires moving it into data warehouses or OLAP systems, introducing latency, added cost, and operational complexity. Although existing query modes—such as Direct Query and SPICE ( Super-fast, Parallel, In-memory Calculation Engine ) with data warehouses —address most analytics needs, customers continue to seek a more seamless way to analyze large, real-time datasets directly from their data lakes. 
 To address this, Amazon Quick introduces Amazon S3 Tables (Apache Iceberg tables) as a new data source. With this feature, customers can directly query and visualize Apache Iceberg tables stored in an Amazon S3 table bucket without the need for intermediate data layers. This approach provides additional architectural choice especially when customers are requiring to reduce data movement, improve performance, and maintain a secure, governed single source of truth. 
 In this post, we explore how Amazon Quick and S3 Tables work together to enable near real-time analytics and streamline modern data architectures. 
 Benefits of directly connecting with S3 Tables: 
 Direct Query and SPICE modes for S3 Tables , a new Amazon Quick feature, enables direct consumption of Apache Iceberg tables in Amazon S3 table bucket without requiring intermediate query layers. This feature is beneficial for enterprise looking to implement modern data architecture using Apache Iceberg open table format to treat their data lake as a “central source of truth,” enabling high-performance analytics without complex data pipeline and the overhead of moving data between disparate systems. 
 Key benefits include: 
 Streamlined architecture 
 Removes the need for separate data warehouses or OLAP layers by enabling direct querying of data in the data lake, reducing operational complexity and infrastructure overhead. 
 Near real-time insights 
 Minimizes data movement and pipeline dependencies, ensuring dashboards and analytics reflect the most current data available. 
 Scalable performance 
 Supports querying large-scale datasets stored in Amazon S3 table bucket without requiring data curation, replication, or size constraints—enabling seamless scalability. 
 Solution overview 
 With this new launch, Amazon Quick now supports querying data lakes using either SPICE or Direct Query mode. In this post, we focus on Direct Query mode, though you can choose SPICE mode when creating your dataset. 
 This solution enables near real-time analytics and decision-making for AnyCompany Corp., a global financial services organization handling card transactions across multiple regions. Transaction data is generated from diverse sources, including point-of-sale systems, mobile banking apps, IoT-enabled payment devices, and online gateways. To address the need for fraud detection, approval rate monitoring, and fast access to actionable insights, the solution uses a combination of streaming data ingestion, open table format data lakes, and AI-powered analytics. 
 Transaction events are streamed into Amazon Kinesis Data Streams and delivered using Amazon Data Firehose into an Amazon S3 table bucket. With the native S3 Tables connector of Quick, business users can query the data lake in near real-time and analyze data using natural language interactions, removing dependency on batch processing. You can use this unified approach to uncover insights such as regional fraud trends and approval rates instantly, improving operational visibility and supporting faster, data-driven decisions. 
 Architecture overview 
 The architecture is composed of four core layers: data ingestion, storage, querying, and analytics. For this post, we focus on the query and analytics layer. Transaction events from distributed payment systems are ingested in real-time using Amazon Kinesis Data Streams, providing a scalable, low-latency streaming layer. These events are continuously delivered to an Amazon S3 table bucket in Apache Iceberg format, forming a high-performance data lake that supports both streaming and analytical workloads. While data could traditionally be queried through Amazon Athena, Amazon Quick allows direct, near real-time querying of S3 Tables and enables AI-powered, natural language analysis. Business users can explore live datasets, generate visualizations, and obtain insights—such as identifying regions with high fraud rates in the last hour—without technical expertise. This architecture keeps decisions informed by the most current data, supporting rapid and accurate business actions. 
 Prerequisites 
 To follow along with this post, ensure that you have the following in place: 
 Your steaming pipeline including data ingestion and storage layers are already set up and your data is available in an Amazon S3 table bucket. 
 An Amazon Quick Enterprise subscription. 
 Implementation steps 
 Here are the steps to give your business users access to your Apache Iceberg tables using Amazon Quick analytical and conversational workloads: 
 Step 1: Enable S3 Tables data access for Amazon Quick 
 Let’s start by configuring Amazon Quick to access S3 Tables, so they can be automatically discovered when building the data source. 
 Select your account name in the top-right corner and select Manage account . 
 In the left navigation menu, under Permissions , choose AWS Resources . 
 In the Allow access and auto discovery for these resources section, select Amazon S3 Tables . 
 Choose Select S3 table buckets , then choose the relevant S3 table bucket containing the sample data for this blog and click Finish . (For this post, we use the s3table-datasamples bucket.) 
 Ensure that the Amazon S3 bucket option is selected, then choose Save . 
 This step adds required permission to your Amazon Quick role and allows your Amazon Quick instances to successfully discover the specific S3 table bucket data while creating a data source. 
 Step 2: Create an Amazon Quick data source using S3 Tables 
 Now, let’s create an Amazon Quick data source pointing to the s3table-datasamples bucket. This bucket contains two tables: customer dimension and transaction_events . The customer dimension table is file-based and includes fictional bank customer information, while transaction_events represents fictional streaming credit card transaction data associated with those customers. 
 Choose Amazon Quick in the top-left corner to navigate to the Quick home page. 
 From the menu, select Datasets , then go to the Data sources tab and choose Create data source . 
 On the next screen, select Amazon S3 Tables (Apache Iceberg tables) as the data source type, then choose Next . 
 Enter a data source name (for example, CustomerTrxn-S3Tables ) and provide the S3 table bucket ARN. In this example, it’s the ARN for the s3table-datasamples bucket. 
 Choose Create data source . 
 Verify that the data source has been created successfully. 
 Step 3: Build a dataset in Amazon Quick 
 In this step, we use the data source created earlier to build a dataset. 
 Select the data source ( CustomerTrxn-S3Tables ) created in the previous step and choose Create dataset . 
 Choose the namespace automatically populated for your data source, then select a table from the list and click Edit/Preview data . 
 In this example, the s3table-data namespace contains two tables. We begin with the customer dimension table. 
 In the Preview tab, review the data pulled from S3 Tables. 
 To add another table, select Add data from the menu. In this example, we will add the transaction_events table. 
 In the Add data screen, select Data source from the dropdown list. 
 Choose CustomerTrxn-S3Tables from the Select a data source list, and then choose Select . 
 From the list of tables, select transaction_events and choose Select . 
 Join the two tables by selecting the plus (+) icon next to the customer_master table and selecting Join . 
 Configure the join using the customer_id column: Select the Inner Join option. 
 Choose transaction_events as the right table. 
 Select customer_id from both the left and right tables as the join keys. 
 Provide a name for the join (for example, TrxnJoin) to help identify it when working with multiple tables. 
 Name the dataset in the top-left corner (for example, CxTrxn_S3TableData). 
 Ensure that Direct Query mode is selected in the top-right corner. This is important to fully use near real-time data access from S3 Tables. Alternatively, you can choose SPICE mode if you prefer scheduled data refreshes rather than near real-time access. 
 Choose Save & Publish . 
 Step 4: Interact with the dataset using Amazon Quick chat 
 Now let’s start chatting with this dataset to gather insights using natural language. For this, we use the default chat named, “My Assistant.” 
 In the Amazon Quick home page, choose Chat agents on the left navigation panel and then My Assistant . 
 Choose Chat next to the My Assistant . 
 From All data and apps , choose Add and select Datasets . Then select the CxTrxn_S3TableData dataset. Choose Save. 
 In the chat panel, enter “ Show the total number of transactions occurred so far in this month ” and press Send . 
 Notice the chat response showing the total transaction count for the current month. Next, let’s ask the agent to break it down by day. 
 In the chat panel, enter “ break it down by day using ingestion timestamp ” and press Send . 
 Review the daily breakdown provided by the agent. In our example, from April 1–April 17. 
 Step 5: Demonstrate real-time user interaction with streaming data 
 Next, we test the near real-time responsiveness of the chat by streaming new transaction data. In this demo, we use AWS Lambda as a producer for a Kinesis Data Stream and then store the incoming data in an S3 table bucket as S3 Tables – in Apache Iceberg format using Firehose. As new data is streamed in, the transaction counts will automatically update within the chat without the end user needing to take any action. This demonstrates seamless near real-time data access without manual intervention or complex architecture. We run this Lambda function a few times to stream new transactional events data. 
 If you’re interested in creating your own streaming source for this demo, you can refer to the official AWS documentation or relevant AWS posts for detailed guidance. 
 Now let’s check the recently streamed data in our chat agent. 
 Navigate back to My Assistant in the same chat session , enter a new prompt “Show the total number of transactions occurred so far in this month, include all recent streaming data and break it down by ingestion timestamp.” and press Send . 
 My Assistant queries the CxTrxn_S3TableData dataset via Direct Query and returns the newly ingested records for April 18. This demonstrates that the recently streamed data is available without requiring a manual dataset refresh. 
 Cleanup 
 If you no longer need the resources deployed as part of this solution and want to avoid ongoing costs, we recommend that you clean up and remove the relevant components by deleting all Amazon Quick–related resources and unsubscribing from your Amazon Quick account. 
 Conclusion 
 In this post, we explored how Amazon Quick’s new Amazon S3 Tables data source enables near real-time analytics while streamlining modern data architectures. By querying Apache Iceberg tables directly in Amazon S3, it removes intermediate layers, reduces data movement, and preserves a single, governed source of truth. Additionally, you can use natural language chat experiences, like My Assistant , to access up-to-date insights effortlessly, without manual refreshes or technical overhead. 
 The result is a unified, AI-powered analytics experience where data, insights, and actions come together seamlessly in near real-time. Organizations can move faster, make better decisions, and unlock the full value of their data—while keeping architectures simpler, more scalable, and cost-efficient. If your use case is a typical analytical scenario sourced from scheduled data refreshes and does not require near real-time access, SPICE mode remains a suitable option. For more details on this feature, see Creating a dataset using Amazon S3 Tables . 
 For additional discussions and help getting answers to your questions, check out the Amazon Quick Community . 
 About the authors 
 Raji Sivasubramaniam is a Principal Solutions Architect at AWS, specializing in Agentic AI. She focuses on helping Fortune 100 and 500 organizations globally implement end-to-end enterprise solutions across Agentic AI, business intelligence, data management, and advanced analytics. Raji brings deep expertise in healthcare, with extensive experience navigating diverse datasets—including managed markets, physician targeting, and patient analytics—to drive high-impact, data-driven decision-making. 
 Emily Zhu is a Senior Product Manager at Amazon Quick, responsible for the full structured data stack — spanning governed and enterprise-scale data architecture, high-performance analytical and conversational query engines, and the semantic and ontology layer that gives data real meaning at scale. She’s passionate about how a strong data strategy unlocks AI strategy, and is on a mission to make the structured data stack the foundation for conversational and analytical experiences across Quick Suite. 
 Priya Kakarla is a Specialist Solutions Architect focused on modern analytics and AI-driven solutions, with experience across industries including healthcare, finance, and digital-native organizations. She is passionate about helping organizations unlock value from their data through scalable, intuitive, and agentic-driven approaches. Known for a strong customer-first mindset, Priya is dedicated to delivering tailored, innovative solutions that align with business goals and drive measurable outcomes. Outside of work, she enjoys traveling, exploring diverse cuisines, and spending time with family and friends.
```

---

## 16. Introducing Dataset Q&A: Expanding natural language querying for structured datasets in Amazon Quick

- 日期: 2026-05-04 16:08
- 链接: https://aws.amazon.com/blogs/machine-learning/introducing-dataset-qa-expanding-natural-language-querying-for-structured-datasets-in-amazon-quick/

```
Every BI team knows this bottleneck: a business user has a question that falls outside existing dashboards, so they file a ticket. An analyst writes the query, validates the results, and delivers them—hours or days later. Multiply that by hundreds of ad-hoc requests per month, and the backlog becomes the single biggest constraint on data team productivity. 
 Amazon Quick now adds a powerful new natural language query capability, Dataset Q&A , to remove this bottleneck. Your question is translated into SQL, run against the full dataset, and the results are returned in seconds—no row sampling, topic curation, or pre-configured calculated fields required. 
 Quick already offers two natural language querying modes. Dashboard Q&A is intended for questions about data visualized in published dashboards, drawing on the business context that authors have built into each view. Topic Q&A goes further. Authors enrich the data model with business-friendly field names and synonyms, so users can query a curated set of fields in plain language. Dataset Q&A now completes the picture. Users can explore any dataset directly, going beyond what an author has pre-configured, while all the security, permissions, and governance that enterprises expect from Quick remain fully enforced. 
 While the industry has raced to ship text-to-SQL demos, the real challenge in enterprise BI has never been generating SQL. The challenge is grounding ambiguous business language against complex schemas, enforcing security at every step, and explaining what the system did and why. The agentic system of Quick is purpose-built for this. The model must resolve lexical ambiguity— does “volume” mean row count, revenue, or units shipped? —and map colloquial business language to the precise column names and calculations in the dataset, without a predefined dictionary. Before any query runs, the system searches across all your structured assets (dashboards, datasets, and topics) using a semantic graph that understands how your assets relate to each other. This lets it find the right source even when your question doesn’t use the exact name of a dataset or column. After the source is identified, the system peeks into the data for context like sample values and distributions and uses author-provided field descriptions and business context to disambiguate before using one of the three capabilities available for generating SQL. 
 This launch also introduces Dataset Enrichment , a streamlined way for authors to ground the system in business context for a single dataset with no topic configuration required. If the business context already exists outside of Quick (in a data catalog, a modeling tool, or a team wiki), authors can upload it directly as a file against the dataset. Field descriptions, intended relationships across fields, custom instructions about specific columns or the dataset as a whole, all of it can be provided in industry-standard formats (YAML, JSON) or as plain-text instructions. The system applies this context automatically to every query, so an author defines it once and every user benefits at scale. 
 Trust requires transparency. With this launch, we also introduce Chat Explainability . For any intermediate step involved in answering a natural language query, the system now gives users mechanisms to explore what happened under the hood. When structured data capabilities are invoked, users see step-by-step reasoning behind each answer—the generated SQL, the assumptions the agent made, filters it applied, and a plain-language explanation for non-technical stakeholders. There is no black box. 
 In this post, you learn how to get started with Dataset Q&A, explore real-world use cases with hands-on examples, and discover advanced capabilities like auto-discovery across all your data assets and multi-dataset querying in a single conversation. 
 Solution overview 
 Dataset Q&A lets any user ask a question in plain natural language, and the system generates SQL, executes it against the full dataset, and returns an answer in seconds. Results are aggregated by design, and every query automatically respects the row-level security (RLS) and column-level security (CLS) you have already configured — no additional setup required. 
 Key benefits include: 
 Analyze millions of rows – Query the complete dataset without row sampling or data caps. 
 Query beyond dashboard – Ask about fields and dimensions that aren’t in any existing dashboard. 
 Start querying immediately – No setup overhead required. Begin exploring your data without creating topics or dashboards. 
 Explore multi-part questions – Combine filters, calculations, and aggregations in a single natural language query. 
 Inspect the generated SQL – Verify query logic, validate accuracy, or learn how the system interpreted your question. 
 Understand how questions are interpreted – Review step-by-step reasoning behind each answer, including the assumptions made and filters applied, before sharing results with stakeholders. 
 Walkthrough 
 In the following walkthrough, we demonstrate Dataset Q&A using a real-world dataset of bicycle rental trips from a city bike-sharing network. To follow along and replicate the steps in your own environment, make sure that you have the following in place: 
 An AWS account. For setup instructions, see Getting Started with AWS. 
 Amazon Quick Enterprise Edition enabled in your account with at least one Enterprise user and Professional user. For details, see Amazon Quick Sight editions and pricing . 
 Familiarity with Amazon Quick Sight concepts such as datasets and the chat interface. See the Amazon Quick Sight documentation to get started. 
 For a sample dataset, this walkthrough uses the publicly available last four months of the 2025 Divvy bike trip dataset , which contains bike-sharing trip records from Chicago. Download the files and create a Quick Sight dataset . You can use the append option to combine multiple files. For more details, see the new data preparation experience in the Quick Sight documentation or this YouTube video . 
 Note: Because the underlying model might phrase or format responses differently across sessions, the exact wording and visual layout of answers may vary from what is shown here. However, the data values and query results should be consistent when using the same question and dataset. 
 Step 1: Connect to your data 
 To use Dataset Q&A in the chat experience, complete the following steps: 
 In Amazon Quick, choose the Open chat icon in the top-right navigation. 
 My Assistant appears as the default system chat agent. 
 Access the knowledge picker from the chat footer and choose Add within Specific data and apps. 
 In Add Quick assets, choose Datasets and select the Divvy_Bike_Trips dataset. 
 Choose Save . 
 With the Divvy_Bike_Trips dataset selected, enter questions in the chat interface. 
 To begin, try a dataset discovery question: Can you describe the structure of this dataset? 
 The Quick chat responds with a detailed breakdown of the dataset structure, explaining what information is captured in each column, describes the available fields and their purpose. 
 Dataset Q&A capabilities can be invoked for both SPICE and direct query datasets including Amazon Redshift, Amazon Athena, Amazon Aurora PostgreSQL and Amazon Simple Storage Service (S3) Tables. 
 Step 2: Explore the dataset 
 After connecting to the Divvy_Bike_Trips dataset, you can explore the data through a series of natural language questions. The following examples show how Dataset Q&A handles increasing complexity while maintaining conversational context. 
 Example 1: Analyze trip patterns 
 Start with a general exploration of trip patterns across months: 
 How many rides do we have for every month in 2025 from September until December?” 
 Your question is translated into a structured SQL query. Results appear in a table visual, including a key observations section and suggested next steps. This query analyzed all 1,857,960 rides in the dataset. Dataset Q&A has no row limits for direct query datasets, so aggregations reflect the complete dataset. For SPICE datasets, the aggregations are subject to SPICE capacity . 
 Example 2: Provide context to guide the model 
 The dataset contains two timestamp fields: started_at (when the ride began) and ended_at (when the ride concluded). When no context is provided, Quick Chat uses started_at as the logical default for grouping trips by month. To analyze by end time instead, add context to your question: 
 “How many rides do we have for every month in 2025 from September until December? Use the ended_at timestamp to determine the month.” 
 The Quick Chat understands the context and ended_at is used for the month grouping in the response. 
 Example 3: Inspect the generated SQL 
 To inspect the SQL that Quick Sight generates, use the Explainability feature available in the chat response. This displays step-by-step reasoning behind each answer, including the generated SQL, so you can verify how the system interpreted your question. 
 “How many rides do we have for every month in 2025 from September until December?” 
 The SQL query appears in the response, showing ended_at used from the previous context, so you can verify that the interpretation is correct. 
 Example 4: Ask multiple questions at once 
 You can explore the data with multiple questions in a single prompt: 
 How many bike rides are there? 
 How many trips by bike type? 
 How many trips by members? 
 Individual SQL queries are run for each question, and a combined summary is returned. 
 Example 5: Combine advanced calculations 
 The next query asks two questions at once, both requiring metrics computed at runtime rather than stored in the dataset. 
 “What percentage of total trips does each member type account for in September 2025, and what is the average ride duration in minutes? Use a dual axis visual with the axis starting at 0.” 
 In the preceding response, the avg_duration_minutes and percentage_of_total_trips are runtime calculations that do not exist in the underlying dataset. You can also instruct Quick on the visual type and axis configuration to use for representing the results.The following SQL query is automatically generated by Quick in response to the natural language question above. It calculates the share of total trips and average ride duration for each rider type in September 2025, using window functions and date arithmetic: 
 SELECT
"member_casual",
COUNT(*) AS trip_count,
ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS percentage_of_total_trips,
ROUND(AVG(date_diff('second', "started_at", "ended_at")) / 60.0, 2) AS avg_duration_minutes
FROM "Divvy_Bike_Trips"
WHERE "ended_at" >= '2025-09-01 00:00:00'
AND "ended_at" < '2025-10-01 00:00:00'
GROUP BY "member_casual"
ORDER BY trip_count DESC 
 Key components of this query: 
 Window Function: SUM(COUNT(*)) OVER () calculates total trips across all rider types for percentage calculation. 
 Percentage Calculation: COUNT(*) * 100.0 / SUM(COUNT(*)) OVER () computes each group’s share of total trips. 
 Duration Calculation: AVG(DATEDIFF(‘minute’, started_at, ended_at)) calculates average trip duration in minutes. 
 Filtering: Limits data to September 2025 (from September 1 to before October 1). 
 Grouping: Groups by member_casual to separate member and casual riders. 
 Ordering: Sorts by total trips in descending order. 
 Working with multiple datasets and spaces 
 Dataset Q&A isn’t limited to a single dataset. Whether you manually select a dataset, add multiple datasets, or curate a Space with mixed asset types, The built-in enterprise knowledge graph identifies the right source of data based on its interpretation of your question. 
 Adding a single dataset 
 The previous walkthrough demonstrated how to connect a single dataset through the knowledge picker and explore it with natural language questions. This is the most straightforward starting point for Dataset Q&A. 
 Adding multiple datasets 
 You can add multiple datasets to the knowledge picker and ask questions that span your data landscape. When multiple datasets are selected, the Quick Chat automatically routes each question to the most relevant dataset based on the question context and available schema. 
 Example scenario: A transportation analyst has access to both the Divvy bike trip dataset and a Chicago weather dataset. By selecting both datasets in the knowledge picker, they can ask: 
 “What was the total number of bike trips in September 2025?” (routes to Divvy dataset) 
 “What were the average temperatures in September 2025?” (routes to weather dataset) 
 “Show me bike trip volumes and weather patterns for each month” (analyzes both datasets separately and presents combined insights) 
 Auto-discovery with All data and apps 
 You don’t even need to know which datasets are available. In Quick Chat, the knowledge picker provides an option to select All data and apps. When selected, you can ask a question and the system discovers the relevant datasets automatically, runs queries across them, and generates a unified response. 
 Curating a Space for cross-asset analysis 
 For the most comprehensive experience, organize related assets together using Amazon Quick Spaces. A Space is a collection of files, datasets, dashboards, and knowledge bases. Example scenario: A “Transportation Analytics” space might contain the Quick Sight Divvy bike trips dataset, a Chicago weather dataset, city infrastructure reports in PDF and event calendar in word formats, and existing Quick Sight transportation dashboards. 
 After this space is selected in the knowledge picker, you can ask questions that draw from all assets within it: 
 “How did weather patterns affect bike ridership in September?” (combines Divvy bike trip dataset with the Chicago weather dataset) 
 “What major events occurred during peak ridership weeks?” (references event calendar documents) 
 “Compare bike-sharing usage with public transit ridership trends” (analyzes multiple datasets) 
 The Quick Chat automatically identifies which assets contain relevant information and synthesizes insights across structured data (datasets) and unstructured content (documents). 
 Use cases 
 The following examples represent four common patterns where Dataset Q&A delivers the most value. 
 Pattern 1: Progressive complexity without reconfiguration 
 What we demonstrated: Starting with monthly aggregations, the walkthrough showed progressively more complex questions, from defining custom metrics (average trip duration) to performing nested aggregations (percentage by member type), all without any setup or configuration changes. 
 Real-world scenario: A business analyst exploring sales data can start by asking “What were total sales last quarter?” and naturally move to “What percentage of revenue came from repeat customers in each region, and how did their average order value compare to new customers?” without waiting for a dashboard update. 
 Why this matters: Dataset Q&A supports iterative exploration where each question builds on the previous one, with context maintained throughout the conversation. 
 Benefit: Natural analytical workflow that matches how analysts think through problems. 
 Pattern 2: SQL Transparency with explainability for technical validation 
 What we demonstrated: For every query in the walkthrough, the generated SQL was available on demand, from straightforward aggregations to nested aggregations with window functions. With this transparency, we can verify that natural language was correctly interpreted before sharing results. 
 Real-world scenario: A data engineer must confirm that “What is the average order value for repeat customers who made purchases in both Q3 and Q4 2025?” correctly identifies repeat customers (those with orders in both quarters, not just either quarter) before sharing the result with executives. 
 With Dataset Q&A, technical users can: 
 Understand how natural language questions are interpreted and executed through the Explainability feature. 
 Review the generated query logic. 
 Verify complex conditions such as AND vs. OR logic, date ranges, and aggregation levels. 
 Request adjustments if the interpretation doesn’t match the intent. 
 Validate the approach before sharing results with stakeholders. 
 Benefit: Confidence in results, ability to explain methodology, and technical credibility. 
 Pattern 3: Complete dataset analysis 
 What we demonstrated: Every query accessed the complete underlying dataset. The monthly analysis processed all 1,857,960 rides. The September percentage calculations aggregated across 714,562 rides. No sampling or truncation occurred. 
 Real-world scenario: An operations manager analyzing customer support tickets needs resolution patterns across all tickets from the past year. A question like “What percentage of tickets were resolved within SLA by priority level and support tier?” requires complete data for accurate insights. 
 Dataset Q&A queries the complete underlying dataset with SQL, delivering accurate aggregations across millions of records without sampling or truncation. 
 Benefit: Complete, accurate results for data-driven decision-making 
 Pattern 4: Multi-asset analysis 
 What this demonstrates: Dataset Q&A works when multiple datasets or a space with mixed assets (datasets + documents) are in scope, enabling holistic analysis across organizational data. 
 Real-world scenario: A transportation planner must understand how bike-sharing usage correlates with public transit ridership and city events. They created a “Transportation Analytics” Space containing: 
 Divvy bike trip dataset (structured data) 
 CTA transit ridership dataset (structured data) 
 City events calendar (PDF document) 
 Weather data (CSV file) 
 With this space selected, they can ask: “What was the impact of major events on bike and transit usage in October 2025?” 
 The conversational assistant: 
 Identifies relevant structured data from bike trip and transit datasets 
 Extracts event information from the PDF calendar 
 Correlates weather patterns from the CSV file 
 Synthesizes insights across all sources 
 Why this matters: Organizations rarely make decisions based on a single dataset. Dataset Q&A with Spaces enables analysis across data silos without manual data integration or complex ETL processes. 
 Benefit: Holistic, context-aware insights that reflect the full complexity of business operations. 
 Key distinctions 
 Dataset Q&A opens up one-time exploration beyond pre-configured boundaries. It provides access to any field with custom runtime calculations in natural language, plus full SQL transparency for technical validation. 
 Dashboard Q&A works well when exploring insights within the boundaries of what dashboard authors have configured, including specific visuals, fields, filters, and curated business logic with calculations. 
 Topic Q&A shines when authors have created and maintained topic configurations with curated field definitions, synonyms, and custom instructions. 
 Supported data sources 
 Supported data sources are Amazon Athena, Amazon Redshift, Amazon Aurora PostgreSQL, and Amazon S3 Tables in direct query mode for Dataset Q&A at this time. 
 Current limitations 
 Composite datasets are not supported when the parent datasets use SPICE and the child dataset is in direct query mode. 
 Custom SQL datasets with parameters are currently not supported. 
 Cleaning up 
 To avoid incurring ongoing charges, delete the Divvy_Bike_Trips dataset that you created as part of this walkthrough. For instructions, see Deleting a dataset in the Amazon Quick documentation. 
 Conclusion 
 Dataset Q&A for datasets in Quick Sight within Amazon Quick removes the barriers between business questions and data insights. It gives analysts the flexibility to go beyond pre-configured dashboard boundaries, gives technical users the SQL transparency to validate complex logic, and gives everyone access to complete datasets without row limits. 
 This capability complements existing Dashboard Q&A and Topic Q&A features, giving you the right tool for every analytical scenario: curated insights when you need guardrails, and flexible exploration when your questions extend beyond pre-configured visualizations. 
 About the authors 
 Koushik Muthanna Koravanda Ganapathy 
 Koushik Muthanna Koravanda Ganapathy is a Specialist Solutions Architect for Amazon Quick at AWS. He helps customers design, implement, and scale Quick across their organization, from architecture to everyday use. 
 Emily Zhu 
 Emily Zhu is a Senior Product Manager at Amazon Quick, responsible for the full structured data stack — spanning governed and enterprise-scale data architecture, high-performance analytical and conversational query engines, and the semantic and ontology layer that gives data real meaning at scale. She’s passionate about how a strong data strategy unlocks AI strategy, and is on a mission to make the structured data stack the foundation for conversational and analytical experiences across Quick Suite. 
 Suren Raju 
 Suren Raju is a Senior Specialist Solutions Architect for GenAI at AWS, where he architects cutting-edge AI solutions with a focus on Amazon Quick. He brings deep expertise in structured data connectors, data prep, datasets, and data modeling, alongside his work with Amazon Quick’s multi-agentic workflows, orchestrations, and unstructured data integration through knowledge bases and action connectors. His innovative approach to AI-driven solutions helps organizations democratize data access and unlock transformative business value across the full spectrum of their data landscape. 
 Priya Mysore 
 Priya Mysore is a Senior Worldwide GenAI Specialist at AWS, with over two decades of experience in data and analytics. She is passionate about helping customers unlock the true potential of their data using AI/ML and agentic capabilities in Amazon Quick. Priya excels at empowering business users to harness data through self-service analytics and intelligent automation. She guides organizations in implementing AI-driven solutions that democratize data access and automate complex workflows, enabling users to uncover actionable insights and drive business value. Her deep expertise in business intelligence and agentic AI drives innovative solutions that meet the evolving needs of AWS customers.
```

---

## 17. Capacity-aware inference: Automatic instance fallback for SageMaker AI endpoints

- 日期: 2026-05-04 16:05
- 链接: https://aws.amazon.com/blogs/machine-learning/capacity-aware-inference-automatic-instance-fallback-for-sagemaker-ai-endpoints/

```
As organizations scale generative AI workloads in production, securing reliable GPU compute has become one of the most persistent operational challenges. Large language models (LLMs) and multimodal architectures demand specific instance types and when that capacity isn’t available, endpoints fail before they serve a single request. 
 Building a real-time inference endpoint on Amazon SageMaker AI has meant committing to a single instance type at creation time. When that type had insufficient capacity, the endpoint failed to reach a running state. You updated your configuration, selected a different instance type, and retried repeating the cycle until a provisioning attempt succeeded. 
 Today, Amazon SageMaker AI introduces capacity aware instance pool for new and existing inference endpoints. You define a prioritized list of instance types, and SageMaker AI automatically works through your list whenever capacity is constrained at creation, during scale-out, and during scale-in. Your endpoint provisions on available AI Infrastructure without manual intervention. This capability is available for Single Model Endpoints, Inference Component-based endpoints, and Asynchronous Inference endpoints. 
 This post walks through how instance pools work and how to get started, whether you’re creating a new endpoint or migrating an existing one. 
 The problem 
 When you deploy a model to a SageMaker AI inference endpoint whether real-time or asynchronous, you specify a single instance type. If that type doesn’t have available capacity, the endpoint fails to create. This limitation appears at every stage of the endpoint lifecycle. 
 Endpoint creation fails on capacity. When your preferred instance type isn’t available, SageMaker AI returns an Insufficient Capacity error. Getting to a running endpoint requires manually iterating through alternatives, with each attempt consuming significant time before you know the outcome. 
 Autoscaling can’t grow the fleet. When a scale-out event triggers and your instance type has insufficient capacity, the autoscaler retries the same type indefinitely. Traffic continues to increase while your endpoint stays at its current size. 
 Scale-down has no priority awareness. With a single instance type, there’s no concept of preferred compared to fallback hardware. Every instance is a candidate for removal without distinction. 
 Observability is aggregated, not actionable. Amazon CloudWatch metrics roll up at the endpoint level. When investigating a latency or capacity issue, the metrics indicate that something is wrong but not which instance type is the cause. 
 How it works: Priority-based instance pools 
 You define a ranked list of instance types called instance pools in your endpoint configuration. SageMaker AI works through that list automatically whenever capacity is constrained. 
 Your endpoints come up. SageMaker AI tries your first-choice instance type. If capacity isn’t available, it immediately tries your second choice, then your third. There’s no manual retry required. Your endpoint reaches InService on the first available AI infrastructure in minutes. 
 Your endpoints stay up. When auto scaling triggers and your preferred instance type is constrained, SageMaker AI scales out on the next available type in your priority list, so traffic keeps flowing. 
 Your fleet trends toward preferred hardware. During scale-in, SageMaker AI removes your lowest-priority (fallback) instances first. On subsequent scale-out events, it again tries your highest-priority type first. As your preferred hardware becomes available, your fleet naturally shifts back toward it over time and no manual intervention is required. 
 You see everything. Every existing CloudWatch metric now includes an InstanceType dimension, so you can track latency, throughput, GPU utilization, and instance count per instance type within a single endpoint. 
 To learn more, see the Amazon SageMaker AI documentation and explore the sample notebook on GitHub . 
 The right model for each instance type 
 Fallback instance types often differ in GPU memory, compute capability, and architecture. A model optimized for a high-memory multi-GPU instance won’t necessarily run on a smaller single-GPU fallback. There are two ways to match each instance type in your pool list to a correctly configured model. 
 Option 1: Bring your own optimized models 
 If you already know your instance type targets, prepare model artifacts for each. For your primary high-end instance, you might use tensor parallelism across multiple GPUs. For a mid-tier fallback, you might apply speculative decoding to accelerate inference. For your lowest-priority fallback, you might use INT4 quantization to fit within a smaller memory budget. 
 Create a separate SageMaker AI model for each configuration and reference it using ModelNameOverride in each InstancePools entry (for Single Model Endpoints) or in per-instance-type Specifications (for InferenceComponent-based endpoints). When SageMaker AI falls back to a lower-priority pool, it deploys the model that you prepared for that hardware. 
 Option 2: Use SageMaker AI inference recommendations 
 If you’d rather not optimize each hardware target manually, SageMaker AI inference recommendations can generate hardware-specific configurations for you. Provide your base model and SageMaker AI produces optimized configurations across your target instance types using techniques like speculative decoding and quantization. 
 The recommendation job returns one result per target instance type. Each result includes a ModelPackageArn and an InferenceSpecificationName in the AIRecommendationModelDetails response, identifying the configuration for that specific hardware. You create one SageMaker AI model per result using both fields, then reference each using ModelNameOverride in its corresponding pool entry—the same pattern as Option 1, with the service handling the optimization work. 
 MODEL_PACKAGE_ARN = "arn:aws:sagemaker:us-west-2:123456789012:model-package/MyModelPkgGroup/1"
 
# Create one model per instance type using both fields from AIRecommendationModelDetails.
sm.create_model(
 ModelName="my-llm-for-p5",
 PrimaryContainer={
 "ModelPackageName": MODEL_PACKAGE_ARN,
 "InferenceSpecificationName": "p5-48xlarge-optimized",
 },
 ExecutionRoleArn="arn:aws:iam::123456789012:role/SageMakerRole",
)
sm.create_model(
 ModelName="my-llm-for-g6",
 PrimaryContainer={
 "ModelPackageName": MODEL_PACKAGE_ARN,
 "InferenceSpecificationName": "g6-48xlarge-optimized",
 },
 ExecutionRoleArn="arn:aws:iam::123456789012:role/SageMakerRole",
)
# Then reference each via ModelNameOverride per pool entry — see Setting up below. 
 Auto scaling on a mixed fleet 
 Auto scaling follows the same priority logic that you define at creation time. Scale-out tries your highest-priority pool first, falling back to the next pool if capacity is unavailable. Scale-in removes your lowest-priority instances first, preserving your preferred hardware as the fleet contracts. 
 Building a weighted scaling metric 
 Because your fleet contains instance types with different throughput capacities, default aggregated metrics can misrepresent actual usage. Consider a p5 instance handling 18 concurrent requests alongside a g6 handling 7 averaging those raw numbers to 12.5 doesn’t accurately reflect the load on either type. 
 You can now use CloudWatch metric math to build a weighted metric based on per-type utilization ratios . Each term divides a type’s observed concurrency by its maximum capacity, producing a value between 0.0–1.0. Averaging those ratios gives a fleet-level usage signal on the same 0.0–1.0 scale as TargetValue . Setting TargetValue to 0.7 means: scale out when the weighted average exceeds 70 percent of capacity across all instance types in the fleet. 
 aas = boto3.client("application-autoscaling")
 
aas.put_scaling_policy(
 PolicyName="weighted-utilization-scaling",
 ServiceNamespace="sagemaker",
 ResourceId="endpoint/my-heterog-endpoint/variant/primary",
 ScalableDimension="sagemaker:variant:DesiredInstanceCount",
 PolicyType="TargetTrackingScaling",
 TargetTrackingScalingPolicyConfiguration={
 "TargetValue": 0.7, # scale out above 70% weighted fleet utilization
 "CustomizedMetricSpecification": {
 "Metrics": [
 {
 "Id": "p5_concurrency",
 "MetricStat": {
 "Metric": {
 "Namespace": "AWS/SageMaker",
 "MetricName": "ConcurrentRequestsPerModel",
 "Dimensions": [
 {"Name": "EndpointName", "Value": "my-heterog-endpoint"},
 {"Name": "VariantName", "Value": "primary"},
 {"Name": "InstanceType", "Value": "ml.p5.48xlarge"},
 ],
 },
 "Stat": "Average",
 },
 "ReturnData": False,
 },
 {
 "Id": "g6_concurrency",
 "MetricStat": {
 "Metric": {
 "Namespace": "AWS/SageMaker",
 "MetricName": "ConcurrentRequestsPerModel",
 "Dimensions": [
 {"Name": "EndpointName", "Value": "my-heterog-endpoint"},
 {"Name": "VariantName", "Value": "primary"},
 {"Name": "InstanceType", "Value": "ml.g6.48xlarge"},
 ],
 },
 "Stat": "Average",
 },
 "ReturnData": False,
 },
 {
 "Id": "weighted_utilization",
 # Utilization ratio per type: observed / max_capacity, then averaged
 "Expression": "(p5_concurrency / 20 + g6_concurrency / 8) / 2",
 "ReturnData": True,
 },
 ],
 },
 },
) 
 In this expression, 20 and 8 are the maximum concurrency values measured for each instance type. A p5 handles up to 20 requests and a g6 handles up to 8 in this example. Replace these values with the maximums you measure for your model during load testing. The following table shows how the metric responds at different traffic levels: 
 Traffic level p5 requests g6 requests Weighted utilization Action 
 Low 5 2 (0.25 + 0.25) / 2 = 0.25 Scale in 
 Moderate 12 5 (0.60 + 0.63) / 2 = 0.61 Hold 
 High 18 7 (0.90 + 0.88) / 2 = 0.89 Scale out 
 At target 14 6 (0.70 + 0.75) / 2 = 0.73 Near target — hold 
 Note : For workloads where all instance types have similar throughput capacity, your existing scaling policy works without modification. The weighted usage metric is most valuable when pool members differ significantly in GPU capacity. 
 Monitoring your fleet 
 All existing CloudWatch metrics now include a new InstanceType dimension: ModelLatency , ConcurrentRequestsPerModel , GPUUtilization , InstanceCount , and InvocationsPerInstance —broken down by hardware type within a single endpoint. You can build dashboards and alarms that track each instance type independently. 
 DescribeEndpoint returns the current instance count per pool, so you always know your fleet composition: 
 response = sm.describe_endpoint(EndpointName="my-heterog-endpoint")
pools = response["ProductionVariants"][0]["InstancePools"]

Example output:
 [
 {"InstanceType": "ml.p5.48xlarge", "CurrentInstanceCount": 4},
 {"InstanceType": "ml.g6.48xlarge", "CurrentInstanceCount": 2},
] 
 Traffic routing 
 For endpoints with instance pools, we recommend enabling Least Outstanding Requests (LOR) routing by setting RoutingConfig in your ProductionVariant . LOR routes each incoming request to the instance with the fewest in-flight requests per model copy. Because higher-capacity instances process requests faster, they drain their queues more quickly and maintain lower in-flight counts at steady state. This means that they naturally receive proportionally more traffic without any manual weight configuration: 
 "RoutingConfig": {"RoutingStrategy": "LEAST_OUTSTANDING_REQUESTS"} 
 Without this setting, the endpoint defaults to RANDOM routing, which distributes requests evenly regardless of instance load. This is less optimal when pool members differ significantly in throughput capacity. For full details, see RoutingConfig in the ProductionVariant API reference. 
 Updates and rollbacks 
 Both blue/green and rolling deployments are supported. 
 Blue/green deployments provision a complete new (green) fleet using the same priority-based fallback logic before shifting traffic. If health checks pass, traffic cuts over. If they fail, automatic rollback preserves your blue fleet and your endpoint stays InService throughout. 
 Rolling deployments update your fleet in configurable batches (5–50 percent of instances at a time), requiring less additional capacity than a full blue/green fleet—particularly valuable for large models or GPU instance types in high demand. SageMaker AI applies the priority-based fallback logic when provisioning each new batch. If a CloudWatch alarm trips during a baking period, traffic rolls back automatically. See Use rolling deployments for configuration details. 
 Prerequisites 
 Before you get started, make sure that you have: 
 An AWS account with sagemaker:CreateEndpointConfig , sagemaker:CreateEndpoint , and sagemaker:UpdateEndpoint IAM permissions 
 At least one SageMaker model with artifacts in Amazon S3 
 Boto3 version 1.43.1 or later (for InstancePools support in the Python SDK) 
 (Optional) Separate optimized model artifacts per target instance type, or a ModelPackage from SageMaker AI inference recommendations 
 Instance pool support for SageMaker AI inference endpoints is available in all commercial AWS Regions. You can get started through the AWS Management Console, AWS Command Line Interface (AWS CLI), or AWS SDK. 
 Workflow to configure endpoints with instance pool 
 There are two ways you can configure the instance pool: for new Amazon SageMaker AI endpoint or with your existing Amazon SageMaker AI endpoint. 
 If you’re creating a new endpoint, below diagram explains the workflow: 
 Choose your instance types and assign priorities (1 is highest). 
 Prepare an optimized model for each instance type, or run SageMaker AI inference recommendations to generate them. 
 Create an endpoint configuration with InstancePools listing your priorities. 
 Create the endpoint. SageMaker AI handles capacity resolution automatically. 
 Set up per-type CloudWatch monitoring using the new InstanceType dimension. 
 If you’re migrating an existing endpoint below diagram explains the workflow: 
 Create a new endpoint configuration: replace InstanceType with InstancePools , keeping your current instance type at Priority: 1 . 
 Call UpdateEndpoint , your endpoint stays InService during the blue/green transition. 
 Optionally add a weighted utilization scaling metric if your fallback instance types differ significantly in throughput capacity. 
 Setting up 
 Adopting instance pools requires one field change to your endpoint configuration: replace the single InstanceType field in your ProductionVariant with an InstancePools list. Your model, scaling policies, and monitoring dashboards continue to work without modification. 
 Migrating an existing endpoint 
 Before: single instance type: 
 import boto3
sm = boto3.client("sagemaker")
 
sm.create_endpoint_config(
 EndpointConfigName="my-config",
 ProductionVariants=[{
 "VariantName": "primary",
 "ModelName": "my-llm",
 "InitialInstanceCount": 2,
 "InstanceType": "ml.g6e.48xlarge", # single type — no capacity fallback
 }],
) 
 After: priority-ordered instance pools: 
 sm.create_endpoint_config(
 EndpointConfigName="my-config-v2",
 ProductionVariants=[{
 "VariantName": "primary",
 "ModelName": "my-llm",
 "InitialInstanceCount": 2,
 "VariantInstanceProvisionTimeoutInSeconds": 1200, # see note below
 " InstancePools ": [
 {"InstanceType": "ml.g6e.48xlarge", "Priority": 1}, # your current type
 {"InstanceType": "ml.g6.48xlarge", "Priority": 2}, # same family, first fallback
 {"InstanceType": "ml.p4d.24xlarge", "Priority": 3}, # broader fallback
 ],
 }],
) 
 Your endpoint stays InService during the blue/green transition. 
 sm.update_endpoint(
 EndpointName="my-endpoint",
 EndpointConfigName="my-config-v2",
) 
 Note : VariantInstanceProvisionTimeoutInSeconds is a new field introduced with instance pool support. It sets the total window for procuring instances from a pool: SageMaker AI continues retrying on Insufficient Capacity errors within this window and moves to the next pool after the timeout expires. The valid range is 300–3600 seconds. 1200 seconds is a reasonable starting value for large GPU instance types. This timer covers instance procurement only, model download and container startup time are governed separately by the existing ModelDataDownloadTimeoutInSeconds and ContainerStartupHealthCheckTimeoutInSeconds fields. To deploy a different optimized model per instance type, add ModelNameOverride to any pool entry. You can see the model configuration options in the previous section. 
 InferenceComponent-based endpoints 
 sm.create_inference_component(
 InferenceComponentName="my-ic",
 EndpointName="my-heterogeneous-endpoint",
 VariantName="primary",
 Specifications=[
 {
 "InstanceType": "ml.p5.48xlarge",
 "ModelName": "my-model-p5-optimized",
 "ComputeResourceRequirements": {
 "NumberOfAcceleratorDevicesRequired": 8,
 "MinMemoryRequiredInMb": 65536,
 },
 },
 {
 " InstanceType ": "ml.g6.48xlarge",
 "ModelName": "my-model-g6-optimized",
 "ComputeResourceRequirements": {
 "NumberOfAcceleratorDevicesRequired": 8,
 "MinMemoryRequiredInMb": 32768,
 },
 },
 ],
 RuntimeConfig={"CopyCount": 4},
) 
 Asynchronous inference endpoints 
 Instance pools work the same way for Asynchronous Inference endpoints. Add an AsyncInferenceConfig block to your CreateEndpointConfig call alongside your InstancePools definition—the priority-based provisioning and fallback logic applies identically. This is particularly useful for asynchronous workloads that scale down to zero instances: when the endpoint scales back up to process queued requests, SageMaker AI provisions using your highest-priority available pool first, giving you resilient cold-start behavior without manual intervention. 
 Conclusion 
 Amazon SageMaker AI Instance Pools let you define a prioritized list of instance types for your inference endpoints, and SageMaker AI automatically manages capacity based on that order. 
 During endpoint creation, scale-out, and scale-in, SageMaker AI works through your preferred instance types so you do not have to manually retry deployments when your first-choice hardware is unavailable. Getting started is simple: replace InstanceType with InstancePools in your endpoint configuration and call UpdateEndpoint. Your existing models, autoscaling policies, and monitoring dashboards continue to work without major changes. 
 With per-instance-type CloudWatch metrics and detailed pool counts from DescribeEndpoint, you also get a clear, real-time view of which instance types are powering your fleet. Whether you are optimizing cost, handling GPU capacity constraints, or building resilient asynchronous pipelines that can cold start from zero, Instance Pools give you the flexibility and automation to keep ML inference running smoothly with less operational overhead. 
 This capability is available today at no additional cost. You incur charges for the actual instance types provisioned at the same rates as a standard single-type endpoint. To learn more, see the Amazon SageMaker AI documentation and explore the sample notebook on GitHub . 
 About the authors 
 Kareem Syed-Mohammed 
 Kareem Syed-Mohammed is a Product Manager at AWS. He is focuses on enabling Gen AI model development and governance on SageMaker HyperPod. Prior to this, at Amazon Quick Sight, he led embedded analytics, and developer experience. In addition to Quick Sight, he has been with AWS Marketplace and Amazon retail as a Product Manager. Kareem started his career as a developer for call center technologies, Local Expert and Ads for Expedia, and management consultant at McKinsey. 
 Dmitry Soldatkin 
 Dmitry Soldatkin is a Worldwide Leader for Specialist Solutions Architecture, SageMaker Inference at AWS. He leads efforts to help customers design, build, and optimize GenAI and AI/ML solutions across the enterprise. His work spans a wide range of ML use cases, with a primary focus on Generative AI, deep learning, and deploying ML at scale. He has partnered with companies across industries including financial services, insurance, and telecommunications. You can connect with Dmitry on LinkedIn . 
 Johna Liu 
 Johna Liu is a Software Development Engineer on the Amazon SageMaker team, where she builds and explores AI/LLM-powered tools that enhance efficiency and enable new capabilities. Outside of work, she enjoys tennis, basketball and baseball. 
 Xu Deng 
 Xu Dengis a Software Engineer Manager with the SageMaker team. He focuses on helping customers build and optimize their AI/ML inference experience on Amazon SageMaker. In his spare time, he loves traveling and snowboarding. 
 Mona Mona 
 Mona Mona currently works as Sr AI/ML specialist Solutions Architect at Amazon. She worked in Google previously as Lead generative AI specialist. She is a published author of two books Natural Language Processing with AWS AI Services: Derive strategic insights from unstructured data with Amazon Textract and Amazon Comprehend and Google Cloud Certified Professional Machine Learning Study Guide. She has authored 19 blogs on AI/ML and cloud technology and a co-author on a research paper on CORD19 Neural Search which won an award for Best Research Paper at the prestigious AAAI (Association for the Advancement of Artificial Intelligence) conference.
```

---

## 18. AWS Transform now automates BI migration to Amazon Quick in days

- 日期: 2026-05-01 18:29
- 链接: https://aws.amazon.com/blogs/machine-learning/aws-transform-now-automates-bi-migration-to-amazon-quick-in-days/

```
Migrating to Amazon Quick doesn’t have to mean starting from scratch. Your dashboards encode hard-won domain knowledge: calculated fields your analysts perfected, layouts your executives rely on every Monday morning, security rules tuned to your org chart. You want AI-powered insights and serverless scale, but you’re staring at hundreds of dashboards and a migration estimate measured in months. Now you can significantly accelerate your migration to Amazon Quick, potentially reducing timelines from months to days. 
 In this post, we walk through the full journey, from setting up your migration workspace in AWS Transform to subscribing to partner agents through AWS Marketplace to unlocking Amazon Quick capabilities that change how your organization consumes data. 
 The real cost of staying on legacy BI 
 If you’re running a legacy BI tool, you face compounding pressures that go beyond licensing fees: 
 You’re spending time on servers instead of analytics. Patching, scaling, and monitoring infrastructure takes effort away from the insights work that drives business value. Amazon Quick is serverless and fully managed, so there’s no capacity planning and no maintenance windows. 
 Traditional BI tools require custom engineering for AI-powered answers. Amazon Quick includes native AI capabilities that your teams can use to ask business questions in natural language and automate workflows directly from dashboards. 
 Your analysts wait too long for answers. Provisioning capacity, managing extracts , and troubleshooting performance creates bottlenecks. The Quick Sight SPICE in-memory engine delivers sub-second query performance at scale, and you can publish dashboards directly into your own applications using its embedded analytics APIs. 
 The case for modernization is clear. The question is how to do it without breaking what already works. To learn more about what Amazon Quick offers, see Getting Started with Amazon Quick . 
 AWS Transform, an AI-powered service built to accelerate enterprise modernization, now answers that how for BI migration. Organizations already use AWS Transform to modernize mainframe applications, transform Windows and SQL Server workloads, migrate VMware environments, and modernize custom applications. Now, the same agentic AI platform extends to BI migration. Wavicle Data Solutions, an AWS Advanced Consulting Partner, integrates the EZConvertBI agents directly into AWS Transform, bringing deep Tableau and Power BI migration expertise for accelerating your cloud journey. 
 How it works: A two-step, chat-based migration 
 In AWS Transform, you create a workspace and launch migration jobs through a conversational interface. For BI migration, Wavicle provides four specialized agents available for purchase through AWS Marketplace: one Analyzer agent and one Converter agent for each BI migration source ( Power BI and Tableau ). 
 Together, these agents deliver a guided, chat-based, AWS-native migration experience. Everything runs within your own AWS account: no data ever leaves your environment, no separate tools to procure, and no external data transfers to approve. This removes the security and procurement friction that typically slows migration projects. 
 Regardless of your source BI tool, the migration follows the same two-step process:In the Analyze step, the analyzer agent connects to your existing BI environment, extracts metadata only, cataloging dashboards, datasets, calculations, and dependencies across your workspaces, and generates a migration readiness assessment. The assessment includes a compatibility report that shows what will convert cleanly and what might require attention. It helps teams understand migration scope before proceeding.In the Convert step, you identify the dashboards to migrate and start a conversion job. The Converter agent rebuilds assets in Amazon Quick Sight, including datasets, calculated fields (both at the dataset and analysis level), visualizations and charts, filters, and parameters. This preserves the analytical logic that your teams spent years developing in your BI tool. 
 The agents use Amazon Bedrock, a fully managed service that provides the underlying AI capabilities needed for migration automation. Amazon Bedrock AgentCore (a secure runtime for hosting and managing AI agents) provides the execution environment, handling credential management through workload identities and AWS Identity and Access Management (IAM)-based access control. The domain expertise comes from Wavicle’s deep BI migration experience encoded into the agent logic. 
 Architecture overview 
 The solution is built on the following AWS-native services: 
 AWS Transform is a collaborative enterprise IT transformation workbench powered by expert agents, agentic AI systems, and continuous learning that accelerates cloud migration, legacy app modernization, and tech debt reduction. It provides the orchestration layer with a conversational interface powered by Amazon Bedrock, so you can create and manage migration jobs through chat, track progress across workspaces, and coordinate across teams. 
 Amazon Bedrock AgentCore serves as the secure runtime environment, managing agent execution, credential storage through workload identities, and IAM-based access control. 
 Amazon Quick Sight acts as the target BI service, offering serverless scalability, SPICE in-memory engine performance, and native integration with AWS data services. 
 Amazon Simple Storage Service (Amazon S3) stores validation reports and migration artifacts for audit and review purposes. 
 Your migration journey 
 Here’s what the full experience looks like, from first selection to migrated dashboards in Amazon Quick Sight: 
 Step 1: Complete the prerequisites on your source BI 
 Before running your first migration, you must prepare your source BI tool so the agent can read your dashboard metadata: 
 For Power BI : Configure workspace access and service principal authentication so the agent can read your Power BI tenant metadata. For instructions, see Power BI Prerequisites. 
 For Tableau : Enable the Metadata API on your Tableau Server and generate a Personal Access Token (PAT) for authenticated API access. For instructions, see Tableau Prerequisites. 
 Step 2: Set up AWS Transform and Subscribe through AWS Marketplace 
 Follow the steps in this interactive demo. 
 AWS Transform provides the orchestration layer for your entire migration. It deploys specialized AI agents that automate assessments, dependency mapping, and transformation planning. Everyone works in the same shared workspace, collaborating in real time, tracking progress, and managing the migration from start to finish. Because AWS Transform executes tasks in parallel, you can convert hundreds of dashboards simultaneously without sacrificing quality or control. 
 Step 3: Analyze your BI dashboards 
 Follow the steps in this Power BI Analyzer agent interactive demo or Tableau Analyzer agent interactive demo . 
 The comprehensive analysis report captures complexity across various dimensions such as number of data sources, analytical calculations, consumption nuances like conditional rules, and cross-dashboard dependencies. This allows migration project managers to define a migration execution plan based on priority and utility of the dashboards, even before committing to additional resources. 
 Step 4: Convert your BI dashboards 
 Follow the steps in this Power BI Convertor agent interactive demo or Tableau Convertor agent interactive demo. 
 The Converter agent rebuilds your selected dashboards in Amazon Quick: datasets with mapped data sources and data types, calculated fields at both the dataset and analysis level, visualizations with preserved chart types and formatting, and filter controls with parameter inputs. Throughout the conversion, you can monitor progress directly in the AWS Transform chat interface. 
 After the conversion completes, you receive your Quick Sight assets and can begin the final validation and go-live process. 
 After migration: From converted to production-ready 
 The migration agent delivers your converted assets: Quick Sight datasets and analyses, including calculated fields, visuals, controls, and parameters. These are the building blocks. What comes next, governance, validation, and publishing, is owned by your team. This deliberate handoff helps maintain quality and clear accountability.Note: The assessment report flags components that might need manual refinement after migration, such as parameters, custom SQL, tool-specific calculations, and third-party visuals. There are no surprises at this stage. 
 For Quick admin: Assign ownership and configure governance 
 As Quick Sight administrator (the role configured in the Quick Sight connector), you assign ownership of each migrated dashboard to the appropriate BI authors.User authentication and directory structures in your source BI tool rarely map one-to-one to Amazon Quick Sight. For example, Tableau environments often rely on Active Directory groups, while Power BI uses workspace-level service principals. The migration agent transfers the analytical assets, not the access controls. You must manually configure user permissions, row-level security (RLS), and sharing settings in Quick Sight to match your organization’s requirements. For enterprises with complex directory hierarchies, plan for this as a distinct workstream. 
 This step establishes clear accountability: who owns each dashboard’s accuracy, who maintains it, and who controls access. Nothing goes live until permissions are properly configured. 
 For Quick authors: Validate and accept 
 You receive the assigned dashboards and own UAT. This means verifying that visualizations, calculated fields, filters, and interactivity match the source through side-by-side metric comparison, testing drill-downs and dashboard actions, and confirming layout consistency. Because the migration agent doesn’t carry over permissions or row-level security, consider verifying that the right users can access the right data in Quick Sight. BI authors know their dashboards better than automated tools do. The agent gets the structure across. Your team confirms the substance is right. 
 Publish and go live 
 After validation, Quick authors publish their dashboards: configuring sharing permissions, setting up email subscriptions, and setting up embedding if needed. For larger migrations, you can learn more about Amazon Quick Sight asset deployment APIs to automate permission assignments and dashboard distribution at scale. At that point, the original source dashboards can be archived. 
 With your dashboards live in Amazon Quick, your teams unlock capabilities that weren’t possible with your legacy BI tool: natural language queries, automated analysis across enterprise data sources, and data-driven actions directly from dashboards. 
 Get started 
 You’ve seen the full journey, from Marketplace subscription to production-ready dashboards. Here’s how to take the first step: 
 Explore the Power BI to Quick Sight Agents and Tableau to Quick Sight Agents . 
 Access user guide and interactive demo on Wavicle Data Solutions website. 
 Contact your AWS account team to discuss your migration requirements and explore available programs for free or discounted Amazon Quick migrations. 
 Whether you’re migrating 10 dashboards or 10,000, AWS Transform gives you a governed, repeatable path to Amazon Quick. Combined with Amazon Bedrock AI capabilities and Wavicle’s migration expertise, your team can stop managing BI infrastructure and start getting insights faster. And because AWS Transform is the one place to go for all your modernization needs, you can use the same workbench for your next modernization challenge.You have invested years in your dashboards. Now bring them to Amazon Quick in days and start asking questions your legacy BI tool could never answer. 
 About the authors 
 Ahil Gunasekaran is a Sr. Solutions Architect and Software Engineering Competency Lead at Wavicle Data Solutions, where he leads the design and delivery of generative AI and agentic frameworks. With over a decade of experience spanning solution architecture, product engineering, data engineering, and cloud modernization, he has designed and architected data products and accelerators, reusable frameworks, complex platforms across lakehouse, streaming, and BI domains. 
 Anantha Choppalli is a Chief Architect at Wavicle Data Solutions, with deep expertise in delivering Data and AI solutions. Over two decades, he has led large-scale cloud and analytics transformation programs across Retail, Manufacturing and Travel and Hospitality, helping enterprises migrate and modernize their technology landscape on AWS. 
 Rajesh Rathod leads product management and go-to-market strategy for AWS Transform at Amazon Web Services. 
 Srikanth Baheti is a Senior Manager for Amazon Quick Sight. He started his career as a consultant and worked for multiple private and government organizations. Later he worked for PerkinElmer Health and Sciences & eResearch Technology Inc, where he was responsible for designing and developing high traffic web applications and highly scalable and maintainable data pipelines for reporting platforms using AWS services and serverless computing. 
 Taher Paratha is a Sr. Software Engineer in AI/ML at Wavicle Data Solutions, where he leads the development of multiple products and accelerators. With over 6 years of experience across data science, machine learning, and AI engineering, he specializes in building agentic applications, generative AI solutions, and machine learning systems. 
 Vasha Bhatari is a Senior Product Manager at Amazon Quick Sight, where she drives solutions that simplify BI migrations and help customers modernize analytics with ease. Since joining Amazon in 2017, she has led initiatives across last-mile routing optimization, database migration, and business intelligence, bringing broad experience to complex data challenges. Outside of work, Vasha is always planning her next trip, trying new foods, and exploring the best hiking and kayaking spots across the Pacific Northwest. 
 Venky Hosur is a Senior Partner Solutions Architect at AWS. With over 20 years of experience architecting enterprise cloud and data solutions, he works closely with AWS partners to design and deliver innovative cloud solutions that drive measurable customer outcomes. Venky leads multiple partner-facing initiatives focused on education and enablement, helping partners build transformative capabilities for their customers. His deep expertise in cloud, AI, and data makes him a trusted advisor for organizations modernizing their most critical workloads. 
 Ying Wang is a Senior Specialist Solutions Architect in the Generative AI organization at AWS, specializing in Amazon Quick and Amazon Q to support large enterprise and ISV customers. She brings 16 years of experience in data analytics and data science, with a strong background as a data architect and software development engineering manager. As a data architect, Ying helped customers design and scale enterprise data architecture solutions in the cloud. In her role as an engineering manager, she enabled customers to unlock the power of their data through Quick Sight by delivering new features and driving product innovation from both engineering and product perspectives.
```

---

## 19. Reinforcement fine-tuning with LLM-as-a-judge

- 日期: 2026-04-30 20:07
- 链接: https://aws.amazon.com/blogs/machine-learning/reinforcement-fine-tuning-with-llm-as-a-judge/

```
Large language models (LLMs) now drive the most advanced conversational agents, creative tools, and decision-support systems. However, their raw output often contains inaccuracies, policy misalignments, or unhelpful phrasing—issues that undermine trust and limit real-world utility. Reinforcement Fine‑Tuning (RFT) has emerged as the preferred method to align these models efficiently, using automated reward signals to replace costly manual labeling. 
 At the heart of modern RFT is reward functions. They’re built for each domain through verifiable reward functions that can score LLM generations through a piece of code (Reinforcement Learning with Verifiable Rewards or RLVR) or with LLM-as-a-judge, where a separate language model evaluates candidate responses to guide alignment (Reinforcement Learning with AI Feedback or RLAIF). Both these methods provide scores to the RL algorithm to nudge the model to solve the problem at hand. In this post, we take a deeper look at how RLAIF or RL with LLM-as-a-judge works with Amazon Nova models effectively. 
 Why RFT with LLM‑as‑a-judge compared to generic RFT? 
 Reinforcement Fine-Tuning can use any reward signal, straightforward hand‑crafted rules (RLVR), or an LLM that evaluates model outputs (LLM-as-a-judge or RLAIF). RLAIF makes alignment far more flexible and powerful, especially when reward signals are vague and hard to craft manually. Unlike generic RFT rewards that rely on blunt numeric scoring like substring matching, an LLM judge reasons across multiple dimensions—correctness, tone, safety, relevance—providing context-aware feedback that captures subtleties and domain-specific nuances without task-specific retraining. Additionally, LLM judges offer built-in explainability through rationales (for example, “Response A cites peer-reviewed studies”), providing diagnostics that accelerate iteration, pinpoint failure modes directly, and reduce hidden misalignments, something static reward functions can’t do. 
 Implementing LLM-as-a-judge: Six critical steps 
 This section covers the key steps involved in designing and deploying LLM-as-a-judge reward functions. 
 Select the judge architecture 
 The first critical decision is selecting your judge architecture. LLM-as-a-judge offers two primary evaluation modes: Rubric-based (point- based) judging and Preference-based judging , each suited to different alignment scenarios. 
 Criteria Rubric-based judging Preference-based judging 
 Evaluation method Assigns a numeric score to a single response using predefined criteria Compares two candidate responses side-by-side and selects the superior one 
 Quality measurement Absolute quality measurements Relative quality through direct comparison 
 Preferred used when Clear, quantifiable evaluation dimensions exist (accuracy, completeness, safety compliance) Policy model should explore freely without reference data restrictions 
 Data requirements Only requires careful prompt engineering to align the model to reward specifications Requires at least one response sample for preference comparison 
 Generalizability Better for out-of-distribution data, avoids data bias Depends on quality of reference responses 
 Evaluation style Mirrors absolute scoring systems Mirrors natural human evaluation through comparison 
 Recommended starting point Start here if preference data is unavailable and RLVR unsuitable Use when comparative data is available 
 Define your evaluation criteria 
 After you’ve selected your judge type, articulate the specific dimensions that you want to improve. Clear evaluation criteria are the foundation of effective RLAIF training. 
 For Preference-based judges: 
 Write clear prompts explaining what makes one response better than another. Be explicit about quality preferences with concrete examples. Example: “Prefer responses that cite authoritative sources, use accessible language, and directly address the user’s question.” 
 For Rubric-based judges: 
 We recommend using Boolean (pass/fail) scoring for rubric-based judges. Boolean scoring is more reliable and reduces judge variability compared to fine-grained 1–10 scales. Define clear pass/fail criteria for each evaluation dimension with specific, observable characteristics. 
 Select and configure your judge model 
 Choose an LLM with sufficient reasoning capability to evaluate your target domain, configured through Amazon Bedrock and called using a reward AWS Lambda function. For common domains like math, coding, and conversational capabilities, smaller models can work well with careful prompt engineering. 
 Model tier Preferred for Cost Reliability Amazon Bedrock model 
 Large/Heavyweight Complex reasoning, nuanced evaluation, multi-dimensional scoring High Very High Amazon Nova Pro, Claude Opus, Claude Sonnet 
 Medium/Lightweight General domains like math or coding, balanced cost-performance Low-Medium Moderate-High Amazon Nova 2 Lite, Claude Haiku 
 Refine your judge model prompt 
 Your judge prompt is the foundation of alignment quality. Design it to produce structured, parseable outputs with clear scoring dimensions: 
 Structured output format – Specify JSON or parseable format for straightforward extraction 
 Clear scoring rules – Define exactly how each dimension should be calculated 
 Edge case handling – Address ambiguous scenarios (for example, “If response is empty, assign score 0”) 
 Desired behaviors – Explicitly state behaviors to encourage or discourage 
 Align judge criteria with production evaluation metrics 
 Your reward function should mirror the metrics that you will use to evaluate the final model in production. Align your reward function with production success criteria to enable models designed for the correct objectives. 
 Alignment workflow: 
 Define production success criteria (for example, accuracy, safety) with acceptable thresholds 
 Map each criterion to specific judge scoring dimensions 
 Validate that judge scores correlate with your evaluation metrics 
 Test the judge on representative samples and edge cases 
 Building a robust reward Lambda function 
 Production RFT systems process thousands of reward evaluations per training step. Build a resilient reward Lambda function to help provide training stability, efficient compute usage, and reliable model behavior. This section covers how to build a reward Lambda function that’s resilient, efficient, and production ready. 
 Composite reward score structuring 
 Don’t rely solely on LLM judges. Combine them with fast, deterministic reward components that catch obvious failures before expensive judge evals: 
 Core components 
 Component Purpose When to use 
 Format correctness Verify JSON structure, required fields, schema compliance Always – catches malformed outputs immediately. Cheap and instant feedback. 
 Length penalties Discourage overly verbose or terse responses When output length matters (for example, summaries) 
 Language consistency Verify responses match input language Critical for multilingual applications 
 Safety filters Rule-based checks for prohibited content Always – prevents unsafe content from reaching production 
 Infrastructure readiness 
 Implement exponential backoff: Handles Amazon Bedrock API rate limits and transient failures gracefully 
 Parallelization strategy : Use ThreadPoolExecutor or async patterns to parallelize judge calls across rollouts to reduce latency 
 Avoid Lambda cold start delays: Set an appropriate Lambda timeout (15 minutes recommended) and provisioned concurrency (~100 for typical setups) 
 Error handling: Add comprehensive error handling that returns neutral/noisy rewards (0.5) rather than failing the entire training step 
 Test your reward Lambda function for resilience 
 Validate judge consistency and calibration: 
 Consistency : Test judge on the same samples multiple times to measure score variance (should be low for deterministic evaluation) 
 Cross-judge comparison: Compare scores across different judge models to identify evaluation blind spots 
 Human calibration: Periodically sample rollouts for human review to catch judge drift or systematic errors 
 Regression testing: Create a “judge test suite” with known good/bad examples to regression test judge behavior 
 RFT with LLM-as-a-judge – Training workflow 
 The following diagram illustrates the complete end-to-end training process, from baseline evaluation through judge validation to production deployment. Each step builds upon the previous one, creating a resilient pipeline that balances alignment quality with computational efficiency while actively preventing reward hacking and supporting production-ready model behavior. 
 Real-world case study: Automating legal contract review 
 In this section, we refer to a real-world use case with a leading legal industry partner. The task is to generate comments on risks, assessments, and actions on legal documentation with respect to the policies and previous contracts as reference documents. 
 Challenge 
 Partner was interested in solving the problem of automating the process of reviewing, assessing, and flagging risks in legal contract documents. Specifically, they wanted to evaluate potential new contracts against internal guidelines and regulations, past contracts, and laws of the country pertaining to the contract. 
 Solution 
 We formulated this problem as one where we are providing a target document (the “contract” that needs evaluation), and a reference document (the grounding document and context) and expect the LLM to generate a JSON with multiple comments, comment types, and recommended actions to take based on the assessment. The original dataset available for this use case was relatively small that included complete contracts along with annotations and comments from legal experts. We used LLM as a judge using GPT OSS 120b model as the judge and a custom system prompt during RFT. 
 RFT workflow 
 In the following section we cover details of the key aspects in the RFT workflow for this use case. 
 Reward Lambda function for LLM-as-a-judge 
 The following code snippets present the key components of the reward Lambda function. 
 Note : name of Lambda function should have “SageMaker”, for example, "arn:aws:lambda:us-east-1:123456789012:function:MyRewardFunction SageMaker " 
 a) Start with defining a high-level objective 
 # Contract Review Evaluation - Unweighted Scoring
You are an expert contract reviewer evaluating AI-generated comments. Your PRIMARY objective is to assess how well each predicted comment identifies issues in the TargetDocument contract clauses and whether those issues are justified by the Reference guidelines. 
 b) Define the evaluation approach 
 ## Evaluation Approach
For each sample, you receive:
- **TargetDocument**: The contract text being reviewed (the document under evaluation)
- **Reference**: Reference guidelines/standards used for the review (the evaluation criteria)
- **Prediction**: One or more comments from the AI model
**Important**: The SystemPrompt shows what instructions the model received. Consider whether the model followed these instructions when evaluating the prediction quality.
**CRITICAL**: Each comment must identify a specific issue, gap, or concern IN THE TARGETDOCUMENT CONTRACT TEXT ITSELF. The comment's text_excerpt field should quote problematic contract language from the TargetDocument, NOT quote text from the Reference guidelines. The Reference justifies WHY the contract clause is problematic, but the issue must exist IN the contract.
Evaluate EACH predicted comment independently. Comments should flag problems in the contract clauses, not merely cite Reference requirements. 
 c) Describe the scoring dimensions with clear specifications on how a particular score should be calculated 
 ## Scoring Dimensions (Per Comment)
**EVALUATION ORDER**: Evaluate in this sequence: (1) TargetDocument_Grounding, (2) Reference_Consistency, (3) Actionability
### 1. TargetDocument_Grounding
**Evaluates**: (a) Whether text_excerpt quotes from TargetDocument contract text, and (b) Whether the comment is relevant to the quoted text_excerpt
**MANDATORY**: text_excerpt must quote from TargetDocument contract text. If text_excerpt quotes from Reference instead, score MUST be 1.
- **5**: text_excerpt correctly quotes TargetDocument contract text AND comment identifies a highly relevant, valid, and notable issue in that quoted text
- **4**: text_excerpt correctly quotes TargetDocument contract text AND comment identifies a valid and relevant issue in that quoted text
- **3**: text_excerpt correctly quotes TargetDocument contract text AND comment is somewhat relevant to that quoted text, but concern has moderate validity
- **2**: text_excerpt correctly quotes TargetDocument contract text BUT comment has weak relevance to that quoted text, or concern is questionable
- **1**: text_excerpt does NOT quote TargetDocument contract text (quotes Reference instead, or no actual quote), OR comment is irrelevant to the quoted text
### 2. Reference_Consistency
...
... 
 d) Clearly define the final output format to parse 
 ## Scoring Calculation
**Comment_Score** = Simple average of the three dimensions:
- Comment_Score = (TargetDocument_Grounding + Reference_Consistency + Actionability) / 3
**Aggregate_Score** = Average of all Comment_Score values for the sample
## Output Format
For each sample, evaluate ALL predicted comments and provide:
```json
{ "comments": [ 
 { "comment_id": "...",
 "TargetDocument_Grounding": {"score": X, "justification": "...", "supporting_evidence": "Verify text_excerpt quotes actual TargetDocument contract text and comment is relevant to it"},
 "Reference_Consistency": {"score": X, "justification": "...", "supporting_reference": "Quote from Reference that justifies the concern OR explain meaningful reasoning"}, 
 "Actionability": {"score": X, "justification": "Assess if action is clear, grounded in TargetDocument and Reference, and relevant to comment"},
 "Comment_Score": X.XX 
 } ],
 "Aggregate_Score": {
 "score": X.XX,
 "total_comments": N,
 "rationale": "..." 
 }
}
``` 
 e) Create a high-level Lambda handler, providing sufficient multithreading for faster inference 
 def lambda_handler(event, context): 
 scores: List[RewardOutput] = []
 samples = event
 max_workers = len(samples)
 print(f"Evaluating {len(samples)} items with {max_workers} threads...")
 with ThreadPoolExecutor(max_workers=max_workers) as executor:
 futures = [executor.submit(judge_answer, sample) for sample in samples]
 scores = [future.result() for future in futures]
 print(f"Completed {len(scores)} evaluations")
 return [asdict(score) for score in scores] 
 Deployment of the Lambda function 
 We used the following AWS Identity and Access Management (IAM) permissions and settings in the Lambda function. The following configurations are required for reward Lambda functions. RFT training can fail if any of them are missing. 
 a) Permissions for Amazon SageMaker AI execution role 
 Your Amazon SageMaker AI execution role must have permission to invoke your Lambda function. Add this policy to your Amazon SageMaker AI execution role: 
 {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "lambda:InvokeFunction"
            ],
            "Resource": "arn:aws:lambda:region:account-id:function:function-name"
        }
    ]
} 
 b) Permissions for Lambda function execution role 
 Your Lambda function’s execution role needs basic Lambda execution permissions and the permissions to Invoke the judge Amazon Bedrock model. 
 Note: This solution follows the AWS shared responsibility model. AWS is responsible for securing the infrastructure that runs AWS services in the cloud. You are responsible for securing your Lambda function code, configuring IAM permissions, implementing encryption and access controls, managing data security and privacy, configuring monitoring and logging, and verifying compliance with applicable regulations. Follow the principle of least privilege by scoping permissions to specific resource ARNs. For more information, see Security in AWS Lambda and Amazon SageMaker AI Security in the AWS documentation. 
 c) Add provisioned concurrency 
 Publish a version of the Lambda and to enable the function to scale without fluctuations in latency, we added some provisioned concurrency. 100 was sufficient in this case, however, there’s more room for cost improvements here. 
 d) Set Lambda timeout to 15 mins 
 Customizing the training configuration 
 We launched Nova Forge SDK, which provides modular components for each stage of the model customization lifecycle; ForgeTrainer for training, ForgeEvaluator for evaluation, ForgeDeployer for deployment, and ForgeInference for inference. Nova Forge SDK removes the need to search for the appropriate recipes or container URI for specific techniques. 
 You can use ForgeTrainer from the Nova Forge SDK to customize training parameters in two ways: provide a full recipe YAML using recipe_path or pass specific fields using overrides for selective changes. For this use case, we use overrides to tune the rollout and trainer settings as shown in the following section. 
 # Launch training with recipe overrides
from amzn_nova_forge.trainer import ForgeTrainer
from amzn_nova_forge.core import ForgeConfig
from amzn_nova_forge.manager import SMTJRuntimeManager
from amzn_nova_forge.model.model_enums import Model, TrainingMethod

trainer = ForgeTrainer(
 model=Model.NOVA_LITE_2,
 method=TrainingMethod.RFT_LORA,
 infra=SMTJRuntimeManager(instance_type="ml.p5.48xlarge", instance_count=2),
 training_data_s3_path="s3://...",
 config=ForgeConfig(output_s3_path="s3://...")
)

result = trainer.train(
 job_name="my-rft-run",
 rft_lambda_arn="",
 overrides={
 "max_length": 64000,
 "global_batch_size": 64,
 "reasoning_effort": None,
 "shuffle": False,
 "type": "off_policy_async",
 "age_tolerance": 2,
 "proc_num": 6,
 "number_generation": 8,
 "max_new_tokens": 16000,
 "set_random_seed": True,
 "temperature": 1,
 "top_k": 0,
 "lambda_concurrency_limit": 100,
 "max_steps": 516,
 "save_steps": 32,
 "save_top_k": 17,
 "refit_freq": 4,
 "clip_ratio_high": 0.28,
 "ent_coeff": 0.0,
 "loss_scale": 1,
 },
) 
 Results 
 RFT with Amazon Nova 2 Lite achieved a 4.33 aggregate score—the highest performance across all evaluated models—while maintaining perfect JSON schema validation. This represents a significant improvement, demonstrating that RFT can produce production-ready, specialized models that outperform larger general-purpose alternatives. 
 We evaluated models using a “best of k” single-comment setting, where each model generated multiple comments per sample and we scored the highest-quality output. This approach establishes an upper bound on performance and enables a fair comparison between models that produce single versus multiple outputs. 
 Figure 1 — JSON Schema Validation Scores (0–1 scale, higher is better) 
 Figure 2 — Aggregate LLM judge scores (1–5 scale, higher is better) 
 Key takeaways: 
 RFT achieved the highest performance among evaluated models in this study. 
 Amazon Nova 2 Lite with RFT achieved a 4.33 aggregate score, outperforming both Claude Sonnet 4.5 and Claude Haiku 4.5, while also achieving perfect JSON schema validation. 
 Removes unnecessary training artifacts 
 During SFT iterations, we observed problematic behaviors including repetitive comment generation and unnatural Unicode character predictions. These issues, likely caused by overfitting or dataset imbalances, didn’t appear in RFT checkpoints. RFT’s reward-based improvements naturally discourages such artifacts, producing more robust and reliable outputs . 
 Strong generalization to new judge criteria 
 When we evaluated RFT models using a modified judge prompt (aligned but not identical to the training reward function), performance remained strong. This demonstrates that RFT learns generalizable quality patterns rather than overfitting specific evaluation criteria. This is a critical advantage for real-world deployment where requirements evolve. 
 Compute considerations 
 RFT required 4–8 rollouts per training sample, increasing compute costs compared to SFT. This overhead is amplified when using non-zero reasoning effort settings. However, for mission-critical applications where alignment quality directly impacts business outcomes—such as legal contract review, financial compliance, or healthcare documentation, the performance gains justify the additional compute costs. 
 Conclusion 
 Reinforcement Fine-Tuning (RFT) with LLM-as-a-judge represents a powerful approach to aligning LLMs for domain-specific applications. As demonstrated in our legal contract review case study, this methodology delivers significant improvements over both base models and traditional supervised fine-tuning (SFT) approaches, with RFT achieving the highest aggregate scores across all evaluation dimensions. For teams building mission-critical AI systems where alignment quality directly impacts business outcomes, RFT with LLM-as-a-judge offers a compelling path forward. The methodology’s explainability, flexibility, and superior performance make it particularly valuable for complex domains like legal review (or Financial Services or Healthcare) where subtle nuances matter. 
 Organizations considering this approach should start small—validate their judge design on curated benchmarks, verify infrastructure resilience, and scale gradually while monitoring for reward hacking. With proper implementation, RFT can transform capable base models into highly specialized, production-ready systems that consistently deliver aligned, trustworthy outputs. 
 References : 
 Amazon Nova Developer Guide for Amazon Nova 2 
 Nova Forge SDK- GitHub 
 Reinforcement Fine-Tuning (RFT) with Amazon Nova models 
 Disclaimer: 
 The legal contract review use case described in this post is for technical demonstration purposes only. AI-generated contract analysis is not a substitute for professional legal advice. Consult qualified legal counsel for legal matters. 
 About the authors 
 Hemanth Kumar Jayakumar is an Applied Scientist at Amazon AGI, where he works on reinforcement learning and foundation models. He translates the latest ML research into scalable solutions, unlocking domain specialization of foundation models for customers. Outside of work, Hemanth enjoys traveling and hiking. 
 Daniel Suarez Souto is a Solutions Architect at Amazon Web Services, specializing in Artificial Intelligence. He helps customers accelerate their AI adoption and build secure, scalable AI systems end-to-end, turning real-world edge cases into reusable patterns that help customers move faster. In his free time, Daniel enjoys playing soccer, running, and hiking. 
 Ajit Kumar K.P. is a Senior Generative AI Partner Solutions Architect at AWS, where he works with enterprise customers and partners deploying AI solutions in the cloud. He brings deep expertise bridging the gap between platform engineering and enterprise-scale AI, having built Computer Vision solutions at the Edge, and AIML and Generative AI solutions in the Cloud. Ajit enjoys reading biographies and playing sports in his free time. 
 Bharathan Balaji is a Senior Applied Scientist at Amazon Web Services, working on reinforcement learning and foundation model services. His work focuses on building AI capabilities that help customers transform their businesses.
```

---

## 20. AWS Generative AI Model Agility Solution: A comprehensive guide to migrating LLMs for generative AI production

- 日期: 2026-04-30 17:04
- 链接: https://aws.amazon.com/blogs/machine-learning/aws-generative-ai-model-agility-solution-a-comprehensive-guide-to-migrating-llms-for-generative-ai-production/

```
Maintaining model agility is crucial for organizations to adapt to technological advancements and optimize their artificial intelligence (AI) solutions. Whether transitioning between different large language model (LLM) families or upgrading to newer versions within the same family, a structured migration approach and a standardized process are essential for facilitating continuous performance improvement while minimizing operational disruptions. However, developing such a solution is challenging in both technical and non-technical aspects because the solution needs to: 
 Be generic to cover a variety of use cases 
 Be specific so that a new user can apply it to the target use case 
 Provide comprehensive and fair comparison between LLMs 
 Be automated and scalable 
 Incorporate domain- and task-specific knowledge and inputs 
 Have a well-defined, end-to-end process from data preparation guidance to final success criteria 
 In this post, we introduce a systematic framework for LLM migration or upgrade in generative AI production, encompassing essential tools, methodologies, and best practices. The framework facilitates transitions between different LLMs by providing robust protocols for prompt conversion and optimization. It includes evaluation mechanisms that assess multiple performance dimensions, enabling data-driven decision-making through detailed and comparative analysis of source and destination models. The proposed approach offers a comprehensive solution that includes the technical aspects of model migration and provides quantifiable metrics to validate successful migration and identify areas for further optimization, facilitating a seamless transition and continuous improvement. Here are a few highlights of the solution: 
 Provides a variety of reporting options with various LLM evaluation frameworks and comprehensive guidance for metrics selection for target use cases. 
 Provides automated prompt optimization and migration with Amazon Bedrock Prompt Optimization and the Anthropic Metaprompt tool , in addition to best practices for further prompt optimization. 
 Provides comprehensive guidance for model selection and an end-to-end solution for model comparison regarding cost, latency, accuracy, and quality. 
 Provides feature examples and use case examples for users to quickly apply the solution to the target use case. 
 The total time required for an LLM migration or upgrade by following this framework is from two days up to two weeks depending on the complexity of the use case. 
 Solution overview 
 The core of the migration involves a three-step approach, shown in the preceding diagram. 
 Evaluate the source model. 
 Prompt migration to and optimization of the target model with Amazon Bedrock prompt optimization and the Anthropic Metaprompt tool. 
 Evaluate the target model. 
 This solution provides a comprehensive approach to upgrade existing generative AI solutions (source model) to LLMs on Amazon Bedrock (target model). This solution addresses technical challenges through: 
 Evaluation metrics selection with a framework that uses various LLMs 
 Prompt improvement and migration with Amazon Bedrock Prompt Optimization and the Anthropic Metaprompt tool 
 Model comparison across cost, latency, and performance 
 This structured approach provides a robust framework for evaluating, migrating, and optimizing LLMs. By following these steps, we can transition between models, potentially unlocking improved performance, cost-efficiency, and capabilities in your AI applications. The process emphasizes thorough preparation, systematic evaluation, and continuous improvement; setting the stage for long-term success in using advanced language models. 
 Solution implementation 
 Dataset preparation 
 An evaluation dataset with high-quality samples is critical to the migration process. For most use cases, samples with ground truth answers are required; while for other use cases, metrics that don’t require ground truth—such as answer relevancy, faithfulness, toxicity, and bias (see Evaluation of frameworks and metrics selection section)—can be used as the determination metrics. Use the following guidance and data format to prepare the sample data for the target use cases. 
 Suggested fields for sample data include: 
 Prompt used for the source model 
 Prompt input (if any), for example: Questions and context for Retrieval-Augmented Generation (RAG)-based answer generation 
 Configurations used for source model invocation, for example, temperature, top_p, top_k, and so on. 
 Ground truths 
 Output from the source model 
 Latency of the source model 
 Input and output tokens from the source model, which can be used for cost calculation 
 It’s important to remember that high quality ground truths are essential to successful migration for most use cases. Ground truths should not only be validated regarding correctness, but also to verify that they fit the subject matter expert’s (SME’s) guidance and evaluation criteria. See Error Analysis section for an example of a SME’s guidance and evaluation criteria. 
 In addition, if any existing evaluation metrics are available, such as a human evaluation score or thumbs up/thumbs down from a SME, include those metrics and corresponding reasoning or comments for each data sample. If any automated evaluations have been conducted, include the automated evaluation scores, methods, and configurations. The following section provides more detailed guidance on selecting evaluation frameworks and defining the metrics. However, it’s still valuable to collect the existing or preferred evaluation metrics from stakeholders for reference. 
 Include the following fields if applicable: 
 Existing human evaluation metrics for the source model, for example, the SME score for source model. 
 Existing automated evaluation metrics for the source model, for example, the LLM-as-a-judge score for the source model. 
 The following table is an example format of the data samples: 
 sample_id … 
 question 
 content 
 prompt_source_llm 
 answer_ground_truth 
 answer_ source_llm 
 latency_ source_llm 
 input_token_source_llm 
 output_token_source_llm 
 llm_judge_score_source_llm 
 human_score_source_llm 
 human_score_reasoning_source_llm 
 Evaluation of frameworks and metrics selection 
 After collecting information and data samples, the next step is to choose the proper evaluation metrics for the generative AI use case. Besides human evaluation by a SME, automated evaluation metrics are recommended because they are more scalable and objective and support the long-term health and sustainability of the product. The following table shows the automated metrics that are available for each use case. 
 Model selection 
 The selection of an appropriate LLM requires careful consideration of multiple factors. Whether migrating to an LLM within the same LLM family or to a different LLM family, understanding the key characteristics of each model and the evaluation criteria is crucial for success. When planning to migrate between LLMs, carefully compare and evaluate various available options and check out the model card and respective prompting guides released by each model provider. When evaluating LLM options, consider several key criteria: 
 Input and output modalities : Text, code, and multi-modal capabilities 
 Context window size : Maximum input tokens the model can process 
 Cost per inference or token 
 Performance metrics : Latency and throughput 
 Output quality and accuracy 
 Domain specialization and specific use case compatibility 
 Hosting options : Cloud, on-premises, and hybrid 
 Data privacy and security requirements 
 After initial filtering based on these characteristics, benchmarking tests should be conducted by evaluating performance on specific tasks to compare shortlisted models. Amazon Bedrock offers a comprehensive solution with access to various LLMs through a unified API. This allows us to experiment with different models, compare their performance, and even use multiple models in parallel, all while maintaining a single integration point. This approach not only simplifies the technical implementation but also helps avoid vendor lock-in by enabling a diversified AI model strategy. 
 Prompt migration 
 Two automated prompt migration and optimization tools are introduced here: the Amazon Bedrock Prompt Optimization and the Anthropic Metaprompt tool. 
 Amazon Bedrock Prompt Optimization 
 Amazon Bedrock Prompt Optimization is a tool available in Amazon Bedrock to automatically optimize prompts written by users. This helps users build high quality generative AI applications on Amazon Bedrock and reduces friction when moving workloads from other providers to Amazon Bedrock. Amazon Bedrock Prompt Optimization can enable migration of existing workloads from a source model to LLMs on Amazon Bedrock with minimal prompt engineering. With this tool, we can choose the model to optimize the prompt for and then generate an optimized prompt for the target model. The main advantage of using Amazon Bedrock Prompt Optimization is the ability to use it from the AWS Management Console for Amazon Bedrock. Using the console, we can quickly generate a new prompt for the target model. We can also use the Bedrock API to generate a migrated prompt, please see the detailed implementation below. 
 Option A) Optimize a prompt from the Amazon Bedrock Console 
 In the Amazon Bedrock console, go to Prompt management . 
 Choose Create prompt , enter a name for the prompt template, and choose Create . 
 Enter the source model prompt. Create variables by enclosing a name with double curly braces: {{variable}} . In the Test variables section, enter values to replace the variables with when testing. 
 Select a Target Model for your optimized prompt . For example, Anthropic’s Claude Sonnet 4. 
 Choose the Optimize button to generate an optimized prompt for the target model. 
 6. After the prompt is generated, the comparison window of the optimized prompt for the target model is shown with your original prompt from source model. 
 7. Save the new optimized prompt before exiting comparing mode. 
 Option B) Optimize a prompt using Amazon Bedrock API 
 We can also use the Bedrock API to generate a migrated prompt, by sending an OptimizePrompt request with an Agents for Amazon Bedrock runtime endpoint . Provide the prompt to optimize in the input object and specify the model to optimize for in the targetModelId field. 
 The response stream returns the following events: 
 analyzePromptEvent – Appears when the prompt is finished being analyzed. Contains a message describing the analysis of the prompt. 
 optimizedPromptEvent – Appears when the prompt has finished being rewritten. Contains the optimized prompt. 
 Run the following code sample to optimize a prompt: 
 import boto3

# Set values here
TARGET_MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0" # Model to optimize for. For model IDs, see https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html
PROMPT = "Please summarize this text: " # Prompt to optimize

def get_input(prompt):
 return {
 "textPrompt": {
 "text": prompt
 }
 }
 
def handle_response_stream(response):
 try:
 event_stream = response['optimizedPrompt']
 for event in event_stream:
 if 'optimizedPromptEvent' in event:
 print("========================== OPTIMIZED PROMPT ======================\n")
 optimized_prompt = event['optimizedPromptEvent']
 print(optimized_prompt)
 else:
 print("========================= ANALYZE PROMPT =======================\n")
 analyze_prompt = event['analyzePromptEvent']
 print(analyze_prompt)
 except Exception as e:
 raise e
 
 
if __name__ == '__main__':
 client = boto3.client('bedrock-agent-runtime')
 try:
 response = client.optimize_prompt(
 input=get_input(PROMPT),
 targetModelId=TARGET_MODEL_ID
 )
 print("Request ID:", response.get("ResponseMetadata").get("RequestId"))
 print("========================== INPUT PROMPT ======================\n")
 print(PROMPT)
 handle_response_stream(response)
 except Exception as e:
 raise e 
 Anthropic Metaprompt tool 
 The Metaprompt is a prompt optimization tool offered by Anthropic where Claude is prompted to write prompt templates on the user’s behalf based on a topic or task. We can use it to instruct Claude on how to best construct a prompt to achieve a given objective consistently and accurately. 
 The key steps are: 
 Specify the raw prompt template, explain the task, and specify the input variables and the expected output. 
 Run Metaprompt with a Claude LLM such as Claude-3-Sonnet by inputting the raw prompt from the source model. 
 The new prompt template is generated with an optimized set of instructions and format following Claude LLM’s best practices. 
 Benefits of using metaprompts: 
 Prompts are much more detailed and comprehensive compared to human-created prompts 
 Helps increase the likelihood that best practices are followed for prompting the Anthropic models 
 Allows specifying that key details such preferred tone 
 Improves quality and consistency of the model’s outputs 
 The Metaprompt tool is particularly useful for learning Claude’s preferred prompt style or as a method to generate multiple prompt versions for a given task, simplifying testing a variety of initial prompt variations for the target use case. 
 To implement this process, follow the steps in the Prompt Migration Jupyter Notebook to migrate source model prompts to target model prompts. This notebook requires Claude-3-Sonnet to be enabled as the LLM in Amazon Bedrock using Model Access to generate the converted prompts. 
 The following is one example of a source model prompt in a financial Q&A use case: 
 To answer the financial question, think step-by-step:
1. Carefully read the question and any provided context paragraphs related to yearly and quarterly document reports to find all relevant paragraphs. Prioritize context paragraphs with CSV tables.
2. If needed, analyze financial trends and quarter-over-quarter (Q/Q) performance over the detected time spans mentioned in the related time keywords. Calculate rates of change between quarters to identify growth or decline.
3. Perform any required calculations to get the final answer, such as sums or divisions. Show the math steps.
4. Provide a complete, correct answer based on the given information. If information is missing, state what is needed to answer the question fully.
5. Present numerical values in rounded format using easy-to-read units.
6. Do not preface the answer with "Based on the provided context" or anything similar. Just provide the answer directly.
7. Include the answer with relevant and exhaustive information across all contexts. Substantiate your answer with explanations grounded in the provided context. Conclude with a precise, concise, honest, and to-the-point answer.
8. Add the page source and number.
9. Add all source files from where the contexts were used to generate the answers.
context = {CONTEXT}
query = {QUERY}
rephrased_query = {REPHARSED_QUERY}
time_kwds = {TIME_KWDS} 
 After completing the steps in the notebook, we can automatically get the optimized prompt for the target model. The following example generates a prompt optimized for Anthropic’s Claude LLMs. 
 Here are the steps to answer the financial question:

1. Read the provided <context>{$CONTEXT}</context> carefully, paying close attention to any paragraphs and CSV tables related to yearly and quarterly financial reports. Prioritize context paragraphs containing CSV tables.

2. Identify the relevant time periods mentioned in the <time_kwds>{$TIME_KWDS}</time_kwds>. Analyze the financial trends and quarter-over-quarter (Q/Q) performance during those time spans. Calculate rates of change between quarters to determine growth or decline.

3. <scratchpad>
In this space, you can perform any necessary calculations to arrive at the final answer to the <query>{$QUERY}</query> or <rephrasedquery>{$REPHARSED_QUERY}</rephrasedquery>. Show your step-by-step work, including formulas used and intermediate values.
</scratchpad>

4. <answer>
Provide a complete and correct answer based on the information given in the context. If any crucial information is missing to fully answer the question, state what additional details are needed.

Present numerical values in an easy-to-understand format using appropriate units. Round numbers as necessary.

Do not include any preamble like "Based on the provided context..." Just provide the direct answer.

Include all relevant and exhaustive information from the contexts to substantiate your answer. Explain your reasoning grounded in the provided evidence. Conclude with a precise, concise, honest, and to-the-point final answer.

Finally, cite the page source and number, as well as list all files that contained context used to generate this answer.
</answer> 
 As shown in the preceding example, the prompt style and format are automatically converted to follow the best practices of the target model, such as using XML tags and regrouping the instructions to be clearer and more direct. 
 Generate results 
 Answer generation during migration is an iterative process. The general flow includes passing migrated prompts and context to the LLM and generating an answer. Multiple iterations are needed to compare different prompt versions, multiple LLMs, and different configurations of each LLM to help us select the best combination. In most cases, the entire pipeline of a generative AI system (such as a RAG-based chatbot) isn’t migrated. Instead, only a portion of the pipeline is migrated. Thus, it’s crucial that a fixed version of the remaining components in the pipeline is available. For example, in a RAG-based question and answer (Q&A) system, we might migrate only the answer generation component of the pipeline. As a result, we can continue to use the already generated context of the existing production model. 
 As a best practice, use the Amazon Bedrock models standard invocation method (in the Migration code repository ) to generate metadata such as latency, time to first token, input token, and output token in addition to the final response. These metadata fields are added as a new column at the end of the results table and used for evaluation. The output format and column name should be aligned with the evaluation metric requirements. The following table shows an example of the sample data before feeding it into the evaluation pipeline for a RAG use case. 
 Example of a sample data before evaluation: 
 financebench_id financebench_id_03029 
 doc_name 3M_2018_10K 
 doc_link https://investors.3m.com/financials/sec-filings/content/0001558370-19-000470/0001558370-19-000470.pdf 
 doc_period 2018 
 question_type metrics-generated 
 question What is the FY2018 capital expenditure amount (in USD millions) for 3M? Give a response to the question by relying on the details shown in the cash flow statement. 
 ground_truths [‘$1577.00’] 
 evidence_text … 
 page_number 60 
 llm_answer According to the cash flow statement in the 3M 2018 10-K report, the capital expenditure (purchases of property, plant and equipment) for fiscal year 
 llm_contexts … 
 latency_meta_time 0.92706 
 latency_meta_kwd 0.60666 
 latency_meta_comb 1.44876 
 latency_meta_ans_gen 2.48371 
 input_tokens 21147 
 output_tokens 401 
 Evaluation 
 Evaluation is one of the most important parts of the migration process because it directly connects to the sign-off criteria and determines the success of the migration. For most cases, evaluation focuses on metrics in three major categories: accuracy and quality, latency, and cost. Either automated evaluation or human evaluation can be used to assess the accuracy and quality of the model response. 
 Automated evaluation 
 The integration of LLMs in the quality evaluation process represents a significant advancement in assessment methodology. These models excel at conducting comprehensive evaluations across multiple dimensions, including contextual relevance, coherence, and factual accuracy, while maintaining consistency and scalability. Two primary categories of the automated evaluation metrics are introduced here: 
 Predefined metrics : Metrics predefined in LLM-based evaluation frameworks such as Ragas , DeepEval , and Amazon Bedrock Evaluations , or directly based on non-LLM algorithms, like those introduced in Evaluation of frameworks . 
 Custom metrics : Customized metrics with user provided definitions, evaluation criteria, or prompts to use LLM as an impartial judge. 
 Predefined metrics 
 These metrics are either using some LLM-based evaluation frameworks such as Ragas and DeepEval or are directly based on non-LLM algorithms. These metrics are widely adopted, predefined, and have limited options for customization. Ragas and DeepEval are two LLM-based evaluation frameworks and metrics that we used as examples in the Migration code repository . 
 Ragas: Ragas is an open source framework that helps to evaluate RAG pipelines. RAG denotes a class of LLM applications that use external data to augment the LLM’s context. It provides a variety of LLM-powered automated evaluation metrics. The following metrics are introduced in the Ragas evaluation notebook in the Migration code repository. Answer precision: Measures how accurately the model’s generated answer contains relevant and correct claims compared to the ground truth answer. 
 Answer recall: Evaluates the completeness of the answer; that is, the model’s ability to retrieve the correct claims and compare them to the ground truth answer. High recall indicates that the answer thoroughly covers the necessary details in line with the ground truth. 
 Answer correctness: The assessment of answer correctness involves gauging the accuracy of the generated answer when compared to the ground truth. This evaluation relies on the ground truth and the answer , with scores ranging from 0 to 1. A higher score indicates a closer alignment between the generated answer and the ground truth, signifying better correctness. 
 Answer similarity: The assessment of the semantic resemblance between the generated answer and the ground truth. This evaluation is based on the ground truth and the answer , with values falling within the range of 0 to 1. A higher score signifies a better alignment between the generated answer and the ground truth. 
 The following table is a sample data output after Ragas evaluation. 
 financebench_id financebench_id_03029 
 doc_name 3M_2018_10K 
 doc_link https://investors.3m.com/financials/sec-filings/content/0001558370-19-000470/0001558370-19-000470.pdf 
 doc_period 2018 
 question_type metrics-generated 
 question What is the FY2018 capital expenditure amount (in USD millions) for 3M?. 
 ground_truths [‘$1577.00’] 
 evidence_text … 
 page_number 60 
 llm_answer According to the cash flow statement in the 3M 2018 10-K report, the capital expenditure (purchases of property, plant and equipment) for fiscal year 2018 was $1,577 million. … 
 llm_contexts … 
 latency_meta_time 0.92706 
 latency_meta_kwd 0.60666 
 latency_meta_comb 1.44876 
 latency_meta_ans_gen 2.48371 
 input_tokens 21147 
 output_tokens 401 
 answer_precision 0 
 answer_recall 1 
 answer_correctness 0.16818 
 answer_similarity 0.33635 
 DeepEval: DeepEval is an open source LLM evaluation framework. It’s similar to Pytest but specialized for unit testing LLM outputs. DeepEval incorporates the latest research to evaluate LLM outputs based on metrics such as the G-Eval, hallucination, answer relevancy, Ragas, and so on. It uses LLMs and various other natural language processing (NLP) models that run locally on your machine for evaluation. In DeepEval, a metric serves as a standard of measurement for evaluating the performance of an LLM output based on specific criteria. DeepEval offers a range of default metrics to quickly get started. The following metrics are introduced in the DeepEval evaluation notebook in the Migration code repository.| Answer relevancy : The answer relevancy metric measures the quality of your RAG pipeline’s generator by evaluating how relevant the actual_output of your LLM application is compared to the provided input. 
 Faithfulness : The faithfulness metric measures the quality of your RAG pipeline’s generator by evaluating whether the actual_output factually aligns with the contents of your retrieval_context . 
 Toxicity : The toxicity metric is another referenceless metric that evaluates toxicity in your LLM outputs. 
 Bias : The bias metric determines whether your LLM output contains gender, racial, or political bias. 
 Amazon Bedrock Evaluations : Amazon Bedrock Evaluations is a suite of tools for evaluating, comparing, and selecting foundation models – including custom or third-party models – for your specific use cases. It supports both model-only and RAG pipelines evaluation. We can use Bedrock Evaluations either via AWS console or API. Amazon Bedrock Evaluations offers an extensive list of built-in metrics for both standalone LLMs and full RAG pipelines, including but not limited to: Accuracy : Measures the correctness of model outputs. 
 Faithfulness: Checks for factual accuracy and avoids hallucinations. 
 Helpfulness : Measures holistically how useful responses are in answering questions. 
 Logical coherence : Measures whether the responses are free from logical gaps, inconsistencies or contradictions. 
 Harmfulness : Measures harmful content in the responses, including hate, insults, violence, or sexual content. 
 Stereotyping : Measures generalized statements about individuals or groups of people in responses. 
 Refusal : Measures how evasive the responses are in answering questions. 
 Following instructions : Measures how well the model’s response respects the exact directions found in the prompt. 
 Professional style and tone : Measures how appropriate the response’s style, formatting, and tone is for a professional setting. 
 Custom metrics 
 These metrics are user defined and are typically tailored to specific tasks or domains. One popular method is to use custom LLM as a judge to provide an evaluation score for an answer using a user-provided prompt. In contrast to using predefined metrics, this method is highly customizable because we can provide the prompt with task-specific evaluation requirements. For example, we can ask the LLM to generate a 10-point scoring system and comprehensively evaluate the answer against ground truth across different dimensions, such as correctness of information, contextual relevance, depth and comprehensiveness of detail, and overall utility and helpfulness. 
 The following is an example of a customized prompt for LLM as a judge: 
 #Prompt:   
System: "You are an AI evaluator that helps in evaluating output from LLM",
 
resp_fmt = """{
               "score":float,
               "reasoning": str
           }
       """
 
User = f"""[Instruction]\nPlease act as an impartial judge and evaluate the quality of the response
    provided by an AI assistant to the user question displayed below. Your evaluation should consider correctness,
    relevance, level of detail and helpfulness. You will be given a reference answer and the assistant's answer.
    Begin your evaluation by comparing the assistant's answer with the reference answer. Identify any mistakes. Be as
    objective as possible. After providing your explanation in the "reasoning" tab , you must score the response on a
    scale of 1 to 10 in the "score" tab. Strictly follow the below json format:{resp_fmt}.
   \n\n[Question]\n{question}\n\n[The Start of Reference Answer]\n{reference}\n[The End of Reference Answer]\n\n[The
    Start of Assistant's Answer]\n{response}\n[The End of Assistant's Answer]""" 
 Human evaluation 
 While quantitative metrics provide valuable data points, a comprehensive qualitative evaluation based on professional guidelines and SME feedback is also necessary to validate model performance. Effective qualitative assessment typically covers several key areas including response theme and tone consistency, detection of inappropriate or unwanted content, domain-specific accuracy, date and time related issues, and so on. By using SME expertise, we can identify subtle nuances and potential issues that might escape quantitative analysis. Error analysis provides some potential aspects that the SME can use for evaluation criteria, which can also serve as the guidance for validating and preparing ground truths. We can use tools such as Amazon Bedrock Evaluations for human evaluation. 
 Though human evaluation or user feedback collected from a UI can directly reflect the SME’s evaluation criteria, it’s not as efficient, scalable, and objective as the automated evaluation methods. Thus, a generative AI system development life cycle might start with human evaluation but eventually moves toward automated evaluation. Human evaluation can be used if automated evaluation isn’t meeting baseline targets or pre-defined evaluation criteria. 
 Latency metrics 
 When migrating language models, runtime performance metrics are crucial indicators of operational success. Total latency and Time to first token (TTFT) are the most common metrics for latency measurement. 
 Total latency is an end-to-end metric that measures the total duration required for complete response generation, from initial prompt to final output. It encompasses processing the input, generating the response, and delivering it to the user. Total latency affects user satisfaction, system throughput, and resource utilization. 
 Time to first token (TTFT) quantifies the initial response speed—specifically, the duration until the model generates its first output token. This metric significantly impacts perceived responsiveness and user experience, especially in interactive applications. TTFT is particularly important in conversational AI and real-time systems (applications such as chatbots, virtual assistants, and interactive search systems) where users expect immediate feedback. A low TTFT creates an impression of system responsiveness and can greatly enhance user engagement. 
 If the results generation step requires multiple LLM calls, the breakdown latency metrics should be provided because only the submodule latency corresponding to LLM migration should be compared in the following model comparison step. 
 Cost calculation 
 For LLM invocation, the cost can be calculated based on the number of input and output tokens and the corresponding price per token: 
 LLM_invocation_cost = number_of_input_tokens * price_per_input_token + number_of_output_tokens * price_per_output_token 
 The cost calculations table for price per input and output token can be found in Amazon Bedrock Pricing . 
 Model comparison report: Performance, latency, and cost 
 We can use the Generate Comparison Report notebook in the code repository to automatically generate a final comparison report for the source and target model in a holistic view. 
 We can also use evaluation reports generated from Ragas and DeepEval with corresponding metrics to compare the models from the two evaluation frameworks. We can obtain a side-by-side comparison of the average input and output tokens and average cost and latency for the selected models. As shown in the following figure, after running this notebook, there are two comparison tables for the source and target models from the two selected evaluation frameworks. 
 Ragas 
 DeepEval 
 Further optimization 
 When enhancing and optimizing a generative AI production pipeline during an LLM migration or upgrade, users typically focus on two key areas: 
 Quality of generated answers 
 Latency of response generation 
 Prompt optimization 
 To optimize the quality of the generated answers, we need to get a good understanding of the errors by conducting error analysis and identifying the items for prompt optimization. 
 Error analysis 
 Getting the best possible response from a candidate LLM is unlikely without any optimization. Thus, conducting error analysis and focusing on possible aspects for error patterns helps us evaluate generated answer quality and identify the opportunities for improvement. Error analysis also provides a path to manual prompt engineering to improve the quality. After gathering error analysis insights and feedback from SMEs, an iterative prompt optimization process can be conducted. To start, formulate the error analysis insights and feedback from SMEs into clear guidance or criteria. Ideally, these criteria should be clarified before starting the prompt migration. These criteria serve as the core considerations for further prompt optimization to help provide consistent, high-quality responses to meet the SME’s bar. The following is an example of possible guidance and criteria we might receive from a SME. 
 Example of an answer formatting style guide from a SME in a financial Q&A use case: 
 Correctness Make sure pulled numbers are correct. All numbers should be matched to ground truth. 
 Make sure all claims from ground truth are available in the LLM answer. 
 Generated responses should not add irrelevant sentences. 
 Time Generated answers must recognize the fiscal year and all needed quarters from the question correctly. 
 In the answer, quarter orders from most recent to the earliest is preferred. 
 When the question asks about year-over-year, the answer should specify overall year or the last quarter, not quarter-by-quarter. 
 When the answer comes from a single news document, include the date of publication in the answer. 
 Theme and tone Use professional language mirroring the style of a newspaper. 
 Format and excerpts When the user query asks for a list, present the list in bullet point format. 
 When the user query asks for excerpts, provide a summary statement followed by a bulleted list of unedited excerpts directly from the document. 
 Queries that ask for a comprehensive list ideally include bullet points. 
 Queries that ask for topics or themes with subjective categories ideally include a bulleted list. 
 Don’t start the answer by referencing the context (according to context). 
 Length Most responses should be between 30–150 words. Longer answers are acceptable when the question involves multiple entities or responding to queries that require sub-categories within the response. 
 Optimization techniques 
 After obtaining clear criteria, several optimization techniques can be used to address these criteria, such as: 
 Prompt engineering to specify certain criteria in the instruction of the prompt 
 Few-shot learning to specify the answer format and generated answer examples 
 Incorporating meta-information that could help the LLM to understand the context of the task and question 
 Pre- or post-processing to enforce the output format or resolve some frequent error patterns 
 Latency optimization 
 There are a few possible solutions to optimize the latency: 
 Optimizing prompts to generate shorter answers 
 The latency of an LLM model is directly impacted by the number of output tokens because each additional token requires a separate forward pass through the model, increasing processing time. As more tokens are generated, latency grows, especially in larger models such as Opus 4. To reduce the latency, we can add instructions to prompt to avoid providing lengthy answers, unrelated explanations, or filler words. 
 Using provisioned throughput 
 Throughput refers to the number and rate of inputs and outputs that a model processes and returns. Purchasing provisioned throughput to provide a higher level of throughput for a dedicated hosted model can potentially reduce the latency compared to using on-demand models. Though it cannot guarantee the improvement of latency, it consistently helps to prevent throttled requests. 
 Improvement lifecycle 
 It’s unlikely that a candidate LLM can achieve the best possible performance without any optimization. It’s also typical for the preceding optimization processes to be conducted iteratively. Thus, the improvement (optimization) lifecycle is critical to improve the performance and identify the gaps or defects in the pipeline or data. The improvement lifecycle typically includes: 
 Prompt optimization 
 Answer generation 
 Evaluation metrics generation 
 Error analysis 
 Sample label verification 
 Dataset updates regarding sample defects and wrong labels 
 Task or domain knowledge identificationThe migration process described in this post can be used in two phases in a generative AI solution production lifecycle. 
 End-to-end LLM migration and model agility 
 New LLMs are released frequently. No LLM can consistently maintain peak performance for a given use case. It’s common for a production generative AI solution to migrate to another family of LLMs or upgrade to a new version of an LLM. Thus, having a standard and reusable end-to-end LLM migration or upgrade process is critical to the long-term success of any generative AI solution. 
 Monitoring and quality assurance 
 When migration or updates are stabilized, there should be a standard monitoring and quality assurance process using a routinely refreshed golden evaluation dataset with ground truth and automated or human evaluation metrics, as well as evaluation of actual user traces. As part of this solution, the established evaluation and data or ground truth collection processes can be reused for monitoring and quality assurance. 
 Tips and suggestions (lessons learned) 
 The following are some tips and suggestions for the success of an LLM migration or upgrade process. 
 Sign-off condition : The data, evaluation criteria and success criteria defined at the start should be sufficient for stakeholders to confidently sign off on the process. Ideally, there should be no changes in the data, ground truths, or SME evaluation and success criteria during the process. 
 Sample data and quality : The data should be of sufficient quality and quantity for confident evaluation. The ground truth answers and labels should be fully aligned with the SME’s evaluation criteria and expectations. Ideally, there should be no changes in the data, ground truths, or SME evaluation criteria during the process. 
 Improvement lifecycle : Make sure to plan and implement an improvement lifecycle to get the most out of your chosen LLM. 
 Model selection : When selecting competing target models against a source model, use resources such as the Artificial Analysis benchmarking website to obtain a holistic comparison of models. These comparisons typically cover quality, performance, and price analysis, providing valuable insights before starting the experiment. This preliminary research can help narrow down the most promising candidates and inform the experimental design. 
 Performance against cost trade-offs : When evaluating different models or solutions, it’s important to consider the balance between performance and cost. In some cases, a model might offer slightly lower performance but at a sufficiently reduced cost to make it a more cost-effective option overall. This is particularly true in scenarios where the performance difference is minimal, but the cost savings are substantial. 
 Optimization techniques : Exploring various optimization techniques, such as prompt engineering or provisioned throughput, can lead to significant improvements in performance metrics like accuracy and latency. These optimizations can help bridge the gap between different models and should be considered as part of the evaluation process. 
 Conclusion 
 In this post, we introduced the AWS Generative AI Model Agility Solution, an end-to-end solution for LLM migrations and upgrades of existing generative AI applications that maintains and improves model agility. The solution defines a standardized process and provides a comprehensive toolkit for LLM migration or upgrade with a variety of ready-to-use tools and advanced techniques that can can be used to migrate generative AI applications to new LLMs. This can be used as a standard process in the lifecycle of your generative AI applications. After an application is stabilized with a specific LLM and configuration, the evaluation and data and ground truth collection processes in this solution can be reused for production monitoring and quality assurance. 
 To learn more about this solution, please check out our AWS Generative AI Model Agility Code Repo . 
 About the authors 
 Long Chen is a Sr. Applied Scientist at AWS Generative AI Innovation Center. He holds a Ph.D. in Applied Physics from University of Michigan – Ann Arbor. With more than a decade of experience for research and development, he works on innovative solutions in various domains using generative AI and other machine learning techniques, ensuring the success of AWS customers. His interests include generative models, multi-modal systems and graph learning. 
 Elaine Wu is a Deep Learning Architect at the AWS Generative AI Innovation Center, specializing in building robust RAG and agentic AI solutions for large enterprises. She has solved real-world business challenges for AWS customers across industries including manufacturing, energy, healthcare, retail, enterprise software, and financial services. Prior to joining AWS, Elaine earned her master’s degree in Information Science from the University of Illinois Urbana-Champaign. 
 Samaneh Aminikhanghahi is an Applied Scientist at the AWS Generative AI Innovation Center, where she works with customers across different verticals to accelerate their adoption of generative AI. She specializes in agentic AI frameworks, building robust evaluation systems, and implementing responsible AI practices that drive sustainable business outcomes. 
 Avinash Yadav is a Deep Learning Architect at the Generative AI Innovation Center, where he designs and implements cutting-edge GenAI solutions for diverse enterprise needs. He specializes in building agentic AI systems and multi-agent frameworks, developing AI agents capable of complex reasoning, tool use, and orchestration across enterprise workflows. His expertise spans ML pipelines using large language models, agentic architectures leveraging frameworks such as LangGraph and Amazon Bedrock AgentCore, along with cloud architecture, Infrastructure as Code (IaC), and automation. His focus lies in creating scalable, end-to-end applications that harness the power of deep learning, agentic workflows, and cloud technologies to solve real-world business challenges. 
 Vidya Sagar Ravipati is a Science Manager at the Generative AI Innovation Center, where he leverages his vast experience in large-scale distributed systems and his passion for machine learning to help AWS customers across different industry verticals accelerate their AI and cloud adoption.
```

---
