import pandas as pd
import numpy as np
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

gw1_data_filepath = "../input/gw1-data/GW1.csv"

plt.figure(figsize=(14, 7))
plt.title("Highest Point Scorers from GW1")

gw1_data = pd.read_csv(gw1_data_filepath, index_col="name")

gw1_data.drop(gw1_data[gw1_data['total_points'] <= 11].index, inplace=True)
sns.barplot(x=gw1_data.index, y=gw1_data['total_points'])

plt.ylabel("Total Points")
plt.xlabel("Player Name")
plt.xticks(rotation=15, horizontalalignment="center")
plt.yticks(np.arange(0, 16, 2))
