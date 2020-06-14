str ='파이썬은 1991년에 발표된 인터프리터 방식의 프로그래밍 언어로, 귀도 반 로섬이 크리스마스 주에 연구실이 닫혀 있어서 심심한 김에 만든 언어인데, 문법이 매우 쉬워서 초보자들이 처음 프로그래밍을 배울 때 추천되는 언어야’'

print (str)
str= str.split(',')

for sentence in str:
    sentence=sentence.strip()
    print(sentence)
