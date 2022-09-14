# Multiclass vs multilabel

- don't confuse multiclass classification with multilabel classification
- multilabel classification is the case where many of the outputs can be true
- for example, if you were trying to predict whether a property listing is pet friendly, allows parties, and is smoking friendly at the same time
- the multilabel model is essentially performing multiple tasks at once to predict multiple labels for the example
- all three of those outputs could true at the same time, false at the same time or anything inbetween
- each of them represents their own binary probability distribution
- which is the probability of that label being true

- multiclass is different
- that's where the example can only take on one of the outputs
- for example, if you're predicting whether a property listing should be labelled as urban, suburban, or rural
- it can only be one of those

# Multiclass multilabel models

- it looks a little more complicated, but the forward pass and the optimisation work in exactly the same way as for multilabel or multiclass
- essentially, it's many multiclass classification models predicting distributions over different labels at the same time
