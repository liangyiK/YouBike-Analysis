import pandas as pd

# 每月使用量分析
def monthly_usage(data):
    monthly_data = data.groupby('民國年月')['臺北市YouBike每月使用量（次數）'].sum()
    return monthly_data

# 函數測試
file_path = '/mnt/data/YouBike臺北市每月使用量.csv'
usage_data = pd.read_csv(file_path)
monthly_usage_result = monthly_usage(usage_data)
print(monthly_usage_result)
