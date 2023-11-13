# Amazon Web Scraper - Sentiment Analysis 

## Overview

The Amazon Web Scraper is a Python project that scrapes product information from Amazon's website. It retrieves data such as product names, ratings and reviews for a given product url and number of pages. The scraped data is stored in a CSV file for performing sentiment analysis. 

## Features

- Search for products on Amazon using a specific product url.
- Specify the number of pages to scrape.
- Extract product names, ratings and reviews.
- Save the data to a CSV file for analysis.

## Prerequisites

- Python 3.6 or higher
- Required Python libraries (you can install them using `pip`):
  - `requests`
  - `BeautifulSoup`
  - `csv`
  - `pandas` (for data analysis)
  - `numpy` (for numerical operations)
  - `matplotlib` (for data visualization)

## Usage

1. Clone this repository to your local machine.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the Python script to scrape Amazon data.
4. Follow the prompts to enter the product url and number of pages to scrape.
5. The scraped data will be stored in a CSV file.

## Output

The output CSV file will have the following columns:  Name, Ratings and Reviews.

# Web Scraper with Sentiment Analysis

## Overview

This project combines web scraping with sentiment analysis to extract product reviews from an e-commerce website and analyze the sentiment of the reviews using VADER (Valence Aware Dictionary and sEntiment Reasoner) from NLTK (Natural Language Toolkit).

## Features

- **Web Scraping:** Utilizes web scraping techniques to extract product reviews from an Amazon's website.

- **Sentiment Analysis:** Applies sentiment analysis to the extracted reviews using VADER and NLTK.

- **Data Storage:** Saves the scraped data and sentiment analysis results to an Excel file for further analysis.`


## Data

- The scraped data and sentiment analysis results are saved in Excel files. 

## Credits

- The web scraper is built using BeautifulSoup and requests.

- Sentiment analysis is performed using VADER from NLTK.


