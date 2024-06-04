# -*- coding: utf-8 -*-
"""
    @Time    : 2024/5/31 16:42
    @Author  : Yanjiakang
    @File    : repack.py
"""

from utils.tools import *
import os

apk_path = '/Users/bytedance/Documents/测试包/腾讯系/QQ音乐/13.5.5.8/base.apk'  # 包路径

lspatch_path = '/Users/bytedance/Documents/测试包/重打包依赖/lspatch_240110.jar'
xpose5_path = '/Users/bytedance/Documents/测试包/重打包依赖/xpose-with-ret.apk'
xpose5_for_kuaishou = '/Users/bytedance/Documents/测试包/重打包依赖/xpose-ks-2.apk'


def repackage():
    # 计算目标目录
    idx = apk_path.rfind('/')
    target_path = apk_path[:idx]
    # 变更当前路径到包目录，否则会下载到当前py目录下
    os.chdir(f'{target_path}')
    print_info(f'current dir: {os.getcwd()}')

    if apk_path.find('快手') != -1:
        # 竞品为快手，拼接快手重打包依赖
        shell = 'java -jar ' + f'{lspatch_path} ' + f'{apk_path} ' + '-l 2 -f -m ' + f'{xpose5_for_kuaishou}'
        subprocess.call(shell2params(shell))
    else:
        # 非快手
        shell = 'java -jar ' + f'{lspatch_path} ' + f'{apk_path} ' + '-l 2 -f -m ' + f'{xpose5_path}'
        subprocess.call(shell2params(shell))


if __name__ == '__main__':
    repackage()
