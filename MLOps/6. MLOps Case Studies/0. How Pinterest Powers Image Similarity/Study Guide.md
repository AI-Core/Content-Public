# Firstly, let's look over the stack
- Apache Flink
- RocksDB
- ZooKeeper
- Custom monitoring built into the system
- Graph storage - storing the image clusters
- Manas - custom search engine

## Situation
- ~200 images created per second
- 10s of billions of historical images

## Pipeline
- User uploads image
- Check image has already been uploaded
    - Generate embedding for new image
    - Use embedding to find similar candidates
    - Enhance the set of candidates
    - "VIP" team handle all media uploaded and generate the embeddings
        - This sends a notification through to Kafka
    - Embeddings produced in a few seconds
    - Embeddings -> LSH terms generated (reduced dimensionality representation of embeddings)
    - Custom search index is built on searching by LSH term
    - Stream-stream join to reduce downstream processing
    - Send image embedding to search engine to get duplicate candidates
    - Enlarge that set of candidates
    - 2000 candidates
    - Sent to ML hosting service "Scorpion"
    - Score each candidate 0-1 to predict if candidates are duplicates
    - If no candidates are similar enough, this image can become it's own cluster, to which future images can be a member
- RocksDB: Given an image, what is the canonical id for it
- Graph storage: given a "cluster head" give me a list of all cluster member images
- Add newly created image to the search index

## Monitoring

You have to be careful that features which your model depend on don't get deprecated over time. It's important to have a system that tells you which features are being used and by which models.

## From batch processing to real time

In real time it's harder to detect anomalies like data volume, which could tell you something is wrong with your back end
In batch processing, you can see the size of the dataset e.g. 10B and know that if it jumps to 20B there is probably a problem.

Monitoring has to be built right into the system so that it can catch problems as they happen.

They have rollbacks built into the system as well which they can trigger if they notice things are going wrong.

## Bootstrapping

Pinterest have already processed billions of historical images

They bootstrapped 3 things:
- search indexes
- data for graph storage
- data for rocksdb to quickly look up data related to a particular image

Finding the delta of what needs to be bootstrapped

## Reprocessing previous images
Currently rescheduled reprocessing of historical images

## The objective

Move from a batch processing job to a real time job for annotating images, detecting duplicates to provide a great customer experience.

They want to get to the point where they can tell an engineer do these 3 steps, and those 3 steps are so easy that no further automation is required.

They can currently handle 200 images per second, but want to scale up to near 1000 to provide any of their consumers with an SLA (service level agreement) that says that if something does go wrong, they will be able to recover in a known time e.g. 2 days.

## Batch and streaming - Are both happening alongside each other?

The goal is to move totally to streaming and deprecate the batch processing.

Each event (image upload) is an independent event. If a complete reprocessing of all images were required, it's not necessary to have a creation time, or a current state for the image. This is unlike other systems, where order is required (customer orders, newsfeed). This means that a "Kappa" architecture is not required for the Pinterest use case. Read more about Kappa architecture here (https://hazelcast.com/glossary/kappa-architecture/).