# -*- coding: utf-8 -*-
"""
    @Time    : 7/22/24 21:12
    @Author  : Yanjiakang
    @File    : test.py
"""
import pandas as pd

lista = [
    {'id': 11},
    {'id': 22, 'age': 18},
    {'id': 33},
    {'id': 44}
]

df = pd.DataFrame(lista)

print(df)