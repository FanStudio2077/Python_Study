# 第1章 基础语法练习：输入、类型转换、if 嵌套
# 需求：输入金额和币种，输出换算成人民币后的金额

sl = eval(input("输入金额："))
bz = input("输入币种:")

if bz == "￥" or bz == "人民币":
    result = sl / 6.87
else:
    if bz == "$" or bz == "美元":
        # TODO: 这里写的是和人民币一样的汇率，美元应该用另一个汇率
        result = sl / 6.87
    else:
        exit()

print(f"{result}")
