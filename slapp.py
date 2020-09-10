import pandas as pd
import numpy as np
import streamlit as st

test_table = pd.read_csv('testdata.csv')

st.title("My Test App for Streamlit")
st.write("Using Pandas DataFrame to create a table overview")
st.write(test_table)


st.title("Using prebuilt map example from Streamlit")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

st.write("Using external data file and Pandas Scatter")
st.write(test_table.plot.scatter('Observation','Observation 2',c='Day')
