import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

# Load your CSV file with reviews
file_path = 'path_to_your_reviews.csv'  # Replace with your file path
df = pd.read_csv(file_path)

# Initialize the VADER SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Define a function to remove stop words from text
def remove_stop_words(text):
    words = text.split()
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

# Apply stop words removal and sentiment analysis
def analyze_sentiment(row):
    text = row['Reviews']
    text = remove_stop_words(text)
    sentiment = sia.polarity_scores(text)
    # Map sentiment polarity to rating
    rating = map_polarity_to_rating(sentiment['compound'])
    return rating

# Define the mapping function
def map_polarity_to_rating(polarity):
    rating = int((polarity + 1) / 0.4) + 1
    # Ensure the rating is within the valid range (1 to 5)
    return max(1, min(rating, 5))

# Apply sentiment analysis and mapping to each row
df['Rating'] = df.apply(analyze_sentiment, axis=1)

# Save the preprocessed data to a new CSV file
output_file = 'path_to_output_file.csv'  # Replace with your desired output file path
df.to_csv(output_file, index=False)

print("Sentiment analysis and rating assignment complete. Data saved to", output_file)
