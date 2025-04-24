import React, { useState } from 'react';

const WeatherApp = () => {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState(null);

  const fetchWeather = async () => {
    try {
      const res = await fetch(`${import.meta.env.VITE_BACKEND_URL}/weather?city=${city}`);
      if (!res.ok) throw new Error("Failed to fetch weather");
      const data = await res.json();
      setWeather(data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div style={{ maxWidth: '400px', margin: '2rem auto', padding: '1rem' }}>
      <h1 style={{ fontSize: '24px', fontWeight: 'bold', textAlign: 'center' }}>Weather Report</h1>
      <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '1rem' }}>
        <input
          type="text"
          placeholder="Enter city name"
          value={city}
          onChange={e => setCity(e.target.value)}
          style={{ flex: 1, padding: '0.5rem' }}
        />
        <button onClick={fetchWeather} style={{ padding: '0.5rem 1rem' }}>Get Weather</button>
      </div>
      {weather && !weather.error && (
        <div style={{ border: '1px solid #ccc', padding: '1rem', borderRadius: '8px' }}>
          <h2 style={{ fontSize: '20px', fontWeight: '600' }}>{weather.city}</h2>
          <p>Temperature: {weather.temperature}</p>
          <p>Condition: {weather.condition}</p>
        </div>
      )}
      {weather && weather.error && (
        <p style={{ color: 'red' }}>{weather.error}</p>
      )}
    </div>
  );
};

export default WeatherApp;