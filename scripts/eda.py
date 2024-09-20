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
