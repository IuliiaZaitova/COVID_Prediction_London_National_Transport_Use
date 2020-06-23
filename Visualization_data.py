# import packages
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

class Visualization_data:
    '''
    contains data required for web-app visualization
    '''

    def __init__(self):
    # importing data from the csv-files
        self.path_london_mobility = 'data/Visualization/London_mobility.csv'
        self.path_uk_mobility = 'data/Visualization/UK_mobility.csv'
        self.path_cases_transport = 'data/Visualization/Cases_Transport.csv'

        self.df_london_mobility = pd.read_csv(self.path_london_mobility, parse_dates=['Date'], dayfirst=False)
        self.df_london_mobility.drop(self.df_london_mobility.columns[0], axis=1, inplace=True)
        self.df_uk_mobility = pd.read_csv(self.path_uk_mobility, parse_dates=['Date'])
        self.df_uk_mobility.drop(self.df_uk_mobility.columns[0], axis=1, inplace=True)
        self.df_cases_transport = pd.read_csv(self.path_cases_transport, parse_dates=['Date'], dayfirst=True)
        self.df_cases_transport.drop(self.df_cases_transport.columns[0], axis=1, inplace=True)

    def predict_transport_use(self, transport, n_cases, mob_percent):
        '''
        param transport: type of transport as a string, either 'TfL Tube' or 'National Rail'

        param n_cases: given number of COVID-19 cases worldwide. Either a number or a list of number

        param mob_percent: given number of corresponsing mobility percent change
        (Transit Stations Percent for TfL and Retail/Recreation for National Rail).
        Either a number or a list of number. The n of el-s in the list should be equal
        to that of n_cases

        returns: an np-array of predicted transport use change from the baseline in %
        '''
        # Create variables for training the Polymodel
        x_train_cases = self.df_cases_transport[['Date', 'new_cases_world']]

        if transport == 'TfL Tube':
            transport = 'Tfl Tube use change percentage'
            mob_variable = 'transit_stations_percent_change_from_baseline'

        elif transport == 'National Rail':
            transport = 'National rail use change percentage'
            mob_variable = 'retail_and_recreation_percent_change_from_baseline'

        y = self.df_cases_transport[transport].values
        x_train = self.df_london_mobility[['Date', mob_variable]]
        x_x_train = pd.merge(x_train_cases, x_train, how='left', on='Date').values
        X = np.delete(x_x_train, 0, 1)
        X_predict = np.column_stack((n_cases, mob_percent))

        # Fit the polynomial Regression
        poly_features = PolynomialFeatures(degree=2)
        X_poly = poly_features.fit_transform(X)
        X_poly_predict = poly_features.fit_transform(X_predict)
        poly_linear_model = LinearRegression(normalize=True, fit_intercept=False)
        poly_linear_model.fit(X_poly, y)
        # Predict the transport use
        transport_predicted = poly_linear_model.predict(X_poly_predict)
        return transport_predicted
