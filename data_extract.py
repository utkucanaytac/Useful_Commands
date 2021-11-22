import pandas as pd

def data_read(location:str):
    input_data = pd.read_csv(location)
    input_data = input_data.rename(columns={'totalrevenue':'value'})
    input_data = input_data.drop(['revenuedate'], axis=1)
    input_data['time'] = pd.date_range(start='1/1/2020', periods=len(input_data), freq='D')
    input_data= input_data.set_index('time')
    return input_data

def data_statistics():
    pass
def data_correlation():
    pass
def data_anomaly_detection():
    pass

# print(data_read("s3://misbucket-uca/habbo.csv"))


