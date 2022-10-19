import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('John Dellape')

st.info('Data professional with a passion for solving meaningful information coordination problems.')

icon_size = 20

st_button('', 'https://jdellape-streamlit-portfolio-app-1ay2ev.streamlitapp.com/', 'View my Streamlit Projects', icon_size)
st_button('', 'https://github.com/jdellape', 'View my GitHub', icon_size)
st_button('', 'https://drive.google.com/file/d/1nELjAIJFVcW-PGYB-yCiscOAUi14_smI/view', 'View my Resume', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/john-dellape/', 'Find me on LinkedIn', icon_size)
st_button('twitter', 'https://twitter.com/JohnDellape', 'Find me on Twitter', icon_size)
