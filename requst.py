import requests
import json

city=input("输入你要查询的城市：")
x=requests.get("https://uapis.cn/api/v1/misc/weather?city=" + city)
data=x.json()
print("--------\n你的城市:"+city+"\n"+city+"的天气为"+data["weather"]+"\n天气发布时间为:"+data["report_time"])


