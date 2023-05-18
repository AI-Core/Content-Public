#%%
import pandas as pd
import numpy as np

def gen_nulls(df,col,frac=0.1):
    #Randomly replace k% of the column with NaN values
    df.loc[df.sample(frac=frac).index, col] = np.nan
    return df
    
    
df = pd.read_csv('jiffs_house_price_my_dataset_v1.csv')
df = gen_nulls(df,'no_of_bathrooms',0.0326)
df = gen_nulls(df,'distance_to_supermarket_km',0.0544)
df = gen_nulls(df,'property_value',0.00944)
# find percentage nulls for each column in nulled_df:
print('percentage of null values in each column:')

# write to csv:
df.to_csv('house_price_dataset_with_nulls.csv',index=False)
df.isnull().sum()/len(df)
# %%
