import requests
import re

#使用urllib爬取58同城的招聘信息
data = {'key':'python','final':1,'jump':1}
url = "https://jn.58.com/tech/"
res = requests.get(url,params=data)



html = res.content.decode("utf-8")

print(len(html))

pat = '<span class="address">(.*?)</span>  \| <span class="name">(.*?)</span>'

dlist = re.findall(pat,html)

#print(len(dlist))
for v in dlist:
    print(v[0]+":"+v[1])
