import requests
import pandas as pd


def fetch_comtrade_data(typeCode, freqCode, clCode):
    url = f"https://comtradeapi.un.org/data/v1/get/{typeCode}/{freqCode}/{clCode}"
    # https://comtradeapi.un.org/data/v1/get
    # https://comtrade.un.org/api/get
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data["dataset"])
        return df
    else:
        print("API请求失败:", response.status_code)
        return None


# 示例参数（查询2022年中国对美国的电机类产品出口）
# params = {
#     "reporterCode": "",
#     "period": "",
#     "partnerCode": "",
#     "partner2Code": "",
#     "cmdCode": "",
#     "flowCode": "",
#     "customsCode": "",
#     "motCode": "",
#     "aggregateBy": "",
#     "breakdownMode": "",
#     "includeDesc": True
# }

if __name__ == "__main__":
    fetch_comtrade_data("C", "A", "HS")
