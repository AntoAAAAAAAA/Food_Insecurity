import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px

st.title("Food Desert Tracts Across Texas Counties")
st.markdown("This interactive map visualizes the number of food desert census tracts in each Texas county, using data from the USDA Food Access Research Atlas.")

# Load and process shapefile
county_shapefile = gpd.read_file("data/tx_counties.geojson")
# county_shapefile = county_shapefile[county_shapefile['STATEFP'] == '48']
county_shapefile.rename(columns={'NAME': 'County'}, inplace=True)
county_shapefile['County'] = county_shapefile['County'].str.replace(' County', '', regex=False)

# Load and group Atlas data
atlas = pd.read_csv("../data/usds_atlas_cleaned.csv")
atlas_grouped = atlas.groupby('County')[['LILATracts_1And10']].sum().reset_index()

# Merge 
atlas_geo = county_shapefile.merge(atlas_grouped, on='County', how='left')
atlas_geo = atlas_geo.to_crs(epsg=4326)
atlas_geo.rename(columns={'LILATracts_1And10': 'Food Desert Tracts'}, inplace=True)

# Map
fig = px.choropleth_mapbox(
    atlas_geo,
    geojson=atlas_geo.geometry.__geo_interface__,
    locations=atlas_geo.index,
    color='Food Desert Tracts',
    hover_name='County',
    hover_data={'Food Desert Tracts': True},
    mapbox_style="carto-positron",
    center={"lat": 31.0, "lon": -99.0},
    opacity=0.6,
    zoom=4.8, # type: ignore
    color_continuous_scale='YlOrBr'
)
fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0})


st.plotly_chart(fig, use_container_width=True)
