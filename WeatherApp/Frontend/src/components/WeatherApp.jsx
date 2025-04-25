import React, { useState } from 'react';
import { Line } from 'react-chartjs-2'; // Import Line chart
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';

// Register Chart.js components
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const WeatherApp = () => {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState(null);
  const [forecast, setForecast] = useState(null);
  const [error, setError] = useState(null);

  const fetchWeather = async () => {
    try {
      // Fetch current weather
      const resWeather = await fetch(`http://localhost:5000/weather?city=${city}`);
      if (!resWeather.ok) throw new Error("Failed to fetch current weather");
      const weatherData = await resWeather.json();
      setWeather(weatherData);

      // Fetch 5-day weather forecast
      const resForecast = await fetch(`http://localhost:5000/forecast?city=${city}`);
      if (!resForecast.ok) throw new Error("Failed to fetch weather forecast");
      const forecastData = await resForecast.json();
      setForecast(forecastData.forecast);
      setError(null); // Clear error if successful
    } catch (err) {
      console.error(err);
      setError("Could not fetch current weather or forecast.");
    }
  };

  // Prepare data for the chart (temperature over the next 5 days)
  const chartData = forecast ? {
    labels: forecast.map(day => day.date),
    datasets: [
      {
        label: 'Temperature (°C)',
        data: forecast.map(day => parseFloat(day.temperature)),
        borderColor: '#FF6347',
        backgroundColor: 'rgba(255, 99, 71, 0.2)',
        fill: true,
        tension: 0.4
      }
    ]
  } : {};

  return (
    <div style={{ maxWidth: '900px', margin: '2rem auto', padding: '2rem' }}>
      <h1 style={{ fontSize: '30px', fontWeight: 'bold', textAlign: 'center' }}>Weather Report</h1>

      <div style={{ display: 'flex', gap: '1rem', marginBottom: '2rem' }}>
        <input
          type="text"
          placeholder="Enter city name"
          value={city}
          onChange={e => setCity(e.target.value)}
          style={{ flex: 1, padding: '0.75rem', fontSize: '16px' }}
        />
        <button onClick={fetchWeather} style={{ padding: '0.75rem 1.5rem', fontSize: '16px' }}>Get Weather</button>
      </div>

      {error && (
        <div style={{ color: 'red', textAlign: 'center', marginBottom: '1rem' }}>
          <p>{error}</p>
        </div>
      )}

      {weather && (
        <div style={{ border: '1px solid #ccc', padding: '1.5rem', borderRadius: '8px', marginBottom: '2rem' }}>
          <h2 style={{ fontSize: '24px', fontWeight: '600' }}>{weather.city}</h2>
          <p>Temperature: {weather.temperature}</p>
          <p>Condition: {weather.condition}</p>
          <img src={`http://openweathermap.org/img/wn/${weather.icon}.png`} alt="weather-icon" />
        </div>
      )}

      {forecast && (
        <div style={{ border: '1px solid #ccc', padding: '1.5rem', borderRadius: '8px' }}>
          <h2 style={{ fontSize: '24px', fontWeight: '600' }}>5-Day Forecast</h2>
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '1rem' }}>
            {forecast.map((day, index) => (
              <div key={index} style={{ textAlign: 'center', flex: '1 1 18%' }}>
                <h3>{day.date}</h3>
                <p>{day.temperature}</p>
                <p>{day.condition}</p>
                <img src={`http://openweathermap.org/img/wn/${day.icon}.png`} alt="weather-icon" />
              </div>
            ))}
          </div>
        </div>
      )}

      {forecast && (
        <div style={{ marginTop: '2rem' }}>
          <Line data={chartData} options={{ responsive: true, maintainAspectRatio: false }} />
        </div>
      )}
    </div>
  );
};

export default WeatherApp;
