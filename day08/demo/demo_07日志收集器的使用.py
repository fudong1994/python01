"""
# @Time : 2022/5/28 0028   19:13
# @File : demo07_日志收集器的使用
# @Project : python01
# @Content :
"""

from day08.demo.handler_log import create_log

log = create_log()

log.info("python001")
log.debug('测试一下')
log.error("用例执行失败")