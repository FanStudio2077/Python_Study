import json
import time
import os

def riqi():
    return time.strftime("%Y-%m-%d", time.localtime())

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
        print(f"编号 {num} 已存在，跳过插入\n")
        return "exists"
    
    # 3. 添加新数据
    all_data[num] = {
        "date": date,
        "scores": scores
    }
    
    # 4. 将合并后的完整数据写回文件
    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(all_data, json_file, indent=4, ensure_ascii=False)
    
    print(f"编号 {num} 插入成功\n")
    return "ok"
def chaxun(num):
    data=json_r()
    print("\n编号:"+num+"\n积分:"+data[num]["scores"]+"\n签到时间:"+data[num]["date"])
# 测试：插入编号 0 到 4
for i in range(5):
    json_w(str(i), riqi(), str(i * 10))  # 分数改成不同值便于观察

num=0
for i in range(5):
    data=json_r()
    if str(num) in data:
        chaxun(str(num))
    else:
        print(str(num)+"不存在")
    num = num+1

def rate():
    num=0
    while True:
        data=json_r()
        if str(num) in data:
            return num
            break
        else:
            num=num + 1

        


