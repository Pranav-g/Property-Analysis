'''
Test Codes
'''

#Test code for 'Dataloader'
# dl = Dataloader()
# file_path = "property_information.csv"
# property_data = dl.extract_property_info(file_path)
# print(property_data)

#Test code for 'CurrencyExchange'.
# dl = Dataloader()
# file_path = "property_information.csv"
# property_data = dl.extract_property_info(file_path)
#
# cv = CurrencyExchange()
# print(cv.currency_exchange(dl.extract_property_info(file_path),50.1))

#Test code for 'Analyzer'

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

#Test code for 'Visualizer'
# dl = Dataloader()
# file_path = "property_information.csv"
# property_data = dl.extract_property_info(file_path)
# print(viz.visualize_suburbs(dl.extract_property_info(file_path)))
# viz = Visualizer()
# print(viz.locate_price(1564000,dl.extract_property_info(file_path), 'Burwood East'))

from dataloader import Dataloader
from analyzer import Analyzer
from currencyexchange import CurrencyExchange
from visualizer import Visualizer
import os

#Function to handle suburb inputs
def sub():
    try:
        print('''
                                            Choose any one
                                            1) Select a suburb
                                            2) Show for all suburb
                                            ''')
        entri = int(input())
        if 1<=entri<=2:
            if entri == 1:
                #prints all the suburbs in the csv file
                print("Following suburbs are present in the system")
                suburbs_data = vs.visualize_suburbs(dl.extract_property_info(file_path))
                for i, suburb in suburbs_data.items():
                    print(f"{i}: {suburb}")
                sub = int(input("Seletc suburb from above: "))
                if 1 <= sub <= len(suburbs_data):
                    suburb_input = suburbs_data[sub]
                    print(f"You selected {suburb_input}")
                    return suburb_input

            if entri == 2:
                #returns data for all suburbs
                suburb_input = 'all'
                print(f"You selected all suburbs")
                return suburb_input
        else:
            print("invalid input")
    except ValueError:
        print("Invalid Input")

#Function to print main menu
def menu():

    print('''
            Welcome to Inverstor.co
            Select any one of the input to begin
            
            1) Summarize properties according to Suburbs
            2) Visualize Property value distribution according to suburb
            3) Get the sales trend around Melbourne
            4) identify a property
            5) Exit  
                
        
        
        ''')


if __name__=="__main__":
    while True:
        try:
            #Currency dictionary, kept outside so that coder can edit it anytime
            currency_dict = {"AUD": 1, "USD": 0.66, "INR": 54.25, "CNY": 4.72, "JPY": 93.87, "HKD": 5.12, "KRW": 860.92,
                             "GBP": 0.51, "EUR": 0.60, "SGD": 0.88}

            menu()
            dl = Dataloader()
            #Directory location
            file_path = "property_information.csv"
            user_input = int(input("\n Enter a Input from above"))
            #Analyzer class object
            an = Analyzer(currency_dict)
            #visualiser class object
            vs = Visualizer()

            if 0<user_input<=5:
                # print("yes")
                if user_input == 1:
                    #output is statistics for various or all suburbs

                    print(an.suburb_summary(dl.extract_property_info(file_path),sub()))
                    print("Check Average Land size also\n")
                    print(f"Average land size for this suburb is {an.avg_land_size(dl.extract_property_info(file_path),sub())}")

                if user_input == 2:
                    #output is a histogram with currency and suburb
                    print(currency_dict)
                    target_currency = input("Select a currency, for other currencies output matrix will be in AUD").upper()

                    print(f"You entered {target_currency}")
                    an.prop_val_distribution(dl.extract_property_info(file_path), sub(), target_currency)
                    print("Matrix saved in local directory")

                if user_input == 3:
                    #output is a line graph showing sales trend arounf Melbourne
                    an.sales_trend(dl.extract_property_info(file_path))
                    print("Sales Trend Matrix saved in local directory")
                    continue

                if user_input == 4:
                    #Checks if property present for a specific price in a suburb
                    price = int(input("Enter a price you are looking for"))
                    if vs.locate_price(price, dl.extract_property_info(file_path), sub()) == True:
                        print(f"Property found with price and suburb")

                    else:
                        print(f"Property could not be found with price and suburb")

                if user_input == 5:
                    #exits the code
                    print("Thank you for the visit")

                    break
            else:
                print("Invalid input, try again")
                continue

        except ValueError:
            print("Invalid Input")
        except FileNotFoundError:
            print("CSV not present in the directory")














