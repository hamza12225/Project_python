import pandas as pd

flight_data = pd.read_csv('flight_data_2024-03-24_22-58-47.csv')

print(flight_data.head())

flight_data['Price'] = flight_data['Price €'].astype(str).str.replace('\xa0', '').str.replace(' ', '').str.replace('€', '').astype(float)

duration_values = flight_data['Duration'].str.extract(r'(\d+)h\s*(\d+)min')
flight_data['Duration'] = duration_values[0].astype(int) * 60 + duration_values[1].astype(int)

grouped_data = flight_data.groupby('Arrival Airport')

statistics_by_destination = grouped_data.agg({
    'Price': ['max', 'min','mean'],
    'Duration': ['max', 'min', 'median', 'std']
})

print("Statistics by Destination:")
print(statistics_by_destination)
