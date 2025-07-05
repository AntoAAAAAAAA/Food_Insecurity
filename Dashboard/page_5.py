import streamlit as st
import pandas as pd

st.title("Find Your County's Food Insecurity Data")
st.markdown("Select your county to see key metrics about food insecurity, SNAP access, and food desert tracts.")

# Load data
from pathlib import Path
import pandas as pd
data_path = Path(__file__).parent.parent /"Dashboard" / "data" / "final_merged_notnormalized.csv"
data = pd.read_csv(data_path)

data.columns = data.columns.str.strip()
counties = sorted(data['County'].dropna().unique())

selected_county = st.selectbox("Select Your County", counties)

if selected_county:
    county_data = data[data['County'] == selected_county].squeeze()

    st.markdown(f"### {selected_county} County Data:")
    st.markdown(f"- **Overall Food Insecurity Rate**: {county_data['Overall Food Insecurity Rate']:.2f}")
    st.markdown(f"- **SNAP Gap**: ${county_data['SNAP Gap']:,.2f}")
    st.markdown(f"- **% FI ≤ SNAP Threshold**: {(county_data['% FI ≤ SNAP Threshold'] * 100):.2f}%")
    st.markdown(f"- **Cost Per Meal**: ${county_data['Cost Per Meal']:.2f}")
    st.markdown(f"- **Food Desert Tracts**: {county_data['LILATracts_1And10']}")