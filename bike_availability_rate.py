import pandas as pd

# 見車率統計
def bike_availability_rate(data):
    data['mday'] = pd.to_datetime(data['mday'])
    daily_data = data.set_index('mday').between_time('06:00', '23:59')
    availability_rate = daily_data.groupby('sno')['sbi'].apply(lambda x: (x > 0).mean())
    return availability_rate

# 函數測試
file_path = '/mnt/data/e036ecfc2105d4be2942c003cfd2afb6_export.csv'
availability_data = pd.read_csv(file_path)
availability_rate = bike_availability_rate(availability_data)
print(availability_rate)
