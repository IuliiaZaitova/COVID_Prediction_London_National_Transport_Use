# import packages
import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import pickle


class PredictionVisualization:
    """
    contains data required for web-app visualization
    """

    tfl_trained_model_name = "data/tfl_poly_model.pkl"
    rail_trained_model_name = "data/rail_poly_model.pkl"
    path_london_mobility = "data/London_mobility.csv"
    path_uk_mobility = "data/UK_mobility.csv"
    path_cases_transport = "data/Cases_Transport.csv"
    poly_features = PolynomialFeatures(degree=2)

    def __init__(self):
        # importing data from the csv-files

        self.df_london_mobility = pd.read_csv(
            self.path_london_mobility, parse_dates=["Date"], dayfirst=False
        )
        self.df_london_mobility.drop(
            self.df_london_mobility.columns[0], axis=1, inplace=True
        )
        self.df_uk_mobility = pd.read_csv(self.path_uk_mobility, parse_dates=["Date"])
        self.df_uk_mobility.drop(self.df_uk_mobility.columns[0], axis=1, inplace=True)
        self.df_cases_transport = pd.read_csv(
            self.path_cases_transport, parse_dates=["Date"], dayfirst=True
        )
        self.df_cases_transport.drop(
            self.df_cases_transport.columns[0], axis=1, inplace=True
        )

        self.tfl_trained_model = self.loadModel(self.tfl_trained_model_name)
        self.rail_trained_model = self.loadModel(self.rail_trained_model_name)

    def loadModel(self, modelFileName):
        print(os.path.join(os.path.dirname(__file__), modelFileName))
        with open(os.path.join(os.path.dirname(__file__), modelFileName), "rb") as f:
            return pickle.load(f)

    def predict_transport_use(self, transport, params):
        """
        param transport: type of transport as a string, either 'TfL Tube' or 'National Rail'

        param params: a 2D array containing the number of cases as the first list, and the number of change
        of use in the corresponding mobility variable as the second list. The two lists should be of the same length

        returns: an np-array of predicted transport use change from the baseline in %
        """
        # Load the finished model from a file
        if transport == "TfL Tube":
            transport = "Tfl Tube use change percentage"
            mob_variable = "transit_stations_percent_change_from_baseline"
            model = self.tfl_trained_model
        elif transport == "National Rail":
            model = self.rail_trained_model
        else:
            return None

        X_poly = self.poly_features.fit_transform(params)

        # Predict target values
        transport_predicted = model.predict(X_poly)
        return transport_predicted
viz = PredictionVisualization()
