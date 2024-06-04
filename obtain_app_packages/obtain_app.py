# -*- coding: utf-8 -*-
"""
    @Time    : 2024/5/30 16:57
    @Author  : Yanjiakang
    @File    : obtain_app.py
"""

from utils.tools import *

# 包名
package_name = 'com.tencent.qqmusic'
# 要保存的路径(最好用绝对路径), 举例：/Users/bytedance/Documents/测试包/腾讯系/QQ音乐/
target_path = '/Users/bytedance/Documents/测试包/腾讯系/QQ音乐/'


@adb_connect
def obtain_app_package_from_phone():
    global package_name, target_path
    # 获取APP在移动设备中路径
    source_path = adb_shell_pm_path(package_name=package_name)
    package_path = source_path[8:].replace('\n', '')
    print_info(package_path)

    # 获取包版本，创建目录
    rst = get_package_version(package_name=package_name)
    package_version = rst[16:].replace('\n', '')
    # 目标安装路径
    target_path = target_path + package_version
    print_info(target_path)
    mkdir(target_path)

    # 下载安装包至目标路径
    adb_pull(package_path=package_path, target_path=target_path)


if __name__ == "__main__":
    obtain_app_package_from_phone()
