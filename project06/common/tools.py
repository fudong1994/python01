import re
from common.handle_conf import conf


# def replace_data(data, cls):
#     """
#
#     :param data:要进行替换的数据（字符串）
#     :param cls:测试类
#     :return:
#     """
#     while re.search('#(.+?)#', data):
#         res = re.search('#(.+?)#', data)
#         item = res.group()
#         attr = res.group(1)
#         value = getattr(cls, attr)
#         # 进行替换
#         data = data.replace(item, str(value))
#
#     return data

# ------------------------------升级版 替换时同时去类跟配置文件去找--------------------------
def replace_data(data, cls):
    """

    :param data:要进行替换的数据（字符串）
    :param cls:测试类
    :return:
    """
    while re.search('#(.+?)#', data):
        res = re.search('#(.+?)#', data)
        item = res.group()
        attr = res.group(1)
        try:
            value = getattr(cls, attr)
        except AttributeError:
            value = conf.get('test_data', attr)
        # 进行替换
        data = data.replace(item, str(value))

    return data
