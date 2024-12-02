import pandas as pd
import folium
import streamlit as st
import pgeocode
import datetime
from streamlit_folium import st_folium # Plots folium map to the Streamlit app
from branca.colormap import linear

# Streamlit app display
st.title("Los Angeles by Region")
st.header("Map of Los Angeles")
st.write("See AirBnB information by region and popular Los Angeles attractions!")

geojson_file = "output_file.geojson"

m = folium.Map([34.000333, -118.213139])

# Add GeoJSON to the map with hover functionality
folium.GeoJson(
    data=open(geojson_file, 'r').read(),  # Load GeoJSON data
    name="Regions",
    tooltip=folium.GeoJsonTooltip(
        fields=["NAME","price", "number"],  # Replace with the property names in your GeoJSON file
        aliases=["Region Name:", "Average Price/Night:", "Number of AirBnBs"],
        localize=True,  # Localize tooltip data
    )
).add_to(m)

attractions = pd.read_csv('attractions.csv')

for index, row in attractions.iterrows():
   folium.Marker(
       location = [row['latitude'], row['longitude']],
       icon = folium.Icon(icon = row['icon'], prefix = 'fa'),
       popup = folium.Popup(
           f"""
           {row['name']}<br>
           Website: {row['website']}<br>
           {row['description']}
           """,
           max_width = 250)
   ).add_to(m)

# Add layer control
folium.LayerControl().add_to(m)

st_folium(m, width = 700, height = 500)

st.write('Press on each icon to see attraction information.')