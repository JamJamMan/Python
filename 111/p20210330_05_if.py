#조건문 줄이 맞아야함
# a=1
# if a>0:
#     print('양수')
#     print(a)
# else:
#     print('음수')
#     print(a)
#
# print('프로그램 종료')

#실습) 회원등급 출력
#a가 90보다 크면 good 아니면 try를 츨력
# a=int(input('숫자입력'))
# if a>90:
#     print('good')
# else:
#     print('try')


#실습) 비밀번호 체크
#비밀번호가 일치하면 '문이 열립니다.'
#일치하지 않으면 '다시 확인하세요.'
# pw='1234' #기존 등록된 비밀번호
# pw=input('비번입력')
# if pw=='1234':
#     print('문이 열립니다.')
# else:
#     print('다시 확인하세요.')

#답
pw='1234'
# inpw = input('비밀번호?')
# if pw==inpw:
#     print('문이열립니다.')
# else:
#     print('다시확인하세요.')

#어떤수가 짝수이면 '짝수', 홀수이면 '홀수'출력
#a=12
# a=int(input('숫자입력 '))
# if a==0:
#     print('짝수도 홀수도 아닙니다.')
# elif a%2==0 :
#     print('짝수')
# else :
#     print('홀수')

#실습) ~90 A, 89~80 B, 79~70 C, 69~60 D, 59~ F
# a=int(input('점수입력 : '))
# if a>=90 :
#     print('A')
# elif a>=80 :
#     print('B')
# # if a<=89 and a>=80: # and 쓰면 범위도 설정됨
# #     print('B')
# elif a>=70 :
#     print('C')
# elif a>=60 :
#     print('D')
# else :
#     print('F')

#실습)몸무게와 키를 입력받아서 비만 여부 출력
# 평균체중 =(키-100)*0.9
# 오차범위 : +- 5%
# h=int(input('키 : '))
# w=int(input('몸무게 : '))
# n=(h-100)*0.9
# print('정상체중 : ',n)
# if w<n*0.95 :
#     print('당신은 말랐네요.')
# elif w>n*1.05  :
#     print('당신은 비만입니다.')
# else :
#     print('당신은 정상체중.')

#실습) 계산기
#두 수와 기호를 입력받아 사칙연산을 출력
# 30 + 20 = 50
# a=int(input('첫번째숫자 : '))
# c=input('기호 ')
# b=int(input('두번째숫자 : '))
# if c=='+' :
#     print(a+b)
# elif c=='*' :
#     print(a*b)
# elif c=='/' :
#     print(a/b)
# elif c=='-':
#     print(a-b)
# else :
#     print("기호틀림")

#2) 한번에 입력 split() : 인덱스 형태([])로 입력시켜줌 괄호안의 문자로 나눔
# data=input('계산식은?').split()
# # print(data)
# a=int(data[0])
# b=int(data[2])
# c=data[1]
# if c=='+' :
#     # print(a+b)
#     print('%d + %d = %d'%(a,b,a+b))
# elif c=='*' :
#     # print(a*b)
#     print('%d * %d = %d'%(a,b,a*b))
# elif c=='/' :
#     # print(a/b)
#     print('%d / %d = %d'%(a,b,a/b))
# elif c=='-':
#     # print(a-b)
#     print('%d - %d = %d'%(a,b,a-b))
# else :
#     print("기호틀림")

# 3)
import os
#print(os.listdir())
# data = input('계산식은?')
# print(eval(data))

# 실습) 두 수를 입력을 받아서 큰수를 화면에 출력
# a=int(input('첫번째숫자'))
# b=int(input('두번째숫자'))
# data=input('두 수를 입력하세요').split()
# a=int(data[0])
# b=int(data[1])
# if a>b :
#     print(a)
# else  :
#     print(b)

# 실습) 현재 있는 금액과 물품 구입 금액을 입력받고 비교하여 거스름돈을 구하자
# a=int(input('현재 금액'))
# b=int(input('물품 금액'))
# if a>b :
#     print('거스름돈',a-b,'원')
#     print('계산완료')
# elif a==b :
#     print('계산완료')
# else :
#     print('돈이',b-a,'원 부족')

# 논리연산자
# a=10;b=20
# print(a>0 and b>0)
# print(a>0 and b<0)
# print(a>0 or b<0)
# print(not (a>0))

# a=0; b=0
# if a>0 and b>0 :
#     print('둘 다 양수')
# elif a==0 or b==0:
#     print('0이 아닌 수를 입력하세요')
# elif a>0 or b>0 :
#     print(' 둘 중 하나는 음수')
# elif a<0 and b<0 :
#     print('둘 다 음수')


# 실습)
# a=input('1. 짜장면, 2. 짬뽕, 3. 설렁탕, 4. 비빔밥, 5. 피자, 6 스파게티 메뉴를 선택하세요. : ')
# if a=='1' or a=='2' :
#     print('중식')
# elif a=='3' or a=='4' :
#     print('한식')
# elif a=='5' or a=='6' :
#     print('양식')
# else :
#     print('메뉴 다시 선택')



# price ={'1':['자장면',5000],'2':['짬뽕',6000],'3':['설렁탕',8000],'4':['비빔밥',5000],'5':['피자',6000],'6':['스파게티',8000]}
# print(price)
# print('-'*22)
# print('[국제식당]오늘의 메뉴')
# print('-'*22)
# print('1.자장면\n2.짬뽕\n3.설렁탕\n4.비빔밥\n5.피자\n6.스파게티')
# print('-'*15)
# a=input('메뉴는? : ')
# print(price[a][0],price[a][1],'원')
# if a in ['1','2']: #in : 포함여부
#     print('중식')
# elif a in ['3','4']:
#     print('한식')
# elif a in ['5','6']:
#     print('양식')
# else :
#     print('메뉴 다시 선택')



#2
price ={'1':['자장면',5000,'중식'],'2':['짬뽕',6000,'중식'],'3':['설렁탕',8000,'한식'],
        '4':['비빔밥',5000,'한식'],'5':['피자',6000,'양식'],'6':['스파게티',8000,'양식']}
print(price)
print('-'*22)
print('[국제식당]오늘의 메뉴')
print('-'*22)
print('1.자장면\n2.짬뽕\n3.설렁탕\n4.비빔밥\n5.피자\n6.스파게티')
print('-'*15)
a=input('메뉴는? : ')
menukey = price.keys()
if a in menukey:
    print(price[a][0],price[a][1],'원',price[a][2],'코너')
else :
    print('다시 입력해 주세요.')








