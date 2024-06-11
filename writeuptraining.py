from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import LSTM, Embedding, Dense

# Sample dataset: List of steps for different techniques
data = [
    "Step 1 of Technique A. Step 2 of Technique A. Step 3 of Technique A.",
    "Step 1 of Technique B. Step 2 of Technique B. Step 3 of Technique B."
]

# Preprocess data
tokenizer = Tokenizer()
tokenizer.fit_on_texts(data)
sequences = tokenizer.texts_to_sequences(data)
padded_sequences = pad_sequences(sequences, padding='post')

# Define model
model = Sequential([
    Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=50, input_length=padded_sequences.shape[1]),
    LSTM(100),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()

# Train model (example)
# model.fit(padded_sequences, labels, epochs=10)  # Replace 'labels' with actual labels for supervised training
