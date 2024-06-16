import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
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

def train_regression_model(data):
    # 選擇特徵和目標變量
    X = data[['Day', 'Month', 'Year', 'Hour']]
    y = data['sbi']  # 使用量
    
    # 拆分資料為訓練集和測試集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 訓練線性回歸模型
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # 預測
    y_pred = model.predict(X_test)
    
    # 評估模型
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')
    print(f'R-squared: {r2}')
    
    # 繪製預測結果圖
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred)
    plt.xlabel('Actual Usage')
    plt.ylabel('Predicted Usage')
    plt.title('Actual vs Predicted Usage')
    plt.savefig('/mnt/data/regression_results.png')
    plt.show()

if __name__ == "__main__":
    file_path = "/mnt/data/youbike_taipei.csv"
    data = load_data(file_path)
    data = preprocess_data(data)
    train_regression_model(data)
