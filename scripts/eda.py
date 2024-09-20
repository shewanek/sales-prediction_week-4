# scripts/eda.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import logging

class EDA:
    def __init__(self, logger=None):
        # If a logger is passed, use it, otherwise create a new logger
        self.logger = logger if logger else logging.getLogger('rossmann_analysis')
    # Plotting the distribution of promotions in training and test sets
    def plot_promo_distribution(self, merge_train_df, merge_test_df):
        """
        Plots the distribution of promotions in the training and test sets.
        
        Args:
            merge_train_df (pandas.DataFrame): Merged train data
            merge_test_df (pandas.DataFrame): Merged test data
        """
        self.logger.info("Plotting promotion distribution")

        # Plotting the distribution of promotions
        fig, ax = plt.subplots(1, 2, figsize=(12, 6))

        # Promo distribution in training set
        sns.histplot(merge_train_df['Promo'], kde=False, ax=ax[0], color='blue')
        ax[0].set_title('Promo Distribution - Training Set')
        ax[0].set_xlabel('Promo')
        ax[0].set_ylabel('Frequency')

        # Promo distribution in test set
        sns.histplot(merge_test_df['Promo'], kde=False, ax=ax[1], color='green')
        ax[1].set_title('Promo Distribution - Test Set')
        ax[1].set_xlabel('Promo')
        ax[1].set_ylabel('Frequency')

        plt.tight_layout()
        plt.show()
        self.logger.info("Promotion distribution plotted successfully")


    def plot_sales_during_holidays(self, train_data):
        self.logger.info("Plotting sales during holidays")
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='StateHoliday', y='Sales', data=train_data)
        plt.title('Sales Behavior During Holidays')
        plt.show()
        self.logger.info("sales during holidays plotted successfully")

    def plot_seasonal_behavior(self, train_data):
        self.logger.info("Plotting seasonal behavior")
        train_data['Month'] = pd.to_datetime(train_data['Date']).dt.month
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='Month', y='Sales', data=train_data.groupby('Month')['Sales'].mean().reset_index())
        plt.title('Seasonal Purchase Behavior')
        plt.show()
        self.logger.info("Seasonal behavior plotted successfully")

    def plot_correlation_sales_customers(self, train_data):
        self.logger.info("Plotting correlation sales customers")
        correlation = train_data[['Sales', 'Customers']].corr()
        sns.heatmap(correlation, annot=True, cmap='coolwarm')
        plt.title('Correlation Between Sales and Number of Customers')
        plt.show()
        self.logger.info("correlation sales customers plotted successfully")

    def plot_promo_vs_sales(self, train_data):
        self.logger.info("Plotting promo_vs_sales")
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='Promo', y='Sales', data=train_data)
        plt.title('Effect of Promo on Sales')
        plt.show()
        self.logger.info("promo_vs_sales plotted successfully")

    def plot_assortment_vs_sales(self, train_data):
        self.logger.info("Plotting assortment_vs_sales")
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='Assortment', y='Sales', data=train_data)
        plt.title('Effect of Assortment Type on Sales')
        plt.show()
        self.logger.info("assortment_vs_sales plotted successfully")

    def plot_competition_distance_vs_sales(self, train_data):
        self.logger.info("Plotting competition_distance_vs_sales")
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='CompetitionDistance', y='Sales', data=train_data)
        plt.title('Competition Distance vs Sales')
        plt.show()
        self.logger.info("competition_distance_vs_sales plotted successfully")

    def plot_competitor_opening_effect(self, train_data):
        self.logger.info("Plotting competitor opening effect")
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='CompetitionOpenSinceYear', y='Sales', data=train_data)
        plt.title('Effect of Competitor Store Openings on Sales')
        plt.show()
        self.logger.info("competitor opening effect plotted successfully")

    def plot_weekend_sales_comparison(self, train_data):
        self.logger.info("Plotting weekend_sales_comparison")
        # Create a flag for weekdays (1 = Monday to 5 = Friday)
        weekdays = [1, 2, 3, 4, 5]
        weekends = [6, 7]  # Saturday = 6, Sunday = 7

        # Find stores that are open all weekdays
        open_all_weekdays = train_data[train_data['DayOfWeek'].isin(weekdays)]
        open_all_weekdays = open_all_weekdays.groupby('Store')['Open'].sum() == 5

        # Separate stores into open on all weekdays vs closed on some weekdays
        train_data['OpenAllWeekdays'] = train_data['Store'].map(open_all_weekdays)
        
        # Filter weekend sales
        weekend_sales = train_data[train_data['DayOfWeek'].isin(weekends)]

        # Group by 'OpenAllWeekdays' and calculate average sales for weekend
        avg_weekend_sales = weekend_sales.groupby('OpenAllWeekdays')['Sales'].mean().reset_index()

        # Plot the comparison
        plt.figure(figsize=(8, 6))
        sns.barplot(x='OpenAllWeekdays', y='Sales', data=avg_weekend_sales, palette="coolwarm")
        
        # Set plot labels and title
        plt.xlabel('Store Open All Weekdays')
        plt.ylabel('Average Weekend Sales')
        plt.title('Comparison of Average Weekend Sales for Stores Open on Weekdays vs. Closed')
        plt.xticks([0, 1], ['Closed on Some Weekdays', 'Open All Weekdays'])
        
        plt.show()
        self.logger.info("weekend_sales_comparison plotted successfully")


