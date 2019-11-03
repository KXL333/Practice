from urllib import request,error
import re

#使用urllib爬取58同城的招聘信息
url = "https://jn.58.com/tech/?key=php&cmcskey=php&final=1&jump=1&specialtype=gls"
req = request.Request(url)

res = request.urlopen(req)

html = res.read().decode("utf-8")

print(len(html))

pat = '<span class="address">(.*?)</span>  \| <span class="name">(.*?)</span>'

dlist = re.findall(pat,html)

#print(len(dlist))
for v in dlist:
    print(v[0]+":"+v[1])
