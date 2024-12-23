import streamlit as st  # Library for creating web apps
import pandas as pd # Library for data manipulation
import plotly.express as px  # Library for creating interactive plots

st.set_page_config(layout="wide")	# Wide layout

# Load the dataset
df_reviews = pd.read_csv('datasets/customer reviews.csv') 
df_top100_books = pd.read_csv('datasets/Top-100 Trending Books.csv')    

df_reviews

# Find the maximum price of the books
price_max = df_top100_books['book price'].max()

# Find the minimum price of the books
price_min = df_top100_books['book price'].min()

# Create a range slider for the price
max_price = st.sidebar.slider('Price Range', price_min, price_max, price_max)

# Filter the books based on the price range
df_books = df_top100_books[df_top100_books['book price'] <= max_price]

# Creating graphs
fig = px.bar(df_books['year of publication'].value_counts())
fig2 = px.histogram(df_books['book price'])

# Update the layout
col1, col2 = st.columns(2) # Create two columns

col1.plotly_chart(fig)
col2.plotly_chart(fig2)