import streamlit
streamlit.title('My Parents new Healthy dinner')
streamlit.header('BREAKFAST FAVORITES')
streamlit.text('🥣 Omega3 & Blueberry Otmeal')
streamlit.text('🥗 Kalet,Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

