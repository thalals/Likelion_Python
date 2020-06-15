# 반복문
print("나는 별이다...")
star = int(input("얼마나 이동할까?"))

i=0
j=0
while(i<star) :
    while(j<i) :
        print("    ",end="")
        j+=1
    j=0
    print("*")
    i+=1
