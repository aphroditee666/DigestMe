# Qdrant

> 分类: AI专题
> URL: https://qdrant.tech/index.xml
> 抓取: 30 篇

---

## 1. Distance-based data exploration

- 日期: 2025-03-11 12:00
- 链接: https://qdrant.tech/articles/distance-based-exploration/

```
Hidden Structure
When working with large collections of documents, images, or other arrays of unstructured data, it often becomes useful to understand the big picture. Examining data points individually is not always the best way to grasp the structure of the data.
As numbers in a table obtain meaning when plotted on a graph, visualising distances (similar/dissimilar) between unstructured data items can reveal hidden structures and patterns.
There are many tools to investigate data similarity, and Qdrant’s 1.12 release made it much easier to start this investigation. With the new Distance Matrix API, Qdrant handles the most computationally expensive part of the process—calculating the distances between data points.
In many implementations, the distance matrix calculation was part of the clustering or visualization processes, requiring either brute-force computation or building a temporary index. With Qdrant, however, the data is already indexed, and the distance matrix can be computed relatively cheaply.
In this article, we will explore several methods for data exploration using the Distance Matrix API.
Dimensionality Reduction
Initially, we might want to visualize an entire dataset, or at least a large portion of it, at a glance. However, high-dimensional data cannot be directly visualized. We must apply dimensionality reduction techniques to convert data into a lower-dimensional representation while preserving important data properties.
In this article, we will use UMAP as our dimensionality reduction algorithm.
Here is a very simplified but intuitive explanation of UMAP:
- Randomly generate points in 2D space: Assign a random 2D point to each high-dimensional point.
- Compute distance matrix for high-dimensional points: Calculate distances between all pairs of points.
- Compute distance matrix for 2D points: Perform similarly to step 2.
- Match both distance matrices: Adjust 2D points to minimize differences.
UMAP preserves the relative distances between high-dimensional points; the actual coordinates are not essential. If we already have the distance matrix, step 2 can be skipped entirely.
Let’s use Qdrant to calculate the distance matrix and apply UMAP. We will use one of the default datasets perfect for experimenting in Qdrant–Midjourney Styles dataset.
Use this command to download and import the dataset into Qdrant:
PUT /collections/midlib/snapshots/recover
{
"location": "http://snapshots.qdrant.io/midlib.snapshot"
}
We also need to prepare our python environment:
pip install umap-learn seaborn matplotlib qdrant-client
Import the necessary libraries:
# Used to talk to Qdrant
from qdrant_client import QdrantClient
# Package with original UMAP implementation
from umap import UMAP
# Python implementation for sparse matrices
from scipy.sparse import csr_matrix
# For visualization
import seaborn as sns
Establish connection to Qdrant:
client = QdrantClient("http://localhost:6333")
After this is done, we can compute the distance matrix:
# Request distances matrix from Qdrant
# `_offsets` suffix defines a format of the output matrix.
result = client.search_matrix_offsets(
collection_name="midlib",
sample=1000, # Select a subset of the data, as the whole dataset might be too large
limit=20, # For performance reasons, limit the number of closest neighbors to consider
)
# Convert distances matrix to python-native format
matrix = csr_matrix(
(result.scores, (result.offsets_row, result.offsets_col))
)
# Make the matrix symmetric, as UMAP expects it.
# Distance matrix is always symmetric, but qdrant only computes half of it.
matrix = matrix + matrix.T
Now we can apply UMAP to the distance matrix:
umap = UMAP(
metric="precomputed", # We provide ready-made distance matrix
n_components=2, # output dimension
n_neighbors=20, # Same as the limit in the search_matrix_offsets
)
vectors_2d = umap.fit_transform(matrix)
That’s all that is needed to get the 2d representation of the data.
UMAP isn’t the only algorithm compatible with our distance matrix API. For example, scikit-learn
also offers:
- Isomap - Non-linear dimensionality reduction through Isometric Mapping.
- SpectralEmbedding - Forms an affinity matrix given by the specified function and applies spectral decomposition to the corresponding graph Laplacian.
- TSNE - well-known algorithm for dimensionality reduction.
Clustering
Another approach to data structure understanding is clustering–grouping similar items.
Note that there’s no universally best clustering criterion or algorithm.
Many clustering algorithms accept precomputed distance matrix as input, so we can use the same distance matrix we calculated before.
Let’s consider a simple example of clustering the Midlib dataset with KMeans algorithm.
From scikit-learn.cluster documentation we know that fit()
method of KMeans algorithm prefers as an input:
X : {array-like, sparse matrix} of shape (n_samples, n_features)
:
Training instances to cluster. It must be noted that the data will be converted to C ordering, which will cause a memory copy if the given data is not C-contiguous. If a sparse matrix is passed, a copy will be made if it’s not in CSR format.
So we can re-use matrix
from the previous example:
from sklearn.cluster import KMeans
# Initialize KMeans with 10 clusters
kmeans = KMeans(n_clusters=10)
# Generate index of the cluster each sample belongs to
cluster_labels = kmeans.fit_predict(matrix)
With this simple code, we have clustered the data into 10 clusters, while the main CPU-intensive part of the process was done by Qdrant.
How to plot this chart
sns.scatterplot(
# Coordinates obtained from UMAP
x=vectors_2d[:, 0], y=vectors_2d[:, 1],
# Color datapoints by cluster
hue=cluster_labels,
palette=sns.color_palette("pastel", 10),
legend="full",
)
Graphs
Clustering and dimensionality reduction both aim to provide a more transparent overview of the data. However, they share a common characteristic - they require a training step before the results can be visualized.
This also implies that introducing new data points necessitates re-running the training step, which may be computationally expensive.
Graphs offer an alternative approach to data exploration, enabling direct, interactive visualization of relationships between data points. In a graph representation, each data point is a node, and similarities between data points are represented as edges connecting the nodes.
Such a graph can be rendered in real-time using force-directed layout algorithms, which aim to minimize the system’s energy by repositioning nodes dynamically–the more similar the data points are, the stronger the edges between them.
Adding new data points to the graph is as straightforward as inserting new nodes and edges without the need to re-run any training steps.
In practice, rendering a graph for an entire dataset at once may be computationally expensive and overwhelming for the user. Therefore, let’s explore a few strategies to address this issue.
Expanding from a single node
This is the simplest approach, where we start with a single node and expand the graph by adding the most similar nodes to the graph.
Sampling from a collection
Expanding a single node works well if you want to explore neighbors of a single point, but what if you want to explore the whole dataset? If your dataset is small enough, you can render relations for all the data points at once. But it is a rare case in practice.
Instead, we can sample a subset of the data and render the graph for this subset. This way, we can get a good overview of the data without overwhelming the user with too much information.
Let’s try to do so in Qdrant’s Graph Exploration Tool:
{
"limit": 5, # node neighbors to consider
"sample": 100 # nodes
}
This graph captures some high-level structure of the data, but as you might have noticed, it is quite noisy. This is because the differences in similarities are relatively small, and they might be overwhelmed by the stretches and compressions of the force-directed layout algorithm.
To make the graph more readable, let’s concentrate on the most important similarities and build a so called Minimum/Maximum Spanning Tree.
{
"limit": 5,
"sample": 100,
"tree": true
}
This algorithm will only keep the most important edges and remove the rest while keeping the graph connected. By doing so, we can reveal clusters of the data and the most important relations between them.
In some sense, this is similar to hierarchical clustering, but with the ability to interactively explore the data. Another analogy might be a dynamically constructed mind map.
Conclusion
Vector similarity goes beyond looking up the nearest neighbors–it provides a powerful tool for data exploration. Many algorithms can construct human-readable data representations, and Qdrant makes using them easy.
Several data exploration instruments are available in the Qdrant Web UI (Visualization and Graph Exploration Tools), and for more advanced use cases, you could directly utilise our distance matrix API.
Try it with your data and see what hidden structures you can reveal!
```

---

## 2. Modern Sparse Neural Retrieval: From Theory to Practice

- 日期: 2024-10-23 00:00
- 链接: https://qdrant.tech/articles/modern-sparse-neural-retrieval/

```
Finding enough time to study all the modern solutions while keeping your production running is rarely feasible.
Dense retrievers, hybrid retrievers, late interaction… How do they work, and where do they fit best?
If only we could compare retrievers as easily as products on Amazon! 
 We explored the most popular modern sparse neural retrieval models and broke them down for you.
By the end of this article, you’ll have a clear understanding of the current landscape in sparse neural retrieval and how to navigate through complex, math-heavy research papers with sky-high NDCG scores without getting overwhelmed.
```

---

## 3. Qdrant Summer of Code 2024 - ONNX Cross Encoders in Python

- 日期: 2024-10-14 08:00
- 链接: https://qdrant.tech/articles/cross-encoder-integration-gsoc/

```
Introduction 
 Hi everyone! I’m Huong (Celine) Hoang, and I’m thrilled to share my experience working at Qdrant this summer as part of their Summer of Code 2024 program. During my internship, I worked on integrating cross-encoders into the FastEmbed library for re-ranking tasks. This enhancement widened the capabilities of the Qdrant ecosystem, enabling developers to build more context-aware search applications, such as question-answering systems, using Qdrant’s suite of libraries. 
 This project was both technically challenging and rewarding, pushing me to grow my skills in handling large-scale ONNX (Open Neural Network Exchange) model integrations, tokenization, and more. Let me take you through the journey, the lessons learned, and where things are headed next.
```

---

## 4. What is a Vector Database?

- 日期: 2024-10-09 09:29
- 链接: https://qdrant.tech/articles/what-is-a-vector-database/

```
An Introduction to Vector Databases
Most of the millions of terabytes of data we generate each day is unstructured. Think of the meal photos you snap, the PDFs shared at work, or the podcasts you save but may never listen to. None of it fits neatly into rows and columns.
Unstructured data lacks a strict format or schema, making it challenging for conventional databases to manage. Yet, this unstructured data holds immense potential for AI, machine learning, and modern search engines.
A Vector Database is a specialized system designed to efficiently handle high-dimensional vector data. It excels at indexing, querying, and retrieving this data, enabling advanced analysis and similarity searches that traditional databases cannot easily perform.
The Challenge with Traditional Databases
Traditional OLTP and OLAP databases have been the backbone of data storage for decades. They are great at managing structured data with well-defined schemas, like name
, address
, phone number
, and purchase history
.
But when data can’t be easily categorized, like the content inside a PDF file, things start to get complicated.
You can always store the PDF file as raw data, perhaps with some metadata attached. However, the database still wouldn’t be able to understand what’s inside the document, categorize it, or even search for the information that it contains.
Also, this applies to more than just PDF documents. Think about the vast amounts of text, audio, and image data you generate every day. If a database can’t grasp the meaning of this data, how can you search for or find relationships within the data?
Vector databases allow you to understand the context or conceptual similarity of unstructured data by representing them as vectors, enabling advanced analysis and retrieval based on data similarity.
When to Use a Vector Database
Not sure if you should use a vector database or a traditional database? This chart may help.
What Is a Vector?
When a machine needs to process unstructured data - an image, a piece of text, or an audio file, it first has to translate that data into a format it can work with: vectors.
A vector is a numerical representation of data that can capture the context and semantics of data.
When you deal with unstructured data, traditional databases struggle to understand its meaning. However, a vector can translate that data into something a machine can process. For example, a vector generated from text can represent relationships and meaning between words, making it possible for a machine to compare and understand their context.
There are three key elements that define a vector in a vector database: the ID, the dimensions, and the payload. These components work together to represent a vector effectively within the system. Together, they form a point, which is the core unit of data stored and retrieved in a vector database.
Each one of these parts plays an important role in how vectors are stored, retrieved, and interpreted. Let’s see how.
1. The ID: Your Vector’s Unique Identifier
Just like in a relational database, each vector in a vector database gets a unique ID. Think of it as your vector’s name tag, a primary key that ensures the vector can be easily found later. When a vector is added to the database, the ID is created automatically.
While the ID itself doesn’t play a part in the similarity search (which operates on the vector’s numerical data), it is essential for associating the vector with its corresponding “real-world” data, whether that’s a document, an image, or a sound file.
After a search is performed and similar vectors are found, their IDs are returned. These can then be used to fetch additional details or metadata tied to the result.
2. The Dimensions: The Core Representation of the Data
At the core of every vector is a set of numbers, which together form a representation of the data in a multi-dimensional space.
From Text to Vectors: How Does It Work?
These numbers are generated by embedding models, such as deep learning algorithms, and capture the essential patterns or relationships within the data. That’s why the term embedding is often used interchangeably with vector when referring to the output of these models.
To represent textual data, for example, an embedding will encapsulate the nuances of language, such as semantics and context within its dimensions.
For that reason, when comparing two similar sentences, their embeddings will turn out to be very similar, because they have similar linguistic elements.
That’s the beauty of embeddings. The complexity of the data is distilled into something that can be compared across a multi-dimensional space.
3. The Payload: Adding Context with Metadata
Sometimes you’re going to need more than just numbers to fully understand or refine a search. While the dimensions capture the essence of the data, the payload holds metadata for structured information.
It could be textual data like descriptions, tags, categories, or it could be numerical values like dates or prices. This extra information is vital when you want to filter or rank search results based on criteria that aren’t directly encoded in the vector.
This metadata is invaluable when you need to apply additional filters or sorting criteria.
For example, if you’re searching for a picture of a dog, the vector helps the database find images that are visually similar. But let’s say you want results showing only images taken within the last year, or those tagged with “vacation.”
The payload can help you narrow down those results by ignoring vectors that don’t match your query vector filtering criteria. If you want the full picture of how filtering works in Qdrant, check out our Complete Guide to Filtering.
The Architecture of a Vector Database
A vector database is made of multiple different entities and relations. Let’s understand a bit of what’s happening here:
Collections
A collection is essentially a group of vectors (or “points”) that are logically grouped together based on similarity or a specific task. Every vector within a collection shares the same dimensionality and can be compared using a single metric. Avoid creating multiple collections unless necessary; instead, consider techniques like sharding for scaling across nodes or multitenancy for handling different use cases within the same infrastructure.
Distance Metrics
These metrics defines how similarity between vectors is calculated. The choice of distance metric is made when creating a collection and the right choice depends on the type of data you’re working with and how the vectors were created. Here are the three most common distance metrics:
Euclidean Distance: The straight-line path. It’s like measuring the physical distance between two points in space. Pick this one when the actual distance (like spatial data) matters.
Cosine Similarity: This one is about the angle, not the length. It measures how two vectors point in the same direction, so it works well for text or documents when you care more about meaning than magnitude. For example, if two things are similar, opposite, or unrelated:
- Dot Product: This looks at how much two vectors align. It’s popular in recommendation systems where you’re interested in how much two things “agree” with each other.
RAM-Based and Memmap Storage
By default, Qdrant stores vectors in RAM, delivering incredibly fast access for datasets that fit comfortably in memory. But when your dataset exceeds RAM capacity, Qdrant offers Memmap as an alternative.
Memmap allows you to store vectors on disk, yet still access them efficiently by mapping the data directly into memory if you have enough RAM. To enable it, you only need to set "on_disk": true
when you are creating a collection:
from qdrant_client import QdrantClient, models
client = QdrantClient(url='http://localhost:6333')
client.create_collection(
collection_name="{collection_name}",
vectors_config=models.VectorParams(
size=768, distance=models.Distance.COSINE, on_disk=True
),
)
For other configurations like hnsw_config.on_disk
or memmap_threshold
, see the Qdrant documentation for Storage.
SDKs
Qdrant offers a range of SDKs. You can use the programming language you’re most comfortable with, whether you’re coding in Python, Go, Rust, Javascript/Typescript, C# or Java.
The Core Functionalities of Vector Databases
When you think of a traditional database, the operations are familiar: you create, read, update, and delete records. These are the fundamentals. And guess what? In many ways, vector databases work the same way, but the operations are translated for the complexity of vectors.
1. Indexing: HNSW Index and Sending Data to Qdrant
Indexing your vectors is like creating an entry in a traditional database. But for vector databases, this step is very important. Vectors need to be indexed in a way that makes them easy to search later on.
HNSW (Hierarchical Navigable Small World) is a powerful indexing algorithm that most vector databases rely on to organize vectors for fast and efficient search.
It builds a multi-layered graph, where each vector is a node and connections represent similarity. The higher layers connect broadly similar vectors, while lower layers link vectors that are closely related, making searches progressively more refined as they go deeper.
When you run a search, HNSW starts at the top, quickly narrowing down the search by hopping between layers. It focuses only on relevant vectors as it goes deeper, refining the search with each step.
1.1 Payload Indexing
In Qdrant, indexing is modular. You can configure indexes for both vectors and payloads independently. The payload index is responsible for optimizing filtering based on metadata. Each payload index is built for a specific field and allows you to quickly filter vectors based on specific conditions.
You need to build the payload index for each field you’d like to search. The magic here is in the combination: HNSW finds similar vectors, and the payload index makes sure only the ones that fit your criteria come through. Learn more about Qdrant’s Filterable HNSW and why it was built like this.
Combining full-text search with vector-based search gives you even more versatility. You can simultaneously search for conceptually similar documents while ensuring specific keywords are present, all within the same query.
2. Searching: Approximate Nearest Neighbors (ANN) Search
Similarity search allows you to search by meaning. This way you can do searches such as similar songs that evoke the same mood, finding images that match your artistic vision, or even exploring emotional patterns in text.
The way it works is, when the user queries the database, this query is also converted into a vector. The algorithm quickly identifies the area of the graph likely to contain vectors closest to the query vector.
The search then moves down progressively narrowing down to more closely related and relevant vectors. Once the closest vectors are identified at the bottom layer, these points translate back to actual data, representing your top-scored documents.
Here’s a high-level overview of this process:
3. Updating Vectors: Real-Time and Bulk Adjustments
Data isn’t static, and neither are vectors. Keeping your vectors up to date is crucial for maintaining relevance in your searches.
Vector updates don’t always need to happen instantly, but when they do, Qdrant handles real-time modifications efficiently with a simple API call:
client.upsert(
collection_name='product_collection',
points=[PointStruct(id=product_id, vector=new_vector, payload=new_payload)]
)
For large-scale changes, like re-indexing vectors after a model update, batch updating allows you to update multiple vectors in one operation without impacting search performance:
batch_of_updates = [
PointStruct(id=product_id_1, vector=updated_vector_1, payload=new_payload_1),
PointStruct(id=product_id_2, vector=updated_vector_2, payload=new_payload_2),
# Add more points...
]
client.upsert(
collection_name='product_collection',
points=batch_of_updates
)
4. Deleting Vectors: Managing Outdated and Duplicate Data
Efficient vector management is key to keeping your searches accurate and your database lean. Deleting vectors that represent outdated or irrelevant data, such as expired products, old news articles, or archived profiles, helps maintain both performance and relevance.
In Qdrant, removing vectors is straightforward, requiring only the vector IDs to be specified:
client.delete(
collection_name='data_collection',
points_selector=[point_id_1, point_id_2]
)
You can use deletion to remove outdated data, clean up duplicates, and manage the lifecycle of vectors by automatically deleting them after a set period to keep your dataset relevant and focused.
Dense vs. Sparse Vectors
Now that you understand what vectors are and how they are created, let’s learn more about the two possible types of vectors you can use: dense or sparse. The main difference between the two are:
1. Dense Vectors
Dense vectors are, quite literally, dense with information. Every element in the vector contributes to the semantic meaning, relationships and nuances of the data. A dense vector representation of this sentence might look like this:
Each number holds weight. Together, they convey the overall meaning of the sentence, and are better for identifying contextually similar items, even if the words don’t match exactly.
2. Sparse Vectors
Sparse vectors operate differently. They focus only on the essentials. In most sparse vectors, a large number of elements are zeros. When a feature or token is present, it’s marked—otherwise, zero.
In the image, you can see a sentence, “I love Vector Similarity,” broken down into tokens like “i,” “love,” “vector” through tokenization. Each token is assigned a unique ID
from a large vocabulary. For example, “i” becomes 193
, and “vector” becomes 15012
.
Sparse vectors, are used for exact matching and specific token-based identification. The values on the right, such as 193: 0.04
and 9182: 0.12
, are the scores or weights for each token, showing how relevant or important each token is in the context. The final result is a sparse vector:
{
193: 0.04,
9182: 0.12,
15012: 0.73,
6731: 0.69,
454: 0.21
}
Everything else in the vector space is assumed to be zero.
Sparse vectors are ideal for tasks like keyword search or metadata filtering, where you need to check for the presence of specific tokens without needing to capture the full meaning or context. They suited for exact matches within the data itself, rather than relying on external metadata, which is handled by payload filtering.
Benefits of Hybrid Search
Sometimes context alone isn’t enough. Sometimes you need precision, too. Dense vectors are fantastic when you need to retrieve results based on the context or meaning behind the data. Sparse vectors are useful when you also need keyword or specific attribute matching.
With hybrid search you don’t have to choose one over the other and use both to get searches that are more relevant and filtered.
To achieve this balance, Qdrant uses normalization and fusion techniques to blend results from multiple search methods. One common approach is Reciprocal Rank Fusion (RRF), where results from different methods are merged, giving higher importance to items ranked highly by both methods. This ensures that the best candidates, whether identified through dense or sparse vectors, appear at the top of the results.
Qdrant combines dense and sparse vector results through a process of normalization and fusion.
How to Use Hybrid Search in Qdrant
Qdrant makes it easy to implement hybrid search through its Query API. Here’s how you can make it happen in your own project:
Example Hybrid Query: Let’s say a researcher is looking for papers on NLP, but the paper must specifically mention “transformers” in the content:
search_query = {
"vector": query_vector, # Dense vector for semantic search
"filter": { # Filtering for specific terms
"must": [
{"key": "text", "match": "transformers"} # Exact keyword match in the paper
]
}
}
In this query the dense vector search finds papers related to the broad topic of NLP and the sparse vector filtering ensures that the papers specifically mention “transformers”.
This is just a simple example and there’s so much more you can do with it. See our complete article on Hybrid Search guide to see what’s happening behind the scenes and all the possibilities when building a hybrid search system.
Quantization: Get 40x Faster Results
As your vector dataset grows larger, so do the computational demands of searching through it.
Quantized vectors are much smaller and easier to compare. With methods like Binary Quantization, you can see search speeds improve by up to 40x while memory usage decreases by 32x. Improvements that can be decisive when dealing with large datasets or needing low-latency results.
It works by converting high-dimensional vectors, which typically use 4 bytes
per dimension, into binary representations, using just 1 bit
per dimension. Values above zero become “1”, and everything else becomes “0”.
Quantization reduces data precision, and yes, this does lead to some loss of accuracy. However, for binary quantization, OpenAI embeddings achieves this performance improvement at a cost of only 5% of accuracy. If you apply techniques like oversampling and rescoring, this loss can be brought down even further.
However, binary quantization isn’t the only available option. Techniques like Scalar Quantization and Product Quantization are also popular alternatives when optimizing vector compression.
You can set up your chosen quantization method using the quantization_config
parameter when creating a new collection:
client.create_collection(
collection_name="{collection_name}",
vectors_config=models.VectorParams(
size=1536,
distance=models.Distance.COSINE
),
# Choose your preferred quantization method
quantization_config=models.BinaryQuantization(
binary=models.BinaryQuantizationConfig(
always_ram=True, # Store the quantized vectors in RAM for faster access
),
),
)
You can store original vectors on disk within the vectors_config
by setting on_disk=True
to save RAM space, while keeping quantized vectors in RAM for faster access
We recommend checking out our Vector Quantization guide for a full breakdown of methods and tips on optimizing performance for your specific use case.
Distributed Deployment
When thinking about scaling, the key factors to consider are fault tolerance, load balancing, and availability. One node, no matter how powerful, can only take you so far. Eventually, you’ll need to spread the workload across multiple machines to ensure the system remains fast and stable.
Sharding: Distributing Data Across Nodes
In a distributed Qdrant cluster, data is split into smaller units called shards, which are distributed across different nodes. which helps balance the load and ensures that queries can be processed in parallel.
Each collection—a group of related data points—can be split into non-overlapping subsets, which are then managed by different nodes.
Raft Consensus ensures that all the nodes stay in sync and have a consistent view of the data. Each node knows where every shard is, and Raft ensures that all nodes are in sync. If one node fails, the others know where the missing data is located and can take over.
By default, the number of shards in your Qdrant system matches the number of nodes in your cluster. But if you need more control, you can choose the shard_number
manually when creating a collection.
client.create_collection(
collection_name="{collection_name}",
vectors_config=models.VectorParams(size=300, distance=models.Distance.COSINE),
shard_number=4, # Custom number of shards
)
There are two main types of sharding:
- Automatic Sharding: Points (vectors) are automatically distributed across shards using consistent hashing. Each shard contains non-overlapping subsets of the data.
- User-defined Sharding: Specify how points are distributed, enabling more control over your data organization, especially for use cases like multitenancy, where each tenant (a user, client, or organization) has their own isolated data.
Each shard is divided into segments. They are a smaller storage unit within a shard, storing a subset of vectors and their associated payloads (metadata). When a query is executed, it targets the only relevant segments, processing them in parallel.
Replication: High Availability and Data Integrity
You don’t want a single failure to take down your system, right? Replication keeps multiple copies of the same data across different nodes to ensure high availability.
In Qdrant, Replica Sets manage these copies of shards across different nodes. If one replica becomes unavailable, others are there to take over and keep the system running. Whether the data is local or remote is mainly influenced by how you’ve configured the cluster.
When a query is made, if the relevant data is stored locally, the local shard handles the operation. If the data is on a remote shard, it’s retrieved via gRPC.
You can control how many copies you want with the replication_factor
. For example, creating a collection with 4 shards and a replication factor of 2 will result in 8 physical shards distributed across the cluster:
client.create_collection(
collection_name="{collection_name}",
vectors_config=models.VectorParams(size=300, distance=models.Distance.COSINE),
shard_number=4,
replication_factor=2,
)
We recommend using sharding and replication together so that your data is both split across nodes and replicated for availability.
For more details on features like user-defined sharding, node failure recovery, and consistency guarantees, see our guide on Distributed Deployment.
Multitenancy: Data Isolation for Multi-Tenant Architectures
Sharding efficiently distributes data across nodes, while replication guarantees redundancy and fault tolerance. But what happens when you’ve got multiple clients or user groups, and you need to keep their data isolated within the same infrastructure?
Multitenancy allows you to keep data for different tenants (users, clients, or organizations) isolated within a single cluster. Instead of creating separate collections for Tenant 1
and Tenant 2
, you store their data in the same collection but tag each vector with a group_id
to identify which tenant it belongs to.
In the backend, Qdrant can store Tenant 1
’s data in Shard 1 located in Canada (perhaps for compliance reasons like GDPR), while Tenant 2
’s data is stored in Shard 2 located in Germany. The data will be physically separated but still within the same infrastructure.
To implement this, you tag each vector with a tenant-specific group_id
during the upsert operation:
client.upsert(
collection_name="tenant_data",
points=[models.PointStruct(
id=2,
payload={"group_id": "tenant_1"},
vector=[0.1, 0.9, 0.1]
)],
shard_key_selector="canada"
)
Each tenant’s data remains isolated while still benefiting from the shared infrastructure. Optimizing for data privacy, compliance with local regulations, and scalability, without the need to create excessive collections or maintain separate clusters for each tenant.
If you want to learn more about working with a multitenant setup in Qdrant, you can check out our Multitenancy and Custom Sharding dedicated guide.
Data Security and Access Control
A common security risk in vector databases is the possibility of embedding inversion attacks, where attackers could reconstruct the original data from embeddings. There are many layers of protection you can use to secure your instance that are very important before getting your vector database into production.
For quick security in simpler use cases, you can use the API key authentication. To enable it, set up the API key in the configuration or environment variable.
service:
api_key: your_secret_api_key_here
enable_tls: true # Make sure to enable TLS to protect the API key from being exposed
Once this is set up, remember to include the API key in all your requests:
from qdrant_client import QdrantClient
client = QdrantClient(
url="https://localhost:6333",
api_key="your_secret_api_key_here"
)
In more advanced setups, Qdrant uses JWT (JSON Web Tokens) to enforce Role-Based Access Control (RBAC).
RBAC defines roles and assigns permissions, while JWT securely encodes these roles into tokens. Each request is validated against the user’s JWT, ensuring they can only access or modify data based on their assigned permissions.
You can easily setup your access tokens and secure access to sensitive data through the Qdrant Web UI:
By default, Qdrant instances are unsecured, so it’s important to configure security measures before moving to production. To learn more about how to configure security for your Qdrant instance and other advanced options, please check out the official Qdrant documentation on security.
Time to Experiment
As we’ve seen in this article, a vector database is definitely not just a database as we traditionally know it. It opens up a world of possibilities, from advanced similarity search to hybrid search that allows content retrieval with both context and precision.
But there’s no better way to learn than by doing. Try building a semantic search engine or experiment deploying a hybrid search service from zero. You’ll realize there are endless ways you can take advantage of vectors.
You can also watch our video tutorial and get started with Qdrant to generate semantic search results and recommendations from a sample dataset.
Phew! I hope you found some of the concepts here useful. If you have any questions feel free to send them in our Discord Community where our team will be more than happy to help you out!
Remember, don’t get lost in vector space! 🚀
```

---

## 5. What is Vector Quantization?

- 日期: 2024-09-25 09:29
- 链接: https://qdrant.tech/articles/what-is-vector-quantization/

```
Vector quantization is a data compression technique used to reduce the size of high-dimensional data. Compressing vectors reduces memory usage while maintaining nearly all of the essential information. This method allows for more efficient storage and faster search operations, particularly in large datasets. 
 When working with high-dimensional vectors, such as embeddings from providers like OpenAI, a single 1536-dimensional vector requires 6 KB of memory . 
 With 1 million vectors needing around 6 GB of memory, as your dataset grows to multiple millions of vectors , the memory and processing demands increase significantly.
```

---

## 6. Fine-Tuning Sparse Embeddings for E-Commerce Search | Part 1: Why Sparse Embeddings Beat BM25

- 日期: 2026-03-09 00:00
- 链接: https://qdrant.tech/articles/sparse-embeddings-ecommerce-part-1/

```
This is Part 1 of a 5-part series on fine-tuning sparse embeddings for e-commerce search. We’ll go from “why bother?” to a production system that beats BM25 by 29%. 
 Series: 
 Part 1: Why Sparse Embeddings Beat BM25 (here) 
 Part 2: Training on Modal 
 Part 3: Evaluation & Hard Negatives 
 Part 4: Specialization vs Generalization 
 Part 5: From Research to Product 
 Search “iPhone 15 Pro Max 256GB” on a dense embedding system and it happily returns the 128GB model. The semantic similarity is high - it’s the same phone! But the customer specified 256GB for a reason. In e-commerce, the details aren’t noise. They’re the whole point.
```

---

## 7. Vector Search Resource Optimization Guide

- 日期: 2025-02-09 00:00
- 链接: https://qdrant.tech/articles/vector-search-resource-optimization/

```
Vector Search Resource Optimization Guide
David Myriel
·February 09, 2025
What’s in This Guide?
Resource Management Strategies: If you are trying to scale your app on a budget - this is the guide for you. We will show you how to avoid wasting compute resources and get the maximum return on your investment.
Performance Improvement Tricks: We’ll dive into advanced techniques like indexing, compression, and partitioning. Our tips will help you get better results at scale, while reducing total resource expenditure.
Query Optimization Methods: Improving your vector database setup isn’t just about saving costs. We’ll show you how to build search systems that deliver consistently high precision while staying adaptable.
Remember: Optimization is a Balancing Act
In this guide, we will show you how to use Qdrant’s features to meet your performance needs. However - there are resource tradeoffs and you can’t have it all. It is up to you to choose the optimization strategy that best fits your goals.
Let’s take a look at some common goals and optimization strategies:
After this article, check out the code samples in our docs on Qdrant’s Optimization Methods.
Configure Indexing for Faster Searches
A vector index is the central location where Qdrant calculates vector similarity. It is the backbone of your search process, retrieving relevant results from vast amounts of data.
Qdrant uses the HNSW (Hierarchical Navigable Small World Graph) algorithm as its dense vector index, which is both powerful and scalable.
Figure 2: A sample HNSW vector index with three layers. Follow the blue arrow on the top layer to see how a query travels throughout the database index. The closest result is on the bottom level, nearest to the gray query point.
Vector Index Optimization Parameters
Working with massive datasets that contain billions of vectors demands significant resources—and those resources come with a price. While Qdrant provides reasonable defaults, tailoring them to your specific use case can unlock optimal performance. Here’s what you need to know.
The following parameters give you the flexibility to fine-tune Qdrant’s performance for your specific workload. You can modify them directly in Qdrant’s configuration files or at the collection and named vector levels for more granular control.
Figure 3: A description of three key HNSW parameters.
1. The m
parameter determines edges per node
This controls the number of edges in the graph. A higher value enhances search accuracy but demands more memory and build time. Fine-tune this to balance memory usage and precision.
2. The ef_construct
parameter controls the index build range
This parameter sets how many neighbors are considered during index construction. A larger value improves the accuracy of the index but increases the build time. Use this to customize your indexing speed versus quality.
You need to set both the m
and ef parameters
as you create the collection:
client.update_collection(
collection_name="{collection_name}",
vectors_config={
"my_vector": models.VectorParamsDiff(
hnsw_config=models.HnswConfigDiff(
m=32,
ef_construct=123,
),
),
}
)
3. The ef
parameter updates vector search range
This determines how many neighbors are evaluated during a search query. You can adjust this to balance query speed and accuracy.
The ef
parameter is configured during the search process:
client.query_points(
collection_name="{collection_name}",
query=[...]
search_params=models.SearchParams(hnsw_ef=128, exact=False),
)
These are just the basics of HNSW. Learn More about Indexing.
Data Compression Techniques
Efficient data compression is a cornerstone of resource optimization in vector databases. By reducing memory usage, you can achieve faster query performance without sacrificing too much accuracy.
One powerful technique is quantization, which transforms high-dimensional vectors into compact representations while preserving relative similarity. Let’s explore the quantization options available in Qdrant.
Scalar Quantization
Scalar quantization strikes an excellent balance between compression and performance, making it the go-to choice for most use cases.
This method minimizes the number of bits used to represent each vector component. For instance, Qdrant compresses 32-bit floating-point values (float32) into 8-bit unsigned integers (uint8), slashing memory usage by an impressive 75%.
Figure 4: The top example shows a float32 vector with a size of 40 bytes. Converting it to int8 format reduces its size by a factor of four, while maintaining approximate similarity relationships between vectors. The loss in precision compared to the original representation is typically negligible for most practical applications.
Benefits of Scalar Quantization:
Set it up as you create the collection:
client.create_collection(
collection_name="{collection_name}",
vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE),
quantization_config=models.ScalarQuantization(
scalar=models.ScalarQuantizationConfig(
type=models.ScalarType.INT8,
quantile=0.99,
always_ram=True,
),
),
)
When working with Qdrant, you can fine-tune the quantization configuration to optimize precision, memory usage, and performance. Here’s what the key configuration options include:
Adjust these settings to strike the right balance between precision and efficiency for your specific workload.
Learn More about Scalar Quantization
Binary Quantization
Binary quantization takes scalar quantization to the next level by compressing each vector component into just a single bit. This method achieves unparalleled memory efficiency and query speed, reducing memory usage by a factor of 32 and enabling searches up to 40x faster.
Benefits of Binary Quantization:
Binary quantization is ideal for large-scale datasets and compatible embedding models, where compression and speed are paramount.
Figure 5: This method causes maximum compression. It reduces memory usage by 32x and speeds up searches by up to 40x.
Here’s how you can enable binary quantization in Qdrant:
client.create_collection(
collection_name="{collection_name}",
vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE),
quantization_config=models.BinaryQuantization(
binary=models.BinaryQuantizationConfig(
always_ram=True,
),
),
)
By default, quantized vectors load like original vectors unless you set
always_ram
toTrue
for instant access and faster queries.
Learn more about Binary Quantization
Scaling the Database
Efficiently managing large datasets in distributed systems like Qdrant requires smart strategies for data isolation. Multitenancy and Sharding are essential tools to help you handle high volumes of user-specific data while maintaining performance and scalability.
Multitenancy
Multitenancy is a software architecture where multiple independent users (or tenants) share the same resources or environment. In Qdrant, a single collection with logical partitioning is often the most efficient setup for multitenant use cases.
Figure 5: Each individual vector is assigned a specific payload that denotes which tenant it belongs to. This is how a large number of different tenants can share a single Qdrant collection.
Why Choose Multitenancy?
- Logical Isolation: Ensures each tenant’s data remains separate while residing in the same collection.
- Minimized Overhead: Reduces resource consumption compared to maintaining separate collections for each user.
- Scalability: Handles high user volumes without compromising performance.
Here’s how you can implement multitenancy efficiently in Qdrant:
client.create_payload_index(
collection_name="{collection_name}",
field_name="group_id",
field_schema=models.KeywordIndexParams(
type="keyword",
is_tenant=True,
),
)
Creating a keyword payload index, with the is_tenant
parameter set to True
, modifies the way the vectors will be logically stored. Storage structure will be organized to co-locate vectors of the same tenant together.
Now, each point stored in Qdrant should have the group_id
payload attribute set:
client.upsert(
collection_name="{collection_name}",
points=[
models.PointStruct(
id=1,
payload={"group_id": "user_1"},
vector=[0.9, 0.1, 0.1],
),
models.PointStruct(
id=2,
payload={"group_id": "user_2"},
vector=[0.5, 0.9, 0.4],
)
]
)
To ensure proper data isolation in a multitenant environment, you can assign a unique identifier, such as a group_id, to each vector. This approach ensures that each user’s data remains segregated, allowing users to access only their own data. You can further enhance this setup by applying filters during queries to restrict access to the relevant data.
Learn More about Multitenancy
Sharding
Sharding is a critical strategy in Qdrant for splitting collections into smaller units, called shards, to efficiently distribute data across multiple nodes. It’s a powerful tool for improving scalability and maintaining performance in large-scale systems.
User-Defined Sharding:
User-Defined Sharding allows you to take control of data placement by specifying a shard key. This feature is particularly useful in multi-tenant setups, as it enables the isolation of each tenant’s data within separate shards, ensuring better organization and enhanced data security.
Figure 6: Users can both upsert and query shards that are relevant to them, all within the same collection. Regional sharding can help avoid cross-continental traffic.
Example:
client.create_collection(
collection_name="my_custom_sharded_collection",
shard_number=1,
sharding_method=models.ShardingMethod.CUSTOM
)
client.create_shard_key("my_custom_sharded_collection", "tenant_id")
When implementing user-defined sharding in Qdrant, two key parameters are critical to achieving efficient data distribution:
Shard Key:
The shard key determines how data points are distributed across shards. For example, using a key like
tenant_id
allows you to control how Qdrant partitions the data. Each data point added to the collection will be assigned to a shard based on the value of this key, ensuring logical isolation of data.Shard Number:
This defines the total number of physical shards for each shard key, influencing resource allocation and query performance.
Here’s how you can add a data point to a collection with user-defined sharding:
client.upsert(
collection_name="my_custom_sharded_collection",
points=[
models.PointStruct(
id=1111,
vector=[0.1, 0.2, 0.3]
)
],
shard_key_selector="tenant_1"
)
This code assigns the point to a specific shard based on the tenant_1
shard key, ensuring proper data placement.
Here’s how to choose the shard_number:
Learn more about Sharding in Distributed Deployment
Query Optimization
Improving vector database performance is critical when dealing with large datasets and complex queries. By leveraging techniques like filtering, batch processing, reranking, rescoring, and oversampling, so you can ensure fast response times and maintain efficiency even at scale.
Filtering
Filtering allows you to select only the required fields in your query results. By limiting the output size, you can significantly reduce response time and improve performance.
The filterable vector index is Qdrant’s solves pre and post-filtering problems by adding specialized links to the search graph. It aims to maintain the speed advantages of vector search while allowing for precise filtering, addressing the inefficiencies that can occur when applying filters after the vector search.
Example:
results = client.search(
collection_name="my_collection",
query_vector=[0.1, 0.2, 0.3],
query_filter=models.Filter(must=[
models.FieldCondition(
key="category",
match=models.MatchValue(value="my-category-name"),
)
]),
limit=10,
)
Figure 7: The filterable vector index adds specialized links to the search graph to speed up traversal.
Filterable vector index: This technique builds additional links (orange) between leftover data points. The filtered points which stay behind are now traversible once again. Qdrant uses special category-based methods to connect these data points.
Read more about Filtering Docs and check out the Complete Filtering Guide.
Batch Processing
Batch processing consolidates multiple operations into a single execution cycle, reducing request overhead and enhancing throughput. It’s an effective strategy for both data insertion and query execution.
Batch Insertions: Instead of inserting vectors individually, group them into medium-sized batches to minimize the number of database requests and the overhead of frequent writes.
Example:
vectors = [
[.1, .0, .0, .0],
[.0, .1, .0, .0],
[.0, .0, .1, .0],
[.0, .0, .0, .1],
…
]
client.upload_collection(
collection_name="test_collection",
vectors=vectors,
)
This reduces write operations and ensures faster data ingestion.
Batch Queries: Similarly, you can batch multiple queries together rather than executing them one by one. This reduces the number of round trips to the database, optimizing performance and reducing latency.
Example:
results = client.search_batch(
collection_name="test_collection",
requests=[
SearchRequest(
vector=[0., 0., 2., 0.],
limit=1,
),
SearchRequest(
vector=[0., 0., 0., 0.01],
with_vector=True,
limit=2,
)
]
)
Batch queries are particularly useful when processing a large number of similar queries or when handling multiple user requests simultaneously.
Hybrid Search
Hybrid search combines keyword filtering with vector similarity search, enabling faster and more precise results. Keywords help narrow down the dataset quickly, while vector similarity ensures semantic accuracy. This search method combines dense and sparse vectors.
Hybrid search in Qdrant uses both fusion and reranking. The former is about combining the results from different search methods, based solely on the scores returned by each method. That usually involves some normalization, as the scores returned by different methods might be in different ranges.
Figure 8: Hybrid Search Architecture
After that, there is a formula that takes the relevancy measures and calculates the final score that we use later on to reorder the documents. Qdrant has built-in support for the Reciprocal Rank Fusion method, which is the de facto standard in the field.
Learn more about Hybrid Search and read out Hybrid Queries docs.
Oversampling
Oversampling is a technique that helps compensate for any precision lost due to quantization. Since quantization simplifies vectors, some relevant matches could be missed in the initial search. To avoid this, you can retrieve more candidates, increasing the chances that the most relevant vectors make it into the final results.
You can control the number of extra candidates by setting an oversampling
parameter. For example, if your desired number of results (limit
) is 4 and you set an oversampling
factor of 2, Qdrant will retrieve 8 candidates (4 × 2).
You can adjust the oversampling factor to control how many extra vectors Qdrant includes in the initial pool. More candidates mean a better chance of obtaining high-quality top-K results, especially after rescoring with the original vectors.
Learn more about Oversampling.
Rescoring
After oversampling to gather more potential matches, each candidate is re-evaluated based on additional criteria to ensure higher accuracy and relevance to the query.
The rescoring process maps the quantized vectors to their corresponding original vectors, allowing you to consider factors like context, metadata, or additional relevance that wasn’t included in the initial search, leading to more accurate results.
Example of Rescoring and Oversampling::
client.query_points(
collection_name="my_collection",
query_vector=[0.22, -0.01, -0.98, 0.37],
search_params=models.SearchParams(
quantization=models.QuantizationSearchParams(
rescore=True, # Enables rescoring with original vectors
oversampling=2 # Retrieves extra candidates for rescoring
)
),
limit=4 # Desired number of final results
)
Learn more about Rescoring.
Reranking
Reranking adjusts the order of search results based on additional criteria, ensuring the most relevant results are prioritized.
This method is about taking the results from different search methods and reordering them based on some additional processing using the content of the documents, not just the scores. This processing may rely on an additional neural model, such as a cross-encoder which would be inefficient enough to be used on the whole dataset.
These methods are practically applicable only when used on a smaller subset of candidates returned by the faster search methods. Late interaction models, such as ColBERT, are way more efficient in this case, as they can be used to rerank the candidates without the need to access all the documents in the collection.
Example:
client.query_points(
"collection-name",
prefetch=prefetch, # Previous results
query=late_vectors, # Colbert converted query
using="colbertv2.0",
with_payload=True,
limit=10,
)
Learn more about Reranking.
Storage: Disk vs RAM
Which Disk Type?
Local SSDs are recommended for optimal performance, as they provide the fastest query response times with minimal latency. While network-attached storage is also viable, it typically introduces additional latency that can affect performance, so local SSDs are preferred when possible, particularly for workloads requiring high-speed random access.
Memory Management for Vectors and Payload
As your data scales, effective resource management becomes crucial to keeping costs low while ensuring your application remains reliable and performant. One of the key areas to focus on is memory management.
Understanding how Qdrant handles memory can help you make informed decisions about scaling your vector database. Qdrant supports two main methods for storing vectors:
1. In-Memory Storage
- How it works: All data is stored in RAM, providing the fastest access times for queries and operations.
- When to use it: This setup is ideal for applications where performance is critical, and your RAM capacity can accommodate all data.
- Advantages: Maximum speed for queries and updates.
- Limitations: RAM usage can become a bottleneck as your dataset grows.
2. Memmap Storage
- How it works: Instead of loading all data into memory, memmap storage maps data files directly to a virtual address space on disk. The system’s page cache handles data access, making it highly efficient.
- When to use it: Perfect for storing large collections that exceed your available RAM while still maintaining near in-memory performance when enough RAM is available.
- Advantages: Balances performance and memory usage, allowing you to work with datasets larger than your physical RAM.
- Limitations: Slightly slower than pure in-memory storage but significantly more scalable.
To enable memmap vector storage in Qdrant, you can set the on_disk parameter to true
when creating or updating a collection.
client.create_collection(
collection_name="{collection_name}",
vectors_config=models.VectorParams(
…
on_disk=True
)
)
To do the same for payloads:
client.create_collection(
collection_name="{collection_name}",
on_disk_payload= True
)
The general guideline for selecting a storage method in Qdrant is to use InMemory storage when high performance is a priority, and sufficient RAM is available to accommodate the dataset. This approach ensures the fastest access speeds by keeping data readily accessible in memory.
However, for larger datasets or scenarios where memory is limited, Memmap and OnDisk storage are more suitable. These methods significantly reduce memory usage by storing data on disk while leveraging advanced techniques like page caching and indexing to maintain efficient and relatively fast data access.
Monitoring the Database
Continuous monitoring is essential for maintaining system health and identifying potential issues before they escalate. Tools like Prometheus and Grafana are widely used to achieve this.
- Prometheus: An open-source monitoring and alerting toolkit, Prometheus collects and stores metrics in a time-series database. It scrapes metrics from predefined endpoints and supports powerful querying and visualization capabilities.
- Grafana: Often paired with Prometheus, Grafana provides an intuitive interface for visualizing metrics and creating interactive dashboards.
Qdrant exposes metrics in the Prometheus/OpenMetrics format through the /metrics endpoint. Prometheus can scrape this endpoint to monitor various aspects of the Qdrant system.
For a local Qdrant instance, the metrics endpoint is typically available at:
http://localhost:6333/metrics
Here are some important metrics to monitor:
Read more about Qdrant Open Source Monitoring and Qdrant Cloud Monitoring for managed clusters.
Recap: When Should You Optimize?
Get the Cheatsheet
Want to download a printer-friendly version of this guide? Download it now..
```

---

## 8. A Complete Guide to Filtering in Vector Search

- 日期: 2024-09-10 00:00
- 链接: https://qdrant.tech/articles/vector-search-filtering/

```
A Complete Guide to Filtering in Vector Search
Sabrina Aquino, David Myriel
·September 10, 2024
Imagine you sell computer hardware. To help shoppers easily find products on your website, you need to have a user-friendly search engine.
If you’re selling computers and have extensive data on laptops, desktops, and accessories, your search feature should guide customers to the exact device they want - or at least a very similar match.
When storing data in Qdrant, each product is a point, consisting of an id
, a vector
and payload
:
{
"id": 1,
"vector": [0.1, 0.2, 0.3, 0.4],
"payload": {
"price": 899.99,
"category": "laptop"
}
}
The id
is a unique identifier for the point in your collection. The vector
is a mathematical representation of similarity to other points in the collection.
Finally, the payload
holds metadata that directly describes the point.
Though we may not be able to decipher the vector, we are able to derive additional information about the item from its metadata, In this specific case, we are looking at a data point for a laptop that costs $899.99.
What is filtering?
When searching for the perfect computer, your customers may end up with results that are mathematically similar to the search entry, but not exact. For example, if they are searching for laptops under $1000, a simple vector search without constraints might still show other laptops over $1000.
This is why semantic search alone may not be enough. In order to get the exact result, you would need to enforce a payload filter on the price
. Only then can you be sure that the search results abide by the chosen characteristic.
This is called filtering and it is one of the key features of vector databases.
Here is how a filtered vector search looks behind the scenes. We’ll cover its mechanics in the following section.
POST /collections/online_store/points/search
{
"vector": [ 0.2, 0.1, 0.9, 0.7 ],
"filter": {
"must": [
{
"key": "category",
"match": { "value": "laptop" }
},
{
"key": "price",
"range": {
"gt": null,
"gte": null,
"lt": null,
"lte": 1000
}
}
]
},
"limit": 3,
"with_payload": true,
"with_vector": false
}
The filtered result will be a combination of the semantic search and the filtering conditions imposed upon the query. In the following pages, we will show that filtering is a key practice in vector search for two reasons:
- With filtering in Qdrant, you can dramatically increase search precision. More on this in the next section.
- Filtering helps control resources and reduce compute use. More on this in Payload Indexing.
What you will learn in this guide:
In vector search, filtering and sorting are more interdependent than they are in traditional databases. While databases like SQL use commands such as WHERE
and ORDER BY
, the interplay between these processes in vector search is a bit more complex.
Most people use default settings and build vector search apps that aren’t properly configured or even setup for precise retrieval. In this guide, we will show you how to use filtering to get the most out of vector search with some basic and advanced strategies that are easy to implement.
Remember to run all tutorial code in Qdrant’s Dashboard
The easiest way to reach that “Hello World” moment is to try filtering in a live cluster. Our interactive tutorial will show you how to create a cluster, add data and try some filtering clauses.
Qdrant’s approach to filtering
Qdrant follows a specific method of searching and filtering through dense vectors.
Let’s take a look at this 3-stage diagram. In this case, we are trying to find the nearest neighbour to the query vector (green). Your search journey starts at the bottom (orange).
By default, Qdrant connects all your data points within the vector index. After you introduce filters, some data points become disconnected. Vector search can’t cross the grayed out area and it won’t reach the nearest neighbor. How can we bridge this gap?
Figure 1: How Qdrant maintains a filterable vector index.
Filterable vector index: This technique builds additional links (orange) between leftover data points. The filtered points which stay behind are now traversible once again. Qdrant uses special category-based methods to connect these data points.
Qdrant’s approach vs traditional filtering methods
The filterable vector index is Qdrant’s solves pre and post-filtering problems by adding specialized links to the search graph. It aims to maintain the speed advantages of vector search while allowing for precise filtering, addressing the inefficiencies that can occur when applying filters after the vector search.
Pre-filtering
In pre-filtering, a search engine first narrows down the dataset based on chosen metadata values, and then searches within that filtered subset. This reduces unnecessary computation over a dataset that is potentially much larger.
The choice between pre-filtering and using the filterable HNSW index depends on filter cardinality. When metadata cardinality is too low, the filter becomes restrictive and it can disrupt the connections within the graph. This leads to fragmented search paths (as in Figure 1). When the semantic search process begins, it won’t be able to travel to those locations.
However, Qdrant still benefits from pre-filtering under certain conditions. In cases of low cardinality, Qdrant’s query planner stops using HNSW and switches over to the payload index alone. This makes the search process much cheaper and faster than if using HNSW.
Figure 2: On the user side, this is how filtering looks. We start with five products with different prices. First, the $1000 price filter is applied, narrowing down the selection of laptops. Then, a vector search finds the relevant results within this filtered set.
In conclusion, pre-filtering is efficient in specific cases when you use small datasets with low cardinality metadata. However, pre-filtering should not be used over large datasets as it breaks too many links in the HNSW graph, causing lower accuracy.
Post-filtering
In post-filtering, a search engine first looks for similar vectors and retrieves a larger set of results. Then, it applies filters to those results based on metadata. The problem with post-filtering becomes apparent when using low-cardinality filters.
When you apply a low-cardinality filter after performing a vector search, you often end up discarding a large portion of the results that the vector search returned.
Figure 3: In the same example, we have five laptops. First, the vector search finds the top two relevant results, but they may not meet the price match. When the $1000 price filter is applied, other potential results are discarded.
The system will waste computational resources by first finding similar vectors and then discarding many that don’t meet the filter criteria. You’re also limited to filtering only from the initial set of vector search results. If your desired items aren’t in this initial set, you won’t find them, even if they exist in the database.
Basic filtering example: ecommerce and laptops
We know that there are three possible laptops that suit our price point. Let’s see how Qdrant’s filterable vector index works and why it is the best method of capturing all available results.
First, add five new laptops to your online store. Here is a sample input:
laptops = [
(1, [0.1, 0.2, 0.3, 0.4], {"price": 899.99, "category": "laptop"}),
(2, [0.2, 0.3, 0.4, 0.5], {"price": 1299.99, "category": "laptop"}),
(3, [0.3, 0.4, 0.5, 0.6], {"price": 799.99, "category": "laptop"}),
(4, [0.4, 0.5, 0.6, 0.7], {"price": 1099.99, "category": "laptop"}),
(5, [0.5, 0.6, 0.7, 0.8], {"price": 949.99, "category": "laptop"})
]
The four-dimensional vector can represent features like laptop CPU, RAM or battery life, but that isn’t specified. The payload, however, specifies the exact price and product category.
Now, set the filter to “price is less than $1000”:
{
"key": "price",
"range": {
"gt": null,
"gte": null,
"lt": null,
"lte": 1000
}
}
When a price filter of equal/less than $1000 is applied, vector search returns the following results:
[
{
"id": 3,
"score": 0.9978443564622781,
"payload": {
"price": 799.99,
"category": "laptop"
}
},
{
"id": 1,
"score": 0.9938079894227599,
"payload": {
"price": 899.99,
"category": "laptop"
}
},
{
"id": 5,
"score": 0.9903751498208603,
"payload": {
"price": 949.99,
"category": "laptop"
}
}
]
As you can see, Qdrant’s filtering method has a greater chance of capturing all possible search results.
This specific example uses the range
condition for filtering. Qdrant, however, offers many other possible ways to structure a filter
For detailed usage examples, filtering docs are the best resource.
Scrolling instead of searching
You don’t need to use our search
and query
APIs to filter through data. The scroll
API is another option that lets you retrieve lists of points which meet the filters.
If you aren’t interested in finding similar points, you can simply list the ones that match a given filter. While search gives you the most similar points based on some query vector, scroll will give you all points matching your filter not considering similarity.
In Qdrant, scrolling is used to iteratively retrieve large sets of points from a collection. It is particularly useful when you’re dealing with a large number of points and don’t want to load them all at once. Instead, Qdrant provides a way to scroll through the points one page at a time.
You start by sending a scroll request to Qdrant with specific conditions like filtering by payload, vector search, or other criteria.
Let’s retrieve a list of top 10 laptops ordered by price in the store:
POST /collections/online_store/points/scroll
{
"filter": {
"must": [
{
"key": "category",
"match": {
"value": "laptop"
}
}
]
},
"limit": 10,
"with_payload": true,
"with_vector": false,
"order_by": [
{
"key": "price",
}
]
}
The response contains a batch of points that match the criteria and a reference (offset or next page token) to retrieve the next set of points.
Scrolling is designed to be efficient. It minimizes the load on the server and reduces memory consumption on the client side by returning only manageable chunks of data at a time.
Available filtering conditions
All clauses and conditions are outlined in Qdrant’s filtering documentation.
Filtering clauses to remember
Advanced filtering example: dinosaur diets
We can also use nested filtering to query arrays of objects within the payload. In this example, we have two points. They each represent a dinosaur with a list of food preferences (diet) that indicate what type of food they like or dislike:
[
{
"id": 1,
"dinosaur": "t-rex",
"diet": [
{ "food": "leaves", "likes": false},
{ "food": "meat", "likes": true}
]
},
{
"id": 2,
"dinosaur": "diplodocus",
"diet": [
{ "food": "leaves", "likes": true},
{ "food": "meat", "likes": false}
]
}
]
To ensure that both conditions are applied to the same array element (e.g., food = meat and likes = true must refer to the same diet item), you need to use a nested filter.
Nested filters are used to apply conditions within an array of objects. They ensure that the conditions are evaluated per array element, rather than across all elements.
POST /collections/dinosaurs/points/scroll
{
"filter": {
"must": [
{
"key": "diet[].food",
"match": {
"value": "meat"
}
},
{
"key": "diet[].likes",
"match": {
"value": true
}
}
]
}
}
client.scroll(
collection_name="dinosaurs",
scroll_filter=models.Filter(
must=[
models.FieldCondition(
key="diet[].food", match=models.MatchValue(value="meat")
),
models.FieldCondition(
key="diet[].likes", match=models.MatchValue(value=True)
),
],
),
)
client.scroll("dinosaurs", {
filter: {
must: [
{
key: "diet[].food",
match: { value: "meat" },
},
{
key: "diet[].likes",
match: { value: true },
},
],
},
});
use qdrant_client::qdrant::{Condition, Filter, ScrollPointsBuilder};
client
.scroll(
ScrollPointsBuilder::new("dinosaurs").filter(Filter::must([
Condition::matches("diet[].food", "meat".to_string()),
Condition::matches("diet[].likes", true),
])),
)
.await?;
import java.util.List;
import static io.qdrant.client.ConditionFactory.match;
import static io.qdrant.client.ConditionFactory.matchKeyword;
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Common.Filter;
import io.qdrant.client.grpc.Points.ScrollPoints;
QdrantClient client =
new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());
client
.scrollAsync(
ScrollPoints.newBuilder()
.setCollectionName("dinosaurs")
.setFilter(
Filter.newBuilder()
.addAllMust(
List.of(matchKeyword("diet[].food", "meat"), match("diet[].likes", true)))
.build())
.build())
.get();
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;
var client = new QdrantClient("localhost", 6334);
await client.ScrollAsync(
collectionName: "dinosaurs",
filter: MatchKeyword("diet[].food", "meat") & Match("diet[].likes", true)
);
This happens because both points are matching the two conditions:
- the “t-rex” matches food=meat on
diet[1].food
and likes=true ondiet[1].likes
- the “diplodocus” matches food=meat on
diet[1].food
and likes=true ondiet[0].likes
To retrieve only the points where the conditions apply to a specific element within an array (such as the point with id 1 in this example), you need to use a nested object filter.
Nested object filters enable querying arrays of objects independently, ensuring conditions are checked within individual array elements.
This is done by using the nested
condition type, which consists of a payload key that targets an array and a filter to apply. The key should reference an array of objects and can be written with or without bracket notation (e.g., “data” or “data[]”).
POST /collections/dinosaurs/points/scroll
{
"filter": {
"must": [{
"nested": {
"key": "diet",
"filter":{
"must": [
{
"key": "food",
"match": {
"value": "meat"
}
},
{
"key": "likes",
"match": {
"value": true
}
}
]
}
}
}]
}
}
client.scroll(
collection_name="dinosaurs",
scroll_filter=models.Filter(
must=[
models.NestedCondition(
nested=models.Nested(
key="diet",
filter=models.Filter(
must=[
models.FieldCondition(
key="food", match=models.MatchValue(value="meat")
),
models.FieldCondition(
key="likes", match=models.MatchValue(value=True)
),
]
),
)
)
],
),
)
client.scroll("dinosaurs", {
filter: {
must: [
{
nested: {
key: "diet",
filter: {
must: [
{
key: "food",
match: { value: "meat" },
},
{
key: "likes",
match: { value: true },
},
],
},
},
},
],
},
});
use qdrant_client::qdrant::{Condition, Filter, NestedCondition, ScrollPointsBuilder};
client
.scroll(
ScrollPointsBuilder::new("dinosaurs").filter(Filter::must([NestedCondition {
key: "diet".to_string(),
filter: Some(Filter::must([
Condition::matches("food", "meat".to_string()),
Condition::matches("likes", true),
])),
}
.into()])),
)
.await?;
import java.util.List;
import static io.qdrant.client.ConditionFactory.match;
import static io.qdrant.client.ConditionFactory.matchKeyword;
import static io.qdrant.client.ConditionFactory.nested;
import io.qdrant.client.grpc.Common.Filter;
import io.qdrant.client.grpc.Points.ScrollPoints;
client
.scrollAsync(
ScrollPoints.newBuilder()
.setCollectionName("dinosaurs")
.setFilter(
Filter.newBuilder()
.addMust(
nested(
"diet",
Filter.newBuilder()
.addAllMust(
List.of(
matchKeyword("food", "meat"), match("likes", true)))
.build()))
.build())
.build())
.get();
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;
var client = new QdrantClient("localhost", 6334);
await client.ScrollAsync(
collectionName: "dinosaurs",
filter: Nested("diet", MatchKeyword("food", "meat") & Match("likes", true))
);
The matching logic is adjusted to operate at the level of individual elements within an array in the payload, rather than on all array elements together.
Nested filters function as though each element of the array is evaluated separately. The parent document will be considered a match if at least one array element satisfies all the nested filter conditions.
Other creative uses for filters
You can use filters to retrieve data points without knowing their id
. You can search through data and manage it, solely by using filters. Let’s take a look at some creative uses for filters:
Filtering with the payload index
When you start working with Qdrant, your data is by default organized in a vector index. In addition to this, we recommend adding a secondary data structure - the payload index.
Just how the vector index organizes vectors, the payload index will structure your metadata.
Figure 4: The payload index is an additional data structure that supports vector search. A payload index (in green) organizes candidate results by cardinality, so that semantic search (in red) can traverse the vector index quickly.
On its own, semantic searching over terabytes of data can take up lots of RAM. Filtering and Indexing are two easy strategies to reduce your compute usage and still get the best results. Remember, this is only a guide. For an exhaustive list of filtering options, you should read the filtering documentation.
Here is how you can create a single index for a metadata field “category”:
PUT /collections/computers/index
{
"field_name": "category",
"field_schema": "keyword"
}
from qdrant_client import QdrantClient
client = QdrantClient(url="http://localhost:6333")
client.create_payload_index(
collection_name="computers",
field_name="category",
field_schema="keyword",
)
Once you mark a field indexable, you don’t need to do anything else. Qdrant will handle all optimizations in the background.
Why should you index metadata?
The payload index acts as a secondary data structure that speeds up retrieval. Whenever you run vector search with a filter, Qdrant will consult a payload index - if there is one.
As your dataset grows in complexity, Qdrant takes up additional resources to go through all data points. Without a proper data structure, the search can take longer - or run out of resources.
Payload indexing helps evaluate the most restrictive filters
The payload index is also used to accurately estimate filter cardinality, which helps the query planning choose a search strategy. Filter cardinality refers to the number of distinct values that a filter can match within a dataset. Qdrant’s search strategy can switch from HNSW search to payload index-based search if the cardinality is too low.
How it affects your queries: Depending on the filter used in the search - there are several possible scenarios for query execution. Qdrant chooses one of the query execution options depending on the available indexes, the complexity of the conditions and the cardinality of the filtering result.
- The planner estimates the cardinality of a filtered result before selecting a strategy.
- Qdrant retrieves points using the payload index if cardinality is below threshold.
- Qdrant uses the filterable vector index if the cardinality is above a threshold
What happens if you don’t use payload indexes?
When using filters while querying, Qdrant needs to estimate cardinality of those filters to define a proper query plan. If you don’t create a payload index, Qdrant will not be able to do this. It may end up choosing a sub-optimal way of searching causing extremely slow search times or low accuracy results.
If you only rely on searching for the nearest vector, Qdrant will have to go through the entire vector index. It will calculate similarities against each vector in the collection, relevant or not. Alternatively, when you filter with the help of a payload index, the HSNW algorithm won’t have to evaluate every point. Furthermore, the payload index will help HNSW construct the graph with additional links.
How does the payload index look?
A payload index is similar to conventional document-oriented databases. It connects metadata fields with their corresponding point id’s for quick retrieval.
In this example, you are indexing all of your computer hardware inside of the computers
collection. Let’s take a look at a sample payload index for the field category
.
Payload Index by keyword:
+------------+-------------+
| category | id |
+------------+-------------+
| laptop | 1, 4, 7 |
| desktop | 2, 5, 9 |
| speakers | 3, 6, 8 |
| keyboard | 10, 11 |
+------------+-------------+
When fields are properly indexed, the search engine roughly knows where it can start its journey. It can start looking up points that contain relevant metadata, and it doesn’t need to scan the entire dataset. This reduces the engine’s workload by a lot. As a result, query results are faster and the system can easily scale.
You may create as many payload indexes as you want, and we recommend you do so for each field that you filter by.
If your users are often filtering by laptop when looking up a product category, indexing all computer metadata will speed up retrieval and make the results more precise.
Different types of payload indexes
Indexing payloads in multitenant setups
Some applications need to have data segregated, whereby different users need to see different data inside of the same program. When setting up storage for such a complex application, many users think they need multiple databases for segregated users.
We see this quite often. Users very frequently make the mistake of creating a separate collection for each tenant inside of the same cluster. This can quickly exhaust the cluster’s resources. Running vector search through too many collections can start using up too much RAM. You may start seeing out-of-memory (OOM) errors and degraded performance.
To mitigate this, we offer extensive support for multitenant systems, so that you can build an entire global application in one single Qdrant collection.
When creating or updating a collection, you can mark a metadata field as indexable. To mark user_id
as a tenant in a shared collection, do the following:
PUT /collections/{collection_name}/index
{
"field_name": "user_id",
"field_schema": {
"type": "keyword",
"is_tenant": true
}
}
Additionally, we offer a way of organizing data efficiently by means of the tenant index. This is another variant of the payload index that makes tenant data more accessible. This time, the request will specify the field as a tenant. This means that you can mark various customer types and user id’s as is_tenant: true
.
Read more about setting up tenant defragmentation in multitenant environments,
Key takeaways in filtering and indexing
Filtering with float-point (decimal) numbers
If you filter by the float data type, your search precision may be limited and inaccurate.
Float Datatype numbers have a decimal point and are 64 bits in size. Here is an example:
{
"price": 11.99
}
When you filter for a specific float number, such as 11.99, you may get a different result, like 11.98 or 12.00. With decimals, numbers are rounded differently, so logically identical values may appear different. Unfortunately, searching for exact matches can be unreliable in this case.
To avoid inaccuracies, use a different filtering method. We recommend that you try Range Based Filtering instead of exact matches. This method accounts for minor variations in data, and it boosts performance - especially with large datasets.
Here is a sample JSON range filter for values greater than or equal to 11.99 and less than or equal to the same number. This will retrieve any values within the range of 11.99, including those with additional decimal places.
{
"key": "price",
"range": {
"gt": null,
"gte": 11.99,
"lt": null,
"lte": 11.99
}
}
Working with pagination in queries
When you’re implementing pagination in filtered queries, indexing becomes even more critical. When paginating results, you often need to exclude items you’ve already seen. This is typically managed by applying filters that specify which IDs should not be included in the next set of results.
However, an interesting aspect of Qdrant’s data model is that a single point can have multiple values for the same field, such as different color options for a product. This means that during filtering, an ID might appear multiple times if it matches on different values of the same field.
Proper indexing ensures that these queries are efficient, preventing duplicate results and making pagination smoother.
Conclusion: Real-life use cases of filtering
Filtering in a vector database like Qdrant can significantly enhance search capabilities by enabling more precise and efficient retrieval of data.
As a conclusion to this guide, let’s look at some real-life use cases where filtering is crucial:
Before you go - all the code is in Qdrant’s Dashboard
The easiest way to reach that “Hello World” moment is to try filtering in a live cluster. Our interactive tutorial will show you how to create a cluster, add data and try some filtering clauses.
It’s all in your free cluster!
```

---

## 9. Qdrant Internals: Immutable Data Structures

- 日期: 2024-08-20 10:45
- 链接: https://qdrant.tech/articles/immutable-data-structures/

```
Data Structures 101 
 Those who took programming courses might remember that there is no such thing as a universal data structure.
Some structures are good at accessing elements by index (like arrays), while others shine in terms of insertion efficiency (like linked lists). 
 Hardware-optimized data structure 
 However, when we move from theoretical data structures to real-world systems, and particularly in performance-critical areas such as vector search , things become more complex. Big-O notation provides a good abstraction, but it doesn’t account for the realities of modern hardware: cache misses, memory layout, disk I/O, and other low-level considerations that influence actual performance.
```

---

## 10. Fine-Tuning Sparse Embeddings for E-Commerce Search | Part 2: Training SPLADE on Modal

- 日期: 2026-03-09 00:00
- 链接: https://qdrant.tech/articles/sparse-embeddings-ecommerce-part-2/

```
This is Part 2 of a 5-part series on fine-tuning sparse embeddings for e-commerce search. In Part 1 , we covered why sparse embeddings beat BM25 for e-commerce. Now we build the training pipeline. 
 Series: 
 Part 1: Why Sparse Embeddings Beat BM25 
 Part 2: Training SPLADE on Modal (here) 
 Part 3: Evaluation & Hard Negatives 
 Part 4: Specialization vs Generalization 
 Part 5: From Research to Product 
 In the last article we made the case for sparse embeddings in e-commerce search. Now we write the code. All source code is available in the GitHub repo , and you can try the fine-tuned models on HuggingFace . Want to skip straight to fine-tuning on your own data? See the sparse-finetune CLI. By the end of this piece, you’ll have a SPLADE model trained on Amazon’s ESCI dataset, running on Modal’s serverless GPUs, with checkpoints saved to persistent storage.
```

---

## 11. Fine-Tuning Sparse Embeddings for E-Commerce Search | Part 3: Evaluation and Hard Negatives

- 日期: 2026-03-09 00:00
- 链接: https://qdrant.tech/articles/sparse-embeddings-ecommerce-part-3/

```
This is Part 3 of a 5-part series on fine-tuning sparse embeddings for e-commerce search. In Part 2 , we trained a SPLADE model on Modal. Now we evaluate it and push further with hard negative mining. 
 Series: 
 Part 1: Why Sparse Embeddings Beat BM25 
 Part 2: Training SPLADE on Modal 
 Part 3: Evaluation & Hard Negatives (here) 
 Part 4: Specialization vs Generalization 
 Part 5: From Research to Product 
 We have a trained SPLADE model sitting on a Modal volume (or grab it from HuggingFace ). Now comes the question that matters: is it actually better? In this article, we’ll index products into Qdrant, run retrieval benchmarks, implement hard negative mining, and dig into what the model learned. Full evaluation code is in the GitHub repo . To run this entire pipeline on your own data, see the sparse-finetune CLI.
```

---

## 12. Fine-Tuning Sparse Embeddings for E-Commerce Search | Part 4: Specialization vs Generalization

- 日期: 2026-03-09 00:00
- 链接: https://qdrant.tech/articles/sparse-embeddings-ecommerce-part-4/

```
This is Part 4 of a 5-part series on fine-tuning sparse embeddings for e-commerce search. In Part 3 , we evaluated our model and implemented hard negative mining. Now we test how well it generalizes. 
 Series: 
 Part 1: Why Sparse Embeddings Beat BM25 
 Part 2: Training SPLADE on Modal 
 Part 3: Evaluation & Hard Negatives 
 Part 4: Specialization vs Generalization (here) 
 Part 5: From Research to Product 
 We’ve built a SPLADE model that beats BM25 by 28% on Amazon ESCI. But here’s the question that determines whether this is a lab result or a production strategy: does it work on data it wasn’t trained on? Full code is on GitHub , you can try the fine-tuned models on HuggingFace , or fine-tune on your own catalog with the sparse-finetune CLI.
```

---

## 13. Fine-Tuning Sparse Embeddings for E-Commerce Search | Part 5: From Research to Product

- 日期: 2026-03-09 00:00
- 链接: https://qdrant.tech/articles/sparse-embeddings-ecommerce-part-5/

```
This is Part 5 of a series on fine-tuning sparse embeddings for e-commerce search. Parts 1 – 4 built the pipeline from scratch. This article packages it into a tool anyone can use. 
 Series: 
 Part 1: Why Sparse Embeddings Beat BM25 
 Part 2: Training SPLADE on Modal 
 Part 3: Evaluation & Hard Negatives 
 Part 4: Specialization vs Generalization 
 Part 5: From Research to Product (here) 
 In Parts 1 through 4, we built a SPLADE fine-tuning pipeline piece by piece: data loading, Modal GPU training, Qdrant evaluation, ANCE hard negative mining, cross-domain experiments. The code worked. The results were strong: 28% over BM25 on Amazon ESCI.
```

---

## 14. miniCOIL: on the Road to Usable Sparse Neural Retrieval

- 日期: 2025-05-13 00:00
- 链接: https://qdrant.tech/articles/minicoil/

```
Have you ever heard of sparse neural retrieval? If so, have you used it in production? 
 It’s a field with excellent potential – who wouldn’t want to use an approach that combines the strengths of dense and term-based text retrieval? Yet it’s not so popular. Is it due to the common curse of “What looks good on paper is not going to work in practice”? ? 
 This article describes our path towards sparse neural retrieval as it should be – lightweight term-based retrievers capable of distinguishing word meanings.
```

---

## 15. Relevance Feedback in Qdrant

- 日期: 2026-02-20 00:00
- 链接: https://qdrant.tech/articles/relevance-feedback/

```
A year ago, we dropped a statement-bomb in the “ Relevance Feedback in Information Retrieval ” article and then went silent. 
 We claimed that even though the information retrieval research field has proposed many useful mechanisms for increasing the relevance of search results, none of them made it to the neural search industry, simply because these approaches are not scalable. 
 Certainly, there are methods widely used to improve the relevance of retrieved results: query rewriting, for example. Yet none of the vector search solutions out there have tried to use the possibilities that come with full access to the vector search index: traversing it in the direction of relevance, instead of guessing where to shoot the query to the vector space.
```

---

## 16. Relevance Feedback in Informational Retrieval

- 日期: 2025-03-27 00:00
- 链接: https://qdrant.tech/articles/search-feedback-loop/

```
Relevance Feedback in Informational Retrieval
Evgeniya Sukhodolskaya
·March 27, 2025
A problem well stated is a problem half solved.
This quote applies as much to life as it does to information retrieval.
With a well-formulated query, retrieving the relevant document becomes trivial. In reality, however, most users struggle to precisely define what they are searching for.
While users may struggle to formulate a perfect request — especially in unfamiliar topics — they can easily judge whether a retrieved answer is relevant or not.
Relevance is a powerful feedback mechanism for a retrieval system to iteratively refine results in the direction of user interest.
In 2025, with social media flooded with daily AI breakthroughs, it almost seems like information retrieval is solved, agents can iteratively adjust their search queries while assessing the relevance.
Of course, there’s a catch: these models still rely on retrieval systems (RAG isn’t dead yet, despite daily predictions of its demise). They receive only a handful of top-ranked results provided by a far simpler and cheaper retriever. As a result, the success of guided retrieval still mainly depends on the retrieval system itself.
So, we should find a way of effectively and efficiently incorporating relevance feedback directly into a retrieval system. In this article, we’ll explore the approaches proposed in the research literature and try to answer the following question:
If relevance feedback in search is so widely studied and praised as effective, why is it practically not used in dedicated vector search solutions?
Dismantling the Relevance Feedback
Both industry and academia tend to reinvent the wheel here and there. So, we first took some time to study and categorize different methods — just in case there was something we could plug directly into Qdrant. The resulting taxonomy isn’t set in stone, but we aim to make it useful.
Pseudo-Relevance Feedback (PRF)
Pseudo-Relevance feedback takes the top-ranked documents from the initial retrieval results and treats them as relevant. This approach might seem naive, but it provides a noticeable performance boost in lexical retrieval while being relatively cheap to compute.
Binary Relevance Feedback
The most straightforward way to gather feedback is to ask users directly if document is relevant. There are two main limitations to this approach:
First, users are notoriously reluctant to provide feedback. Did you know that Google once had an upvote/downvote mechanism on search results but removed it because almost no one used it?
Second, even if users are willing to provide feedback, no relevant documents might be present in the initial retrieval results. In this case, the user can’t provide a meaningful signal.
Instead of asking users, we can ask a smart model to provide binary relevance judgements, but this would limit its potential to generate granular judgements.
Re-scored Relevance Feedback
We can also apply more sophisticated methods to extract relevance feedback from the top-ranked documents - machine learning models can provide a relevance score for each document.
The obvious concern here is twofold:
- How accurately can the automated judge determine relevance (or irrelevance)?
- How cost-efficient is it? After all, you can’t expect GPT-4o to re-rank thousands of documents for every user query — unless you’re filthy rich.
Nevertheless, automated re-scored feedback could be a scalable way to improve search when explicit binary feedback is not accessible.
Has the Problem Already Been Solved?
Digging through research materials, we expected anything else but to discover that the first relevance feedback study dates back sixty years. In the midst of the neural search bubble, it’s easy to forget that lexical (term-based) retrieval has been around for decades. Naturally, research in that field has had enough time to develop.
Neural search — aka vector search — gained traction in the industry around 5 years ago. Hence, vector-specific relevance feedback techniques might still be in their early stages, awaiting production-grade validation and industry adoption.
As a dedicated vector search engine, we would like to be these adopters. Our focus is neural search, but approaches in both lexical and neural retrieval seem worth exploring, as cross-field studies are always insightful, with the potential to reuse well-established methods of one field in another.
We found some interesting methods applicable to neural search solutions and additionally revealed a gap in the neural search-based relevance feedback approaches. Stick around, and we’ll share our findings!
Two Ways to Approach the Problem
Retrieval as a recipe can be broken down into three main ingredients:
- Query
- Documents
- Similarity scoring between them.
Query formulation is a subjective process – it can be done in infinite configurations, making the relevance of a document unpredictable until the query is formulated and submitted to the system.
So, adapting documents (or the search index) to relevance feedback would require per-request dynamic changes, which is impractical, considering that modern retrieval systems store billions of documents.
Thus, approaches for incorporating relevance feedback in search fall into two categories: refining a query and refining the similarity scoring function between the query and documents.
Query Refinement
There are several ways to refine a query based on relevance feedback. Globally, we prefer to distinguish between two approaches: modifying the query as text and modifying the vector representation of the query.
Query As Text
In term-based retrieval, an intuitive way to improve a query would be to expand it with relevant terms. It resembled the “aha, so that’s what it’s called” stage in the discovery search.
Before the deep learning era of this century, expansion terms were mainly selected using statistical or probabilistic models. The idea was to:
- Either extract the most frequent terms from (pseudo-)relevant documents;
- Or the most specific ones (for example, according to IDF);
- Or the most probable ones (most likely to be in query according to a relevance set).
Well-known methods of those times come from the family of Relevance Models, where terms for expansion are chosen based on their probability in pseudo-relevant documents (how often terms appear) and query terms likelihood given those pseudo-relevant documents - how strongly these pseudo-relevant documents match the query.
The most famous one, RM3
– interpolation of expansion terms probability with their probability in a query – is still appearing in papers of the last few years as a (noticeably decent) baseline in term-based retrieval, usually as part of anserini.
With the time approaching the modern machine learning era, multiple studies began claiming that these traditional ways of query expansion are not as effective as they could be.
Started with simple classifiers based on hand-crafted features, this trend naturally led to use the famous BERT (Bidirectional encoder representations from transformers). For example, BERT-QE
(Query Expansion) authors came up with this schema:
- Get pseudo-relevance feedback from the finetuned BERT reranker (~10 documents);
- Chunk these pseudo-relevant documents (~100 words) and score query-chunk relevance with the same reranker;
- Expand the query with the most relevant chunks;
- Rerank 1000 documents with the reranker using the expanded query.
This approach significantly outperformed BM25 + RM3 baseline in experiments (+11% NDCG@20). However, it required 11.01x more computation than just using BERT for reranking, and reranking 1000 documents with BERT would take around 9 seconds alone.
Query term expansion can hypothetically work for neural retrieval as well. New terms might shift the query vector closer to that of the desired document. However, this approach isn’t guaranteed to succeed. Neural search depends entirely on embeddings, and how those embeddings are generated — consequently, how similar query and document vectors are — depends heavily on the model’s training.
It definitely works if query refining is done by a model operating in the same vector space, which typically requires offline training of a retriever.
The goal is to extend the query encoder input to also include feedback documents, producing an adjusted query embedding. Examples include ANCE-PRF
and ColBERT-PRF
– ANCE and ColBERT fine-tuned extensions.
The reason why you’re most probably not familiar with these models – their absence in the industry – is that their training itself is a high upfront cost, and even though it was “paid”, these models struggle with generalization, performing poorly on out-of-domain tasks (datasets they haven’t seen during training). Additionally, feeding an attention-based model a lengthy input (query + documents) is not a good practice in production settings (attention is quadratic in the input length), where time and money are crucial decision factors.
Alternatively, one could skip a step — and work directly with vectors.
Query As Vector
Instead of modifying the initial query, a more scalable approach is to directly adjust the query vector. It is easily applicable across modalities and suitable for both lexical and neural retrieval.
Although vector search has become a trend in recent years, its core principles have existed in the field for decades. For example, the SMART retrieval system used by Rocchio in 1965 for his relevance feedback experiments operated on bag-of-words vector representations of text.
Rocchio’s idea — to update the query vector by adding a difference between the centroids of relevant and non-relevant documents — seems to translate well to modern dual encoders-based dense retrieval systems. Researchers seem to agree: a study from 2022 demonstrated that the parametrized version of Rocchio’s method in dense retrieval consistently improves Recall@1000 by 1–5%, while keeping query processing time suitable for production — around 170 ms.
However, parameters (centroids and query weights) in the dense retrieval version of Roccio’s method must be tuned for each dataset and, ideally, also for each request.
Gradient Descent-Based Methods
The efficient way of doing so on-the-fly remained an open question until the introduction of a gradient-descent-based Roccio’s method generalization: Test-Time Optimization of Query Representations (TOUR)
.
TOUR adapts a query vector over multiple iterations of retrieval and reranking (retrieve → rerank → gradient descent step), guided by a reranker’s relevance judgments.
The next iteration of gradient-based methods of query refinement – ReFit
– proposed in 2024 a lighter, production-friendly alternative to TOUR, limiting retrieve → rerank → gradient descent sequence to only one iteration. The retriever’s query vector is updated through matching (via Kullback–Leibler divergence) retriever and cross-encoder’s similarity scores distribution over feedback documents. ReFit is model- and language-independent and stably improves Recall@100 metric on 2–3%.
Gradient descent-based methods seem like a production-viable option, an alternative to finetuning the retriever (distilling it from a reranker). Indeed, it doesn’t require in-advance training and is compatible with any re-ranking models.
However, a few limitations baked into these methods prevented a broader adoption in the industry.
The gradient descent-based methods modify elements of the query vector as if it were model parameters; therefore, they require a substantial amount of feedback documents to converge to a stable solution.
On top of that, the gradient descent-based methods are sensitive to the choice of hyperparameters, leading to query drift, where the query may drift entirely away from the user’s intent.
Similarity Scoring
Another family of approaches is built around the idea of incorporating relevance feedback directly into the similarity scoring function. It might be desirable in cases where we want to preserve the original query intent, but still adjust the similarity score based on relevance feedback.
In lexical retrieval, this can be as simple as boosting documents that share more terms with those judged as relevant.
Its neural search counterpart is a k-nearest neighbors-based method
that adjusts the query-document similarity score by adding the sum of similarities between the candidate document and all known relevant examples.
This technique yields a significant improvement, around 5.6 percentage points in NDCG@20, but it requires explicitly labelled (by users) feedback documents to be effective.
In experiments, the knn-based method is treated as a reranker. In all other papers, we also found that adjusting similarity scores based on relevance feedback is centred around reranking – training or finetuning rerankers to become relevance feedback-aware. Typically, experiments include cross-encoders, though simple classifiers are also an option. These methods generally involve rescoring a broader set of documents retrieved during an initial search, guided by feedback from a smaller top-ranked subset. It is not a similarity matching function adjustment per se but rather a similarity scoring model adjustment.
Methods typically fall into two categories:
- Training rerankers offline to ingest relevance feedback as an additional input at inference time, as here — again, attention-based models and lengthy inputs: a production-deadly combination.
- Finetuning rerankers on relevance feedback from the first retrieval stage, as Baumgärtner et al. did, finetuning bias parameters of a small cross-encoder per query on 2k, k={2, 4, 8} feedback documents.
The biggest limitation here is that these reranker-based methods cannot retrieve relevant documents beyond those returned in the initial search, and using rerankers on thousands of documents in production is a no-go – it’s too expensive. Ideally, to avoid that, a similarity scoring function updated with relevance feedback should be used directly in the second retrieval iteration. However, in every research paper we’ve come across, retrieval systems are treated as black boxes — ingesting queries, returning results, and offering no built-in mechanism to modify scoring.
So, what are the takeaways?
Pseudo Relevance Feedback (PRF) is known to improve the effectiveness of lexical retrievers. Several PRF-based approaches – mainly query terms expansion-based – are successfully integrated into traditional retrieval systems. At the same time, there are no known industry-adopted analogues in neural (vector) search dedicated solutions; neural search-compatible methods remain stuck in research papers.
The gap we noticed while studying the field is that researchers have no direct access to retrieval systems, forcing them to design wrappers around the black-box-like retrieval oracles. This is sufficient for query-adjusting methods but not for similarity scoring function adjustment.
Perhaps relevance feedback methods haven’t made it into the neural search systems for trivial reasons — like no one having the time to find the right balance between cost and efficiency.
Getting it to work in a production setting means experimenting, building interfaces, and adapting architectures. Simply put, it needs to look worth it. And unlike 2D vector math, high-dimensional vector spaces are anything but intuitive. The curse of dimensionality is real. So is query drift. Even methods that make perfect sense on paper might not work in practice.
A real-world solution should be simple. Maybe just a little bit smarter than a rule-based approach, but still practical. It shouldn’t require fine-tuning thousands of parameters or feeding paragraphs of text into transformers. And for it to be effective, it needs to be integrated directly into the retrieval system itself.
```

---

## 17. Built for Vector Search

- 日期: 2025-02-17 10:00
- 链接: https://qdrant.tech/articles/dedicated-vector-search/

```
Built for Vector Search
Evgeniya Sukhodolskaya & Andrey Vasnetsov
·February 17, 2025
Any problem with even a bit of complexity requires a specialized solution. You can use a Swiss Army knife to open a bottle or poke a hole in a cardboard box, but you will need an axe to chop wood — the same goes for software.
In this article, we will describe the unique challenges vector search poses and why a dedicated solution is the best way to tackle them.
Vectors
Let’s look at the central concept of vector databases — vectors.
Vectors (also known as embeddings) are high-dimensional representations of various data points — texts, images, videos, etc. Many state-of-the-art (SOTA) embedding models generate representations of over 1,500 dimensions. When it comes to state-of-the-art PDF retrieval, the representations can reach over 100,000 dimensions per page.
This brings us to the first challenge of vector search — vectors are heavy.
Vectors are Heavy
To put this in perspective, consider one million records stored in a relational database. It’s a relatively small amount of data for modern databases, which a free tier of many cloud providers could easily handle.
Now, generate a 1536-dimensional embedding with OpenAI’s text-embedding-ada-002
model from each record, and you are looking at around 6GB of storage. As a result, vector search workloads, especially if not optimized, will quickly dominate the main use cases of a non-vector database.
Having vectors as a part of a main database is a potential issue for another reason — vectors are always a transformation of other data.
Vectors are a Transformation
Vectors are obtained from some other source-of-truth data. They can be restored if lost with the same embedding model previously used. At the same time, even small changes in that model can shift the geometry of the vector space, so if you update or change the embedding model, you need to update and reindex all the data to maintain accurate vector comparisons.
If coupled with the main database, this update process can lead to significant complications and even unavailability of the whole system.
However, vectors have positive properties as well. One of the most important is that vectors are fixed-size.
Vectors are Fixed-Size
Embedding models are designed to produce vectors of a fixed size. We have to use it to our advantage.
For fast search, vectors need to be instantly accessible. Whether in RAM or disk, vectors should be stored in a format that allows quick access and comparison. This is essential, as vector comparison is a very hot operation in vector search workloads. It is often performed thousands of times per search query, so even a small overhead can lead to a significant slowdown.
For dedicated storage, vectors’ fixed size comes as a blessing. Knowing how much space one data point needs, we don’t have to deal with the usual overhead of locating data — the location of elements in storage is straightforward to calculate.
Everything becomes far less intuitive if vectors are stored together with other data types, for example, texts or JSONs. The size of a single data point is not fixed anymore, so accessing it becomes non-trivial, especially if data is added, updated, and deleted over time.
Storing vectors together with other types of data, we lose all the benefits of their characteristics; however, we fully “enjoy” their drawbacks, polluting the storage with an extremely heavy transformation of data already existing in that storage.
Vector Search
Unlike traditional databases that serve as data stores, vector databases are more like search engines. They are designed to be scalable, always available, and capable of delivering high-speed search results even under heavy loads. Just as Google or Bing can handle billions of queries at once, vector databases are designed for scenarios where rapid, high-throughput, low-latency retrieval is a must.
Pick Any Two
Distributed systems are perfect for scalability — horizontal scaling in these systems allows you to add more machines as needed. In the world of distributed systems, one well-known principle — the CAP theorem — illustrates that you cannot have it all. The theorem states that a distributed system can guarantee only two out of three properties: Consistency, Availability, and Partition Tolerance.
As network partitions are inevitable in any real-world distributed system, all modern distributed databases are designed with partition tolerance in mind, forcing a trade-off between consistency (providing the most up-to-date data) and availability (remaining responsive).
There are two main design philosophies for databases in this context:
ACID: Prioritizing Consistency
The ACID model ensures that every transaction (a group of operations treated as a single unit, such as transferring money between accounts) is executed fully or not at all (reverted), leaving the database in a valid state. When a system is distributed, achieving ACID properties requires complex coordination between nodes. Each node must communicate and agree on the state of a transaction, which can limit system availability — if a node is uncertain about the state of another, it may refuse to process a transaction until consistency is assured. This coordination also makes scaling more challenging.
Financial institutions use ACID-compliant databases when dealing with money transfers, where even a momentary discrepancy in an account balance is unacceptable.
BASE: Prioritizing Availability
On the other hand, the BASE model favors high availability and partition tolerance. BASE systems distribute data and workload across multiple nodes, enabling them to respond to read and write requests immediately. They operate under the principle of eventual consistency — although data may be temporarily out-of-date, the system will converge on a consistent state given time.
Social media platforms, streaming services, and search engines all benefit from the BASE approach. For these applications, having immediate responsiveness is more critical than strict consistency.
BASEd Vector Search
Considering the specifics of vector search — its nature demanding availability & scalability — it should be served on BASE-oriented architecture. This choice is made due to the need for horizontal scaling, high availability, low latency, and high throughput. For example, having BASE-focused architecture allows us to easily manage resharding.
A strictly consistent transactional approach also loses its attractiveness when we remember that vectors are heavy transformations of data at our disposal — what’s the point in limiting data protection mechanisms if we can always restore vectorized data through a transformation?
Vector Index
Vector search relies on high-dimensional vector mathematics, making it computationally heavy at scale. A brute-force similarity search would require comparing a query against every vector in the database. In a database with 100 million 1536-dimensional vectors, performing 100 million comparisons per one query is unfeasible for production scenarios. Instead of a brute-force approach, vector databases have specialized approximate nearest neighbour (ANN) indexes that balance search precision and speed. These indexes require carefully designed architectures to make their maintenance in production feasible.
One of the most popular vector indexes is HNSW (Hierarchical Navigable Small World), which we picked for its capability to provide simultaneously high search speed and accuracy. High performance came with a cost — implementing it in production is untrivial due to several challenges, so to make it shine all the system’s architecture has to be structured around it, serving the capricious index.
Index Complexity
HNSW is structured as a multi-layered graph. With a new data point inserted, the algorithm must compare it to existing nodes across several layers to index it. As the number of vectors grows, these comparisons will noticeably slow down the construction process, making updates increasingly time-consuming. The indexing operation can quickly become the bottleneck in the system, slowing down search requests.
Building an HNSW monolith means limiting the scalability of your solution — its size has to be capped, as its construction time scales non-linearly with the number of elements. To keep the construction process feasible and ensure it doesn’t affect the search time, we came up with a layered architecture that breaks down all data management into small units called segments.
Each segment isolates a subset of vectorized corpora and supports all collection-level operations on it, from searching to indexing, for example segments build their own index on the subset of data available to them. For users working on a collection level, the specifics of segmentation are unnoticeable. The search results they get span the whole collection, as sub-results are gathered from segments and then merged & deduplicated.
By balancing between size and number of segments, we can ensure the right balance between search speed and indexing time, making the system flexible for different workloads.
Immutability
With index maintenance divided between segments, Qdrant can ensure high performance even during heavy load, and additional optimizations secure that further. These optimizations come from an idea that working with immutable structures introduces plenty of benefits: the possibility of using internally fixed sized lists (so no dynamic updates), ordering stored data accordingly to access patterns (so no unpredictable random accesses). With this in mind, to optimize search speed and memory management further, we use a strategy that combines and manages mutable and immutable segments.
Immutable segments are an implementation detail transparent for users — they can delete vectors at any time, while additions and updates are applied to a mutable segment instead. This combination of mutability and immutability allows search and indexing to smoothly run simultaneously, even under heavy loads. This approach minimizes the performance impact of indexing time and allows on-the-fly configuration changes on a collection level (such as enabling or disabling data quantization) without downtimes.
Filterable Index
Vector search wasn’t historically designed for filtering — imposing strict constraints on results. It’s inherently fuzzy; every document is, to some extent, both similar and dissimilar to any query — there’s no binary “fits/doesn’t fit” segregation. As a result, vector search algorithms weren’t originally built with filtering in mind.
At the same time, filtering is unavoidable in many vector search applications, such as e-commerce search/recommendations. Searching for a Christmas present, you might want to filter out everything over 100 euros while still benefiting from the vector search’s semantic nature.
In many vector search solutions, filtering is approached in two ways: pre-filtering (computes a binary mask for all vectors fitting the condition before running HNSW search) or post-filtering (running HNSW as usual and then filtering the results).
Qdrant took filtering in vector search further, recognizing the limitations of pre-filtering & post-filtering strategies. We developed an adaptation of HNSW — filterable HNSW — that also enables in-place filtering during graph traversal. To make this possible, we condition HNSW index construction on possible filtering conditions reflected by payload indexes (inverted indexes built on vectors’ metadata).
Qdrant was designed with a vector index being a central component of the system. That made it possible to organize optimizers, payload indexes and other components around the vector index, unlocking the possibility of building a filterable HNSW.
In general, optimizing vector search requires a custom, finely tuned approach to data and index management that secures high performance even as data grows and changes dynamically. This specialized architecture is the key reason why dedicated vector databases will always outperform general-purpose databases in production settings.
Vector Search Beyond RAG
Many discussions about the purpose of vector databases focus on Retrieval-Augmented Generation (RAG) — or its more advanced variant, agentic RAG — where vector databases are used as a knowledge source to retrieve context for large language models (LLMs). This is a legitimate use case, however, the hype wave of RAG solutions has overshadowed the broader potential of vector search, which goes beyond augmenting generative AI.
Discovery
The strength of vector search lies in its ability to facilitate discovery. Vector search allows you to refine your choices as you search rather than starting with a fixed query. Say, you’re ordering food not knowing exactly what you want — just that it should contain meat & not a burger, or that it should be meat with cheese & not tacos. Instead of searching for a specific dish, vector search helps you navigate options based on similarity and dissimilarity, guiding you toward something that matches your taste without requiring you to define it upfront.
Recommendations
Vector search is perfect for recommendations. Imagine browsing for a new book or movie. Instead of searching for an exact match, you might look for stories that capture a certain mood or theme but differ in key aspects from what you already know. For example, you may want a film featuring wizards without the familiar feel of the “Harry Potter” series. This flexibility is possible because vector search is not tied to the binary “match/not match” concept but operates on distances in a vector space.
Big Unstructured Data Analysis
Vector search nature makes it also ideal for big unstructured data analysis, for instance, anomaly detection. In large, unstructured, and often unlabelled datasets, vector search can help identify clusters and outliers by analyzing distance relationships between data points.
Fundamentally Different
Vector search beyond RAG isn’t just another feature — it’s a fundamental shift in how we interact with data. Dedicated solutions integrate these capabilities natively and are designed from the ground up to handle high-dimensional math and (dis-)similarity-based retrieval. In contrast, databases with vector extensions are built around a different data paradigm, making it impossible to efficiently support advanced vector search capabilities.
Even if you want to retrofit these capabilities, it’s not just a matter of adding a new feature — it’s a structural problem. Supporting advanced vector search requires dedicated interfaces that enable flexible usage of vector search from multi-stage filtering to dynamic exploration of high-dimensional spaces.
When the underlying architecture wasn’t initially designed for this kind of interaction, integrating interfaces is a software engineering team nightmare. You end up breaking existing assumptions, forcing inefficient workarounds, and often introducing backwards-compatibility problems. It’s why attempts to patch vector search onto traditional databases won’t match the efficiency of purpose-built systems.
Making Vector Search State-of-the-Art
Now, let’s shift focus to another key advantage of dedicated solutions — their ability to keep up with state-of-the-art solutions in the field.
Vector databases are purpose-built for vector retrieval, and as a result, they offer cutting-edge features that are often critical for AI businesses relying on vector search. Vector database engineers invest significant time and effort into researching and implementing the most optimal ways to perform vector search. Many of these innovations come naturally to vector-native architectures, while general-purpose databases with added vector capabilities may struggle to adapt and replicate these benefits efficiently.
Consider some of the advanced features implemented in Qdrant:
GPU-Accelerated Indexing
By offloading index construction tasks to the GPU, Qdrant can significantly speed up the process of data indexing while keeping costs low. This becomes especially valuable when working with large datasets in hot data scenarios.GPU acceleration in Qdrant is a custom solution developed by an enthusiast from our core team. It’s vendor-free and natively supports all Qdrant’s unique architectural features, from FIlterable HNSW to multivectors.
Multivectors
Some modern embedding models produce an entire matrix (a list of vectors) as output rather than a single vector. Qdrant supports multivectors natively.This feature is critical when using state-of-the-art retrieval models such as ColBERT, ColPali, or ColQwen. For instance, ColPali and ColQwen produce multivector outputs, and supporting them natively is crucial for state-of-the-art (SOTA) PDF-retrieval.
In addition to that, we continuously look for improvements in:
These advancements are not just incremental improvements — they define the difference between a system optimized for vector search and one that accommodates it.
Staying at the cutting edge of vector search is not just about performance — it’s also about keeping pace with an evolving AI landscape.
Summing up
When it comes to vector search, there’s a clear distinction between using a dedicated vector search solution and extending a database to support vector operations.
For small-scale applications or prototypes handling up to a million data points, a non-optimized architecture might suffice. However, as the volume of vectors grows, an unoptimized solution will quickly become a bottleneck — slowing down search operations and limiting scalability. Dedicated vector search solutions are engineered from the ground up to handle massive amounts of high-dimensional data efficiently.
State-of-the-art (SOTA) vector search evolves rapidly. If you plan to build on the latest advances, using a vector extension will eventually hold you back. Dedicated vector search solutions integrate these features natively, ensuring that you benefit from continuous innovations without compromising performance.
The power of vector search extends into areas such as big data analysis, recommendation systems, and discovery-based applications, and to support these vector search capabilities, a dedicated solution is needed.
When to Choose a Dedicated Database over an Extension:
- High-Volume, Real-Time Search: Ideal for applications with many simultaneous users who require fast, continuous access to search results—think search engines, e-commerce recommendations, social media, or media streaming services.
- Dynamic, Unstructured Data: Perfect for scenarios where data is continuously evolving and where the goal is to discover insights from data patterns.
- Innovative Applications: If you’re looking to implement advanced use cases such as recommendation engines, hybrid search solutions, or exploratory data analysis where traditional exact or token-based searches hold short.
Investing in a dedicated vector search engine will deliver the performance and flexibility necessary for success if your application relies on vector search at scale, keeps up with trends, or requires more than just a simple small-scale similarity search.
```

---

## 18. Any* Embedding Model Can Become a Late Interaction Model... If You Give It a Chance!

- 日期: 2024-08-14 00:00
- 链接: https://qdrant.tech/articles/late-interaction-models/

```
* At least any open-source model, since you need access to its internals. 
 You Can Adapt Dense Embedding Models for Late Interaction 
 Qdrant 1.10 introduced support for multi-vector representations, with late interaction being a prominent example of this model. In essence, both documents and queries are represented by multiple vectors, and identifying the most relevant documents involves calculating a score based on the similarity between the corresponding query and document embeddings. If you’re not familiar with this paradigm, our updated Hybrid Search article explains how multi-vector representations can enhance retrieval quality.
```

---

## 19. Optimizing Memory for Bulk Uploads

- 日期: 2025-02-13 00:00
- 链接: https://qdrant.tech/articles/indexing-optimization/

```
Optimizing Memory Consumption During Bulk Uploads 
 Efficient memory management is a constant challenge when you’re dealing with large-scale vector data . In high-volume ingestion scenarios, even seemingly minor configuration choices can significantly impact stability and performance. 
 Let’s take a look at the best practices and recommendations to help you optimize memory usage during bulk uploads in Qdrant. We’ll cover scenarios with both dense and sparse vectors, helping your deployments remain performant even under high load and avoiding out-of-memory errors.
```

---

## 20. Introducing Gridstore: Qdrant's Custom Key-Value Store

- 日期: 2025-02-05 00:00
- 链接: https://qdrant.tech/articles/gridstore-key-value-storage/

```
Why We Built Our Own Storage Engine 
 Databases need a place to store and retrieve data. That’s what Qdrant’s key-value storage does—it links keys to values. 
 When we started building Qdrant, we needed to pick something ready for the task. So we chose RocksDB as our embedded key-value store. 
 It is mature, reliable, and well-documented. 
 Over time, we ran into issues. Its architecture required compaction (uses LSMT ), which caused random latency spikes. It handles generic keys, while we only use it for sequential IDs. Having lots of configuration options makes it versatile, but accurately tuning it was a headache. Finally, interoperating with C++ slowed us down (although we will still support it for quite some time 😭).
```

---

## 21. What is Agentic RAG? Building Agents with Qdrant

- 日期: 2024-11-22 00:00
- 链接: https://qdrant.tech/articles/agentic-rag/

```
Standard Retrieval Augmented Generation follows a predictable, linear path: receive
a query, retrieve relevant documents, and generate a response. In many cases that might be enough to solve a particular
problem. In the worst case scenario, your LLM will just decide to not answer the question, because the context does not
provide enough information. 
 On the other hand, we have agents. These systems are given more freedom to act, and can take multiple non-linear steps
to achieve a certain goal. There isn’t a single definition of what an agent is, but in general, it is an application
that uses LLM and usually some tools to communicate with the outside world. LLMs are used as decision-makers which
decide what action to take next. Actions can be anything, but they are usually well-defined and limited to a certain
set of possibilities. One of these actions might be to query a vector database, like Qdrant, to retrieve relevant
documents, if the context is not enough to make a decision. However, RAG is just a single tool in the agent’s arsenal.
```

---

## 22. Hybrid Search Revamped - Building with Qdrant's Query API

- 日期: 2024-07-25 00:00
- 链接: https://qdrant.tech/articles/hybrid-search/

```
It’s been over a year since we published the original article on how to build a hybrid
search system with Qdrant. The idea was straightforward: combine the results from different search methods to improve
retrieval quality. Back in 2023, you still needed to use an additional service to bring lexical search
capabilities and combine all the intermediate results. Things have changed since then. Once we introduced support for
sparse vectors, the additional search service became obsolete , but you were still
required to combine the results from different methods on your end.
```

---

## 23. What is RAG: Understanding Retrieval-Augmented Generation

- 日期: 2024-03-19 09:29
- 链接: https://qdrant.tech/articles/what-is-rag-in-ai/

```
Retrieval-augmented generation (RAG) integrates external information retrieval into the process of generating responses by Large Language Models (LLMs). It searches a database for information beyond its pre-trained knowledge base, significantly improving the accuracy and relevance of the generated responses. 
 Language models have exploded on the internet ever since ChatGPT came out, and rightfully so. They can write essays, code entire programs, and even make memes (though we’re still deciding on whether that’s a good thing).
```

---

## 24. BM42: New Baseline for Hybrid Search

- 日期: 2024-07-01 12:00
- 链接: https://qdrant.tech/articles/bm42/

```
Please note that the benchmark section of this article was updated after the publication due to a mistake in the evaluation script.
BM42 does not outperform BM25 implementation of other vendors.
Please consider BM42 as an experimental approach, which requires further research and development before it can be used in production. For the last 40 years, BM25 has served as the standard for search engines.
It is a simple yet powerful algorithm that has been used by many search engines, including Google, Bing, and Yahoo.
```

---

## 25. Qdrant 1.8.0: Enhanced Search Capabilities for Better Results

- 日期: 2024-03-06 00:00
- 链接: https://qdrant.tech/articles/qdrant-1.8.x/

```
Unlocking Next-Level Search: Exploring Qdrant 1.8.0’s Advanced Search Capabilities 
 Qdrant 1.8.0 is out! .
This time around, we have focused on Qdrant’s internals. Our goal was to optimize performance so that your existing setup can run faster and save on compute. Here is what we’ve been up to: 
 Faster sparse vectors : Hybrid search is up to 16x faster now! 
 CPU resource management: You can allocate CPU threads for faster indexing. 
 Better indexing performance: We optimized text indexing on the backend. 
 Faster search with sparse vectors 
 Search throughput is now up to 16 times faster for sparse vectors. If you are using Qdrant for hybrid search , this means that you can now handle up to sixteen times as many queries. This improvement comes from extensive backend optimizations aimed at increasing efficiency and capacity.
```

---

## 26. Optimizing RAG Through an Evaluation-Based Methodology

- 日期: 2024-06-12 00:00
- 链接: https://qdrant.tech/articles/rapid-rag-optimization-with-qdrant-and-quotient/

```
In today’s fast-paced, information-rich world, AI is revolutionizing knowledge management. The systematic process of capturing, distributing, and effectively using knowledge within an organization is one of the fields in which AI provides exceptional value today. 
 The potential for AI-powered knowledge management increases when leveraging Retrieval Augmented Generation (RAG) , a methodology that enables LLMs to access a vast, diverse repository of factual information from knowledge stores, such as vector databases. 
 This process enhances the accuracy, relevance, and reliability of generated text, thereby mitigating the risk of faulty, incorrect, or nonsensical results sometimes associated with traditional LLMs. This method not only ensures that the answers are contextually relevant but also up-to-date, reflecting the latest insights and data available.
```

---

## 27. Is RAG Dead? The Role of Vector Databases in Vector Search | Qdrant

- 日期: 2024-02-27 00:00
- 链接: https://qdrant.tech/articles/rag-is-dead/

```
Is RAG Dead? The Role of Vector Databases in AI Efficiency and Vector Search 
 When Anthropic came out with a context window of 100K tokens, they said: “ Vector search is dead. LLMs are getting more accurate and won’t need RAG anymore. ” 
 Google’s Gemini 1.5 now offers a context window of 10 million tokens. Their supporting paper claims victory over accuracy issues, even when applying Greg Kamradt’s NIAH methodology . 
 It’s over. RAG (Retrieval Augmented Generation) must be completely obsolete now. Right?
```

---

## 28. Optimizing OpenAI Embeddings: Enhance Efficiency with Qdrant's Binary Quantization

- 日期: 2024-02-21 13:12
- 链接: https://qdrant.tech/articles/binary-quantization-openai/

```
OpenAI Ada-003 embeddings are a powerful tool for natural language processing (NLP). However, the size of the embeddings are a challenge, especially with real-time search and retrieval. In this article, we explore how you can use Qdrant’s Binary Quantization to enhance the performance and efficiency of OpenAI embeddings. 
 In this post, we discuss: 
 The significance of OpenAI embeddings and real-world challenges. 
 Qdrant’s Binary Quantization, and how it can improve the performance of OpenAI embeddings 
 Results of an experiment that highlights improvements in search efficiency and accuracy 
 Implications of these findings for real-world applications 
 Best practices for leveraging Binary Quantization to enhance OpenAI embeddings 
 If you’re new to Binary Quantization, consider reading our article which walks you through the concept and how to use it with Qdrant
```

---

## 29. How to Implement Multitenancy and Custom Sharding in Qdrant

- 日期: 2024-02-06 13:21
- 链接: https://qdrant.tech/articles/multitenancy/

```
Scaling Your Machine Learning Setup: The Power of Multitenancy and Custom Sharding in Qdrant 
 We are seeing the topics of multitenancy and distributed deployment pop-up daily on our Discord support channel . This tells us that many of you are looking to scale Qdrant along with the rest of your machine learning setup. 
 Whether you are building a bank fraud-detection system, RAG for e-commerce, or services for the federal government - you will need to leverage a multitenant architecture to scale your product.
In the world of SaaS and enterprise apps, this setup is the norm. It will considerably increase your application’s performance and lower your hosting costs.
```

---

## 30. Data Privacy with Qdrant: Implementing Role-Based Access Control (RBAC)

- 日期: 2024-06-18 08:00
- 链接: https://qdrant.tech/articles/data-privacy/

```
Data stored in vector databases is often proprietary to the enterprise and may include sensitive information like customer records, legal contracts, electronic health records (EHR), financial data, and intellectual property. Moreover, strong security measures become critical to safeguarding this data. If the data stored in a vector database is not secured, it may open a vulnerability known as “ embedding inversion attack ,” where malicious actors could potentially reconstruct the original data from the embeddings themselves.
```

---
