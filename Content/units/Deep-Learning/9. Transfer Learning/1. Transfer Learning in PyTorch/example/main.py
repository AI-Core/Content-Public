from datasets import DogHotdogClassificationDataset
import torch
from torch.utils.data import DataLoader
import torch.nn.functional as F


class DogHotdogClassifier(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.resnet50 = torch.hub.load(
            'NVIDIA/DeepLearningExamples:torchhub', 'nvidia_resnet50', pretrained=True)
        self.resnet50.fc = torch.nn.Linear(2048, 1)

    def forward(self, X):
        return F.sigmoid(self.resnet50(X))


def train(model, dataloader, epochs=20):
    optimiser = torch.optim.Adam(model.parameters(), lr=0.001)
    for epoch in range(epochs):
        for batch in dataloader:
            features, labels = batch
            predictions = model(features)
            labels = labels.unsqueeze(1)
            labels = labels.float()

            loss = F.binary_cross_entropy(predictions, labels)
            loss.backward()
            optimiser.step()
            optimiser.zero_grad()
            print(loss.item())


def accuracy(model, dataset, dataloader):
    m = len(dataset)
    n_correct = 0
    for batch in dataloader:
        features, labels = batch
        predictions = model(features)
        correct = torch.round(predictions.squeeze()) == labels
        n_correct += sum(correct)
    print(f"Accuracy: {torch.round(100*n_correct / m)} %")


if __name__ == '__main__':
    classifier = DogHotdogClassifier()
    dataset = DogHotdogClassificationDataset()
    train_loader = DataLoader(dataset, batch_size=16)
    accuracy(classifier, dataset, train_loader)
    train(classifier, train_loader)
    accuracy(classifier, dataset, train_loader)
