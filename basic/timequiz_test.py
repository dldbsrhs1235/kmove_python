#사칙연산
import random
import time

input('Enter를 누르면 게임을 시작합니다.')
start=time.time()

count=0
oper=['+','-','*','/']
for x in range(0,5):
    a=random.randint(1,50)
    b=random.randint(1,50)
    op=random.choice(oper)

    quiz=str(a)+op+str(b)
    quiz='%d %s %d'%(a,op,b)

    print(quiz,'=')
    print(eval(quiz))
    c=int(input('정답='))

    if int(eval(quiz))==c:
        print("정답!")
        count+=1
    else:
        print("오답1")
end=time.time()
print("%d개 맞음"%count)

ff=end-start
print('문제걸린 시간은',ff,'입니다.')