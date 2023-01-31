# %%
from torchtext.data.utils import get_tokenizer

text = "The quick BROWN fox jumps over the: lazy dog. The quick brown fox; jumps over the lazy dog!"

tokenizer = get_tokenizer('basic_english')

tokenizer(text)
# %%
