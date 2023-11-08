import pandas as pd
from io import open

encodings = ['utf-8', 'ISO-8859-1', 'Windows-1252']
filepath = 'C:/Users/Haritha/Downloads/AmazonScraperFinal-main/csv/amazon_reviews_Consolidated.xlsx'

for encoding in encodings:
    try:
        with open(filepath, 'r', encoding=encoding, errors='replace') as file:
            df = pd.read_excel(filepath)
            print(df.head())
        print("CSV file successfully loaded with encoding:", encoding)
        break  # Exit the loop if successful
    except UnicodeDecodeError:
        print("Could not read the file with encoding:", encoding)
    