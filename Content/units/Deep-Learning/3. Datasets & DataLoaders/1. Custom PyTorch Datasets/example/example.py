import pandas as pd
from torch.utils.data import Dataset
import torch
from sklearn.datasets import load_iris


class IrisDataset(Dataset):
    def __init__(self):
        super().__init__()
        self.X, self.y = load_iris(return_X_y=True)

    def __getitem__(self, index):
        features = self.X[index]
        features = torch.tensor(features).float()
        label = torch.tensor(self.y[index]).float()
        return (features, label)

    def __len__(self):
        return len(self.X)


dataset = IrisDataset()
print(dataset[10])
print(len(dataset))
