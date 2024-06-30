from dataloader import Dataloader
from currencyexchange import CurrencyExchange
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Analyzer:
    '''
    Analyzer class for all anaylizing part of the code

    Attributes:
    -----------
    currency_dict: dict
        dictionary to store currency exchange values

    Methods:
    ---------
    suburb_summary(self,dataframe,suburb)
        return summary of specific subrub or all sububrb
    valid sizes(self,sizes,unit)
        returns pandas series of valid sizes
    avg_land_size(self, dataframe, suburb)
        returns average land size
    prop_val_distribution(self,dataframe, suburb, target_currency = "AUD")
        returns a hostogram
    sales_trend(self, dataframe)
        returns a line graph



    '''
    def __init__(self, currency_dict):
        self.currency_dict = currency_dict

    #3.4 Method to get the suburb summary
    def suburb_summary(self,dataframe, suburb):
        if suburb == "all":
           #Summary of all suburbs
            summary = dataframe[['bedrooms','bathrooms','parking_spaces']].describe()

        else:
            #Summary for specified suburb
            data_suburb = dataframe[dataframe['suburb']==suburb]

            if data_suburb.empty:
                raise ValueError(f"The suburb {suburb} does not exist in the data")

            #statistics for specified suburb

            summary = data_suburb[['bedrooms','bathrooms','parking_spaces']].describe()

        print(summary)
        # print(data_suburb['bedrooms'])


    #Extra method to convert land size into sq meter

    def valid_sizes(self, sizes, unit):
        val_sizes = []
        for s, u in zip(sizes,unit):
            if u == 'm²' and s > 0:
                val_sizes.append(s)

            elif u == 'ha' and s > 0:
                val_sizes.append(s*10000)
        return pd.Series(val_sizes)


    #3.5 Method to calculate the average land size

    def avg_land_size(self, dataframe, suburb):
        if 'land_size' not in dataframe.columns:
            raise ValueError("Land size column is missing from CSV")
        if 'land_size_unit' not in dataframe.columns:
            raise ValueError("Land size unit column missing from CSV")

        #Avg size for 'all' suburb

        if suburb == 'all':
            sizes = self.valid_sizes(dataframe['land_size'],dataframe['land_size_unit'])
            return sizes.mean()

        #AVG size for specific suburb

        data = dataframe[dataframe['suburb'] == suburb]

        #For invalid suburb or suburb not found

        if data.empty:
            return "Invalid Suburb"

        sizes = self.valid_sizes(data['land_size'], data['land_size_unit'])
        if not sizes.empty:
            return sizes.mean()
        else:
            return 'Something is not right'



    # 3.6 Method to plot propert value distribution based on currency

    def prop_val_distribution(self,dataframe, suburb, target_currency = "AUD"):
        #price column present in dataframe
        if 'price' not in dataframe.columns:
            raise ValueError("Price Column is missing from CSV")

        if target_currency not in self.currency_dict:
            print(f"Currency {target_currency} not in system, showing results in AUD")
            target_currency = "AUD"

        #Property values in target currency
        currency_exchange = self.currency_dict[target_currency]
        # new_price = CurrencyExchange().currency_exchange(dataframe,currency_exchange)
        # print(new_price)

        #Suburb filter
        if suburb != "all":
            data = dataframe[dataframe['suburb'] == suburb]
            new_price = CurrencyExchange().currency_exchange(data, currency_exchange)

        else:
            data = dataframe
            new_price = CurrencyExchange().currency_exchange(data, currency_exchange)

        #records with no price
        data = data.dropna(subset=['price'])
        # unique_values, counts = np.unique(new_price, return_counts=True)


        #Histogram
        plt.hist(new_price, bins=75, rwidth=0.8)
        plt.title(f"Distribution Property Value in {suburb} according to currency ({target_currency})")
        plt.xlabel(f"Value of the Property in {target_currency}")
        plt.ylabel("Number of Properties")

        #Saving
        plt.savefig('property_value_distribution.png')
        plt.show()

    # 3.7 Sales Trend
    def sales_trend(self, dataframe):
        #check sold_date is present or not
        if 'sold_date' not in dataframe.columns:
            raise ValueError("Sold date is not present in the CSV file")

        #Converting column in datetime
        dataframe['sold_date'] = pd.to_datetime(dataframe['sold_date'], format='%d/%m/%Y')

        #Extracting the year
        dataframe['sold_year'] = dataframe['sold_date'].dt.year
        count = dataframe['sold_year'].value_counts()

        #Bubble sort for ascending order of years
        total_years = count.index.tolist()
        num = count.tolist()
        n = len(total_years)
        for i in range(n):
            for j in range(0,n-i-1):
                if total_years[j] > total_years[j+1]:
                    total_years[j], total_years[j+1] = total_years[j+1], total_years[j]
                    num[j], num[j+1] = num[j+1], num[j]

        #Create a line chart
        plt.plot(total_years,num,marker='o',linestyle='-')
        plt.xlabel('Year')
        plt.ylabel('Total number of properties Sold')
        plt.title('Trend sales over the year')

        #Saving the file
        plt.savefig('sales_trend.png')
        plt.show()






# dl = Dataloader()
# file_path = "property_information.csv"
# property_data = dl.extract_property_info(file_path)
# print(property_data)

# da = Analyzer()
# print(da.suburb_summary(dl.extract_property_info(file_path),'all'))
# print(da.avg_land_size(dl.extract_property_info(file_path),'Burwood'))
#
# currency_dict = {"AUD": 1, "USD": 0.66, "INR": 54.25, "CNY": 4.72, "JPY": 93.87, "HKD": 5.12, "KRW": 860.92, "GBP": 0.51, "EUR": 0.60, "SGD": 0.88}
# an = Analyzer(currency_dict)
# an.prop_val_distribution(dl.extract_property_info(file_path),'all',"INR")




# an.sales_trend(dl.extract_property_info(file_path))
# print(an.avg_land_size(dl.extract_property_info(file_path),'Burwood'))