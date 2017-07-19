# lambda-dynamodb-aggregator
Aggregation data in DynamoDB with Lambda(Python)

# Preparation
## Input data (Common)
As common input data, needs to prepare following values.

|Column|Contents|
|---|---|
|label_id|Hash key of DynamoDB table|
|label_range|Range key of DynamoDB table|
|id|Target ID (Array format)|
|aggregator|Types of Aggregator(latest, max, min, avg, sum, count)|
|time_from|Starting time of aggregation|
|time_to|Ending time of aggregation|
|params|[Individual] Necessary parameters for individual aggregation|

## Input data (Individual)
As individual data, needs to prepare following values.

|Aggregation Type|Necessary data|
|---|---|
|Latest（latest）|range: Range key name (Currently same as common data)|
|Maximum（max）|score: Aggregation target column name|
|Minimum（min）|score: Aggregation target column name|
|Average（avg）|score: Aggregation target column name|
|Total（sum）|score: Aggregation target column name|
|Count（count）|score: Aggregation target column name|

# Sample Input data

```
{
  "label_id": "id",
  "label_range": "timestamp",
  "id": [
    "sensor1",
    "sensor2"
  ],
  "aggregator": "latest",
  "time_from": "2017-04-30T22:00:00.000",
  "time_to": "2017-04-30T22:06:00.000",
  "params": {
    "range": "timestamp"
  }
}
```
