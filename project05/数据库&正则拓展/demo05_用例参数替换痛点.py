class Test01:
    id = 10
    name = 'yanzu'
    data = '0011'
    title = 'OK'


params = '{"id": "#id#", "name": "#name#", "data": "#data#", "title": "#title#", "aa": 11, "bb": 22}'

# params = params.replace("#id#", str(Test01.id))
# params = params.replace("#name#", str(Test01.name))
# params = params.replace("#data#", str(Test01.data))
# params = params.replace("#title#", str(Test01.title))

# print(params)

import re

res = re.findall("#.+?#", params)
print(res)
