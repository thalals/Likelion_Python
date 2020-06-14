#class 와 객체
#사칙연산
class Four_cal:
                                                    #self 는 객체 (자기 자신호출)
    def setdata(self, first, second) :
        self.first = first
        self.second = second

    def add(self) :
        return self.first + self.second
    def mul(self) :
        return self.first * self.second
    def sub(self) :
        return self.first - self.second
    def div(self) :
        return self.first / self.second

cal = Four_cal()
cal.setdata(4,5)
