from requests.exceptions import RequestEception
import requests
import re 
import time

#爬取
def getPage(url):
	'''爬取指定url地址的页面信息'''
	try:
		res = requests.get(url)
		if status_code == 200:
			return res.text
		else:
			return None
	except RequestEception:
		return None

#解析
def parsePage(html):
	'''解析指定网页信息'''
	pass

#存储
def writeFile(content):
	'''储存信息'''
	pass

def main():
	'''主函数'''
	url = "https://maoyan.com/board/4"
	html = getPage(url)
	parsePage(html)
	print(html)

if __name__ == '__main__':
	main()