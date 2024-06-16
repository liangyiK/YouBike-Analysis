import pandas as pd
from sklearn.cluster import DBSCAN

# 區域互補站點分析
def complementary_stations(data):
    db = DBSCAN(eps=0.01, min_samples=5).fit(data[['longitude1', 'latitude1', 'longitude2', 'latitude2']])
    data['cluster'] = db.labels_
    return data

# 函數測試
file_path = '/mnt/data/互補站點1.csv'
complementary_data = pd.read_csv(file_path)
complementary_result = complementary_stations(complementary_data)
print(complementary_result)
