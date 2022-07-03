"""
# @Time : 2022/5/28 0028   19:08
# @File : handler_log
# @Project : python01
# @Content :
"""

import logging


def create_log(name='musen', level='DEBUG', filename='log.log', fh_level='DEBUG', sh_level='DEBUG'):
    # 第一步：创建日志收集器
    log = logging.getLogger(name)
    # 第二步：设置收集器收集日志的等级
    log.setLevel(level)
    # 第三步:设置日志输出渠道
    # 3.1、输出到文件
    fh = logging.FileHandler(filename, encoding='utf-8')
    fh.setLevel(fh_level)
    log.addHandler(fh)
    # 输出到控制台
    sh = logging.StreamHandler()
    sh.setLevel(sh_level)
    log.addHandler(sh)
    # 第四步：设置日志输出的格式
    log_format = logging.Formatter('%(asctime)s--%(filename)s--%(lineno)d--%(levelname)s:%(message)s')
    # 设置输出到控制台的日志格式
    sh.setFormatter(log_format)
    # 设置输出到文件的日志格式
    fh.setFormatter(log_format)
    # 第五步：返回一个日志收集器
    return log
