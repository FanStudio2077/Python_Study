# 第1章 基础语法练习：密码验证（未完成）
# 需求：最多输入 3 次密码，输入正确则通过，错误则提示剩余次数

n = input("输入密码:")
password = "1314"
count = 3

for i in range(3):
    count -= 1
    if n == password:
        pass  # TODO: 这里应该提示“验证成功”并 break
    # TODO: 密码错误时，要提示还剩几次机会；次数用完则锁定
