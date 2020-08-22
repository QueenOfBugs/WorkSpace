# token
#"name="authenticity_token" value="BlVSRXhkgJyPnTxJI6fiG4AXB8JMrqF8K5g4sSJoY7A4VkiXjJdq9s+c775Wn3VI1wwpTFauM8auiiX/6/a/jQ=="

# 正则
# name="authenticity_token" value="(.*?)"

import re
import requests

def login():
    session = requests.session()
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'
    }
    ## url1 获取token
    url1 = 'https://github.com/login'
    ## 需要正则处理获取token 正则只能对str数据类型处理，要decode
    response1 = session.get(url1).content.decode()
    token_str = re.findall('name="authenticity_token" value="(.*?)"', response1)[0]
    # print(token_str)
    ## url2 登录
    url2 = 'https://github.com/session'
    # 构建表单数据
    data = {
        'commit': 'Sign in',
        'login': 'wj915614874 @ 163.com',
        'password': '13387683422jian'

    }
    session.post(url2, data=data)
    ## url3 验证
    url3 = 'https://github.com/QueenOfBugs'
    cookies = {
        'Cookie':' _octo = GH1.1.986704088.1597720347;tz = Asia % 2FShanghai;_ga = GA1.2.1996796347.1597721335;_device_id = facf183cd27aa119af079545f9f08865; tz = Asia % 2FShanghai;has_recent_activity = 1;user_session = cXRA2fFw764 - QX8SDQqe5yT8xKrbaE - _8qf_FkJNlDHKJMzl;__Host - user_session_same_site = cXRA2fFw764 - QX8SDQqe5yT8xKrbaE - _8qf_FkJNlDHKJMzl;logged_in = yes;dotcom_user = QueenOfBugs;
    _gat = 1;
    _gh_sess = 18
    AISCj5Mq1bQCYe2A42suaAOuwDEI3LVLFI3KZeN4fue2ET01GFgvt2QD % 2
    Bi0wYRXp4bYgNY0MrjYgA % 2
    BxZVkqUlhmnNb44zIlIiB7L0WVjGN63fq15jIITo88FlmnUSt9lVVwjWuhmTnPs2xf9i6iz07EvbrOJgq16RvzH8Pd4rCCQyo % 2
    B % 2
    Fs % 2
    FWk % 2
    F5ZDyI70K % 2
    Brt4Fj7Vy4YzLUN % 2
    FV8yrdX1jJQ50m6kLRXm3ZLRY5foFvW55ruw9sj28eGCLp6RyHjYr % 2
    BuxSxr1pjQYKrv % 2
    FIfrDIWLU5kSRL % 2
    FqnrGEHg % 2
    FBH7cepUmEDKkC8OCRuVFCCExna0bRNXux % 2
    Bi3n7qqDC2aJS1w47wQwSQrCJXXu % 2
    F4VXVddfTyWNq29cA770ktaI % 2
    F9TN3GsJ5xaq9XIpfAjUjZx4XQJwz6dFI3XSPr1Kval1 % 2
    FRaaparTePKSDk % 2
    FpV9E3RTOgO1uHmQbGrJ62gES88d % 2
    B % 2
    Fei72V7KMj6Wyb9EguAt4BRGLccF3CMzHzqzy6JT9RzPmIKiqpl0i4K % 2
    F4okLegVBBWo65raOzdllIZAmRe % 2
    FKV2rAAWM9wSSd0wYvdgYVIlTpCBJDGLS1x2G9P6MCis % 2
    BQMKFHtoq % 2
    Fk784B1V % 2
    Fnd43j % 2
    BngIwakg2Qngrrv5iXlEQ % 2
    BKLBSxxqADWvlH2xOgaZW2ZZWI5ylMXflARbF2X4Esx % 2
    BgLzDBvAvHRoWaxfTzMYrgb0o1ghpZOkiajQkTBeG % 2
    ByT5mwdzUi0ozorROkqma99GuqB4BSavRYoTGC % 2
    Bp % 2
    BH % 2
    BPbXc % 2
    Ba4J92R % 2
    Ff % 2
    FoTcYaoBfDsH8Bub07hVzvOKu7NMnDusYPc0AJCd % 2
    FEt9pMx5qnU % 2
    BJ9tUH2ZUkfnsK9T0e3t % 2
    FC6xra87rF69B % 2
    B0cdoOCsH7XuV9ssmGTmHY5IO6vCOsW4Mw3jLoVe5JRPE1WqshQLKK8n9OiBJMMpRpW1WMp5aFIXkspQcI5IhwCnwgdbZTc5ur % 2
    BKgRy5MxM3u263pmDX7EbHUFUx7gqLo3aKftzF % 2
    BQbvP5xQSrDeY62BQQqc3u0XyegU05wy711IM % 3D - -TSZFBB707Umtqf % 2Bm - -t % 2FVo5vpBmQsp8 % 2FvAoTHxrQ % 3D % 3D'
    }
    response = session.get(url3)
    print(response.status_code)
    with open('github_session.html', 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    login()