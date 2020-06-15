#딕셔너리 전화부
likelion = {'이남준':'010-6757-8402','최민석':'010-3759-9397'}

name = input("이름을 입력하세요 : ")

if name in likelion :
    print(name,"의 연락처는 ",likelion[name],"입니다.")
    del likelion[name]                                       #있으면 삭제

elif name not in likelion :
    print(name,"에 대한 정보가 없습니다. 등록합니다.")
    number = input("전화번호를 입력하세요 : ")
    likelion[name] = number                                 #없으면 추가

print("==현재 등록된 이름과 전화번호==")
for a,b in likelion.items() :
    print(a,b)