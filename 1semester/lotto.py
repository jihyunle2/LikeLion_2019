import random

list1=[14,18,22,26,31,44,40] #당첨번호, list[6]은 보너스번호
list2=[]

count=0

list2=random.sample(range(1, 46), 6)

list2.sort()
print("당첨 번호는",list1,"입니다.")
print("제시된 번호는",list2,"입니다.")

for i in range(0,6):
    for j in range(0,6):
        if list1[i]==list2[j]:
            count= count + 1
if count==6:
    print(count,"개의 숫자가 일치하여, 1등입니다.")
else:
    count=0
    for i in range(0,7):
        for j in range(0,6):
            if list1[i]==list2[j]:
                count=count+1
    if count==6:
        print(count,"개의 숫자가 일치하여, 2등입니다. 하나는 보너스 번호입니다.")
    elif count==5:
        print(count, "개의 숫자가 일치하여, 3등입니다.")
    elif count==4:
        print(count, "개의 숫자가 일치하여, 4등입니다.")
    elif count==3:
        print(count, "개의 숫자가 일치하여, 3등입니다.")
    else:
        print(count, "개의 숫자가 일치합니다.")

