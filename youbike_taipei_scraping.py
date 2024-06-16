import requests
import json
import pandas as pd


# 台北公開平台
url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"

def append_data_to_csv(data, filename):
    """
    將資料附加到 CSV 檔案

    Args:
      data: 要附加的資料
      filename: CSV 檔案名稱

    Returns:
      None
    """

    # 嘗試讀取現有的 CSV 檔案
    try:
      df = pd.read_csv(filename)
    except FileNotFoundError:
      # 如果檔案不存在，則創建新的 CSV 檔案
      df = pd.DataFrame()

    # 將新資料附加到 DataFrame
    df = df.append(data, ignore_index=True)

    # 保存 DataFrame 到 CSV 檔案
    df.to_csv(filename, index=False, encoding="utf-8")

# 抓取資料並轉換為 DataFrame
response = requests.get(url)
ybike = json.loads(response.text)
df = pd.DataFrame(ybike)

fn = "youbike_taipei.csv"
# 將資料附加到 CSV 檔案
append_data_to_csv(df, fn)
