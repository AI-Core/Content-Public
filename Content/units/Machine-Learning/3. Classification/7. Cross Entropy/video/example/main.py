import numpy as np


def cross_entropy_loss(predictions, target):
    true_class_probability = predictions[target]
    return - np.log(true_class_probability)


predictions = [1, 0, 0]
target = 0
print(cross_entropy_loss(predictions, target))
