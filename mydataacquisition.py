import pandas as pd

class dataAcquisition():
    def __init__(self, file_csv):
        self.file_csv = file_csv
        self.df = pd.read_csv(file_csv)
        #print(self.df)
        
    # read rows 'name' from csv file
    def sensorData(self, name_data):
        self.name_data = name_data
        self.df = self.df[self.df['Name'].str.contains('{}'.format(self.name_data))]
        self.productList = self.df.values.tolist()
        return self.productList
    
    # read all data from csv file
    def allsensorData(self):
        self.allVal = self.df.values.tolist()
        return self.allVal
    
    