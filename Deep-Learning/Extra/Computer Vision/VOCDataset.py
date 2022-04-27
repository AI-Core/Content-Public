import torch
from torchvision import transforms
import os
from PIL import Image

label_transform = transforms.Compose([
    transforms.ToTensor()
])

class VOC(torch.utils.data.Dataset):
    def __init__(self, root, input_transform=None):
        self.root = root
        self.filenames = [fn.split('.')[0] for fn in os.listdir(f'{self.root}/SegmentationClass')]
        self.input_transform = input_transform

    def __getitem__(self, idx):
        fn = self.filenames[idx]
        img = Image.open(f'{self.root}/JPEGImages/{fn}.jpg')
        label = Image.open(f'{self.root}/SegmentationClass/{fn}.png')

        if self.input_transform:
            img = self.input_transform(img)

        label = label_transform(label)
        return (img, label)
    
    def __len__(self):
        return len(self.input_fps)
