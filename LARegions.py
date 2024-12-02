import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

# Load the LA region boundaries
regions_gdf = gpd.read_file('SCAG_Regions.geojson')

# Ensure the CRS is consistent
regions_gdf = regions_gdf.to_crs(epsg=4326)  # WGS 84

# Load the CSV file with latitudes and longitudes
df = pd.read_csv('California_airbnb.csv')

# Create a geojson from the CSV
geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
points_gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")

# Spatial join to determine which region each point belongs to
joined_gdf = gpd.sjoin(points_gdf, regions_gdf, how='left', predicate='within')

# Save the output with region information
joined_gdf[['latitude', 'longitude', 'NAME']].to_csv('output_with_regions.csv', index=False)