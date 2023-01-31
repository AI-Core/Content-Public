import torch
from torchvision.datasets import MNIST
from torch.utils.data import DataLoader
from torchvision.transforms import PILToTensor

dataset = MNIST(root='./data', download=True,
                train=True, transform=PILToTensor())

train_loader = DataLoader(dataset, batch_size=16, shuffle=True)

for batch in train_loader:
    print(batch)
    features, labels = batch
    print(features.shape)
    print(labels.shape)
    break
