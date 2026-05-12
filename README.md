# Flight Delay Prediction

## Project Overview

This project aims to predict whether a US domestic flight will be delayed upon arrival. A flight is considered "delayed" if it arrives 15 minutes or more behind its scheduled time.

The primary goal is to build a model that can predict delays **before the aircraft departs**. This constraint is crucial for practical applications, such as proactively notifying passengers or optimizing airline operations. To achieve this, the model is trained only on features that are available before takeoff.

### Key Features
- **Data Cleaning & Feature Engineering:** Rigorous cleaning to handle missing data and remove features that would cause data leakage. New features were created to better represent time and day-of-the-week patterns.
- **Exploratory Data Analysis (EDA):** Visualizations to understand the factors influencing flight delays, such as time of day, month, and day of the week.
- **Predictive Modeling:** A baseline Logistic Regression model and a more advanced LightGBM model were built and evaluated.
- **Model Evaluation:** The models were assessed using metrics like ROC AUC, precision, and recall to determine their effectiveness in predicting delays.

## Visualizing Delays Across the US

The map below shows the total number of delayed flights originating from different airports across the United States. Larger circles indicate a higher number of delays, providing a clear view of which airports are most affected.

![Flight Delays by Origin Airport](/data/map.png)

## Workflow

The project follows these steps:
1.  **Data Cleaning and Preparation:** The dataset was cleaned by handling missing values and removing features unavailable before departure to prevent data leakage.
2.  **Feature Engineering:** New features were created, including `IS_WEEKEND` and cyclical time representations (`SIN`/`COS`), to improve model performance.
3.  **Exploratory Data Analysis (EDA):** Data was visualized to uncover patterns, such as the increase in delays during summer months and in the evening.
4.  **Predictive Modeling:** Two models were trained:
    *   **Logistic Regression:** A baseline model that achieved a ROC AUC of ~0.68.
    *   **LightGBM:** A gradient boosting model that significantly outperformed the baseline with a ROC AUC of ~0.73.
5.  **Conclusion:** The LightGBM model was identified as the more effective solution for predicting flight delays.

## Data
Data source: https://www.kaggle.com/datasets/usdot/flight-delays

## How to Run

1.  Clone the repository.
2.  Install the required libraries:
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn lightgbm plotly
    ```
3.  Open and run the `notebooks/flight_delay_prediction.ipynb` notebook to see the full analysis and model training process.
4.  To generate the map, run the Python script provided in the section below.

## Technologies Used
- Python
- Pandas & NumPy for data manipulation
- Matplotlib & Seaborn for data visualization
- Scikit-learn & LightGBM for modeling
- Jupyter Notebook for analysis