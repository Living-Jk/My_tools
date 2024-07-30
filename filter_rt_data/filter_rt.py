# -*- coding: utf-8 -*-
"""
    @Time    : 6/18/24 AM11:17
    @Author  : Yanjiakang
    @File    : filter_rt.py
"""
import json
import requests
import pandas as pd
from filter_stack_data import get_all_stack_data
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
    "did": "1716273679",
    "task_id": "V320240719152726",
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


def get_all_monitor_history():
    global url, request_headers, request_body
    all_monitor_history = []
    while 1:
        response = requests.post(url=url, headers=request_headers, data=json.dumps(request_body))
        result = None
        if response.status_code == 200:
            result = json.loads(response.text)
            if len(result['history']) == 0:
                # 如果没数据了，返回结果，退出循环
                return all_monitor_history
        else:
            raise ValueError("status_code is not 200, please check post request!")

        # 过滤100条数据
        filter_resp = filter_non_sensitive_data(data=result)
        # 将过滤后的数据插入结果list
        all_monitor_history.extend(filter_resp)
        request_body["skip"] += 100


def filtered_monitor_history_to_excel(data=None):
    if data is None:
        raise ValueError("data is None")

    fields = ["_id", "label", "desc", "foreground"]
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


def monitor_history_and_stack_to_excel(monitor_history_data: list = None, stack_data: list = None):
    if monitor_history_data is None or stack_data is None:
        raise ValueError("monitor_history_data or stack_data is None!")

    # 将 monitor_history 数据转换为DataFrame
    df_a = pd.DataFrame(monitor_history_data)
    print(df_a)

    # 将 stack_data 数据转换为DataFrame
    df_b = pd.DataFrame(stack_data)
    print(df_b)

    # 合并
    df_merge = pd.merge(df_a, df_b, on="_id", how="inner")
    print(df_merge)

    # 写入Excel
    with pd.ExcelWriter("/Users/bytedance/Documents/海外合规/CapCut三方SDK/outflow_ad.xlsx", engine="openpyxl") as writer:
        df_merge.to_excel(writer, sheet_name="数据详情", index=False)

    print("Data has been written to file~~~")


def filter_monitor_history_data(monitor_history_data: list=None):
    if monitor_history_data is None:
        raise ValueError("monitor_history_data is None!")

    fields = ["_id", "label", "desc", "foreground"]
    # 提取monitor_history需要的字段数据
    filtered_monitor_history_data = [{field: item[field] for field in fields} for item in monitor_history_data]

    # 将 monitor_history 数据转换为DataFrame 并做相应处理
    df = pd.DataFrame(filtered_monitor_history_data)
    df_unique = df.drop_duplicates(subset=["desc"], keep="first")
    df_sorted = df_unique.sort_values(by="label")

    # 转换回列表
    return df_sorted.to_dict(orient='records')


if __name__ == '__main__':
    # 获取所有 monitor_history 数据
    all_monitor_history = get_all_monitor_history()
    # 过滤
    filtered_monitor_history = filter_monitor_history_data(all_monitor_history)
    # print_info(filtered_monitor_history)

    # 获取堆栈信息并写入Excel
    stack_data = get_all_stack_data(filtered_monitor_history, request_body["task_id"])
    # print_info(stack_data)

    monitor_history_and_stack_to_excel(filtered_monitor_history, stack_data)
