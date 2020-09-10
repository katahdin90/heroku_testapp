import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st

test_table = pd.read_csv('testdata.csv')
test_table.plot.scatter('Observation','Observation 2',c='Day')

"""
# My Test App for Streamlit
Using Pandas DataFrame to create a table overview
"""
test_table

"""
### Demo Map Data
Using prebuilt map example from Streamlit
"""
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

"""
### Demo Graph - Pandas Scatter
Using external data file and Pandas Scatter
"""
test_table.plot.scatter('Observation','Observation 2',c='Day')


"""
### Demo Graph - Seaborn Scatter
Using external data file and Seaborn Scatter
"""
sns.scatterplot(data=test_table,x='Observation',y="Observation 2",size = 'Day')
