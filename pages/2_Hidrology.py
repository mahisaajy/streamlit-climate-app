import streamlit as st

st.markdown("# Hidrology 🎉")
st.sidebar.markdown("# Hidrology 🎉")

option = st.selectbox(
    'Climate Indicator?',
    ('Precipitation', 'Air Temperature', 'Soil Moisture'))

st.write('You selected:', option)