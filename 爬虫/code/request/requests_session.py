# token
#"name="authenticity_token" value="BlVSRXhkgJyPnTxJI6fiG4AXB8JMrqF8K5g4sSJoY7A4VkiXjJdq9s+c775Wn3VI1wwpTFauM8auiiX/6/a/jQ=="

# 正则
# name="authenticity_token" value="(.*?)"

import re
import requests

def login():
    #创建session对象
    session = requests.session()
    #设置请求头
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'
    }
    ## url1 获取token
    url1 = 'https://github.com/login'
    ## 需要正则处理获取token 正则只能对str数据类型处理，要decode
    response1 = session.get(url1).content.decode()
    token_str = re.findall('name="authenticity_token" value="(.*?)"', response1)[0]
    ## timestamp_secret = re.findall('name="timestamp_secret" value="(.*?)" />', res_init)[0]
    timestamp_secret_str = re.findall('name="timestamp_secret" value="(.*?)"', response1)[0]
    timestamp_str = re.findall('name="timestamp" value="(.*?)"', response1)[0]
    print(token_str,timestamp_str,timestamp_secret_str)
    ## url2 登录
    url2 = 'https://github.com/session'
    # 构建表单数据
    # {
    # "commit":"Sign+in",
    # "authenticity_token":"svJ/K7dGiZ4GDnOD9NaxogVsIb6asCyULwiBPsn/KQhi3RxuBmmSUTvOS3gnkWAgcOJBA5bQAqO29bMO9n7sAQ==",
    # "ga_id":"",
    # "login":"wj915614874@163.com",
    # "password":"13387683422jian",
    # "webauthn-support":"supported",
    # "webauthn-iuvpaa-support":"unsupported",
    # "return_to":"",
    # "required_field_5810":"",
    # "timestamp":"1598942371618",
    # "timestamp_secret":"c96c0896385f45bda4dac0f0c0bb81bd597b4bca6bbc8393c1945ee9a0560c79"
    # }
    # authenticity_token,timestamp,timestamp_secret都需要在骨骼文件中提取

    data = {
        'commit': 'Sign+in',
        'authenticity_token': token_str,
        'login': 'wj915614874@163.com',
        'password': '13387683422jian',
        'ga_id': '',
        "webauthn-support": "supported",
        "webauthn-iuvpaa-support": "unsupported",
        "return_to":"",
        "required_field_5810":"",
        "timestamp":timestamp_str,
        "timestamp_secret":timestamp_secret_str
    }
    session.post(url2, data=data)
    ## url3 验证
    url3 = 'https://github.com/QueenOfBugs'

    response = session.get(url3)
    print(response.status_code)
    with open('github_session.html', 'wb') as f:
        f.write(response.content)
        f.close()


if __name__ == '__main__':
    login()