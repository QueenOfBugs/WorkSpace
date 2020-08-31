import urllib.request

url = "http://www.baidu.com"

response = urllib.request.urlopen(url)

data = response.read()

dataline = response.readline()