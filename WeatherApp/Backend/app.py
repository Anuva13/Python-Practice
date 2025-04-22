from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'Unknown')
    weather_data = {
        'city': city,
        'temperature': f"{random.randint(15, 35)}°C",
        'condition': random.choice(['Sunny', 'Rainy', 'Cloudy', 'Windy'])
    }
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)