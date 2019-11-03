import urllib.request
import re

url="http://news.baidu.com/"
#伪装浏览器用户
headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'}
req = urllib.request.Request(url,headers=headers)
res = urllib.request.urlopen(req)
#从相应对象中读取信息并解码
html = res.read().decode("utf-8")

#print(len(html))
#使用正则解析新闻标题信息
pat = '<a href="(.*?)" .*? target="_blank">(.*?)</a>'

dlist = re.findall(pat,html)
#遍历输出结果
for i in dlist:
    print(i[1]+":"+i[0])
