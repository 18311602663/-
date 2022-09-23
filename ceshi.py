# -*- coding: utf-8 -*-
import http.client, urllib
import json      #引入json库

conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
params = urllib.parse.urlencode({'key':'c4429af7cd7580e47f1bf5a38bef32a7'})
headers = {'Content-type':'application/x-www-form-urlencoded'}
conn.request('POST','/dujitang/index',params,headers)
res = conn.getresponse()
data = res.read()
print(data.decode('utf-8'))
data = json.loads(data)  #转换成字典
print (data["newslist"][0]["content"])
