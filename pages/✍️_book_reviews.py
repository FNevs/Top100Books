import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")	# Wide layout

df_reviews = pd.read_csv('dataset/customer reviews.csv') 
df_top100_books = pd.read_csv('dataset/Top-100 Trending Books.csv')

# List of unique book titles
books = df_top100_books['book title'].unique()

# Create a dropdown menu for selecting the book title
book = st.sidebar.selectbox('Select a book title', books)

# Filter the dataset based on the selected book title
df_book = df_top100_books[df_top100_books['book title'] == book]

# Filter the reviews dataset based on the selected book title
df_reviews_f = df_reviews[df_reviews['book name'] == book]

bookt_title = df_book['book title'].iloc[0]	# iloc get only the book title
book_genre = df_book['genre'].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}" # Add $ sign to the price
book_rating = df_book['rating'].iloc[0]
book_year = df_book['year of publication'].iloc[0]

# Display the book details
st.title(bookt_title)
st.subheader(book_genre)

col1, col2, col3 = st.columns(3)

# Columms for the book details
col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of Publication", book_year)

st.divider() # Add a divider in the page

for row in df_reviews_f.values:
    message = st.chat_message(f"{row[4]}") # Display the username
    message.write(f"**{row[2]}**") # Display the review
    message.write(row[5])  # Display the rating 