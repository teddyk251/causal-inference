from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
from sklearn.preprocessing import Normalizer, MinMaxScaler, StandardScaler
from sklearn.impute import SimpleImputer

import log

logger = log.setup_custom_logger(__name__, file_name='logs/datacleaner.log')

# To Preproccesing our data


class DataCleaner:

    def drop_duplicate(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        drop duplicate rows
        """
        df.drop_duplicates(inplace=True)

        return df

    def convert_to_datetime(self, df: pd.DataFrame, col: list) -> pd.DataFrame:
        """
        convert column to datetime
        """

        df[col] = df[col].apply(pd.to_datetime)

        return df

    def convert_to_string(self, df: pd.DataFrame, cols: list) -> pd.DataFrame:
        """
        convert columns to string
        """
        for col in cols:
            df[col] = df[col].astype(str)

        return df

    def remove_whitespace_column(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        remove whitespace from columns
        """
        df.columns = [column.replace(' ', '_').lower()
                      for column in df.columns]

        return df

    def percent_missing(self, df: pd.DataFrame) -> float:
        """
        calculate the percentage of missing values from dataframe
        """
        totalCells = np.product(df.shape)
        missingCount = df.isnull().sum()
        totalMising = missingCount.sum()

        return round(totalMising / totalCells * 100, 2)

    def get_numerical_columns(self, df: pd.DataFrame) -> list:
        """
        get numerical columns
        """
        return df.select_dtypes(include=['number']).columns.to_list()

    def get_categorical_columns(self, df: pd.DataFrame) -> list:
        """
        get categorical columns
        """
        return df.select_dtypes(exclude=['number']).columns.to_list()

    def percent_missing_column(self, df: pd.DataFrame, col: str) -> float:
        """
        calculate the percentage of missing values for the specified column
        """
        try:
            col_len = len(df[col])
        except KeyError:
            logger.error("%i not found", col)
        missing_count = df[col].isnull().sum()

        return round(missing_count / col_len * 100, 2)

    def fill_missing_values_categorical(self, df: pd.DataFrame, method: str) -> pd.DataFrame:
        """
        fill missing values with specified method
        """

        categorical_columns = self.get_categorical_columns(df)

        if method == "ffill":

            for col in categorical_columns:
                df[col] = df[col].fillna(method='ffill')

            return df

        elif method == "bfill":

            for col in categorical_columns:
                df[col] = df[col].fillna(method='bfill')

            return df

        elif method == "mode":

            imputer = SimpleImputer(strategy='most_frequent')
            filled_df = pd.DataFrame(
                imputer.fit_transform(df[categorical_columns]))
            filled_df.columns = categorical_columns
            # df[categorical_columns] = filled_df
            return filled_df
        else:
            logger.info("Method unknown")
            return df

    def fill_missing_values_numeric(self, df: pd.DataFrame, method: str) -> pd.DataFrame:
        """
        fill missing values with specified method
        """
        numeric_columns = self.get_numerical_columns(df)
        if method == "mean":
            for col in numeric_columns:
                df[col].fillna(df[col].mean(), inplace=True)

        elif method == "median":
            for col in numeric_columns:
                df[col].fillna(df[col].median(), inplace=True)
        else:
            logger.info("Method unknown")

        return df

    def remove_nan_categorical(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        remove columns with nan values for categorical columns
        """

        categorical_columns = self.get_categorical_columns(df)
        for col in categorical_columns:
            df = df[df[col] != 'nan']

        return df

    def normalizer(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        normalize numerical columns
        """
        norm = Normalizer()
        return pd.DataFrame(norm.fit_transform(df[self.get_numerical_columns(df)]), columns=self.get_numerical_columns(df))

    def min_max_scaler(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        scale numerical columns
        """
        minmax_scaler = MinMaxScaler()
        return pd.DataFrame(minmax_scaler.fit_transform(df[self.get_numerical_columns(df)]), columns=self.get_numerical_columns(df))

    def standard_scaler(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        scale numerical columns
        """
        standard_scaler = StandardScaler()
        return pd.DataFrame(standard_scaler.fit_transform(df[self.get_numerical_columns(df)]), columns=self.get_numerical_columns(df))

    def handle_outliers(self, df: pd.DataFrame, col: str, method: str = 'IQR') -> pd.DataFrame:
        """
        Handle Outliers of a specified column using Turkey's IQR method
        """
        df = df.copy()
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)

        lower_bound = q1 - ((1.5) * (q3 - q1))
        upper_bound = q3 + ((1.5) * (q3 - q1))
        if method == 'mode':
            df[col] = np.where(df[col] < lower_bound,
                               df[col].mode()[0], df[col])
            df[col] = np.where(df[col] > upper_bound,
                               df[col].mode()[0], df[col])

        elif method == 'median':
            df[col] = np.where(df[col] < lower_bound, df[col].median, df[col])
            df[col] = np.where(df[col] > upper_bound, df[col].median, df[col])
        else:
            df[col] = np.where(df[col] < lower_bound, lower_bound, df[col])
            df[col] = np.where(df[col] > upper_bound, upper_bound, df[col])

        return df

    def encode_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Encode features using LabelEncoder.
        """
        features = self.get_categorical_columns(df)
        for feature in features:
            le = LabelEncoder()
            le.fit(df[feature])
            df[feature] = le.transform(df[feature])
        return df
