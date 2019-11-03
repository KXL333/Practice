import urllib.request
import re

url = "http://www.baidu.com"

res = urllib.request.urlopen(url)
html = res.read().decode("utf-8")
#print(len(html))

dlist = re.findall("<link rel=(.*?) type=(.*?) href=(.*?)>",html)
print(dlist)
