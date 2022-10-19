import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('John Dellape')

st.info('Data professional with a passion for solving meaningful information coordination problems.')

icon_size = 20

#st_button('youtube', 'https://youtube.com/dataprofessor', 'Data Professor YouTube channel', icon_size)
#st_button('youtube', 'https://youtube.com/codingprofessor', 'Coding Professor YouTube channel', icon_size)
#st_button('medium', 'https://data-professor.medium.com/', 'Read my Blogs', icon_size)
st_button('resume', 'https://drive.google.com/file/d/12q8t23CVe2gRy8giusX-Q83d2ta2wFYS/view', 'View my Resume', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/john-dellape/', 'Follow me on LinkedIn', icon_size)
st_button('twitter', 'https://twitter.com/JohnDellape', 'Follow me on Twitter', icon_size)
#input a button to view resume here
#st_button('newsletter', 'https://sendfox.com/dataprofessor/', 'Sign up for my Newsletter', icon_size)
#st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/', 'Buy me a Coffee', icon_size)
