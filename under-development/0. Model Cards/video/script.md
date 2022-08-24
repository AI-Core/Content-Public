# Model cards

## Motivation

### Many commercial systems were found to have biases

- face detection and tracking, attribute detection, criminal justice, toxic commen detection and more

### Intersectional analysis

- several cases where on aggregate, things loooked fair
- e.g. GM hires lots of black people and lots of women
- but when intersectional samples were tested, it was found that they only hired black men, and white women

## What are model cards?

- model cards are short documents that highlight the limitations of trained machine learning models and point out the intended use cases, information about attributes for which model performance can vary, and measures of model performance.

- analogous to "Datasheets for datasets" which highlight similar biases in datasets

_show model card sections_

### Talk through model card sections

#### Out of scope uses

- analogous to warning labels on food
- e.g. not for use on text examples shorter than 100 tokens
- e.g. for use on greyscale images only

#### Factors

- section shows performance across a number of different factors

##### Groups

- perform

## Metrics

- model card shows metrics about the model
- 1. model performance measures.
- it should specify what is being reported and why that was prioritised
- e.g. false negative vs false positive
- 2. decision thresholds.
- what decision thresholds are being used and why were they chosen
- recommendes providing a slider if digital to view performance parameters across various decision thresholds
- 3. approaches to undertainty and variability
- should explain how the measurements are calculated. things like the variance and confidence intervals rather than just the predicted value
- should also include over how many runs and what kind of cross validation

## 5. Evaluation data

- recommended details include

1. What datasets were used to evaluate the model?
2. why were they chosen?
3. How were they preprocessed?

## Ideal impact

- allow stakeholders to compare candidate models for deployment across ethical, inclusive, and fairness considerations

### Aims to define a standardised way to report model biases

- defines a standardised way to compare models

## How is the use of model cards playing out so far?

- used at huggingface
- used at wikipedia
