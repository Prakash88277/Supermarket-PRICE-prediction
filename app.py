from flask import Flask,request, url_for, redirect, render_template, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open('TotalSpending.pkl', 'rb') as f:
    model = pickle.load(f)
model=pickle.load(open('TotalSpending.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    hour = float(data['hour'])
    weather_encoded = 0 if data['weather'] == 'Clear' else 1
    age = int(data['age'])
    loyalty_member = 1 if data['loyalty_member'] == 'Yes' else 0
    
    prediction = model.predict([[hour, weather_encoded, age, loyalty_member]])
    
    return jsonify({'predictions': prediction.tolist()})

if __name__ == "__main__":
    app.run(debug=True)