names=[]
scores=[]
total=0
highest=0
winner=''
loser=''
lowest=10000000
number=int(input('請輸入班上有多少人'))
for a in range(number):
    name=input('請輸入名字')
    score=int(input('請輸入分數'))
    names.append(name)
    scores.append(score)
for b in range(number):
    total=scores[b]+total
print("總分是",int(total))
average=float(total/number)
print("平均是",float(average))
def highest(number,scores,names):
    highest=0
    for c in range(number):
        if scores[c]>highest:
            highest=scores[c]
            winner=names[c]
    print('最高分是',winner,'的',highest,'分')
    return
highest(number,scores,names)

def lowest(number,scores,names):
    lowest=10000000000000
    for d in range(number):
        if scores[d]<lowest:
            lowest=scores[d]
            loser=names[d]
    print('最低分是',loser,'的',lowest,'分')
    return
lowest(number,scores,names)
    


 

      