from urllib import request,error

url = "http://www.baidsu.com"
req = request.Request(url)

try:
        
    res = request.urlopen(req)
    html = res.read().decode("utf-8")

    print(len(html))
except error.HTTPError as e:
    print(e.reason)
    print(e.code)

    
print("ok")
