import re

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
        value = getattr(cls, attr)
        # 进行替换
        data = data.replace(item, str(value))

    return data


if __name__ == '__main__':
    class TestData:
        id = 10
        name = 'yanzu'
        data = '0011'
        title = 'OK'


    s = '{"id": "#id#", "name": "#name#", "data": "#data#", "title": "#title#", "aa": 11, "bb": 22}'

    res = replace_data(s, TestData)
    print(res)
