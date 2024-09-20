# Rossmann Store Sales Analysis Project

This project is aimed at analyzing the Rossmann Pharmaceuticals store sales, with a focus on exploring factors that influence sales and identifying trends. The analysis involves cleaning and preparing data, performing exploratory data analysis (EDA), and visualizing key insights using different plots.

## Project Structure

### 1. `logger.py` - Logging Utility

The `Logger` class is responsible for logging messages throughout the data processing and analysis. It creates both file and console handlers to ensure logs are captured and easily accessible.

#### Key Features:
- **Initialization**: The logger is initialized with a log file name and configured to log both to a file and the console.
- **Methods**:
  - `log(message)`: Logs an informational message.
  - `error(message)`: Logs an error message.
  - `debug(message)`: Logs a debug message for detailed tracking.



---

### 2. `data_cleaner.py` - Data Cleaning Module

The `DataCleaner` class is responsible for cleaning and preprocessing the raw data before performing any analysis. This includes handling missing values and merging datasets.

#### Key Functions:
- **fill_missing_values(train_data, test_data, store_data)**: 
  - Merges store data with train and test datasets.
  - Fills missing values in `CompetitionDistance`, competition-related fields, and promotion fields.
  - Logs the progress of each step of the cleaning process.


---

### 3. `eda.py` - Exploratory Data Analysis (EDA) Module

The `EDA` class contains methods for generating various visualizations to explore the store sales data. These visualizations help to uncover trends and patterns in customer purchasing behavior and sales.

#### Key Functions:
- **plot_promo_distribution(merge_train_df, merge_test_df)**: 
  - Plots the distribution of promotions in the training and test datasets.
  
- **plot_sales_during_holidays(train_data)**:
  - Visualizes sales behavior during holidays using box plots.
  
- **plot_seasonal_behavior(train_data)**:
  - Plots seasonal sales trends based on the month.
  
- **plot_correlation_sales_customers(train_data)**:
  - Displays a heatmap showing the correlation between sales and the number of customers.
  
- **plot_promo_vs_sales(train_data)**:
  - Shows the effect of promotional offers on sales using a box plot.
  
- **plot_assortment_vs_sales(train_data)**:
  - Explores how different assortment types affect sales.
  
- **plot_competition_distance_vs_sales(train_data)**:
  - Visualizes the relationship between the distance to competitors and sales.
  
- **plot_competitor_opening_effect(train_data)**:
  - Analyzes the effect of competitor store openings on sales.
  
- **plot_weekend_sales_comparison(train_data)**:
  - Compares weekend sales between stores that remain open on all weekdays and those that close on some weekdays.



---

## How to Use

1. **Install Dependencies**: Ensure you have the necessary Python packages installed. Use `pip` to install dependencies if needed.


2. **Run Data Cleaning**: Use the `DataCleaner` class to clean your data before proceeding to analysis.
   

3. **Perform EDA**: Generate visualizations using the `EDA` class to gain insights from the data.
   

4. **Logging**: Logs are automatically generated and stored in the file specified during the logger initialization (e.g., `rossmann_analysis.log`).

---


## Summary

This project provides a robust structure for analyzing and visualizing store sales data from Rossmann Pharmaceuticals. The combination of logging, data cleaning, and visualization enables efficient exploration of the factors affecting store sales, such as promotions, competition, and seasonality.