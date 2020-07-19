# 나는 천재다 나는 최고다 내가 짱이다
# git에 올릴거
number = int(input("숫자를 입력하세요 >> "))
result = 1
print(number,"! = ", number,end='')         #end=' ' 줄바꿈 무시
while(number>1) :
    result = result*number
    number =number -1
    print(" x",number,end='')

print(" = ",result)
