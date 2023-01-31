import torch
from torch.utils.data import DataLoader
from torch.utils.data import Dataset
import torch
from sklearn.datasets import make_classification
import torch.nn.functional as F
from torch.utils.tensorboard import SummaryWriter
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


class LogisticRegression(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_layer = torch.nn.Linear(4, 3)  # initialise parameters

    def forward(self, features):
        return F.softmax(self.linear_layer(features))  # make prediction


def train(model, epochs=10):

    optimiser = torch.optim.SGD(model.parameters(), lr=0.001)

    writer = SummaryWriter()

    batch_idx = 0

    for epoch in range(epochs):
        for batch in train_loader:
            features, labels = batch
            prediction = model(features)
            loss = F.cross_entropy(prediction, labels.long())
            loss.backward()
            print(loss.item())
            optimiser.step()  # optimisation step
            optimiser.zero_grad()
            writer.add_scalar('loss', loss.item(), batch_idx)
            batch_idx += 1


if __name__ == '__main__':
    dataset = IrisDataset()
    train_loader = DataLoader(dataset, shuffle=True, batch_size=8)
    model = LogisticRegression()
    train(model)
