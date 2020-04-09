# Libraries
# import numpy as np
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

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

# Set column to call
variable = 'Week1'

# Set range for the choropleth
vmin, vmax = 0, 150

# Create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(20, 12))

# Create first map
merged.plot(column=variable, cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8')

# Remove the all axis
ax.axis('off')

# Adding Title
ax.set_title('Healthcare Staff Capacity Week 1 Projection', \
              fontdict={'fontsize': '25',
                        'fontweight' : '3'})

# Data source annontation
ax.annotate('Source: PEPFAR',
           xy=(0.3, .10), xycoords='figure fraction',
           horizontalalignment='left', verticalalignment='top',
           fontsize=10, color='#555555')
           
# Colorbar legend
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)

# Export test map
fig.savefig('testmap.png', dpi=300)