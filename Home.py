import streamlit as st

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")


st.image('bmkg.png', caption='BMKG')


video_file = open('star.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)