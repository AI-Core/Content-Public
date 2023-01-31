# %%
import numpy as np


def softmax(logits):
    return np.exp(logits) / np.sum(np.exp(logits))


print(softmax([1, 2, 3]))

# %%
