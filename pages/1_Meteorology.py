import streamlit as st
import pandas as pd
import numpy as np

st.markdown("# Meteorology ❄️")
st.sidebar.markdown("# Page 2 ❄️")

st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)


df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)