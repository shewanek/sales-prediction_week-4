from scripts.logger import Logger

class DataCleaner:
    def __init__(self, logger=None):
        # Initialize logger if passed, otherwise create a new one
        self.logger = logger if logger else Logger('rossmann_analysis.log')

    def fill_missing_values(self, train_data, test_data, store_data):
        self.logger.log('Merging store data with train and test datasets.')

        # Merging store data with train and test data
        train_data = train_data.merge(store_data, on='Store', how='left')
        test_data = test_data.merge(store_data, on='Store', how='left')

        # Handling missing values in CompetitionDistance
        self.logger.log('Filling missing values in CompetitionDistance.')
        train_data['CompetitionDistance'].fillna(train_data['CompetitionDistance'].median(), inplace=True)
        test_data['CompetitionDistance'].fillna(test_data['CompetitionDistance'].median(), inplace=True)

        # Filling missing competition and promo fields
        fields = ['CompetitionOpenSinceMonth', 'CompetitionOpenSinceYear', 'Promo2SinceWeek', 'Promo2SinceYear']
        for field in fields:
            self.logger.log(f'Filling missing values in {field}.')
            train_data[field].fillna(0, inplace=True)
            test_data[field].fillna(0, inplace=True)

        # Fill PromoInterval with 'None'
        self.logger.log('Filling missing values in PromoInterval.')
        train_data['PromoInterval'].fillna('None', inplace=True)
        test_data['PromoInterval'].fillna('None', inplace=True)

        self.logger.log('Data cleaning complete.')
        return train_data, test_data
