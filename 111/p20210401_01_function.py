#내장함수
# data=[5,8,4,6]
# print(sum(data))

#사용자함수 sum정의:
#매개변수:리스트, 반환값:합계
# def mysum(data):
#     s=0
#     for x in data:
#         s += x
#     # print(s)
#     return s
#
# data=[5,8,4,6]
# r=mysum(data)
#
# print('리턴값 : ', r)

#max, min 함수
# data=[5,18,4,6]
# m=max(data)
# print('가장큰값 :',m)
# mi=min(data)
# print('가장작은값 :',mi)

#max값 사용자 함수
# def mymax(data):
#     mx = data[0]
#     for a in data:
#         if a>mx:
#             mx=a
#     return mx
##전역변수
# data = [5, 18, 4, 6]
# print('가장큰값 :',mymax(data))
# print(data)
# data = [78, 8, 5, 16]
# print('가장큰값 :',mymax(data))

#min값을 구하는 함수
# def mymin(mindata):
#     mi = mindata[0]
#     for x in mindata:
#         if x < mi:
#             mi = x
#     return mi
#
# data=[10,20,30,40]
# result=mymin(data)
# print('가장작은값:',result)

#ord() 함수
#한글은 유니코드 체계
# print(ord('A'), len('A'))
# print(ord('가'), len('가'), '가'.encode(),len('가'.encode()))
# print(chr(44032))

#실습)사칙연산 함수
#매개변수 : 두 수, 반환값 : 결과
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def cal(a,b):
#     return [a+b,a-b]
#
# print('더하기 :', add(10,20))
# print('빼기 :', sub(10,20))
# print('계산 :', cal(10,20)[0],cal(10,20)[1])

#실습3)월급 구하기 연봉, 시급, 초과근무 시작을 매개변수로 받아 월급을 계산하고반환
#(월급 = 년봉 / 12 + 시급 * 초과근무시간
def m(a,b,c) :
    return a/12+b*c
a=int(input('연봉'))
b=int(input('시급'))
c=int(input('초과근무시간'))
print('월급 :' ,m(a,b,c))














