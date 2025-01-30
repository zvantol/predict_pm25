# predict_pm25
### PM2.5 Prediction Using SVR Model
Author: Jianghai Peng  
Last Updated: 1/30/2025

### Description: 
  This script loads a pre-trained Support Vector Regression (SVR) model 
  and a corresponding scaler to predict PM2.5 levels based on input meteorological 
  and environmental data. The script standardizes new input data before 
  making predictions.

### Dependencies:
  - joblib
  - numpy
  - scikit-learn (for loading the scaler)

### Usage:
  Ensure that 'scaler.pkl' and 'svr_model.pkl' are stored in the specified 
  file paths. Modify `new_data` with appropriate input values before execution.

### File Paths:
  - Scaler: G:\svr_pm25_model\scaler.pkl
  - Model: G:\svr_pm25_model\svr_model.pkl

### Inputs:
  - temperature_2m (Kelvin)
  - u_component_of_wind_10m (m/s)
  - surface_pressure (Pa)
  - v_component_of_wind_10m (m/s)
  - hour (0-23)
  - Nighttime Light (NTL) index
  - Normalized Difference Vegetation Index (NDVI)
  - Day of Year (doy)

### Data Suggestions:
  - [Temperature](https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_LAND_HOURLY)
  - [NDVI](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED)
  - [NTL](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMCFG)

### Outputs:
  - Predicted PM2.5 concentration in µg/m³

# Error Handling:
  - Handles missing model/scaler files
  - Handles data transformation errors
  - Handles prediction errors
