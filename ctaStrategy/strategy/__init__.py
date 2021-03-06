# encoding: UTF-8

"""
动态载入所有的策略类
"""

import os
import importlib


# 用来保存策略类的字典
STRATEGY_CLASS = {}

# 获取目录路径
path = os.path.abspath(os.path.dirname(__file__))

# 遍历strategy目录下的文件
for file in os.listdir(path):
    # 只有文件名中包含strategy且非.pyc的文件，才是策略文件
    if 'strategy' in file and '.py' in file:
        # 模块名称需要上前缀
        moduleName = 'ctaStrategy.strategy.' + file.replace('.py', '')

        # 使用importlib动态载入模块
        module = importlib.import_module(moduleName)

        # 遍历模块下的对象，只有名称中包含'Strategy'的才是策略类
        for k in dir(module):
            if 'strategy' in k:
                v = module.__getattribute__(k)
                STRATEGY_CLASS[k] = v
