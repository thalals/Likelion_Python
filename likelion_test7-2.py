#과제2 (구구단) 클래스
list = [2,3,4,5,6,7,8,9]

class gugu :
    def prints(self) :
        for i in list :
            print(i,"단 : ",end="")
            for j in range(9) :
               j+=1
               print(i*j," ",end="")
            print()

a= gugu()
a.prints()