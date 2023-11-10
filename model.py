import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# Load your CSV file with reviews
file_path = 'C:/Users/Haritha/Downloads/AmazonScraperFinal-main/csv/amazon_reviews_preprocessed.xlsx'  
df = pd.read_excel(file_path)

# Split the data into training and testing sets
train_data, test_data, train_labels, test_labels = train_test_split(
    df['Reviews'], df['Score'], test_size=0.2, random_state=42
)

# Tokenize the text
tokenizer = Tokenizer()
tokenizer.fit_on_texts(train_data)
total_words = len(tokenizer.word_index) + 1

# Convert text to sequences
train_sequences = tokenizer.texts_to_sequences(train_data)
test_sequences = tokenizer.texts_to_sequences(test_data)

# Pad sequences to have the same length
max_length = max(len(seq) for seq in train_sequences)
train_padded = pad_sequences(train_sequences, maxlen=max_length, padding='post')
test_padded = pad_sequences(test_sequences, maxlen=max_length, padding='post')

# Build the LSTM model
model = Sequential()
model.add(Embedding(input_dim=total_words, output_dim=100, input_length=max_length))
model.add(LSTM(units=100))
model.add(Dense(units=1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_padded, train_labels, epochs=5, validation_data=(test_padded, test_labels))

# Evaluate the model
loss, accuracy = model.evaluate(test_padded, test_labels)
print(f'Accuracy: {accuracy}')
