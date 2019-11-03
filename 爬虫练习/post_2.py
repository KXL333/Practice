import requests
import json

def fanyi(keyword):
    # 定义请求URL地址和参数
    url = "https://fanyi.baidu.com/sug"
    data = {'kw':keyword}

    #发送请求，爬取信息
    res = requests.post(url,data = data)

    # 解析结果
    str_json = res.content.decode("utf-8")
    #print(str_json)
    myjson = json.loads(str_json)

    print(myjson['data'][0]['v'])

# 主程序
if __name__ == '__main__':
    while True:
        keyword = input("请输入要翻译词：")
        if keyword == 'q':
            break
        fanyi(keyword)

        
