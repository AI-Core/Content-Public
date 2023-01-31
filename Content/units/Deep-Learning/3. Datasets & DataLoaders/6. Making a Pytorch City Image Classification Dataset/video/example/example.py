# %%
from torch.utils.data import Dataset
import os
from PIL import Image
from torchvision.transforms import ToTensor


class CityImageClassificationDataset(Dataset):
    def __init__(self):
        super().__init__()
        self._load_examples()

    def _load_examples(self):
        root_dir = "images"
        classes = os.listdir(root_dir)
        class_to_idx = {classname: idx for idx,
                        classname in enumerate(classes)}
        transform = ToTensor()
        self.examples = []
        for classname in classes:
            class_img_fps = os.listdir(os.path.join(root_dir, classname))
            for img_fp in class_img_fps:
                img_fp = os.path.join(root_dir, classname, img_fp)
                img = Image.open(img_fp)
                img_tensor = transform(img)
                example = (img_tensor, class_to_idx[classname])
                self.examples.append(example)

    def __getitem__(self, idx):
        return self.examples[idx]

    def __len__(self):
        return len(self.examples)


dataset = CityImageClassificationDataset()
print(dataset[200])
len(dataset)

# %%
