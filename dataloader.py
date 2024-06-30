#function 3.2
import os
import pandas as pd
# import numpy as np

class Dataloader:
    '''
    Class to load data from CSV

    Attributes:
    -----------
    None

    Methods:
    --------
    extract_property_info(self, file_path)
        returns a dataframe from csv file
    '''
    # def __init__(self):
    #     self.file_path = property_information


    #Method to read the property info and return a data frame
    try:

        def extract_property_info(self, file_path):
            if not os.path.isfile(file_path):
                raise FileNotFoundError("File not present at specified location, kindly check")

            #File data into dataframe

            try:
                filedata = pd.read_csv(file_path)
                return filedata
            except:
                print("Error reading the file")
    except FileNotFoundError:
        print("CSV missing from local directory")



# dl = Dataloader()
# file_path = "property_information.csv"
# property_data = dl.extract_property_info(file_path)
# print(property_data)

