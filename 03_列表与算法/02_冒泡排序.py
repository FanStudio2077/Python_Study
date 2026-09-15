nums=[30,40,22,90,55,20]
i=0

temp=0

while i<6:
    
    j=0
    while j < 5-i:
        
        if nums[j] < nums[j+1]:
            temp=nums[j]
            nums[j]=nums[j+1]
            nums[j+1]=temp
        j+=1    
    print(f"第{i}轮排序结果: {nums}")
    i+=1
