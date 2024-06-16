import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap
from sklearn.cluster import DBSCAN
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.cluster import KMeans
import subprocess

# 見車率統計
def bike_availability_rate(data):
    data['mday'] = pd.to_datetime(data['mday'])
    daily_data = data.set_index('mday').between_time('06:00', '23:59')
    availability_rate = daily_data.groupby('sno')['sbi'].apply(lambda x: (x > 0).mean())
    return availability_rate

# 區域互補站點分析
def complementary_stations(data):
    db = DBSCAN(eps=0.01, min_samples=5).fit(data[['longitude1', 'latitude1', 'longitude2', 'latitude2']])
    data['cluster'] = db.labels_
    return data

# 每月熱門站點分析
def popular_stations(data):
    monthly_popular = data.groupby('時間')['站位名稱'].apply(lambda x: x.value_counts().head(10))
    return monthly_popular

# 潛在需求預測
def demand_forecast(data):
    data['datetime'] = pd.to_datetime(data['datetime'])
    data['day'] = data['datetime'].dt.day
    data['month'] = data['datetime'].dt.month
    data['year'] = data['datetime'].dt.year
    data['hour'] = data['datetime'].dt.hour
    X = data[['day', 'month', 'year', 'hour']]
    y = data['demand']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return model, mse, r2

# 每月使用量分析
def monthly_usage(data):
    monthly_data = data.groupby('民國年月')['臺北市YouBike每月使用量（次數）'].sum()
    return monthly_data

def run_analysis_scripts():
    scripts = [
        "data_preprocessing.py",
        "geo_analysis.py",
        "user_behavior_analysis.py",
        "time_series_analysis.py",
        "machine_learning_model.py",
        "clustering_analysis.py",
    ]
    
    for script in scripts:
        result = subprocess.run(["python", script], capture_output=True, text=True)
        print(f"Running {script}...")
        print(result.stdout)
        print(result.stderr)

if __name__ == "__main__":
    # 讀取資料
    availability_data = pd.read_csv('/mnt/data/e036ecfc2105d4be2942c003cfd2afb6_export.csv')
    complementary_data = pd.read_csv('/mnt/data/互補站點1.csv')
    popular_data = pd.read_csv('/mnt/data/YouBike站位每月熱門站點.csv')
    demand_data = pd.read_csv('/mnt/data/331f5e155d12f703213fad3d343d004a_export.csv')
    usage_data = pd.read_csv('/mnt/data/YouBike臺北市每月使用量.csv')

    # 見車率統計
    availability_rate = bike_availability_rate(availability_data)
    print(availability_rate)

    # 區域互補站點分析
    complementary_result = complementary_stations(complementary_data)
    print(complementary_result)

    # 每月熱門站點分析
    popular_result = popular_stations(popular_data)
    print(popular_result)

    # 潛在需求預測
    model, mse, r2 = demand_forecast(demand_data)
    print(f'Mean Squared Error: {mse}')
    print(f'R-squared: {r2}')

    # 每月使用量分析
    monthly_usage_result = monthly_usage(usage_data)
    print(monthly_usage_result)

    # 繪製圖表
    monthly_usage_result.plot(kind='bar')
    plt.title('Monthly Usage')
    plt.xlabel('Month')
    plt.ylabel('Usage Count')
    plt.savefig('/mnt/data/monthly_usage.png')
    plt.show()

    # 運行其他分析scripts
    run_analysis_scripts()
