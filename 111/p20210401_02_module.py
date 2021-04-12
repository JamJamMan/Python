#모듈
# import time
# print(time.localtime().tm_year,'년',time.localtime().tm_mon,'월',
#       time.localtime().tm_mday,'일',time.localtime().tm_hour,'시',
#       time.localtime().tm_min,'분',time.localtime().tm_sec,'초')

# from datetime import datetime
# now=datetime.now()
# print(now)
# print(now.strftime('%Y-%m-%d %H:%M:%S'))

#sleep 함수 : 프로그램 실행 속도를 제어
# import time
# print('시작')
# time.sleep(3)
# print('3초지남')


#타이머
# from time import sleep
# sec=int(input('몇초?'))
# print('타이머시작')
# # t=[1,2,3]
# for a in range(1,sec+1) :
#     sleep(1)
#     print(a,'초')
# print('타이머 종료')

#난수모듈
#주사위 게임
# import random
# awin=0 #a이 긴횟수
# bwin=0 #b가 이긴횟수
# while True :
#     a= random.randint(1,6)
#     b= random.randint(1,6)
#     print('1번 주사위 :',a,'2번 주사위 :',b)
#     if a>b :
#         print('1번 주사위',a,'가 이겼다.')
#
#     elif a<b :
#         print('2번 주사위',b, '가 이겼다.')
#
#     else :
#         print('무승부')




# import random
#sample()
# print(random.sample(range(1,46),6))

#choice()
# print(random.choice(['가위','바위','보']))

#shuffle() :섞는다
# data=['나비','나비','벌','벌','꽃','꽃']
# random.shuffle(data)
# print(data)

import turtle
turtle.shape('turtle')
turtle.color('red')
for x in range(100):
    turtle.forward(11)
    turtle.right(90)
    turtle.forward(11)
    turtle.left(90)
    turtle.forward(11)
    turtle.left(90)

turtle.done()















