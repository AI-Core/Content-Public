# %%
import torch
import numpy as np

print(torch.tensor(np.array([2.0, 3.0, 4.0])))

# %%
x = torch.rand(3, 4, 4, 5)
print(x)
print(x.shape)
print(x.dtype)
# %%
torch.ones(3, 4)
# %%
x + 1
# %%
torch.matmul(torch.rand(2, 3), torch.rand(3, 1))

# %%
x.sum()
# %%
