#연습문제 별찍기
#실습1)
# a=0
# while True:
#     a+=1
#     print('*'* a)
#     if a==6:break
#
# #2)
# a=7
# while True:
#     a-=1
#     print('*'* a)
#     if a==0:break
#
# #3)
# a=0
# b=7
# while True:
#     a+=1
#     b-=1
#     print(' '*b,'*'* a)
#     if a==6 : break

#for 사용
#1)
# for x in range(1,7):
#     print('*'*x)

#2)
# for x in range(6,0,-1) :
#     print(' '*x)



#실습2)구구단
# a=int(input('숫자입력'))
# for x in range(1,10) :
#     print(a*x)
#답
# for x in range(1,10):
#     for y in range(1,10):
#         print('%d' '*' '%d' '=' '%d'%(x,y,x*y))


#실습3)숫자를 입력 받아 그 범위안의 수 중 0부터 3의 배수를 출력
# a=int(input('숫자입력'))
# print(list(range(0,a,3)))
#답
# last= int(input('마지막수는?'))
# for x in range(0,last+1,3):
#     print(x,end='\t')
#
# print()
# for x in range(0,last+1):
#     if x%3==0:
#         print(x,end='\t')


#실습4) 숫자 두 개와 기호를 입력 받아 계산기 만들기, 단 q를 입력하면 종료
# while True :
#     a = int(input('숫자입력'))
#     c = input('기호입력')
#     b = int(input('숫자입력'))
#     if c=='q':
#         break
#     elif c=='+':
#         print(a,c,b,'=',a+b)
#     elif c=='-':
#         print(a,c,b,'=',a-b)
#     elif c=='*':
#         print(a,c,b,'=',a*b)
#     elif c=='/':
#         print('%d / %d = %.2f'%(a,b,a/b))
#     else :
#         print('다시입력')

#답
#1
# while True:
#     a=input('first')
#     if a == 'q': break
#     a=int(a)
#     b=input('second')
#     if b == 'q': break
#     b = int(b)
#     sign=input('기호는?')
#     if sign=='q': break
#     if sign=='+':
#         print(a+b)
#     elif sign =='-':
#         print(a-b)
#     elif sign =='*':
#         print(a*b)
#     elif sign=='/':
#         print(a/b)
#     else:
#         print('잘못된 기호')
#
#     if input('종료(y)?')=='y': break
#2
# while True:
#     a=input('first')
#     if a == 'q': break
#     a=int(a)
#     b=int(input('second'))
#     # 원하는 기호가 입력될때까지 계속입력
#     while True :
#         sign=input('기호는?')
#         if sign in['+','-','*','/']:
#             break
#     if sign=='+':
#         print(a+b)
#     elif sign =='-':
#         print(a-b)
#     elif sign =='*':
#         print(a*b)
#     elif sign=='/':
#         print(a/b)
#     else:
#         print('잘못된 기호')
#
#     if input('종료(y)?')=='y': break



#실습5)점수가 딕셔너리로 저장되어 있을 때 값이 90점 이상인 학생들의 key만 출력
# dicA={1:94,2:87,3:91,4:75,5:92}
# if dicA>=90
# print(dicA[1])

#답
# dicA={1:94,2:87,3:91,4:75,5:92}
# print(dicA.keys())
# print(dicA.values())
# print(dicA.items())
# for no, score in dicA.items():
#     if score>=90:
#         print(no,'번')


#실습6)listA의 일 판매수량을 입력 받아 히스토그램을 늘리는 프로그램을 만들자
#1)사원의 판매수량 입력
#2)히스토그램 그리기
#데이터구조 = ['홍길동':10,'이순신':15,'김순희':5,'이철수':7]
# listA = ['홍길동','이순신','김순희','이철수']
# qty={} #판매수량을 저장할 딕셔너리
# for name in listA:
#     qty[name] = int(input(name + '?'))
# print(qty)
#
# for name, saleqty in qty.items():
#     print(name,'*'* saleqty)

#실습7)











