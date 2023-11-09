#%%
import numpy as np
import pandas as pd

# Generate 99 random ages for dogs between 1 and 15
np.random.seed(42)  # for reproducibility
ages = np.random.randint(1, 16, 99)

# Add one outlier age of 30
ages = np.append(ages, 30)

# Convert to a pandas DataFrame for easier handling
df_dog_ages = pd.DataFrame(ages, columns=['Age'])

df_dog_ages.to_csv('dog_ages.csv', index=False)

# %%
