from requests.exceptions import RequestException
from lxml import etree
from bs4 import Beautifulsoup
from pyquery import PyQuery
import requests
import time


def getPage(url):
	'''爬取指定url地址的信息'''
	try:
		#定义请求头部信息
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
		#执行爬取
		res = requests.get(url)
		if res.status_code ==200:
			return res.text
		else:
			return None
	except RequestException:
		return None

def parsePage(content):
	'''解析指定网页内容，并返回结果'''
	#print(content)
	#========使用XPATH解析=========
	#1初始化，返回根节点对象
	html = etree.HTML(content)
	#2解析网页中<div class="item">...</div>信息（一部电影信息）
	items = html.xpath('//div[@class="item"]')
	#遍历并解析每部电影信息
	for item in items:
		yield{
			'insex':item.xpath(".//div/em[@class='']/text()")[0],
			'title':item.xpath(".//span[@class='title']/text()")[0],
			
		}

def writeFile(content):
	'''储存信息'''
	pass

def main(offset):
	'''主程序函数，负责调度执行爬取处理'''
	url = 'https://movie.douban.com/top250?start='+str(offset)
	html = getPage(url)     #执行爬取
	if html:
		parsePage(html)    #执行解析

#判断当前执行是否为主程序，并遍历调度主函数来爬取信息
if __name__ == '__main__':
	main()
	#for i in range(10):
	#	main(offset=i*25)
	#	time.sleep(5)