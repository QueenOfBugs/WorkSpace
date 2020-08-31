import requests

url = 'https://www.baidu.com/baidu?'

parameters = {'wd': 'python1'}

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}

response = requests.get(url, headers = headers, params=parameters)

print(url)

print(response.request.url)

print(response.request.headers)

print(response.content.decode())

with open('baidu.html', 'wb') as f:
    f.write(response.content)
    f.close()
