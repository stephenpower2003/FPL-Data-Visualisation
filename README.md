# FPL-Data-Visualisation
Gameweek 1 data from the Fantasy Premier League (FPL) game is used to produce data visualisation using the Seaborn library. This is to aid decision making and strategy calls for future gameweeks, as well as understanding patterns and trends. Using Seaborn, which is a Python data visualization library based on matplotlib, barplots and scatter plots were created to display data in order to gain a better understanding of this data. All data used was obtained from the 'Fantasy-Premier-League' repository, owned by @vaastav. 

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
This categorcial scatter plot displays total GW1 points by players and their respective positions. FPL allows users to choose a formation for their team (e.g 4 defenders, 4 midfielders, 2 forwards), ideally you'd want a formation that is tailored to the positions that score a high amount of points. From the scatter plot, it's clear to see that midfielders had the most conistent double digit scorers (players with 10+ points), followed by defenders and then forwards. Defenders were also the only position to have players with minus points, meaning there is some risk with that position. From this GW1 data alone, a 4-5-1 or 3-5-2 formation may be the preferred options for future gameweeks as they are midfielder heavy formations. Python Code: [position_points.py](https://github.com/stephenpower2003/FPL-Data-Visualisation/blob/main/position_points.py)

![Points by Position Categorical Scatter Plot](https://github.com/stephenpower2003/FPL-Data-Visualisation/blob/main/position_points.png)

### Total Points by Home or Away
This categorical scatter plot displays total GW1 points by players and whether or not they played their fixture at home or away from home. A lot is made about playing a fixture at home in front of home support or away against an opposing crowd. FPL users can choose a single player as their captain for each gameweek, which this player will have their points doubled. Choosing between a player with a home fixture or a player with an away fixture to set as your captain comes into in the decision making process. Judging by this GW1 data, playing home or away had no effect on the general spread of point scoring by players. Python Code: [points_home_away.py](https://github.com/stephenpower2003/FPL-Data-Visualisation/blob/main/points_home_away.py)

![Points by Home/Away Categorical Scatter Plot](https://github.com/stephenpower2003/FPL-Data-Visualisation/blob/main/points_home_away.png)

### Total Points vs ICT Score
This scatter plot displays GW1 points by players on the y axis and their ICT score on the x axis. It's clear to see from the scatter plot that there is a strong positive relationship between total points in GW1 and ICT score. This tells us that players who are scoring a large amount of points are also getting a high ICT score meaning they are influencing games, showing creativity and are threatening in front of goal. Conversely, players who scored a low amount of points have a low ICT score. Python Code: [points_ict.py](https://github.com/stephenpower2003/FPL-Data-Visualisation/blob/main/points_ict.py)

![Points vs ICT Scatter Plot](https://github.com/stephenpower2003/FPL-Data-Visualisation/blob/main/points_ict.png)
 
