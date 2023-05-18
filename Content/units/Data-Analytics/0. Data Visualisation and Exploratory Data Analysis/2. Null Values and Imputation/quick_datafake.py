#%%
from sklearn.datasets import fetch_california_housing
import pandas as pd
import numpy as np

df = fetch_california_housing(as_frame=True).frame

class NullGenerator:
    '''replaces a random 10% of the values in each column with nulls '''
    
    def __init__(self,df):
        self.df = df
        self.ruin_all_columns()

    def gen_nulls(self,col,frac=0.1):
        #Randomly replace k% of the column with NaN values
        self.df.loc[self.df.sample(frac=frac).index, col] = np.nan
    
    
    def ruin_all_columns(self):
        for col in self.df.columns:
            if col != 'MedHouseVal':
                frac = np.random.choice([0.05, 0.01, 0.001, 0.35, 0.1, 0.39, 0.2])
                self.gen_nulls(col,frac)
            


nullerator = NullGenerator(df)
nulled_df = nullerator.df
nulled_df.head()


nulled_df.head()
nulled_df.info()

# find percentage nulls for each column in nulled_df:
print('percentage of null values in each column:')

# write to csv:
nulled_df.to_csv('nulled_df.csv',index=False)
nulled_df.isnull().sum()/len(nulled_df)
# %%
