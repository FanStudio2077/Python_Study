from operator import truediv
import random

rand_num=random.randint(1,50)
score=6

while True:
    input_num=int(input("输入你的数字："))

    if score > 0:
        if input_num == rand_num:
            if int(input("你拆队了，需要继续不，输入1继续游戏，输入2退出游戏:\n")) == 1:
                score+=1
                continue
            else:
                break
            
        elif input_num > rand_num:
            print("数字大了,扣一分")
            score-=1
        elif input_num < rand_num:
            print("数字小了，扣一分")    
            score-=1
        else:
            print("error,游戏出错，立刻退出")
    else:
        break
    
