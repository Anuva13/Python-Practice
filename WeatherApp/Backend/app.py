from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City not provided'}), 400

    url = (
        f"https://api.openweathermap.org/data/2.5/weather?q={city}"
        f"&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200:
            return jsonify({'error': data.get('message', 'Failed to get data')}), 500

        weather = {
            'city': data['name'],
            'temperature': f"{data['main']['temp']}°C",
            'condition': data['weather'][0]['description'].capitalize()
        }
        return jsonify(weather)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/')
def home():
    return "Weather API is running."

if __name__ == '__main__':
    app.run(debug=True)