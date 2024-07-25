#%%

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.style as style

df_1 = pd.read_csv("https://aicore-files.s3.amazonaws.com/Data-Science/influential/1.txt", sep="\t", encoding="utf-16")
df_2 = pd.read_csv("https://aicore-files.s3.amazonaws.com/Data-Science/influential/2.txt", sep="\t", encoding="utf-16")
df_3 = pd.read_csv("https://aicore-files.s3.amazonaws.com/Data-Science/influential/3.txt", sep="\t", encoding="utf-16")
df_4 = pd.read_csv("https://aicore-files.s3.amazonaws.com/Data-Science/influential/4.txt", sep="\t", encoding="utf-16")
df_list = [df_1, df_2, df_3, df_4]

for df in df_list:
    df.drop("Row", axis=1, inplace=True)
    df.columns = ["YoE", "Salary"] # YoE = Years of Experience

#plot the data with seaborn
plt.rc("axes.spines", top=False, right=False)
sns.set_style(style='darkgrid', rc=None)

five_thirty_eight = [
    "#30a2da",
    "#fc4f30",
    "#e5ae38",
    "#6d904f",
    "#8b8b8b",
]
style.use('fivethirtyeight')
sns.set_palette(five_thirty_eight)

#


# %%
