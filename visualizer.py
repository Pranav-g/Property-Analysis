from dataloader import Dataloader

class Visualizer:

    '''
    Class to Visualise parts of code

    Attributes:
    ----------
    None

    Methods:
    -------
    locate_price(self,target_price, data, target_suburb)
        returns true or false for a property

    bn_search(self, prop_prices, target_price)
        returns a binary serach output
    visualize_suburbs(self, dataframe)
        load the unique suburbs in dataframe


    '''
    # Method 3.8 Identifying a Property of a Specific Price in a Suburb
    def locate_price(self,target_price, data, target_suburb):
        if 'price' not in data.columns:
            raise ValueError("price column is missing")
        if 'suburb' not in data.columns:
            raise ValueError("suburb is misisng from csv")

        #Filter suburb
        data_suburb = data[data['suburb'] == target_suburb]

        if data_suburb.empty:
            return False #suburb not found

        #list of prices in specific suburb

        prop_prices = data_suburb['price'].tolist()

        #Descending order usind reverse insertion sort
        for i in range(1,len(prop_prices)):
            key = prop_prices[i]
            j = i-1
            while j >= 0 and key > prop_prices[j]:
                prop_prices[j+1] = prop_prices[j]
                j -= 1
                prop_prices[j+1] = key

        #Binary Search

        match = self.bn_search(prop_prices, target_price)

        return match


    # Extra method for binary search
    def bn_search(self, prop_prices, target_price):
        #Method for recursive binary search
        def rec_bn_search(prop_prices, l, h, target_price):
            if l<=h:
                m = (l+h)//2
                if prop_prices[m] == target_price:
                    return True
                elif prop_prices[m] > target_price:
                    return rec_bn_search(prop_prices, m+1, h, target_price)
                else:
                    return rec_bn_search(prop_prices, l, m-1, target_price)

            else:
                return False

        return rec_bn_search(prop_prices,0,len(prop_prices)-1, target_price)

    def visualize_suburbs(self, dataframe):
        if 'suburb' not in dataframe.columns:
            raise ValueError("Suburb is missing from CSV")

        uni_sub = dataframe['suburb'].unique()
        return{i+1: suburb for i, suburb in enumerate(uni_sub)}

# dl = Dataloader()
# file_path = "property_information.csv"
# property_data = dl.extract_property_info(file_path)
#
# viz = Visualizer()
# print(viz.locate_price(1564000,dl.extract_property_info(file_path), 'Burwood East'))
# print(viz.visualize_suburbs(dl.extract_property_info(file_path)))