import pandas as pd
import json

# File paths
geojson_file = "SCAG_Regions.geojson"
csv_file = "Ca_map.csv"
output_geojson_file = "output_file.geojson"

# Load GeoJSON data
with open(geojson_file, 'r') as f:
    geojson_data = json.load(f)

# Load CSV data into a Pandas DataFrame
csv_data = pd.read_csv(csv_file)

# Ensure column names match between CSV and GeoJSON
geojson_key = "NAME"  # Key in GeoJSON (e.g., region name)
csv_key = "region"  # Key in CSV (e.g., region name)

valid_regions = set(csv_data[csv_key])

# Filter GeoJSON features
filtered_features = [
    feature for feature in geojson_data['features']
    if feature['properties'].get(geojson_key) in valid_regions
]

# Update the GeoJSON data with the filtered features
geojson_data['features'] = filtered_features

# Iterate over GeoJSON features and add data from CSV
for feature in geojson_data['features']:
    region_name = feature['properties'].get(geojson_key)
    # Find matching row in the CSV
    match = csv_data[csv_data[csv_key] == region_name]
    if not match.empty:
        # Add data to GeoJSON properties
        for col in csv_data.columns:
            if col != csv_key:  # Skip the key column
                feature['properties'][col] = match.iloc[0][col]

# Save the updated GeoJSON file
with open(output_geojson_file, 'w') as f:
    json.dump(geojson_data, f)

print(f"Data merged successfully. Output saved to {output_geojson_file}")
