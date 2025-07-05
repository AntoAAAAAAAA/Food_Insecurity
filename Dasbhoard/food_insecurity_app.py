import streamlit as st
from data_loader import prepare_shapefile, maybe_download_visuals

#set up files 
maybe_download_visuals(st.sidebar.checkbox("Download visuals.ipynb?", value=False))
prepare_shapefile()

#load pages 
st.set_page_config(
    page_title="Texas Food Insecurity Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

home_page = st.Page(page='home_page.py', title='Home Page')
page_2 = st.Page(page='page_2.py', title='Interactive Map')
page_3 = st.Page(page='page_3.py', title='Visuals')
page_4 = st.Page(page='page_4.py', title='Key Takeaways')
page_5 = st.Page(page='page_5.py', title='Your County Data')
page_6 = st.Page(page='page_6.py', title='Personal Reflection')
page_7 = st.Page(page='page_7.py', title='In-Depth Analysis and Findings')

pg = st.navigation([home_page, page_2, page_7, page_3, page_4, page_5, page_6])
pg.run()