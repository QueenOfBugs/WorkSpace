import re
import requests


class LoginGithub(object):

    def __init__(self, username, password, name):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'Host': 'github.com',
            'Referer': 'https://github.com/'
        }
        self.init_url = 'https://github.com/login'
        self.login_url = 'https://github.com/session'
        self.verify_url = 'https://github.com/{}'.format(name)
        self.username = username
        self.password = password

    def login(self):
        session = requests.session()
        session.headers = self.headers
        # init_url 获取token
        # 发送请求获取响应
        res_init = session.get(self.init_url).content.decode()

        # 正则提取
        token = re.findall('name="authenticity_token" value="(.*?)" />', res_init)[0]
        timestamp = re.findall('name="timestamp" value="(.*?)" />', res_init)[0]
        timestamp_secret = re.findall('name="timestamp_secret" value="(.*?)" />', res_init)[0]
        print(token, timestamp, timestamp_secret)
        # login_url 登录
        # 构建表单数据
        data = {
            'commit': 'Sign in',
            'authenticity_token': token,
            'ga_id': '634981938.1538980191',
            'login': self.username,
            'password': self.password,
            'webauthn-support': 'supported',
            'webauthn-iuvpaa-support': 'unsupported',
            'return_to': '',
            'required_field_0f3c': '',
            'timestamp': timestamp,
            'timestamp_secret': timestamp_secret
        }
        # 发送请求登录
        session.post(self.login_url, data=data, verify=False, timeout=10)
        # verify_url 验证
        response = session.get(self.verify_url, timeout=20).content.decode()
        return response


if __name__ == "__main__":
    lg = LoginGithub('wj915614874@163.com', '13387683422jian', 'QueenOfBugs')
    res = lg.login()
    print(res)