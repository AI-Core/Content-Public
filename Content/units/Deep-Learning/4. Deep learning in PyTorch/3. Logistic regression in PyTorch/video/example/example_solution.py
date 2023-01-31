import torch
from torch.utils.data import DataLoader
from torch.utils.data import Dataset
import torch
from sklearn.datasets import make_classification
import torch.nn.functional as F
from torch.utils.tensorboard import SummaryWriter


class BinaryClassificationDataset(Dataset):
    def __init__(self):
        super().__init__()
        self.X, self.y = make_classification(
            n_features=3, n_classes=2, n_redundant=0, n_informative=2, random_state=1, n_clusters_per_class=1
        )
        self.X = torch.tensor(self.X).float()
        self.y = torch.tensor(self.y).float()

    def __getitem__(self, idx):
        return (self.X[idx], self.y[idx].reshape(1))

    def __len__(self):
        return len(self.X)


dataset = BinaryClassificationDataset()

train_loader = DataLoader(dataset, shuffle=True, batch_size=8)

example = next(iter(train_loader))
features, labels = example
print(features)
print(labels)


class LogisticRegression(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_layer = torch.nn.Linear(3, 1)  # initialise parameters

    def forward(self, features):
        return F.sigmoid(self.linear_layer(features))  # make prediction


model = LogisticRegression()


def train(model, epochs=10):

    optimiser = torch.optim.SGD(model.parameters(), lr=0.001)

    writer = SummaryWriter()

    batch_idx = 0

    for epoch in range(epochs):
        for batch in train_loader:
            features, labels = batch
            prediction = model(features)
            loss = F.binary_cross_entropy(prediction, labels)
            loss.backward()
            print(loss.item())
            optimiser.step()  # optimisation step
            optimiser.zero_grad()
            writer.add_scalar('loss', loss.item(), batch_idx)
            batch_idx += 1


train(model)
