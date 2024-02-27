from flask import Flask, request, render_template
from flask import Flask, request, render_template
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import json
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load the AI model
model = load_model('/model/prompt_classification_model/prompt_classification_model.h5')

# Load the tokenizer
with open('/Users/nick/Desktop/aimee/aimaze/dolphinkiller/Terminal-Cancer/model/tokenizer.json') as f:
    data = json.load(f)
    tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(data)

def preprocess_input(user_input):
    # Tokenize the text
    sequences = tokenizer.texts_to_sequences([user_input])
    # Pad the sequences
    padded = pad_sequences(sequences, maxlen=100)  # Adjust maxlen according to your model's training
    return padded

def generate_response(prediction):
    # Assuming your model outputs a binary classification (for simplicity)
    response_class = ['Negative', 'Positive'][int(prediction > 0.5)]
    return f"Model predicts: {response_class}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute_command():
    user_input = request.form['command']
    processed_input = preprocess_input(user_input)
    prediction = model.predict(processed_input)
    response = generate_response(prediction[0])
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)

