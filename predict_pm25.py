import joblib
import numpy as np

# File paths for the saved scaler and model
scaler_path = r'G:\svr_pm25_model\scaler.pkl'
model_path = r'G:\svr_pm25_model\svr_model.pkl'

# Load the saved scaler and model
try:
    scaler = joblib.load(scaler_path)
    svr_model = joblib.load(model_path)
    print("Scaler and SVR model loaded successfully!")
except FileNotFoundError as e:
    print(f"Error loading files: {e}")
    exit()

# New data for prediction: [temperature_2m, u_component_of_wind_10m, surface_pressure,
# v_component_of_wind_10m, hour, NTL, NDVI, doy]
new_data = np.array([[308, 3.07, 96766, -1.02, 0, 32.72, 0.15, 267]])

# Standardize the new data using the saved scaler
try:
    new_data_scaled = scaler.transform(new_data)
except Exception as e:
    print(f"Error during data scaling: {e}")
    exit()

# Make predictions using the saved SVR model
try:
    prediction = svr_model.predict(new_data_scaled)[0]
    print(f"Predicted PM2.5: {prediction:.2f} µg/m³")
except Exception as e:
    print(f"Error during prediction: {e}")
    exit()
