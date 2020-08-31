from jsonpath import jsonpath
import json

data = {'key1': {'key2': {'key3': {'key4': {'key5': {'key6': 'python'}}}}}}

# 字典读取
#print(data['key1']['key2']['key3']['key4']['key5']['key6'])

# jsonpath提取的数据以列表形式返回，读取的数据要是字典类型
print(type(jsonpath(data, '$..key6')))
print(jsonpath(data, '$..key6')[0])

