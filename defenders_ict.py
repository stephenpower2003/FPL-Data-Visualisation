# Import statements
import pandas as pd
import numpy as np
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

# Path of the file
gw1_data_filepath = "../input/gw1-data/GW1.csv"

plt.figure(figsize=(14, 7))
plt.title("Highest Amount of ICT Score by Defenders from GW1")

# Pandas reads the file
gw1_data = pd.read_csv(gw1_data_filepath, index_col="name")

# Midfielders, Forwards and Goalkeepers are dropped
gw1_data.drop(gw1_data[gw1_data['position'] == 'MID'].index, inplace=True)
gw1_data.drop(gw1_data[gw1_data['position'] == 'FWD'].index, inplace=True)
gw1_data.drop(gw1_data[gw1_data['position'] == 'GK'].index, inplace=True)
gw1_data.drop(gw1_data[gw1_data['ict_index'] <= 7.5].index, inplace=True)

# Barplot is defined
sns.barplot(x=gw1_data.index, y=gw1_data['ict_index'])

plt.ylabel("ICT Score")
plt.xlabel("Player Name")
plt.xticks(rotation=15, horizontalalignment="center")
plt.yticks(np.arange(0, 12.5, 2.5))
