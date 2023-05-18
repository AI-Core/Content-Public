import matplotlib.pyplot as plt
import matplotlib.style as style
import seaborn as sns
plt.rc("axes.spines", top=False, right=False)
sns.set_style(style='darkgrid', rc=None)
style.use('fivethirtyeight')
five_thirty_eight = [
    "#30a2da",
    "#fc4f30",
    "#e5ae38",
    "#6d904f",
    "#8b8b8b",
]
sns.set_palette(five_thirty_eight)