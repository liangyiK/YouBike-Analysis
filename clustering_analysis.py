import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 讀取資料
def load_data(file_path):
    data = pd.read_csv(file_path, low_memory=False)
    return data

def preprocess_data(data):
    # 假設資料有 'mday' 欄位，將其轉換為日期時間格式
    data['mday'] = pd.to_datetime(data['mday'])
    data['Day'] = data['mday'].dt.day
    data['Month'] = data['mday'].dt.month
    data['Year'] = data['mday'].dt.year
    data['Hour'] = data['mday'].dt.hour
    return data

def perform_clustering(data):
    # 選擇特徵進行聚類
    X = data[['Day', 'Month', 'Year', 'Hour']]
    
    # 訓練 K-means 模型
    kmeans = KMeans(n_clusters=3, random_state=42)
    data['Cluster'] = kmeans.fit_predict(X)
    
    # 繪製聚類結果圖
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Hour'], data['sbi'], c=data['Cluster'], cmap='viridis')
    plt.xlabel('Hour')
    plt.ylabel('Usage Count')
    plt.title('Clustering of Usage Patterns')
    plt.colorbar()
    plt.savefig('/mnt/data/clustering_results.png')
    plt.show()

if __name__ == "__main__":
    file_path = "/mnt/data/youbike_taipei.csv"
    data = load_data(file_path)
    data = preprocess_data(data)
    perform_clustering(data)
