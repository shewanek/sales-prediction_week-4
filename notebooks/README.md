
# Rossmann Pharmaceuticals Sales Forecasting

This repository contains an end-to-end analysis of sales data for Rossmann Pharmaceuticals, focusing on exploring key factors that affect store sales. The project utilizes various data cleaning and exploratory data analysis techniques to extract meaningful insights from the data.

## Project Overview

Rossmann Pharmaceuticals aims to forecast future sales across its stores. The project includes:
- **Data cleaning**: Handling missing values and merging datasets.
- **Exploratory Data Analysis (EDA)**: Investigating customer purchasing behavior, promotions, holidays, seasonality, and competition effects on sales.
- **Visualizations**: A set of plots that help in understanding the key trends in sales.
- **Logging**: Comprehensive logging to track the data processing workflow.

## Project Structure

```bash
├── scripts/
│   ├── data_cleaner.py     # Data cleaning functions
│   ├── eda.py              # EDA functions
│   ├── logger.py           # Logging utility
├── notebooks/
│   ├── eda.ipynb           # Exploratory Data Analysis notebook
│   ├── understanding_data.ipynb # Understanding Data notebook
    ├── rossmann_analysis.log    # Log file for tracking data processing
├── README.md               # Project description

```

## Files

1. **`logger.py`**: Handles logging of key events in the data cleaning and analysis process.
   - **Methods**:
     - `log(message)`: Logs informational messages.
     - `error(message)`: Logs errors encountered.
     - `debug(message)`: Logs detailed debugging information.

2. **`data_cleaner.py`**: Contains the `DataCleaner` class, which is used to handle missing values and perform data preprocessing.
   - **Methods**:
     - `fill_missing_values(train_data, test_data, store_data)`: Merges store data and fills missing values in competition and promotion fields.

3. **`eda.py`**: Contains the `EDA` class, which provides functions to create various visualizations and explore key trends in the data.
   - **Methods**:
     - `plot_promo_distribution`: Plots promotion distribution in the training and test datasets.
     - `plot_sales_during_holidays`: Analyzes sales behavior during holidays.
     - `plot_seasonal_behavior`: Displays seasonal trends in sales.
     - `plot_weekend_sales_comparison`: Compares weekend sales for stores open all weekdays versus those closed on some weekdays.

4. **Jupyter Notebooks**: `eda.ipynb` and `understanding_data.ipynb` contain the exploratory analysis, cleaning steps, and insights extracted from the data.

## Key Insights from Data

- **Promotions**: Promotional periods significantly increase sales, and stores offering regular promotions attract more customers.
- **Holidays**: Sales behavior during state holidays varies significantly compared to non-holiday periods, with some stores performing better during the holidays.
- **Seasonality**: There is a clear seasonal trend in sales, with peak sales during certain months of the year.
- **Competition**: The distance to competing stores impacts sales, especially when competitors are located close to Rossmann stores.


## Logging
The logger will automatically log the progress of the data processing and EDA steps. Logs can be viewed in the `rossmann_analysis.log` file.

---

