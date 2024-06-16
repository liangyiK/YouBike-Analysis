import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

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

# 函數測試
file_path = '/mnt/data/331f5e155d12f703213fad3d343d004a_export.csv'
demand_data = pd.read_csv(file_path)
model, mse, r2 = demand_forecast(demand_data)
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')
