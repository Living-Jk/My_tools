# -*- coding: utf-8 -*-
"""
    @Time    : 7/22/24 19:10
    @Author  : Yanjiakang
    @File    : filter_stack_data.py
"""
import json
import requests

# 请求 url
url = 'https://cloudapi.bytedance.net/faas/services/ttcdmy/invoke/monitorDetail'

# 请求头
request_headers = {
    "Content-Type": "application/json",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

# 请求体
request_body = {
    "id": "66951236a564f9002f82f36c",
    "task": "V320240715195527"
}


def get_stack_data(id: str = None, task_id: str = None):
    global url, request_headers, request_body

    if id is not None:
        request_body['id'] = id
    else:
        raise ValueError("request parameter id is None!")

    if task_id is not None:
        request_body['task'] = task_id
    else:
        raise ValueError("request parameter task_id is None!")

    # 调用方法获取堆栈数据
    response = requests.post(url=url, headers=request_headers, data=json.dumps(request_body))
    if response.status_code == 200:
        result = json.loads(response.text)
        stack_data = {"_id": result.get("_id", "0"), "stack": result.get("stack", "没有堆栈信息")}
        return stack_data  # 包含id + stack数据
    else:
        raise ValueError("status_code is not 200, please check post request!")


def get_all_stack_data(all_monitor_history: list = None, task_id: str = None):
    if all_monitor_history is None:
        raise ValueError("all_monitor_history is Node, please check parameter!")

    all_stack_data = []
    # 循环获取
    for monitor_data in all_monitor_history:
        stack_data = get_stack_data(monitor_data['_id'], task_id)
        all_stack_data.append(stack_data)
    return all_stack_data