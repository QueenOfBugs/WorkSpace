import requests


url = 'https://github.com'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}

cookie_str = '_octo=GH1.1.1310319776.1585638523; logged_in=yes; _ga=GA1.2.150556382.1585657024; experiment:homepage_signup_flow=eyJ2ZXJzaW9uIjoiMSIsInJvbGxPdXRQbGFjZW1lbnQiOjU1LjIwNDQ4OTI1NzkzMjc2LCJzdWJncm91cCI6bnVsbCwiY3JlYXRlZEF0IjoiMjAyMC0wMy0zMVQxMjoxNzowNC40MjRaIiwidXBkYXRlZEF0IjoiMjAyMC0wMy0zMVQxMjoxNzowNC40MjRaIn0=; _device_id=678adb1e5fe193f4925289600b3880ac; user_session=cosND-005AomKEF76jOvy4OtFWK0mk2tgd83WtDqTWvRqmZS; __Host-user_session_same_site=cosND-005AomKEF76jOvy4OtFWK0mk2tgd83WtDqTWvRqmZS; dotcom_user=QueenOfBugs; _gh_sess=r%2Bz6gc4fN2C1h6NMqsNLo7VR4r7rlrlymIDBEav7EuViZI%2BaJfmi5uAqjm03zHp9vttSstolaqyC5PMr4dZ2HD99J4qzwCl47oVzzcQJSyDjoxB2u7uoe2TaiFaBtajEisQwlNtItNmlShxb4AMQdkhmJ%2FwPujEKQHP1%2BJVogb6Q94UKbimlbqpsjT5ynxRgl7s%2FNl3EL3jJNeEeSkshjZdPWnvtQyIC%2BRQT1PNVJNnZ6zeoUl9qfWaSX%2BJfNpztarm4VS3oN2bF83euofPAlK93X4%2FFl1vUDx8C7at1DzsTSpXM4hCCF9lYVzK65yMdPboMPPEyxuHl1kJBq9pBq6diXOyJ%2Bo%2F4eAyRRWa1PafBgOYmoFA4Qqj7czUckrpGm4Zafw%2FFMNW7KKhG2%2BMypRx9vq9mOVsIbmoPScRnUsp%2FhBRBRTgzG66HhXSaeT7MQKsjTby0iGBM7wmJT6%2BrzE0JRr1MELVayojOfI1YjmrBRTAOasoP6SQ8fQ%2B1L%2BAUFa9ItRIWA2K%2BBnzygcIGCufiRKJB7J9ePOAtFFWMJxJlkx6dvTbI%2Bn4Gg4RIhTa4KGUjdoy%2Fj6Mg%2Fj9bnh7pt91wxvXhdp4oBHXd5jvXk2NsSehdhlSuHg0XZZlB9srWLTcRZvqydKWWmkFpFZepIwtFKGsn%2FkYB7hR8M6iO4DCIwSpOXAPhj2hfIBZ%2FGu8bcAbNXqEqeAkQ0XSuIO65AfSEdHUcQ%2BF8iX0FaPwwfkVxNvSwsdZ8elVQ%2Bkc5GLjF3%2F3BxnIGsc5%2B6%2BzifWitMyYHHMhCsFgM0ldIW%2BsKrAZqxEmf9qfX%2B3UfvgkmDsXRsybpOY4pXlcTIineVHPOIOm%2Bg%2FR%2FeX0coFQsDGeZdbIB28D8HpZNFZ1MRN3p9x4NU5GHKIy285rmiIhwkzWhBwRWRBZdIoFTwsPXGM4mQuH5adjJ4x2x4zxZ5QeigDo2sG28EsG17h9EGtRwRdo89CGKk%2BcOhY%2BIH0iiQC3Bb%2FJp8Tn%2FZ0DfPS%2F%2B%2F49ZI1pw%2FEaCa9LZCc4%3D--l3LEYFfPQ9oohyYb--BrKWmWJ7tu39qr8o2dHsng%3D%3D; tz=Asia%2FShanghai; has_recent_activity=1 '

cookie = {cookie.split('=')[0]: cookie.split('=')[-1] for cookie in cookie_str.split('; ') }

response = requests.get(url, headers=headers, cookies=cookie)
cookie = requests.utils.dict_from_cookiejar(response.cookies)
print(cookie)
with open('github_request_Cookie.html', 'wb') as f :
    f.write(response.content)
    f.close()
