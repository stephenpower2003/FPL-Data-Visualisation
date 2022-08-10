# Import statements
import pandas as pd
import numpy as np
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

# Path of the file
gw1_data_filepath = "../input/gw1-data/GW1.csv"

plt.figure(figsize=(14, 7))
plt.title("Total Points vs ICT Score")

# Pandas reads the file
gw1_data = pd.read_csv(gw1_data_filepath)

# Scatter Plot is defined
sns.regplot(x=gw1_data['ict_index'], y=gw1_data['total_points'])

plt.ylabel("Total Points")
plt.xlabel("ICT Score")
plt.yticks(np.arange(0, 16, 2))

