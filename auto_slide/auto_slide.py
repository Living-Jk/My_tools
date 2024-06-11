# -*- coding: utf-8 -*-
"""
    @Time    : 2024/6/5 17:27
    @Author  : Yanjiakang
    @File    : auto_slide.py
"""
from appium import webdriver

desired_capabilities = {
    'platformName': 'Android',
    'deviceName': 'Your Device Name',
    'appPackage': 'Your App Package Name',
    'appActivity': 'Your App Activity Name'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

# 获取屏幕的尺寸
size = driver.get_window_size()

# 定义 swipe 的起始点和结束点
start_x = size['width'] // 2
start_y = size['height'] * 3//4
end_x = size['width'] // 2
end_y = size['height'] // 4

# 对屏幕进行 swipe 动作
driver.swipe(start_x, start_y, end_x, end_y, duration=500)


