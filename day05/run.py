"""
# @Time : 2022/5/23 0023   19:53
# @File : run
# @Project : python01
# @Content :
"""
import unittest

# 第一步：创建测试套件，加载测试用例到套件
# 1、创建套件
# sutie = unittest.TestSuite()
# 2、创建一个用例加载器
# load = unittest.TestLoader()
# 3、加载测试用例到套件
# sutie.addTest(load.discover(r'D:\pythonworkspace\python01\day05\testcases'))

# 上面三行代码的一行代替方式
sutie = unittest.defaultTestLoader.discover(r'D:\pythonworkspace\python01\day05\testcase')


# 第二步：创建一个测试用例运行程序
runner = unittest.TextTestRunner()

# 第三步：运行测试用例
runner.run(sutie)