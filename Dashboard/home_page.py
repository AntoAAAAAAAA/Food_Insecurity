import streamlit as st

st.title("Texas Food Insecurity Dashboard")
st.markdown("""
Welcome to the Texas Food Insecurity Dashboard.

This tool visualizes county-level data on food insecurity, access, and cost in Texas using:
- USDA Food Access Research Atlas
- Map the Meal Gap dataset (Feeding America)

Navigate through the tabs to explore maps, statistics, and insights.
""")

st.subheader('Citations/Sources:')
st.markdown("""
- USDA Food Access Research Atlas: [https://www.ers.usda.gov/data-products/food-access-research-atlas/download-the-data](https://www.ers.usda.gov/data-products/food-access-research-atlas/download-the-data)
    - Gundersen, C., Strayer, M., Dewey, A., Hake, M., & Engelhard, E. (2021). Map the Meal Gap 2021: An Analysis of County and Congressional District Food Insecurity and County Food Cost in the United States in 2019. Feeding America. 
- Feeding America - Map the Meal Gap: [https://map.feedingamerica.org/](https://map.feedingamerica.org/)

    - Dewey, A., Harris, V., Hake, M., & Engelhard, E. (2024). Map the Meal Gap 2024: An Analysis of County and Congressional
District Food Insecurity and County Food Cost in the United States in 2022. Feeding America.)"""
)
