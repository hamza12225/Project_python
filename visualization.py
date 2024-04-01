import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('flight_data_2024-03-24_22-58-47.csv')

plt.figure(figsize=(10, 6))
sns.boxplot(x='Arrival Airport', y='Price €', data=data)
plt.title('Price Distribution by Arrival Airport')
plt.xlabel('Arrival Airport')
plt.ylabel('Price €')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='Arrival Airport', hue='Airline', data=data)
plt.title('Count of Flights by Arrival Airport and Airline')
plt.xlabel('Arrival Airport')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Airline', loc='upper right')
plt.show()
