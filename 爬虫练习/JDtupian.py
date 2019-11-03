#爬取京东商品图片信息的案例
import requests
from bs4 import beautifulsoup

url = 'https://list.jd.com/list.html?cat=9987,653,655'
#url地址

#爬取数据
res = requests.get(url)
#print(res.text)
#使用beautifulsoup解析数据
soup = Beautifulsoup(res.text,'lxml')

#获取图片信息
imlist = soup.find_all(name="img",attrs={'width':'220','height':'220'})

#遍历
for im in imlist:
	if "src" in im.attrs:
		imurl = "https:"+im.attrs['src']
	else:
		imurl = "https:"+im.attrs['data-lazy-img']
	#存储图片
	with requests.get(imurl,stream=Ture) as ir:
		with open("./mypic/p"+str(m)+".jpg","wb") as f:
			for chunk in ir:
				f.write(chunk)
	print('p'+str(m)+".jpg")
	m += 1