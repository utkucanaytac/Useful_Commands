import pandas as pd

class data_input_pipeline:
    def __init__(self, location:str):
        self.location = location

    def data_read(self):
        self.input_data = pd.read_csv(self.location)
        self.input_data = self.input_data.rename(columns={'TotalRevenue':'value'})
        #self.input_data = self.input_data.drop(['revenuedate'], axis=1)
        self.input_data['time'] = pd.date_range(start='1/1/2020', periods=len(self.input_data), freq='D')
        self.input_data= self.input_data.set_index('time')
        return self.input_data

    def data_info(self):
        return self.input_data.describe()

    def data_statistics(self):
        pass

    def data_correlation(self):
        pass

    def data_anomaly_detection(self):
        pass


a = data_input_pipeline("s3://misbucket-uca/Habbo/habbo.csv")

print(a.data_read())

print(a.data_info())