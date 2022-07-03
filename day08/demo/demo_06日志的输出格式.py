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

# 1、创建日志收集器
log = logging.getLogger('musen')

# 2、设置日志收集器收集日志的等级
log.setLevel("DEBUG")

# 3、设置输出渠道
# 3.1、输出到文件
fh = logging.FileHandler('yanzu.log', encoding='utf-8')
fh.setLevel('WARNING')
log.addHandler(fh)

# 3.2、输出到控制台
sh = logging.StreamHandler()
sh.setLevel('DEBUG')
log.addHandler(sh)

# 4、设置日志输出的格式
log_format = logging.Formatter('%(asctime)s--%(filename)s--%(lineno)d--%(levelname)s:%(message)s')
# 4.1、设置输出到控制台的日志格式
sh.setFormatter(log_format)
# 4.2、设置输出到文件的日志格式
fh.setFormatter(log_format)

log.debug("-----debug--------")
log.info("-----info--------")
log.warning("-----warning--------")
log.error("-----error--------")
log.critical("-----critical--------")
