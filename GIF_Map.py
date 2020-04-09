# Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import os
# from pysal.esda.mapclassify import Quantiles, Equal_Interval
import geopandas as gpd


# Loading Shapefiles
kenya = "shapefiles\KenyaAdmins.shp"
kenyadoc = "shapefiles\Kenya_April08_Doc_Projections.shp"

map_df = gpd.read_file(kenya)

# GEOdataframe Check
map_df.head()
print(map_df.head())

# Kenya admin test
map_df.plot()

# Adding CSV File
df = pd.read_csv("csv/KenyaSimWeeksDoc.csv", header=0)

df.head()
print(df.head())

# Columns for Map
doc = df[['Admin2', 'uid', 'Week0','Week1', 'Week2', 'Week3', 'Week4', 'Week5', 'Week6']]

# Check dataframe
doc.head()
print(doc.head())

# Join GEOdataframe and CSV datafram
merged = map_df.set_index('uid').join(doc.set_index('uid'))

# Check merged file
merged.head()
print(merged.head())



# CREATE A LOOP TO MAKE MULTIPLE MAPS WITH YEAR ANNOTATIONS

# Setting Loop
output_path = 'charts/maps'
i = 0
list_of_weeks = ['Week0','Week1', 'Week2', 'Week3', 'Week4', 'Week5', 'Week6']
vmin, vmax = 0, 150

for week in list_of_weeks:
    # Create Map
    fig = merged.plot(column=week, cmap='Blues', figsize=(10,10), linewidth=0.8, edgecolor='0.8', vmin=vmin, vmax=vmax, 
                       legend=True, norm=plt.Normalize(vmin=vmin, vmax=vmax))
    # Remove Chart Axis
    fig.axis('off')
    
    # Title
    fig.set_title('Projection of Number of Doctors in Kenya', \
              fontdict={'fontsize': '25',
                         'fontweight' : '3'})
    
    #Add Labels (lvl5name)
    # ax = df.fig()
    # df.apply(lambda x: ax.annotate(s=x.NAME, xy=x.geometry.centroid.coords[0], ha='center'),axis=1);
    
    # Annontate Week
    only_week = week[:7]
    
    # Move Annontation to Bottom Left
    fig.annotate(only_week,
            xy=(0.1, .225), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize=35)
    
    # Export Each Map
    filepath = os.path.join(output_path, only_week+'_Doc.png')
    chart = fig.get_figure()
    chart.savefig(filepath, dpi=300)