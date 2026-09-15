# 第1章 基础语法练习：四则运算计算器
# 需求：输入两个数和运算符，输出计算结果（除法要判断除数是否为 0）

x = int(input("X:"))
y = int(input("y:"))
r = input("+,-,*,/")

if r == "+":
    print(x + y)
elif r == "-":
    print(x - y)
elif r == "*":
    print(x * y)
elif r == "/":
    if y == 0:
        print("有问题")
    else:
        print(x / y)
else:
    print("非法输入")
