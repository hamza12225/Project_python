import pandas as pd
from sklearn.impute import SimpleImputer

data = pd.read_csv('flight_data_2024-03-24_22-58-47.csv')

def impute_by_group(df, group_col, target_col, strategy):
    imputer = SimpleImputer(strategy=strategy)
    filled_values = df.groupby(group_col)[target_col].transform(lambda x: imputer.fit_transform(x.values.reshape(-1, 1)).flatten())
    df[target_col] = filled_values
    return df

print(data.isnull().sum())

airports = ["PAR", "JFK","ROM","FRA","YYZ","IST","ABJ","ZRH","JED","LON","SYD"]
strategy = 'mean'

for airport in airports:
    data = impute_by_group(data, 'Arrival Airport', 'Price €', strategy)

print(data.isnull().sum())

