import torch
from torch.utils.data import DataLoader
from torch.utils.data import Dataset
import torch
from sklearn.datasets import load_diabetes


class DiabetesDataset(Dataset):
    def __init__(self):
        super().__init__()
        self.X, self.y = load_diabetes(return_X_y=True)

    def __getitem__(self, idx):
        return (torch.tensor(self.X[idx]).float(), torch.tensor(self.y[idx]).float())

    def __len__(self):
        return len(self.X)


dataset = DiabetesDataset()

train_loader = DataLoader(dataset, shuffle=True, batch_size=4)

example = next(iter(train_loader))
features, labels = example
print(features)
print(labels)


class LinearRegression(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.linear_layer = torch.nn.Linear(10, 1)

    def forward(self, features):
        return self.linear_layer(features)


model = LinearRegression()
prediction = model(features)
print(prediction)
