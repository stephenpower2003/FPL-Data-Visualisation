# Import statements
import pandas as pd
import numpy as np
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

# Path of the file
gw1_data_filepath = "../input/gw1-data/GW1.csv"

plt.figure(figsize=(14, 7))
plt.title("Highest Point Scorers from GW1")

# Pandas reads the file
gw1_data = pd.read_csv(gw1_data_filepath, index_col="name")

# Players with less than 12 total points are dropped
gw1_data.drop(gw1_data[gw1_data['total_points'] <= 11].index, inplace=True)

# Bar plot is defined
sns.barplot(x=gw1_data.index, y=gw1_data['total_points'])

plt.ylabel("Total Points")
plt.xlabel("Player Name")
plt.xticks(rotation=15, horizontalalignment="center")
plt.yticks(np.arange(0, 16, 2))
