import pandas as pd
import folium
from folium.plugins import HeatMap

# 讀取資料
def load_data(file_path):
    data = pd.read_csv(file_path, low_memory=False)
    return data

def analyze_station_usage(data):
    # 計算每個站點的使用頻率
    station_usage = data['sna'].value_counts().reset_index()
    station_usage.columns = ['sna', 'UsageCount']
    return station_usage

def generate_heatmap(data, station_usage):
    # 創建地圖中心點
    map_center = [data['lat'].mean(), data['lng'].mean()]
    base_map = folium.Map(location=map_center, zoom_start=12)
    
    # 添加站點使用頻率熱點
    heat_data = [[row['lat'], row['lng'], row['sbi']] for index, row in data.iterrows()]
    HeatMap(heat_data).add_to(base_map)
    
    # 保存地圖
    base_map.save('/mnt/data/station_usage_heatmap.html')
    print("Heatmap saved as station_usage_heatmap.html")

if __name__ == "__main__":
    file_path = "/mnt/data/youbike_taipei.csv"
    data = load_data(file_path)
    station_usage = analyze_station_usage(data)
    generate_heatmap(data, station_usage)
