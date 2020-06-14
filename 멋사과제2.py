# 마라톤 참여자와 완주자의 리스트가 주어졌을때 낙오자를 출력해라

participants = ['mislav','stanko','mislav','ana']
completions=['stanko','ana','mislav']

maratoner=dict()                #딕셔너리 생성
for i in participants :
    if i not in maratoner :     #없으면 추가
        maratoner[i] = 1     
    else :
        maratoner[i] += 1       #중복되면 value 값 증가

for i in completions :
    if i in maratoner : 
        maratoner[i] += -1


for i,j in maratoner.items() :      #item 은 key, value 반환
    if j>0 :
        print(i)