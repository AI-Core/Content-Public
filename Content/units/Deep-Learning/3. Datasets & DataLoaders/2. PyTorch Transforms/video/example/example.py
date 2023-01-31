import torch
from torchvision.datasets import MNIST
from torch.utils.data import DataLoader
from torchvision import transforms

dataset = MNIST(root='./data', download=True,
                train=True, transform=transforms.PILToTensor())

example = dataset[0]
features, label = example

print(features)
