import streamlit as st
import pandas as pd

st.write('Hello World1')


age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')



df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df



st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))