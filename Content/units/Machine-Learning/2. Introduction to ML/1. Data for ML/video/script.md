- one of the key components for building machine learning systems is data
- and that data typically takes a specific format

- in a supervised dataset, we have both features and labels for every example

- the label is the thing that we want to predict
- and the features are the things that we want to predict the label from
- we often call the label the target

- in an unsupervised dataset, we only have features, and no labels
- but everything i'll mention about features still applies

- for example, predicting how many of a product are going to be sold at a certain price is a common example
- in that case you might have a dataset of products
- their details and their previous price could be the features
- and the number of them which were sold could be the labels

- we denote the features as X, and the labels as y
- and each of these is essentially a list of features or labels for each example

_Show vector version_

- the typical case is that each example has multiple features, and a single label

_Show X as matrix_

- and that's why I've drawn the X capitalised and the y lowercase
- because X is a matrix and y is a vector

- but you can also have problems with single examples or multiple labels or any combination of those

- in the simplest case, the features are numbers, and the target is a single number
- for example, if you're predicting the price per night of a new property uploaded to your app from the number of rooms and area of floor space it has
- but the features and labels can take any format
- for example, the input features might be an image or a video or text that you want to make some prediction about

- commonly, the output is formatted as a classification
- specifically, a distribution of probabilities over the different possible output classes
- this would be the case if you were doing image classification

- whatever the format of data it's important to note that the first dimension is almost always what we call the batch dimension, along that dimension is every example in the dataset

- to give a few more examples
- object detection is a problem where you try to predict a bounding box around a specific object in an image
- in that case, you have image data as an input, and multiple labels - the height, width, and coordinates of the centre of the box
- that could easily be extended to video detection too, where you'd have bounding box predictions for every frame

- another very common situation is recommendation systems

- there are a number of different ways that you could tackle any of these problems, but the point here, is that almost any kind of problem can be framed as a mapping between numerical features and numerical targets, and there is always a way to represent the data in this format...
- although some types of data can be harder to format than others

- notably, text data is not numerical
- but there are ways that you can transform it into a numerical representation
- an example where you'd want to do that would be text autocompletion
- in that case, your dataset would be a load of text examples
- the features would be the text up to a certain point
- and the labels would be the complete text
- that makes what is called a self-supervised dataset, where the text itself is both the features and the labels
- but to do that you have to do some more complex transformations to get the text into numerical format

- so stay tuned and you'll learn how to do that
<!-- 


- Before we talk about how machine learning algorithms find those relationships though, it's critical to understand the format of the data

- Depending on the problem, we can classify the data can be divided into labeled or unlabeled

  - Machine Learning systems can be classified according to the type of data they take in and the predictions they make
    - This data is composed of features and labels
    - The labels are the solutions that the system is trying to predict
    - The features are the variables we use to predict the labels
  - Let's take a look at an example using the California house dataset
  - **`[RUN THE NOTEBOOK]`**
    - We are using the sci-kit learn library to load the dataset. We will talk about sci-kit learn shortly, but for now, we will just mention that this library is a toolkit for machine learning algorithms that also contains datasets
    - One of the datasets you can load is the California housing dataset
    - This dataset has 8 features, and one label, which is the median home value in the state of California
    - It also contains 20640 samples
    - So, as mentioned earlier, this data is composed of features, which are the variables we use to predict the label
    - And the label, which is the variable we are trying to predict
    - **`[RUN THE CELL]`**
  - **`[OPEN THE NOTEBOOK AND RUN THE FIRST CELL]`**

  - If the data is unlabeled, then the system is unsupervised because it doesn't know what the correct label is
  - On the other hand, if the data is labeled, then the system is supervised because it knows what the correct label is
    - Depending on the label's data type, the system can be classified as either a regression or a classification
    - Regression is a system that predicts a continuous value
    - Whereas classification is a system that predicts a discrete value
  - Once we have our data, we can train our model to predict the labels

    - However, we need to preprocess the data to make it suitable for the model
    - One of the most common preprocessing steps is to split the data into a training set and a test set
    - This is done to make sure that the model can't get information from the test set, so everything in the training set is new for the model

  - With this in mind, let's take a look at one of the most powerful tools for machine learning: "S" "K" learn

- Sklearn is a Python library that implements many machine learning algorithms

  - Apart from ML algorithms, it also contains:
    - Toy datasets
    - Functions and methods to preprocess our data
    - Metrics to measure the performance of our models
    - It also counts with base classes that allows us to create our algorithms

- Let's see how to use this library

  - We can see that using sklearn is incredibly easy
  - In this example, I will use the California house price dataset again
  - **`[RUN THE SECOND CELL]`**
  - This dataset contains information about the median house price in California
  - The data is split into two parts:
    - The first part is the features
    - The second part is the labels
  - Some of the features we can find are median income, median house age in block group, average number of rooms, and so on.
  - **`[RUN THE THIRD CELL] sklearn.model_selection.train_test_split`**
  - As mentioned, the data is split into two sets: training and testing
  - We will see that you can, and should, split the data into another set called validation. But that is not in the scope of this video
  - Now that we have our data ready, let's initialize a simple linear regression model
  - **`[RUN THE FOURTH CELL] sklearn.linear_model.LinearRegression`**
  - Training the model with this data is trivial
  - Use the fit method from the LinearRegression class
  - And the instance we have contains now the parameters to make a prediction
  - **`[RUN THE FIFTH CELL] y_pred = lr.predict(X_test)`**
  - Now that we trained our model, let's make a prediction
  - To do so, simply use the predict method
  - And we obtain the predicted values
  - **`[RUN THE SIXTH CELL] `**
  - We need a way to measure the performance of our model
  - We can use the mean squared error, which measures the difference between the predicted and the actual values
  - So we compare the predicted values with the actual values
  - And we obtain the performance of our model
  - Right now, the number we obtain might not tell you a lot, we will eventually see how to interpret this number
  - Usually linear regression is used to get a baseline
  - We can use sklearn to train models that are better than this baseline, but we won't cover that yet

- Even though sklearn is very powerful and has a great variery of resources, it is not ready for production on its own
  - sklearn is great for testing and learning
  - However, it is not modular enough to be used in production.
  - For example, if you need to implement a pipeline in production, apart from your model, you will need to serialize it with other tools
  - Sklearn, on its own, needs to be implemented within those pipelines, and it is not ready for production until someone implements it
  - Another disadvantage is that it is not suitable to be used for Deep Learning
  - However, it is still a great tool for machine learning
  - And it is hugely used in industry due to its simplicity -->
