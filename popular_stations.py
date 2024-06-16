import pandas as pd

# 每月熱門站點分析
def popular_stations(data):
    monthly_popular = data.groupby('時間')['站位名稱'].apply(lambda x: x.value_counts().head(10))
    return monthly_popular

# 函數測試
file_path = '/mnt/data/YouBike站位每月熱門站點.csv'
popular_data = pd.read_csv(file_path)
popular_result = popular_stations(popular_data)
print(popular_result)
