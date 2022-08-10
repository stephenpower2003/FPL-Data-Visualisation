# FPL-Data-Visualisation
Gameweek 1 data from the Fantasy Premier League (FPL) game is used to produce data visualisation using the Seaborn library. This is to aid decision making and strategy calls for future gameweeks. Using Seaborn, which is a Python data visualization library based on matplotlib, barplots, scatter plots and histograms were created to display data in order to gain a better understanding of this data. All data used was obtained from the 'Fantasy-Premier-League' repository, owned by @vaastav. 

## Bar Plots

### Highest Point Scorers
This bar chart displays the players who scored the highest amount of points in GW1. Scoring points is crucial in FPL, these players who scored highly in GW1 will be in high demand for GW2 and future gameweeks. Python Code: [highest_scorers.py](https://github.com/stephenpower2003/FPL-Data-Visualisation/blob/main/highest_scorers.py)

![Highest Scorers Bar Plot](https://github.com/stephenpower2003/FPL-Data-Visualisation/blob/main/highest_scorers.png)

### Most Saves
This bar chart displays the goalkeepers with the most amount of saves in GW1. A goalkeeper is awarded a single point for every 3 saves made, meaning that the goalkeeper's who racked up a large number of saves will be popular options for the goalkeeper slot within teams. Python Code: [highest_saves.py](https://github.com/stephenpower2003/FPL-Data-Visualisation/blob/main/highest_saves.py)

![Highest Saves Bar Plot](https://github.com/stephenpower2003/FPL-Data-Visualisation/blob/main/highest_saves.png)

### ICT Defenders
This bar chart displays defenders with the best ICT score from GW1. ICT is a feature that uses match-event data to generate a score based on three areas: Influence, Creativity and Threat. Defenders that can provide attacking returns can be very valuable in FPL, meaning defenders with a high ICT score are favourable options. Python Code: [defenders_ict.py](https://github.com/stephenpower2003/FPL-Data-Visualisation/blob/main/defenders_ict.py)

![Defenders ICT Bar Plot](https://github.com/stephenpower2003/FPL-Data-Visualisation/blob/main/defenders_ict.png)

## Scatter Plots

### Total Points by Position
This categorcial scatter plot displays total GW1 points by players and their respective positions. FPL allows users to choose a formation for their team (e.g 4 defenders, 4 midfielders, 2 forwards), ideally you'd want a formation that is tailored to the positions that score a high amount of points. From the scatter plot, it's clear to see that midfielders had the most conistent double digit scorers (players with 10+ points), followed by defenders and then forwards. From this GW1 data alone, a 4-5-1 formation may be the preferred option for future gameweeks as it's a midfielder heavy formation. Python Code: [position_points.py](https://github.com/stephenpower2003/FPL-Data-Visualisation/blob/main/position_points.py)

![Points by Position Categorical Scatter Plot](https://github.com/stephenpower2003/FPL-Data-Visualisation/blob/main/position_points.png)
