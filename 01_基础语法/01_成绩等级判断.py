# 第1章 基础语法练习：if / elif / else 多分支
# 需求：输入分数，输出对应等级 A~E

a = int(input("输入数字"))

if 90 <= a <= 100:
    level = "A"
elif 80 <= a < 90:
    level = "B"
elif 70 <= a < 80:
    level = "C"
elif 60 <= a < 70:
    level = "D"
else:
    level = "E"

print(f"{level}")
