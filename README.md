# Amazon Web Scraper - Sentiment Analysis 

## Overview

This project combines web scraping with sentiment analysis to extract product reviews from Amazon's website and analyze the sentiment of the reviews using VADER (Valence Aware Dictionary and sEntiment Reasoner) from NLTK (Natural Language Toolkit).

## Features

- Search for products on Amazon using a specific product url.
- Specify the number of pages to scrape.
- Extract product names, ratings and reviews.
- Save the data to an Excel file for sentiment analysis.
- Applies sentiment analysis to the extracted reviews using VADER and NLTK.

## Prerequisites

- Python 3.6 or higher
- Required Python libraries (you can install them using `pip`):
  - `requests`
  - `BeautifulSoup`
  - `csv`
  - `pandas` (for data analysis)
  - `numpy` (for numerical operations)
  - `matplotlib` (for data visualization)
  - `sci-kit learn`
  - `joblib`
  - `spacy`

## Usage

1. Clone this repository to your local machine.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the Python script to scrape Amazon data.
4. Follow the prompts to enter the product url and number of pages to scrape.
5. The scraped data will be stored in an Excel file.
6. The reviews are pre-processed to remove stop words and lemmatization is performed.
7. Sentiment Analysis is performed on the lemmatized reviews, calculating the sentiment polarity and assigning a sentiment score.

## Output

The output Excel file will have the following columns:  Name, Rating, Reviews, Lemmatized Reviews, Sentiment Polarity and Sentiment Score.
