# %%

import torch

from torchvision.datasets import MNIST

dataset = MNIST(root='./data', download=True, train=True)

example = dataset[45]
print(example)

features, label = example

print(features)
print(label)
features.show()

# %%
