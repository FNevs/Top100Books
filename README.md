# 📚 Top 100 Trending Books 

This project is a Streamlit-based web application for visualizing and exploring data about trending books, including their reviews, prices, and publication years. The app provides interactive tools for filtering and analyzing the dataset.

## Features

- 📈 **Price Range Filter:** Adjust the price range of books to filter the displayed results.
- 📊 **Interactive Visualizations:** View bar charts of book publication years and histograms of book prices.
- 📖 **Detailed Book Pages:** Select individual books to view their details (e.g., price, genre, rating, and reviews).
- 🗂️ **Multi-Page Layout:** Modular structure with separate pages for different functionalities.

## Requirements

To run this project, you need to have the following installed:

- Python 3.7 or higher
- Streamlit
- Pandas
- Plotly

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/FNevs/Top100Books.git
   cd Top100Books
   ```

2. Install the required dependencies:
   ```bash
   pip install streamlit
   pip install pandas
   pip install plotly
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run 📚_top100.py
   ```

## Usage

### Top 100 (`📚_top100.py`):
- Use the sidebar to adjust the price range of books.
- Explore visualizations of publication years and book prices.

### Book Details (`pages/✍️_book_details.py`):
- Select a book from the dropdown menu.
- View detailed information about the book, including reviews and ratings.

## Data Sources

The datasets used in this project are sourced from [Kaggle: Top 100 Bestselling Book Reviews on Amazon](https://www.kaggle.com/datasets/anshtanwar/top-200-trending-books-with-reviews).

## Technologies Used

- **Streamlit**: For building the web application.
- **Pandas**: For data manipulation and processing.
- **Plotly Express**: For creating interactive visualizations.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the project. 

## Future Improvements 🚧
- Integrate an API: Implement an API like the Google Books API or Open Library API to fetch real-time book data, reviews, and ratings. 
- Dynamic Dataset Updates: Replace the static dataset with a system that allows periodic updates, ensuring that the information remains current and relevant.
- Enhanced Visualizations: Add new types of visualizations, such as word clouds for reviews or scatter plots to analyze correlations between book ratings and prices.