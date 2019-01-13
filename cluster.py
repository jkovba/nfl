import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import spectral_clustering
import pandas

#plays_df = pandas.read_csv("~/nfl/plays.csv", usecols=["personnel.offense", "personnel.defense", "defendersInTheBox", "PlayResult", "offenseFormation", "numberOfPassRushers", "down", "YardsAfterCatch"])
plays_df = pandas.read_csv("~/nfl/plays.csv")

# re-size the plot
fig, ax = plt.subplots(figsize=(14,11))

# computer the correlation
correlation = plays_df.corr()

# build a heatmap of the correlation and tweakthe labels 
fig = sns.heatmap(correlation, square=True, ax=ax)
fig.set_xticklabels(fig.get_xticklabels(), rotation='vertical')
fig.set_yticklabels(fig.get_yticklabels(), rotation='horizontal')

fig_rotated = fig.get_figure()

fig_rotated.savefig("heat_map.jpg")

