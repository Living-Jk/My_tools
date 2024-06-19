# -*- coding: utf-8 -*-
"""
    @Time    : 6/18/24 AM11:17
    @Author  : Yanjiakang
    @File    : filter_rt.py
"""
import json
import requests
import pandas as pd
from utils.tools import *

# 请求 url
url = 'https://cloudapi.bytedance.net/faas/services/ttcdmy/invoke/monitorHistory'

# 请求头
request_headers = {
    "Content-Type": "application/json",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

# 请求体
request_body = {
    "did": "2143762954",
    "task_id": "V320240617180607",
    "cur": "0",
    "skip": 0
}


def filter_non_sensitive_data(data=None):
    if data is None:
        raise ValueError("data is None")

    history = data['history']
    new_history = list()
    for item in history:
        # 过滤掉 label == normal 或 AppInfo的元素
        if item['label'] != 'normal':
            new_history.append(item)
    return new_history


def get_all_filter_data():
    global url, request_headers, request_body
    all_filter_data = []
    while 1:
        response = requests.post(url=url, headers=request_headers, data=json.dumps(request_body))
        result = None
        if response.status_code == 200:
            result = json.loads(response.text)
            if len(result['history']) == 0:
                # 如果没数据了，返回结果，退出循环
                return all_filter_data
        else:
            raise ValueError("status_code is not 200, please check post request!")

        # 过滤100条数据
        filter_resp = filter_non_sensitive_data(data=result)
        # 将过滤后的数据插入结果list
        all_filter_data.extend(filter_resp)
        request_body["skip"] += 100


def data2excel(data=None):
    if data is None:
        raise ValueError("data is None")

    fields = ["label", "desc"]
    # 提取需要的字段数据
    filtered_data = [{field: item[field] for field in fields} for item in data]
    # 转换为DataFrame
    df = pd.DataFrame(filtered_data)
    # 将 desc 去重
    df_unique = df.drop_duplicates(subset=["desc"], keep="first")
    # 排序
    df_sorted = df_unique.sort_values(by="label")
    # 写入 Excel
    df_sorted.to_excel("filtered_data.xlsx", index=False)


if __name__ == '__main__':
    all_filter_data = get_all_filter_data()
    data2excel(all_filter_data)
