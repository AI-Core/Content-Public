import enum
from torch.utils.data import Dataset
import os
from PIL import Image
from torchvision import transforms


class DogHotdogClassificationDataset(Dataset):
    def __init__(self):
        super().__init__()
        self.examples = self._load_examples()

        self.pil_to_tensor = transforms.ToTensor()
        self.resize = transforms.RandomCrop((64, 64))

    def _load_examples(self):
        classes = os.listdir("classes")  # list all classes
        class_to_idx = {class_name: idx for idx, class_name in enumerate(
            classes)}  # load in all examples
        idx_to_class = {idx: class_name for class_name,
                        idx in class_to_idx.items()}

        examples = []
        for class_name in classes:
            example_img_fps = os.listdir(os.path.join("classes", class_name))
            example_img_fps = [os.path.join(
                "classes", class_name, img_name) for img_name in example_img_fps]
            examples = [(img_fp,  class_to_idx[class_name])
                        for img_fp in example_img_fps]
            examples.extend(examples)

        return examples

    def __getitem__(self, idx):
        img_fp, label = self.examples[idx]  # get image and get label
        print(img_fp)
        img = Image.open(img_fp)
        features = self.pil_to_tensor(img)  # turn image into torch tensor
        features = self.resize(features)
        return (features, label)

    def __len__(self):
        return len(self.examples)


dataset = DogHotdogClassificationDataset()

print(len(dataset))

for example in dataset:

    features, label = example
    print(features.shape)
