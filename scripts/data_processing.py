import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from scripts.logger import Logger

class DataProcessor:
    def __init__(self, train_data, test_data, logger=None):
        # Initialize logger if passed, otherwise create a new one
        self.train_data = train_data
        self.test_data = test_data
        self.logger = logger if logger else Logger('rossmann_analysis.log')
        self.scaler = StandardScaler()

    def calculate_days_to_nearest_holiday(self, date, holiday_dates):
        """
        Calculate the minimum number of days to the next holiday (future).
        """
        days_to_holidays = [(holiday - date).days for holiday in holiday_dates if (holiday - date).days > 0]
        return min(days_to_holidays) if days_to_holidays else float('inf')

    def calculate_days_after_last_holiday(self, date, holiday_dates):
        """
        Calculate the number of days since the last holiday (past).
        """
        days_after_holidays = [(date - holiday).days for holiday in holiday_dates if (date - holiday).days > 0]
        return min(days_after_holidays) if days_after_holidays else float('inf')

    def encode_categorical_values(self, df):
        # Label Encoding for categorical variables
        label_encoders = {}
        categorical_columns = ['StoreType', 'Assortment', 'StateHoliday', 'PromoInterval']
        
        for col in categorical_columns:
            self.logger.log(f'Encoding {col}.')
            le = LabelEncoder()
            df[col] = df[col].astype(str)  # Ensure all data is in string format for encoding
            df[col] = le.fit_transform(df[col])
            label_encoders[col] = le
        
        self.logger.log('Encoding complete.')
        return df, label_encoders


    def feature_engineering(self, df):
        # Extract date features
        df['Date'] = pd.to_datetime(df['Date'])
        df['Year'] = df['Date'].dt.year
        df['Month'] = df['Date'].dt.month
        df['Day'] = df['Date'].dt.day
        df['WeekOfYear'] = df['Date'].dt.isocalendar().week
        df['Weekday'] = df['Date'].dt.weekday
        df['Weekend'] = df['Weekday'].apply(lambda x: 1 if x >= 5 else 0)

        # Create the DayType column
        df['DayType'] = 'Regular'
        df.loc[df['StateHoliday'] != '0', 'DayType'] = 'Holiday'
        df['DayType'] = pd.Categorical(df['DayType'], categories=['Before Holiday', 'Holiday', 'After Holiday', 'Regular'], ordered=True)

        # Calculate DaysToHoliday and DaysAfterHoliday
        holiday_dates = df[df['DayType'] == 'Holiday']['Date'].unique()
         # Apply the corrected logic
        df['DaysToHoliday'] = df['Date'].apply(lambda x: self.calculate_days_to_nearest_holiday(x, holiday_dates))
        df['DaysAfterHoliday'] = df['Date'].apply(lambda x: self.calculate_days_after_last_holiday(x, holiday_dates))


        df['DaysToHoliday'].replace(float('inf'), 999, inplace=True)
        df['DaysAfterHoliday'].replace(float('inf'), 999, inplace=True)

        # Encode categorical variables
        df, _ = self.encode_categorical_values(df)

        # Drop unnecessary columns
        columns_to_drop = ['Customers', 'PromoInterval', 'CompetitionOpenSinceMonth', 'CompetitionOpenSinceYear',
                           'Promo2SinceWeek', 'Promo2SinceYear', 'Date']
        df.drop(columns=columns_to_drop, inplace=True, errors='ignore')

        return df

    def preprocess(self):
        # Preprocess the training data
        self.logger.log('Starting feature engineering for training data.')
        self.train_data = self.feature_engineering(self.train_data)
        
        # Split features and target
        X = self.train_data.drop(columns=['Sales'])
        y = self.train_data['Sales']
        
        # Select only numerical columns for scaling
        numerical_columns = X.select_dtypes(include=['float64', 'int64']).columns
        X_numerical = X[numerical_columns]
        
        # Scale the numerical features
        self.logger.log('Scaling the numerical features.')
        X_scaled = self.scaler.fit_transform(X_numerical)
        
        # Return train/test split
        return train_test_split(X_scaled, y, test_size=0.2, random_state=42)


    def preprocess_test_data(self):
        self.logger.log('Starting feature engineering for test data.')
        self.test_data = self.feature_engineering(self.test_data)
        return self.scaler.transform(self.test_data)
