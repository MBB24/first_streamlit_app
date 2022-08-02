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
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
Fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
Fruits_to_show=my_fruit_list.loc[Fruits_selected]

# Display the table on the page.
streamlit.dataframe(Fruits_to_show)

#New section to display fruitvice api response}
streamlit.header("Fruityvice Fruit Advice!")
#Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")


# take the jason format of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output in the screen as a table
streamlit.dataframe(fruityvice_normalized)














