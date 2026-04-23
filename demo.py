'''
a =int(input("输入数字"))

if 90 <= a <= 100:
    level="A"
elif 80 <= a < 90:
    level="B"
elif 70 <= a < 80:
    level="C"
elif 60 <= a < 70:
    level="D"
else:
    level="E"

print(f"{level}")

'''
'''

sl=eval(input("输入金额："))

bz=input("输入币种:")



if bz == "￥" or bz == "人民币":
    result=sl / 6.87
else:
    if bz == "$" or bz == "美元":
        result=sl / 6.87
    else:
        exit()    


print(f"{result}")
'''

'''
import math

a=int(input("shu:"))
b=a%10 #个
c=int(a/10)%10 #十
d=int(a/100)%10 #百
e=int(a/1000)%10 #千
f=int(a/10000)%10 #万
print(f"{f}")
if b == f and e == c:
    print("为回文数")
    '''
'''
x=int(input("X:"))
y=int(input("y:"))
r=input("+,-,*,/")
if r == "+":
    print(x+y)
elif r =="-":
    print(x-y)
elif r == "*":
    print(x*y)
elif r =="/":
    if y == 0:
        print("有问题")
    else:
     print(x/y)
else:
 print("非法输入")

 '''
'''

for i in range(0,10):
    for j in range(0,i+1):
        print(f"{i}*{j}={i*j}",end="")

    print()      
'''
'''
a=[1,2,3]
a.append(7)
print(a[3])
'''

n=input("输入密码:")
password="1314"
count=3
for i in range(3):
    count-=1
    if n==password:
        
    