from jsonpath import jsonpath
import json
import requests

data = {'key1': {'key2': {'key3': {'key4': {'key5': {'key6': 'python'}}}}}}

# 字典读取
#print(data['key1']['key2']['key3']['key4']['key5']['key6'])

# jsonpath提取的数据以列表形式返回，读取的数据要是字典类型
print(type(jsonpath(data, '$..key6')))
print(jsonpath(data, '$..key6')[0])

## 拉勾网JSON文件:https://www.lagou.com/lbs/getAllCitySearchLabels.json

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'
}
url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'

response = requests.get(url, headers=headers)

json_dict = json.loads(response.content.decode())
print(type(json_dict))
print(jsonpath(json_dict, '$..name'))
