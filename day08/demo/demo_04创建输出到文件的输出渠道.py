"""
# @Time : 2022/5/24 0024   19:03
# @File : demo_01logging模块的基本使用
# @Project : python01
# @Content :
"""

"""
logging.getLogger:创建日志收集器
    创建日志收集器的时候不传name参数，返回的是默认的收集器（root）
    传name参数则会创建一个新的日志收集器
    
"""
import logging

# 创建日志收集器
log = logging.getLogger('musen')

# 设置日志收集器收集日志的等级
log.setLevel("DEBUG")

# 设置输出日志等级
# 1、创建一个日志输出的渠道(输出到文件)
sh = logging.FileHandler('musen.log', encoding='utf-8')
sh.setLevel('DEBUG')
# 2、将输出渠道绑定到日志收集器上
log.addHandler(sh)

log.debug("-----debug--------")
log.info("-----info--------")
log.warning("-----warning--------")
log.error("-----error--------")
log.critical("-----critical--------")
