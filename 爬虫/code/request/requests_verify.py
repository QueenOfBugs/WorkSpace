# ssl.CertificateErrot...
# import requests
# url = 'https://sam.huat.edu.cn:8443/selfservice'
# response = requests.get(url)
import requests
url = 'https://sam.huat.edu.cn:8443/selfservice'
response = requests.get(url, verify=False)