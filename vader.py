import pandas as pd
import spacy
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

# Load your CSV file with reviews
file_path = 'C:/Users/Haritha/Downloads/AmazonScraperFinal-main/csv/amazon_reviews_preprocessed.xlsx'
df = pd.read_excel(file_path)

# Initialize the VADER SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Initialize spaCy with the English language model
nlp = spacy.load('en_core_web_sm')

# Define a function to remove stop words from text
def remove_stop_words(text):
    # Check if the text is a non-NaN string
    if isinstance(text, str):
        words = text.split()
        stop_words = set(stopwords.words('english'))
        filtered_words = [word for word in words if word.lower() not in stop_words]
        return ' '.join(filtered_words)
    else:
        return ''  # Return an empty string for NaN values

# Define a function for lemmatization
def lemmatize_text(text):
    doc = nlp(text)
    lemmatized_words = [token.lemma_ for token in doc]
    return ' '.join(lemmatized_words)

# Define the mapping function
def map_polarity_to_rating(polarity):
    score = int((polarity + 1) / 0.4) + 1
    # Ensure the rating is within the valid range (1 to 5)
    return max(1, min(score, 5))

# Apply stop words removal, lemmatization, sentiment analysis, and mapping
def analyze_sentiment(row):
    text = row['Reviews']
    text_no_stopwords = remove_stop_words(text)
    lemmatized_text = lemmatize_text(text_no_stopwords)
    sentiment = sia.polarity_scores(lemmatized_text)
    # Map sentiment polarity to rating
    row['Score'] = map_polarity_to_rating(sentiment['compound'])
    # Add Polarity to the DataFrame
    row['Polarity'] = sentiment['compound']
    # Add Lemmatized Reviews next to the Reviews column
    row['Lemmatized_Reviews'] = lemmatized_text
    return row

# Apply sentiment analysis and mapping to each row
df = df.apply(analyze_sentiment, axis=1)

# Reorder the columns to have 'Lemmatized_Reviews' next to 'Reviews'
df = df[['Name', 'Reviews', 'Lemmatized_Reviews', 'Polarity', 'Score', ]]

# Save the updated data to the existing Excel file
df.to_excel(file_path, index=False)

print("Sentiment analysis, rating assignment, and lemmatization complete. Data saved to", file_path)
