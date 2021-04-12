# #사용자에게 입력받기
# a=input('이름은?')
# print('입력한 값은', a)

#실습) 나이를 입력받아 화면에 출력
#입력한 값은 문자취급

# a=input('나이는?')
# print('나이 :',a)

#답
# age=input('나이는?')
# print('당신의 나이는'  +age + '입니다.')


#실습) 날씨를 입력받아 오늘의 날씨 출력
#예) 오늘의 날씨는 맑음
# txt='오늘의 날씨는'
# a=input(txt)
# print(txt, a)

#답
# txt='오늘의 날씨는'
# w=input('날씨 :')
# print(txt,w,sep='*')

#도움말 출력
# help(print)

#사용자가 입력한 값에 100을 더해서 출력
# a=input('숫자는?')
# a=int(a) #정수로 변환해서 반환해주는 함수
# a=float(a) #실수로 변환해서 반환해주는 함수
# print(a+100)

#실습) 두 수를 입력받아 사칙연산 프로그램
# a=input('첫번째숫자')
# c=input('부호')
# b=input('두번째숫자')
# a=int(a)
# b=int(b)
# print("결과",a+b)
# print("결과",a-b)
# print("결과",a*b)
# print("결과",a/b)

#답
# a= int(input('첫번째수?'))
# b= int(input('두번째수?'))
# print('%d + %d = %d'%(a,b,a+b))
# print('두 수를 더한 값은 ', a+b, '입니다.')

#2)
# data = input('두수는?').split()
# a,b = map(int,data) #data의 각값을 int함수를 젹용한후 a,b에 대입
# print(a,'+',b,'=',a+b)

#실습) 원의 넓이를 구하기
# a=int(input('반지름의 길이는?'))
# print('원의 넓이는', a*a*3.14, '입니다')

#답
# r=float(input('반지름 :'))  # 반지름이 소수일수도 있어서 float씀
# print('원의 넓이는', r**2 * 3.14)































