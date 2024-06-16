import pandas as pd

# 讀取資料
def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path, low_memory=False)
    
    # 顯示資料基本資訊
    print("Data Info:")
    print(data.info())
    
    # 描述性統計
    print("Descriptive Statistics:")
    print(data.describe())
    
    # 檢查缺失值
    missing_values = data.isnull().sum()
    print("Missing Values:")
    print(missing_values)
    
    return data

if __name__ == "__main__":
    file_path = "/mnt/data/youbike_taipei.csv"
    data = load_and_preprocess_data(file_path)
