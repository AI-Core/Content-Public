<!-- MOTIVATION -->

- to get a picture of data engineering, you need to understand the data engineering lifecycle

<!-- OUTLINE OF THE LIFECYCLE -->

_Show infographic of lifecycle_

<!-- DESCRIBE EACH PART OF THE LIFECYCLE -->

### Data Ingestion

- the first part is data ingestion
- this is where data enters the system
- it could come from any kind of source
- from interactions with an app
- to files uploaded by employees
- when data gets big, this gets harder than it sounds
- ingestion systems might need to be able to handle very high volumes of data in real time

### Data Storage

- the next part of the lifecycle is data storage
- once the data is in the system, how is it formatted and where is it saved?
- the storage system needs to be able to scale to contain large volumes of data
- there are so many options for how to store data, and the best option varies for different use cases
- all the right people need to have access, but this needs to remain secure

### ELT/ETL

- once you've ingested and stored the data, you need to extract the data from where it is stored, process it to compute useful things by applying some transformations, and then move those results to where they are needed
- we call abbreviate this process of extracting, transforming, and loading the data ETL

## OUTRO

- those are the three main sections of the data engineering lifecycle
