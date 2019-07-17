import time

input('Enter를 누르면 게임이 시작합니다.')
a=time.time()
input('20초 후에 다시 Enter를 누르시오.')
b=time.time()
f=b-a
print('시간:',f,'초')
print('차이:',abs(f-20),'초')

