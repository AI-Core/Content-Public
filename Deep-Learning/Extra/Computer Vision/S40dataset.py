import os
from PIL import Image, ImageDraw
import xml.etree.ElementTree as ET
import torch
from torchvision import transforms

def unnormalise(bndbox, img):
    pass

class S40dataset():

    def __init__(self, img_dir='S40-data/images', annotation_dir='S40-data/annotations', transform=None):
        self.img_dir = img_dir
        self.annotation_dir = annotation_dir
        self.transform = transform

        self.img_names = os.listdir(img_dir)                                  # list all files in the img folder
        self.img_names.sort()                                                   # order the images alphabetically
        self.img_names = [os.path.join(img_dir, img_name) for img_name in self.img_names]   # join folder and file names

        self.annotation_names = os.listdir(annotation_dir)                      # list all annotation files
        self.annotation_names.sort()                                            # order annotation files alphabetically
        self.annotation_names = [os.path.join(annotation_dir, ann_name) for ann_name in self.annotation_names]   # join folder and file names

        #print(self.img_names)
        #print(self.annotation_names)

    def __getitem__(self, idx):
        img_name = self.img_names[idx]
        img = Image.open(img_name)
        #print(img_name)

        annotation_name = self.annotation_names[idx]
        annotation_tree = ET.parse(annotation_name)
        bndbox_xml = annotation_tree.find("object").find("bndbox")

        xmax = int(bndbox_xml.find('xmax').text)
        ymax = int(bndbox_xml.find('ymax').text)
        xmin = int(bndbox_xml.find('xmin').text)
        ymin = int(bndbox_xml.find('ymin').text)
        #print(xmax, ymax, xmin, ymin)

        # CONVERT
        w = xmax - xmin
        h = ymax - ymin
        x = int(xmin + w / 2)
        y = int(ymin + h / 2)

        # NORMALISE
        x /= img.size[0]
        w /= img.size[0]
        y /= img.size[1]
        h /= img.size[1]

        bndbox = (x, y, w, h)

        if self.transform:
            img = self.transform(img)

        bndbox = torch.tensor(bndbox)

        return img, bndbox

    def __len__(self):
        return len(self.img_names)


def unpack_bndbox(bndbox, img):
    bndbox = list(bndbox[0])
    x, y, w, h = tuple(bndbox)
    x *= img.size[0]
    w *= img.size[0]
    y *= img.size[1]
    h *= img.size[1]
    xmin = x - w / 2
    xmax = x + w / 2
    ymin = y - h / 2
    ymax = y + h / 2
    bndbox = [xmin, ymin, xmax, ymax]
    #print(bndbox)
    return bndbox

def show(batch, pred_bndbox=None):
    img, bndbox = batch

    img = img[0]
    #print(img.shape)
    img = transforms.ToPILImage()(img)
    img = transforms.Resize((512, 512))(img)
    draw = ImageDraw.Draw(img)

    bndbox = unpack_bndbox(bndbox, img)
    #print(bndbox)
    draw.rectangle(bndbox)
    if pred_bndbox is not None:
        pred_bndbox = unpack_bndbox(pred_bndbox, img)
        draw.rectangle(pred_bndbox, outline=1000)
    img.show()
    
if __name__ == '__main__':
    from torchvision import transforms
    t = transforms.ToTensor()
    s40 = S40dataset(transform=t)
    ex = s40[0]
    show(s40)
