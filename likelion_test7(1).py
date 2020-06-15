#test4,5,6 을 클래스로
print("나는 별이다...")
star = int(input("얼마나 이동할까?"))

class stars :
    def setdata(self,stars) :
       self.stars=stars

    def prints(self) :
        i=0
        j=0
        while(i<self.stars) :
            while(j<i) :
                print("    ",end="")
                j+=1
            j=0
            print("*")
            i+=1

a= stars()
a.setdata(star)
a.prints()

