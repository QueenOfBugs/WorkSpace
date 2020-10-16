import base64

f = open("数据解析.png", "rb")

ls_f = base64.b64encode(f.read())

print(type(ls_f))

x = open('base64.txt', 'wb')
x.write(ls_f)