import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("In-Depth Analysis and Findings")

st.markdown("""
This page consolidates the key questions and findings from your three core analyses: the USDA Atlas, Map the Meal Gap (MMG), and the merged dataset. It serves as a readable narrative that explains what was discovered and why it matters.

---

## USDA Food Access Research Atlas (FARA)

**1. Which counties have the most number of food desert tracts?**  
Counties like Harris, Dallas, Bexar, and El Paso had the highest raw number of food desert tracts due to their large urban size and dense populations.

**2. What about less strict food desert definitions (LILATracts_halfAnd10, 1And20, Vehicle)?**  
Using these looser definitions, the number of tracts labeled as food deserts increases, and rural counties show up more prominently. 
1,022 census tracts were defined as food deserts under the stricter definition, but 1,035 tracts were included under the looser definitions. 
Vehicle access plays a key role in identifying these more vulnerable regions.  

**3. What tracts are food deserts, but also have low vehicle access? Which ones are food deserts, but don't have low vehicle access?**  
A notable subset of food desert tracts also met the criteria for low vehicle access. These were most commonly found in rural counties or outer suburbs.
"""
)
grid = pd.read_csv('Dashboard/data/fd_and_lva_grid.csv')
st.table(grid)
st.markdown("""

**4. Which counties don't have any food desert tracts?**   
There are 84 counties in Texas that, according to the USDS FARA, do not report any food desert census tracts. 
            
**5. What percent of all Texas tracts are food deserts?**  
Roughly 15–20% of all census tracts in Texas qualify under one of the USDA's food desert definitions.

**6. How many people live in food deserts across Texas?**  
Using the most specific definition of a food desert in the dataset, 4,926,344 Texans live in food deserts. 
This is roughly 20% of Texans. When expanding our definition of a food desert to less strict definitions, we see the percentage skyrocket to nearly 40% of all Texans
living in food deserts. 
            
**7. Rural vs. urban: how does food desert prevalence differ?**  
According to the dataset, the large majority of all food desert tracts are located in urban areas. Food desert prevalence tends to 
concentrate in more urban regions of Texas. Roughly 22% of urban tracts are food deserts, meanwhile roughly 10% of rural tracts are food desert tracts. 
Of all food desert tracts in Texas, nearly 90% are urban and 10% are rural. 
            
**8. Which counties have the most children in low-income tracts?**  
Counties like Harris, Dallas, and Bexar had large numbers of children living in low-income areas, especially those identified as food deserts.

**9. Do food deserts correlate with minority population %?**  
No. There did no seem to be a significant correlation. Looking at the counties that had the most amount of food desert tracks and comparing them to the counties that had the highest percentages of black persons, there was no significant overlap.

---

## Map the Meal Gap (MMG)

**1. What counties have the highest food insecurity rates?**  
Dimmit, Starr, Zavala, and Presidio frequently ranked among the highest in FI rate (>30%). These are rural, low-income counties with limited access.
Top 10 counties by average food insecurity rate (2019–2023):
1. Presidio: 26.78%
2. Dimmit: 25.52%
3. Starr: 24.70%
4. Brooks: 24.48%
5. Zavala: 23.96%
6. Zapata: 23.48%
7. San Augustine: 22.44%
8. Real: 22.02%
9. Jim Hogg: 21.28%
10. Cottle: 21.18%
""")
st.markdown("""
**2. Where is food insecurity especially high among minorities?**  
Counties like Maverick, Webb, and Hidalgo showed high food insecurity among Hispanic populations. Similar patterns appeared for Black populations in certain urban areas.
""")
col1, col2 = st.columns(2)
with col1:
    st.text('''Counties with the highest food insecurity rates among black persons:
1. Ward: 56.00%
2. Fannin: 46.00%
3. Ward: 46.00%
4. Matagorda: 45.00%
5. Kleberg: 45.00%
6. Jasper: 44.00%
7. Fannin: 44.00%
8. Newton: 44.00%
9. Tyler: 43.00%
10. Matagorda: 43.00%''')

with col2: 
    st.text('''Counties with the highest food insecurity rates among hispanic people:
1. Newton: 53.00%
2. Menard: 41.00%
3. Menard: 40.00%
4. Presidio: 40.00%
5. Dimmit: 37.00%
6. San Augustine: 37.00%
7. Newton: 36.00%
8. San Augustine: 36.00%
9. Presidio: 35.00%
10. Duval: 34.00%''')

st.markdown("""
**3. Where is there a mismatch between Percent of People **ABOVE** the SNAP threshold and Overall Food Insecurity Rate?**  
Some suburban counties showed alarmingly high proportions of food-insecure people who did not meet SNAP eligibility, indicating gaps in coverage. 
Counties like Loving, Kenedy, and Kent counties stuck out as counties where there were large portions of people who were elgible for SNAP, yet had higher than expected rates of overall food insecurity. 
""")
#import data
data = pd.read_csv('Dashboard/data/t19_23_cleaned.csv')
data.rename(columns={'County, State': 'County'}, inplace=True)

#plot
graph = data[['County', 'Overall Food Insecurity Rate', '% FI > SNAP Threshold']].copy()
fig, ax = plt.subplots()
ax.scatter(graph['Overall Food Insecurity Rate'], graph['% FI > SNAP Threshold'])
ax.set_title('Percent of People Over the SNAP Threshold vs. Overall Food Insecurity Rate (per county)')
ax.set_xlabel('Overall Food Insecurity Rate')
ax.set_ylabel('% FI > SNAP Threshold')
st.pyplot(fig)
st.caption('''
Fig 1. The graph shows the expected negative correlation between food insecurity and percentage of people OVER the SNAP Threshold.
However, this graph is helpful in helping identify that there are in fact counties that don't follow this trend. Dots in the top right side of the 
graph in particular indicate counties with high food insecurity, yet also have a large percent of the population above the SNAP threshold. These are interesting cases that can be studied further. 
''')

#table
graph['SNAP Gap Index'] = (
    graph['% FI > SNAP Threshold'] * graph['Overall Food Insecurity Rate']
).round(4)
st.table(graph.sort_values(ascending=False, by='SNAP Gap Index').head(10).reset_index(drop=True))
st.caption('''
Fig 2. This table uses a created variable called 'SNAP Gap Index' to track the overall food insecurity of a county. This variable was created with the normalization and addition of multiple variables that we believe add to the food insecurity of a county. This index helps show which counties are in the most dire need. 
''')

# Z-score
from scipy.stats import zscore
graph['z_FI'] = zscore(graph['Overall Food Insecurity Rate'])
graph['z_SNAP'] = zscore(graph['% FI > SNAP Threshold'])
graph['Outlier Score (combined Z-score)'] = (graph['z_FI'] + graph['z_SNAP']) / 2
graph = graph[['County', 'Outlier Score (combined Z-score)']]
st.table(graph.sort_values(by='Outlier Score (combined Z-score)', ascending=False).head(5))
st.caption('''
Fig 3. This table calculates separate z-scores for Overall Food Insecurity and the percentage of people that are above the SNAP threshold. These z-scores were then combined into a single variable to then be compared across counties. This is another indicator a counties general need for help with respect to food insecurity.
''')

st.markdown('''---''')

st.markdown('''
## Merged Data (FARA + MMG)

**1. Do the number of food deserts relate to the food insecurity rates in a county?**    
When looking at the graph showing the relationship between food insecurity rates and the number of food deserts (can be found in Visuals tab to the left), 
there is no significant correlation found between these variables (pearson correlation = 0.0278, p > 0.05). 

**2. What is the SNAP 'coverage gap' that exists and in which counties is it the highest?**    
A SNAP coverage gap was determined by finding the number of people in a county that qualify for SNAP and subtracting the number of people that actually use SNAP benefits.
This number gives us a clear indication of how many people qualify as food insecure, but don't use government assistance as aid. A final list of counties along with their 
respective SNAP coverage gaps was calculated:
1. Harris: 249,374
2. Dallas: 152,172
3. Bexar: 111,606
4. Tarrant: 81,214
5. Hidalgo: 74,054
6. El Paso: 49,804
7. Travis: 48,244
8. Cameron: 38,580
9. Collin: 27,996
10. Denton: 22,276

**3. How can we determine which counties are in the more dire need of help to fight against food insecurity?**  
We calculated a final composite score that could be used to directly correlate a counties food insecurity level. This final composite score was calculated using these variables:
1. food insecurity rate
2. SNAP Gap
3. % FI ≤ SNAP Threshold
4. Number of food desert tracts
5. Cost per Meal
              
These variables were first normalized to a number between 0 and 1 for every county. Then, they were added together across each county to create 
the final composite score. Using this method, we created a list of 10 counties that we determined were in the most dire need for immediate help with regard to 
food insecurity:  
***1. Harris: 3.4565  
2. Dallas: 2.9020  
3. Presidio: 2.6639  
4. Hidalgo: 2.5217  
5. Bexar: 2.4040  
6. Cottle: 2.2411  
7. El Paso: 2.2356  
8. Starr: 2.2060  
9. Tarrant: 2.1390  
10. Hall: 2.1277***
''')


st.markdown("""
----
This analysis page connects the statistical insights from your notebooks with the visualizations in the dashboard. For further discussion of patterns and implications, see the Key Takeaways or Personal Reflection tabs.
""")
