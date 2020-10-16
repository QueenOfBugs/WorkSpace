#!/usr/bin/env python
# coding=utf-8

import requests
import re

loginUrl = 'https://github.com/login'
sessionUrl = 'https://github.com/session'
userName = 'wj915614874@163.com'
passWord = '13387683422jian'
headers = {

}
# 实例化session对象
session = requests.session()

class githubLogin(object):
    def __init__(self):
        self.initUrl = loginUrl
        self.sessionUrl = sessionUrl
        self.userName = userName
        self.passWord = passWord
        self.headers = headers
        self.data = data
