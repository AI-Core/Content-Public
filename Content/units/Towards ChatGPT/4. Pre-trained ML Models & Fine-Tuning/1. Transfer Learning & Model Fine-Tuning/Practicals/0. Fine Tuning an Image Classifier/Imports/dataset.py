# %%
import os
import random
from PIL import Image
from torchvision import transforms
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt


class City:
    def __init__(self, city_name):
        self.images = os.listdir(os.path.join("images", city_name))
        self.images = [os.path.join("images", city_name, fp)
                       for fp in self.images]
        self.name = city_name

    def __repr__(self):
        return f"{self.name} ({len(self.images)} images)"

    def show(self):
        img_fp = random.choice(self.images)
        img = Image.open(img_fp)
        img.show()


class CitiesDataset:
    """Many examples of images from different cities"""

    def __init__(self, transform):
        self.cities = self.get_cities().values()

        self.city_name_to_idx = {
            city.name: city_idx for city_idx, city in enumerate(self.cities)
        }
        self.idx_to_city_name = {
            value: key for
            key, value in self.city_name_to_idx.items()
        }

        self.all_imgs = []
        for city in self.cities:
            self.all_imgs.extend(city.images)
        self.transform = transform

    def __len__(self):
        return len(self.all_imgs)

    def get_normalisation_parameters(self):
        images, _ = self.get_X_y()
        print(images)
        

    def get_cities(self):
        city_map = {}
        city_fps = os.listdir("images")
        # print(cities)
        for city_name in city_fps:
            city_map[city_name] = City(city_name)
        return city_map

    def __repr__(self):
        return "hello"  # str(self.cities)

    # TODO define how to index this class with a city name
    def __getitem__(self, example_idx):
        """Get me the image of example 10 (example_idx)"""
        img_fp = self.all_imgs[example_idx]
        return self.get_X_y_from_fp(img_fp)

    def get_X_y_from_fp(self, img_fp):
        city_name = img_fp.split("/")[1]
        # print(img_fp)
        img = Image.open(img_fp)
        if self.transform:
            img = self.transform(img)
        city_idx = self.city_name_to_idx[city_name]
        return img, city_idx

    def get_X_y(self):

        images = [
            np.array(
                self.transform(
                    Image.open(img_fp)
                )
            ).flatten()
            for img_fp in self.all_imgs
        ]
        city_names = [img_fp.split("/")[1] for img_fp in self.all_imgs]
        # extra transform

        return images, city_names




if __name__ == "__main__":
    cities = CitiesDataset(transform=None)
    # for example in cities:
    #     print(example)
    print(len(cities))


# %%
