## 註：已拿不到最新使用者資料，此項目不更新

import pandas as pd
import matplotlib.pyplot as plt

# 讀取資料
def load_data(file_path):
    data = pd.read_csv(file_path, low_memory=False)
    return data

def user_behavior_analysis(data):
    # 分析每個使用者的使用次數
    user_usage = data['sno'].value_counts().reset_index()
    user_usage.columns = ['UserID', 'UsageCount']
    
    # 標記重複使用者與新使用者
    user_usage['UserType'] = user_usage['UsageCount'].apply(lambda x: 'Repeated' if x > 1 else 'New')
    
    # 計算重複使用者與新使用者的比例
    user_type_counts = user_usage['UserType'].value_counts()
    
    # 繪製使用者行為圖
    plt.figure(figsize=(10, 6))
    plt.bar(user_type_counts.index, user_type_counts.values, color=['blue', 'orange'])
    plt.xlabel('User Type')
    plt.ylabel('Count')
    plt.title('User Behavior Analysis')
    plt.savefig('/mnt/data/user_behavior_analysis.png')
    plt.show()
    
    return user_usage

if __name__ == "__main__":
    file_path = "/mnt/data/youbike_taipei.csv"
    data = load_data(file_path)
    user_usage = user_behavior_analysis(data)
    print(user_usage.head())
