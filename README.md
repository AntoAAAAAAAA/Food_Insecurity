# Texas Food Insecurity Dashboard

An interactive, county-level dashboard that visualizes food insecurity rates and food desert designations across Texas. Built with Streamlit to support public health research, awareness, and policy conversations.

## Live App
**Try it here:** https://foodinsecurity.streamlit.app/

## Purpose
This dashboard helps users:
- Explore where food insecurity is most concentrated in Texas
- Understand how food deserts and low vehicle access impact rural and urban areas
- Analyze disparities affecting minority populations and children

It was developed as part of a public health project focused on health equity and data storytelling.

## Features
- **Choropleth maps** showing:
  - Food desert tracts (low income + low access)
  - Counties with high food insecurity rates
  - Areas with low vehicle access
- **Bar and scatter plots** comparing food insecurity across demographic groups
- **Merged datasets** from USDA, Feeding America, and U.S. Census
- **Key findings** and **personal reflections** built into the app

## Why This Matters
Access to nutritious food is a core driver of health outcomes. This tool helps:
- Visualize need at a hyperlocal level
- Inform policy and resource distribution
- Provide a starting point for further research or community interventions

## Built With
- **Streamlit** (frontend)
- **Pandas / GeoPandas** (data processing)
- **Plotly** (maps & charts)
- **Python**
- Public datasets: USDA Food Access Atlas, Feeding America Map the Meal Gap, U.S. Census
