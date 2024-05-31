# -*- coding: utf-8 -*-
"""
    @Time    : 2024/5/30 16:54
    @Author  : Yanjiakang
    @File    : tools.py
"""

import subprocess


def print_info(info):
    print(f"------<log>: {info}------")


# 装饰器，判断adb是否连接成功
def adb_connect(func):
    def adb_devices():
        result = subprocess.check_output(['adb', 'devices'])
        lines = result.splitlines()
        if len(lines) <= 2:  # 当无设备连接时，返回长度为2，<=2说明当前无设备连接
            print_info('adb connection error')
            return
        func()
    return adb_devices


def ls():
    return subprocess.check_output(['ls', '-al'])


def shell2params(shell, *args):
    params = shell.split(' ')
    params.extend(args)
    return params


# adb shell pm path <package_name> 获取指定包路径
def adb_shell_pm_path(package_name=None):
    if package_name is None or not package_name:
        print_info('package_name invalid')
        return
    shell = 'adb shell pm path'
    return subprocess.check_output(shell2params(shell, f'{package_name}')).decode('utf-8')


# adb pull  提起包到指定目录
def adb_pull(package_path=None, target_path='./'):
    if package_path is None or target_path is None:
        print_info('param invalid')
        return
    shell = 'adb pull'
    return subprocess.call(shell2params(shell, f'{package_path}', f'{target_path}'))


# 获取包版本信息
def get_package_version(package_name):
    if package_name is None or not package_name:
        print_info('package_name invalid')
        return
    shell = f'adb shell dumpsys package ' + f'{package_name}' + ' | grep versionName'
    return subprocess.check_output(shell2params(shell)).decode('utf-8')


def mkdir(path):
    if path is None or not path:
        print_info('path invalid')
        return
    shell = 'mkdir ' + f'{path}'
    try:
        return subprocess.check_output(shell2params(shell)).decode('utf-8')
    except:
        print_info(f'<error>=={path} File exists')


# def test(a='./aaa', b='./bbb'):
#     result = get_package_version(package_name='com.tencent.qqmusic')
#     print(result)
#     package_version = result[16:]
#     print('/Users/bytedance/Documents/测试包/腾讯系/QQ音乐/' + package_version)
#
# test()

