from dataloader import Dataloader
import numpy as np
import pandas as pd

class CurrencyExchange:

    '''
    Class to change currency values

    Attributes:
    ----------
    None

    Methods:
    --------
   currency_exchange(self, dataframe, exchange_rate)
    returns numpy array of converted currency
    '''
    # def __init__(self, exchange_rate = 1):
    #     self.exchange_rate = exchange_rate

    #method to convert property prices to target currency

    def currency_exchange(self, dataframe, exchange_rate):
        if not isinstance(exchange_rate,(float,int)):
            raise ValueError("The exchange rate should be a numeric value")

        if 'price' not in dataframe.columns:
            raise ValueError("Price column is missing from CSV file")

        # Converting AUD in target currency and updating price column with new price
        prices_aud = dataframe['price'].values
        prices_targetcurr = prices_aud * exchange_rate

        return prices_targetcurr


# dl = Dataloader()
# file_path = "property_information.csv"
# property_data = dl.extract_property_info(file_path)
#
# cv = CurrencyExchange()
# print(cv.currency_exchange(dl.extract_property_info(file_path),50.1))