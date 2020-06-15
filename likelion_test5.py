# 구구단
list = [2,3,4,5,6,7,8,9]

for i in list :
    print(i,"단 : ",end="")
    for j in range(9) :
        j+=1
        print(i*j," ",end="")
    print()