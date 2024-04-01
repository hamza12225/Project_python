import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv('flight_data_2024-03-24_22-58-47.csv')

data['Duration_minutes'] = data['Duration'].str.extract('(\d+)').astype(int)

data.drop(['Departure Time', 'Arrival Time', 'Departure Airport', 'Arrival Airport',
           'Flight Type', 'Airline', 'Class Info', 'Flight URL'], axis=1, inplace=True)

data.dropna(inplace=True)

selected_features = ['Duration_minutes', 'Price €']

X = data[selected_features]

# Apply K-means clustering
kmeans = KMeans(n_clusters=5, random_state=42)
clusters = kmeans.fit_predict(X)

# Visualize clusters
plt.scatter(X['Duration_minutes'], X['Price €'], c=clusters, cmap='viridis', alpha=0.5)
plt.title('K-means Clustering')
plt.xlabel('Duration (minutes)')
plt.ylabel('Price €')
plt.colorbar(label='Cluster')
plt.show()
