from ast import literal_eval
import time
import requests
import json
import os
 
sign_list=[]
def weather(city_in):
    x=requests.get("https://uapis.cn/api/v1/misc/weather?city=" + city_in)
    data=x.json()
    return data["weather"]
def json_r():
    """读取JSON文件，如果文件不存在则返回空字典"""
    if not os.path.exists('data.json'):
        return {}
    with open('data.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def json_w(num, date, scores):
    # 1. 先读取已有的全部数据
    all_data = json_r()
    
    # 2. 检查编号是否已存在
    if num in all_data:
        return "exists"
    
    # 3. 添加新数据
    all_data[num] = {
        "date": date,
        "scores": scores
    }
    
    # 4. 将合并后的完整数据写回文件
    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(all_data, json_file, indent=4, ensure_ascii=False)
    return "ok"
def chaxun(num):
    data=json_r()
    print("\n编号:"+num+"\n积分:"+data[num]["scores"]+"\n签到时间:"+data[num]["date"])
def yiyan():
    x=requests.get("https://v1.hitokoto.cn/")
    data=x.json()
    print("\n"+data["hitokoto"]+"\t--"+data["from"])
def riqi():
    return time.strftime("%Y-%m-%d", time.localtime())
def sign(num):
    return json_w(str(num), riqi(), str(num * 10))

def rate():
    num=0
    data=json_r()
    while True:
        if str(num) in data:
            return num
            break
        num=num + 1

def Message(msg):

    
    if "天气" in msg:
        city=msg[2:]
        wea=weather(city)
        print("--------\n你的城市:"+city+"\n"+city+"的天气为"+wea)
    
    if msg=="一言":
        yiyan()

    if "签到" in msg:
        num=msg[2:]
        code=sign(num)
        if code == "exists":
            print("你今天已签到过了，不必在签到啦")
        elif code == "ok":
            level=rate()-1
            print("签到成功\n"+"你的排行为"+str(level))
        else:
            print("未知错误")

while True:
    msg=input("输入你的消息:")
    Message(msg)