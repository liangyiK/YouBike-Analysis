import pandas as pd
import matplotlib.pyplot as plt

# 讀取資料
def load_data(file_path):
    data = pd.read_csv(file_path, low_memory=False)
    return data

def preprocess_data(data):
    # 假設資料有 'mday' 欄位，將其轉換為日期時間格式
    data['mday'] = pd.to_datetime(data['mday'])
    # 設置日期為索引
    data.set_index('mday', inplace=True)
    return data

def analyze_usage_trends(data):
    # 按天計算使用量
    daily_usage = data.resample('D').size()
    
    # 按小時計算使用量
    hourly_usage = data.resample('H').size()
    
    # 繪製日趨勢圖
    plt.figure(figsize=(12, 6))
    daily_usage.plot()
    plt.title('Daily Usage Trend')
    plt.xlabel('Date')
    plt.ylabel('Usage Count')
    plt.savefig('/mnt/data/daily_usage_trend.png')
    plt.show()
    
    # 繪製小時趨勢圖
    plt.figure(figsize=(12, 6))
    hourly_usage.plot()
    plt.title('Hourly Usage Trend')
    plt.xlabel('Hour')
    plt.ylabel('Usage Count')
    plt.savefig('/mnt/data/hourly_usage_trend.png')
    plt.show()
    
    return daily_usage, hourly_usage

if __name__ == "__main__":
    file_path = "/mnt/data/youbike_taipei.csv"
    data = load_data(file_path)
    data = preprocess_data(data)
    daily_usage, hourly_usage = analyze_usage_trends(data)
    print(daily_usage.head())
    print(hourly_usage.head())
