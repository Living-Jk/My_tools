# -*- coding: utf-8 -*-
"""
    @Time    : 2024/6/5 17:27
    @Author  : Yanjiakang
    @File    : auto_slide.py
"""
from appium import webdriver
import time
from appium.options.android import UiAutomator2Options


def setup_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"  # 操作系统
    options.platform_version = "13"  # 系统版本
    options.device_name = "493ed7d"  # 设备ID
    options.app_package = "com.ss.android.ugc.aweme"  # 包名
    options.app_activity = ".splash.SplashActivity"  # 活动名
    options.automation_name = "UiAutomator2"  # 自动化引擎
    options.no_reset = True  # 不重置应用状态

    print("Options: ", options.to_capabilities())  # 打印 options 信息

    driver = webdriver.Remote("http://localhost:4723", options=options)
    return driver

    # desired_caps = {
    #     "platformName": "Android",
    #     "platformVersion": "13",
    #     "deviceName": "493ed7d",
    #     "appPackage": "com.ss.android.ugc.aweme",  # 目标应用的包名
    #     "appActivity": ".splash.SplashActivity",  # 目标应用的主活动
    #     "noReset": True,  # 不重置应用的状态
    #     "automationName": "UIAutomator2"
    # }


def swipe_up(driver):
    size = driver.get_window_size()
    start_x = size['width'] * 0.5
    start_y = size['height'] * 0.8
    end_y = size['height'] * 0.2
    driver.swipe(start_x, start_y, start_x, end_y, 1000)


def main():
    # 创建WebDriver实例
    driver = setup_driver()

    try:
        while True:
            swipe_up(driver)  # 上滑视频
            time.sleep(2)  # 等待视频播放一段时间

    except KeyboardInterrupt:
        print("自动化操作已停止")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()