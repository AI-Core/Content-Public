import torch
from torch.utils.data import DataLoader
from torch.utils.data import Dataset
import torch
from sklearn.datasets import load_diabetes
import torch.nn.functional as F
from torch.utils.tensorboard import SummaryWriter


class DiabetesDataset(Dataset):
    def __init__(self):
        super().__init__()
        self.X, self.y = load_diabetes(return_X_y=True)

    def __getitem__(self, idx):
        return (torch.tensor(self.X[idx]).float(), torch.tensor(self.y[idx]).float())

    def __len__(self):
        return len(self.X)


class LinearRegression(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_layer = torch.nn.Linear(10, 1)  # initialise parameters

    def forward(self, features):
        return self.linear_layer(features)  # make prediction


def train(model, epochs=10):

    optimiser = torch.optim.SGD(model.parameters(), lr=0.001)

    writer = SummaryWriter()

    batch_idx = 0

    for epoch in range(epochs):
        for batch in train_loader:
            features, labels = batch
            prediction = model(features)
            loss = F.mse_loss(prediction, labels)
            loss.backward()
            print(loss.item())
            optimiser.step()  # optimisation step
            optimiser.zero_grad()
            writer.add_scalar('loss', loss.item(), batch_idx)
            batch_idx += 1


if __name__ == '__main__':
    dataset = DiabetesDataset()
    train_loader = DataLoader(dataset, shuffle=True, batch_size=4)
    model = LinearRegression()
    train(model)
