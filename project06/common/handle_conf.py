"""
# @Time : 2022/6/5 0005   22:48
# @File : handle_conf
# @Project : python01
# @Content :
"""
import os
from configparser import ConfigParser
from common.handle_path import CONF_DIR


class Config(ConfigParser):
    def __init__(self, conf_file):
        super().__init__()
        self.read(conf_file, encoding='utf-8')


conf = Config(os.path.join(CONF_DIR, 'config.ini'))
