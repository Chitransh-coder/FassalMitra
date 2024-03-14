# Fasal Mitra App

This repository contains the source code of the Fasal Mitra App. The app helps farmers to get the latest information about the weather, atmosphere and rains using machine learning models.

## Datasets

The datasets used for training the model inside the app are:

1. **[ERA5 Daily Aggregates - Latest Climate Reanalysis Produced by ECMWF / Copernicus Climate Change Service](https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_DAILY)**
2. **[ERA5 Monthly Aggregates - Latest Climate Reanalysis Produced by ECMWF / Copernicus Climate Change Service](https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_MONTHLY)**
3. **[Cloud Score+ S2_HARMONIZED V1](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_CLOUD_SCORE_PLUS_V1_S2_HARMONIZED)**
4. **[Copernicus Atmosphere Monitoring Service (CAMS) Global Near-Real-Time](https://developers.google.com/earth-engine/datasets/catalog/ECMWF_CAMS_NRT)**

## Brief Overview

This app uses a machine learning model to predict the climate of specific region of India and helps the farmer in planting different crops bassed on the predictions. Moreover, this app also compares those predictions with the data provided by Meterological Department of India and tries to provide the best possible solution to the farmers.

## Features (To be implemented)

1. **Climate Forecasting**
2. **Crop Recommendation**
3. **Crop Identification**

## Technologies/Languages Used

1. **Multi-platform App Development (MAUI)/C#** - App Interface
2. **Flask/Python** - API creation and User Authentication
3. **Google Earth Engine** - Datasets
4. **Tensorflow/Python** - Machine Learning Model
5. **SQLite/SQL** - Database Management

## Status

5/2/24 - Idea originated
12/2/24 - Inital dataset collection and instantiating the project.
13/2/24 - Learning about Google Earth Engine and its datasets.
