from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return 'Weather API is running. Use /weather?city=CityName'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        weather_data = {
            'city': data['name'],
            'temperature': f"{data['main']['temp']}°C",
            'condition': data['weather'][0]['main'],
            'icon': data['weather'][0]['icon'],
        }
        return jsonify(weather_data)

    except requests.exceptions.HTTPError as err:
        return jsonify({'error': f"API error: {err}"}), 500
    except Exception as e:
        return jsonify({'error': f"Something went wrong: {str(e)}"}), 500

@app.route('/forecast', methods=['GET'])
def get_forecast():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Simplify forecast to one entry every 24 hours (every 8th entry since each is 3 hours apart)
        forecast_list = []
        for i in range(0, len(data['list']), 8):
            item = data['list'][i]
            forecast_list.append({
                'date': item['dt_txt'].split()[0],
                'temperature': f"{item['main']['temp']}°C",
                'condition': item['weather'][0]['main'],
                'icon': item['weather'][0]['icon'],
            })

        return jsonify({
            'city': data['city']['name'],
            'forecast': forecast_list
        })

    except requests.exceptions.HTTPError as err:
        return jsonify({'error': f"API error: {err}"}), 500
    except Exception as e:
        return jsonify({'error': f"Something went wrong: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
