# %%
import torch
from torchvision import transforms
from PIL import Image

model = torch.hub.load('hustvl/yolop', 'yolop', pretrained=True)

# %%

img = Image.open('road.jpeg')
# img.show()

t = transforms.ToTensor()
resize_transform = transforms.Resize((640, 640))
tensor_to_img = transforms.ToPILImage()


features = t(img)
features = resize_transform(features)

# tensor_to_img(features).show()

print(features.shape)
features = features.unsqueeze(0)
print(features.shape)


# %%
# img = torch.randn(1, 3, 640, 640)
det_out, da_seg_out, ll_seg_out = model(features)

# %%
print(det_out)
print(det_out[0].shape)
# %%
