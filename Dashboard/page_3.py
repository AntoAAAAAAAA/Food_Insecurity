# Dashboard/page_3.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title("Food Insecurity Metrics by County")
st.markdown("Use the filters below to explore how food insecurity varies across Texas counties.")

# Load merged data
# data = pd.read_csv("../data/final_merged_notnormalized.csv")
# data.columns = data.columns.str.strip()
mmg = pd.read_csv("data/t19_23_cleaned.csv")
mmg['County'] = mmg['County, State'].str.split(',').str[0]
sns.set(style="whitegrid")
plt.rcParams.update({'figure.figsize': (10, 6)})


# Filter by Overall Food Insecurity Rate
min_cost, max_cost = float(mmg['Overall Food Insecurity Rate'].min()), float(mmg['Overall Food Insecurity Rate'].max())
cost_range = st.slider("Select Food Insecurity Rate Range", min_value=min_cost, max_value=max_cost, value=(min_cost, max_cost))

filtered_data = mmg[(mmg['Overall Food Insecurity Rate'] >= cost_range[0]) & (mmg['Overall Food Insecurity Rate'] <= cost_range[1])]

# 1 Food Insecurity Rate
top_fi = mmg[['County', 'Overall Food Insecurity Rate']].sort_values(by='Overall Food Insecurity Rate', ascending=False).head(18)

fig1 = px.bar(
    top_fi,
    x='Overall Food Insecurity Rate',
    y='County',
    orientation='h',
    color_discrete_sequence=['#2ca02c'],
    title='Top 10 Counties by Food Insecurity Rate'
)
fig1.update_layout(yaxis=dict(autorange="reversed"))
st.plotly_chart(fig1)
st.caption("This horizontal bar chart displays the ten county-year pairs with the highest overall food insecurity rates in Texas. The rates exceed 40% in some counties, highlighting extreme food access disparities.")

#2 Top 20 by % FI ≤ SNAP Threshold
top_snap = mmg[['County', '% FI ≤ SNAP Threshold']].sort_values(by='% FI ≤ SNAP Threshold', ascending=False)
top_snap = top_snap[top_snap['% FI ≤ SNAP Threshold'] < 0.999].head(12)

fig2 = px.bar(
    top_snap,
    x='% FI ≤ SNAP Threshold',
    y='County',
    orientation='h',
    color_discrete_sequence=["#32d7da"],
    title='Top 10 Counties by % FI ≤ SNAP Threshold'
)
fig2.update_layout(yaxis=dict(autorange="reversed"))
st.plotly_chart(fig2)
st.caption("This chart shows counties where the highest proportion of food-insecure individuals fall below the SNAP eligibility threshold, suggesting significant unmet need for nutritional assistance programs.")


# 3 Top 20 by Cost Per Meal
top_cost = mmg[['County', 'Cost Per Meal']].sort_values('Cost Per Meal', ascending=False).head(20)

fig3 = px.bar(
    top_cost,
    x='Cost Per Meal',
    y='County',
    orientation='h',
    color_discrete_sequence=["#94df32"],
    title='Top 20 Counties by Cost Per Meal'
)
fig3.update_layout(yaxis=dict(autorange="reversed"))
st.plotly_chart(fig3)
st.caption("This chart highlights counties with the highest average cost per meal, which can reflect supply chain limitations, geographic isolation, or a lack of affordable food retailers.")


# 4  FI Rate vs. Number of Food Desert Tracts
atlas = pd.read_csv("data/usds_atlas_cleaned.csv")
fd_tracts = atlas.groupby('County')[['LILATracts_1And10']].sum().reset_index()
mmg_fd = mmg.merge(fd_tracts, on='County', how='left')

fig4 = px.scatter(
    mmg_fd,
    y='LILATracts_1And10',
    x='Overall Food Insecurity Rate',
    hover_name='County',
    title='FI Rate vs. Number of Food Desert Tracts'
)
fig4.update_layout(
    yaxis_title="Number of Food Desert Tracts",
    xaxis_title="Overall Food Insecurity Rate"
)
st.plotly_chart(fig4)
st.caption(
    "This scatter plot explores the relationship between the number of food desert tracts and overall food insecurity rates across Texas counties. There appears to be little direct correlation — counties with both very high and very low food insecurity rates often have relatively few food desert tracts, while some mid-range counties show higher counts. This suggests that food deserts may contribute to food insecurity in specific contexts but are not the sole driver statewide."
)



# 5 FI Rate vs. Cost Per Meal
fig5 = px.scatter(
    mmg,
    x='Cost Per Meal',
    y='Overall Food Insecurity Rate',
    hover_name='County',
    color_discrete_sequence=["#6c54e5"],
    title='FI Rate vs. Cost Per Meal'
)
st.plotly_chart(fig5)
st.caption("This scatter plot shows no clear relationship between overall food insecurity rate and cost per meal. Counties with both low and high food insecurity are spread across a wide range of meal costs, suggesting that cost alone is not a consistent predictor of food insecurity.")

# 6 Cost Per Meal vs. Food Insecurity Rate (Filtered)
from pathlib import Path
import pandas as pd
data_path = Path(__file__).parent.parent / "Dashboard" / "data" / "final_merged_notnormalized.csv"
data = pd.read_csv(data_path)

data.columns = data.columns.str.strip()

fig_scatter = px.scatter(
    data, 
    x='Cost Per Meal', 
    y='Overall Food Insecurity Rate',
    hover_name='County',
    color='SNAP Gap',
    color_discrete_sequence=["#a5e9b1"],
    title="Cost Per Meal vs. Food Insecurity Rate (Filtered)"
)
st.plotly_chart(fig_scatter, use_container_width=True)
st.caption("This scatter plot visualizes the relationship between cost per meal and food insecurity rate, with each point colored by SNAP Gap. While no strong trend is evident, the darkest points—indicating the largest SNAP Gaps—cluster around average cost and FI rates. This suggests that counties with the biggest coverage gaps are not necessarily the most food insecure or the most expensive, pointing to potential systemic enrollment or outreach issues.")

# Data table
st.subheader("Filtered Data Table")
st.dataframe(filtered_data, use_container_width=True)

# CSV download
@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv_data = convert_df_to_csv(filtered_data)
st.download_button("⬇️ Download Filtered Data as CSV", csv_data, "filtered_data.csv", "text/csv")
