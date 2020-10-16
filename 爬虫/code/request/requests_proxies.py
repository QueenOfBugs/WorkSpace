import requests

# url = 'http://www.baidu.com'

proxies = {
    'http': 'http://117.41.38.18:9000'
}
# https://icanhazip.com/
url = 'http://icanhazip.com/'
response = requests.get(url, proxies)
# print(response.request.__getattribute__('proxies'))
print(response.content)