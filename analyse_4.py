import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('flight_data_2024-03-24_22-58-47.csv')

# Preprocessing: Encode categorical variables
label_encoder = LabelEncoder()
data['Arrival Airport'] = label_encoder.fit_transform(data['Arrival Airport'])
data['Airline'] = label_encoder.fit_transform(data['Airline'])
data['Class Info'] = label_encoder.fit_transform(data['Class Info'])

# Drop other irrelevant columns
data.drop(['Departure Time', 'Arrival Time', 'Departure Airport', 'Flight Type', 'Flight URL'], axis=1, inplace=True)

# Drop rows with missing values
data.dropna(inplace=True)

# Feature selection
selected_features = ['Arrival Airport', 'Airline', 'Class Info']

# Clustering
X = data[selected_features]

# Apply DBSCAN clustering
dbscan = DBSCAN(eps=0.5, min_samples=5)
clusters = dbscan.fit_predict(X)

# Visualize clusters
plt.scatter(X['Arrival Airport'], X['Airline'], c=clusters, cmap='viridis', alpha=0.5)
plt.title('DBSCAN Clustering')
plt.xlabel('Arrival Airport')
plt.ylabel('Airline')
plt.colorbar(label='Cluster')
plt.show()
