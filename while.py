i=1
j=1
sum=0
while i==1:

    a=input(f"输入第{j}位的成绩:")
    if a=="Q":
        break
    sum=sum+int(a)
    j+=1
print(sum) 
print(sum/j)
    