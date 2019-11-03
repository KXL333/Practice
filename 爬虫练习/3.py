from urllib import request,error

url = "http://www.bsagdsfdsau.com"
req = request.Request(url)

try:
        
    res = request.urlopen(req)
    html = res.read().decode("utf-8")

    print(len(html))
except Exception as e:
    if hasattr(e,"code"):
        print('HTTPERROR')
        print(e.reason)
        print(e.code)
    elif hasattr(e,"reason"):
        print(e.reason)
        print('URLERROR')
        
print("ok")
