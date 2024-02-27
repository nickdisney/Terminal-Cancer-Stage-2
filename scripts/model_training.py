import json
import os
import numpy as np

import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# Load and preprocess data
data_path = ('/Users/nick/Desktop/aimee/aimaze/dolphinkiller/Terminal-Cancer/data/training_data.csv')  # Update this path
data = pd.read_csv(data_path, encoding='ISO-8859-1')
# Assuming 'input_text' for text inputs and 'label' for binary labels
texts = data['input_text'].tolist()
labels = data['label'].tolist()  # Make sure labels are numeric

# Tokenization and sequence padding
tokenizer = Tokenizer(num_words=100000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
padded_sequences = pad_sequences(sequences, maxlen=100)

# Split the data
X_train, X_val, y_train, y_val = train_test_split(padded_sequences, labels, test_size=0.2, random_state=42)

# Model architecture
model = Sequential([
    Embedding(10000, 128, input_length=100),
    LSTM(64),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
y_train = np.array(y_train)
y_val = np.array(y_val)
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

# Save the tokenizer and model
if not os.path.exists('model'):
    os.makedirs('model')
tokenizer_json = tokenizer.to_json()
with open('model/tokenizer.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(tokenizer_json, ensure_ascii=False))
model.save('model/command_model.keras')

print("Model training complete.")
