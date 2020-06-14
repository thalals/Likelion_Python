#입력한 숫자중에 최소값과 최대값을 비교출력하여라
#split= 공백을 기준으로 리스트에 추가
number = list(map(int, input('숫자를 입력하세요 >>').split()))

numberbox=list()                   #최대 최소값의 인덱스를 저장할 리스트

for i in range(len(number)) :        #number list의 수만큼 초기화
    numberbox.append(0) 

for i in range(len(number)) :
    print('{}      '.format(number[i]),end = '')
    if(number[i]==max(number)) :                 #최대 최소값 인덱스 저장
        numberbox[i]= 2
    elif(number[i]==min(number)) :
        numberbox[i] = 1


print()                                              #줄바꿈
for i in range(len(numberbox)) :
    if(numberbox[i]==1) :
        print("최소값 ",end = '')
    elif(numberbox[i]==2) :
        print("최대값 ",end = '')
    else :
        print("       ",end='')
