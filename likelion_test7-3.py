#전화부 클래스
#딕셔너리 전화부
likelion = {'이남준':'010-6757-8402','최민석':'010-3759-9397'}

class directory :
    def scan_name(self) :
        name = input("이름을 입력하세요 : ")
        return name
    def plus_minus(self,name_s) :
        if name_s in likelion :
            print(name_s,"의 연락처는 ",likelion[name_s],"입니다.")
            del likelion[name_s]                                       #있으면 삭제

        elif name_s not in likelion :
            print(name_s,"에 대한 정보가 없습니다. 등록합니다.")
            number = input("전화번호를 입력하세요 : ")
            likelion[name_s] = number                                 #없으면 추가
    
    def prints(self) :
        print("==현재 등록된 이름과 전화번호==")
        for a,b in likelion.items() :
            print(a,b)


a=directory()
b=a.scan_name()
a.plus_minus(b)
a.prints()