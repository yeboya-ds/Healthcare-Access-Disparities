# load data source
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from geopy.distance import geodesic
import sqlite3
import folium
from shapely.geometry import Point, Polygon
import geopandas as gpd

# Step 1: Data Collection & Exploration
# Load the hospital data
hospitals_df = pd.read_csv(r"C:\Users\bye\OneDrive - County of San Mateo\Desktop\hospital parity study\OK maternal hospitals 2019.csv")
print("Hospital data shape:", hospitals_df.shape)
print(hospitals_df.head())
print(hospitals_df.info())
