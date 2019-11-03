import urllib3
import re

url = "http://www.baidu.com"

http = urllib3.PoolManager()

res = http.request("GET",url)

print("status:%d" % res.status)
