import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download NLTK resources if not already installed
nltk.download('punkt')
nltk.download('stopwords')

# Load your CSV file
file_path = 'C:/Users/Dell/Downloads/AmazonScraperFinal-main/AmazonScraperFinal-main/AmazonScraperFinal-main/csv/amazon_reviews_Consolidated.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

# Handle missing values (NaN) in the 'Reviews' column
df['Reviews'].fillna("", inplace=True)

# Initialize the Porter Stemmer
stemmer = PorterStemmer()

# Define a function to perform tokenization, stemming, and remove stop words
def preprocess_text(text):
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    stemmed_words = [stemmer.stem(word) for word in words if word.lower() not in stop_words]
    return ' '.join(stemmed_words)

# Apply tokenization, stemming, and stop word removal
df['Reviews'] = df['Reviews'].apply(preprocess_text)

# Save the preprocessed data to an XLSX file
new_file_path = 'C:/Users/Dell/Downloads/AmazonScraperFinal-main/AmazonScraperFinal-main/AmazonScraperFinal-main/csv/amazon_preprocessed.xlsx'  # Replace with your desired file path
df.to_excel(new_file_path, index=False)

print("Preprocessing complete. Preprocessed data saved to", new_file_path)
