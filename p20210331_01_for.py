#반복문 : for
# for x in [1,2,3,4,5]:
#     print('python',x)

# data=['이선희','최불암','BTS']
# for x in data:
#     print(x)
# for x in [0,1,2]:
#     print(data[x])

#실습)0~9 출력
# n=[0,1,2,3,4,5,6,7,8,9]
# for z in n:
#     print(z)


#정수를 생성
#range(start,stop,step)
# print(list(range(10,101,1)))
# print(list(range(101)))
# print(list(range(10,20))) #start, stop

# for x in range(0,10,2):
#     print(x)

#합계를 구하기
# s=0 #합계를 저장할 변수
# for x in range(1,11) :
#     # s=x+s
#     s+=x # s = s+x
# print(s)

#실습)사용자에게 마지막 숫자를 입력받아 1부터 그 수까지 더하기
# s=0
# a=int(input('숫자입력'))
# for z in range(1,a+1) :
#    s+=z
# print(s)

#실습) 1부터 100까지 합이 2000이 넘을때의 수를 출력
# s=0
# for x in range(1,101):
#     s+=x
#     if s>2000:
#         break  #반복문을 종료할때
# print('x=',x,'s=',s)

#실습) 바보라는 글자가 발견되면 강퇴
# data = ['안녕','반가워','방가','바보','오늘만나']
# bad=['바보','멍청이']
# for z in data :
#     print(z)
#     if z in bad:
#         print('강퇴')
#         break
# print('바른말 사용')



#continue : 계속진행
# data=[3,4,6,8,7,10]
# for z in data:
#     if z%2==1 : continue
#     print(z)

#실습) 모든 점수 60이상 합격
# data=[65,45,95,55,70]
# for z in data :
#     if z>60 :
#         print(z,'합격')

#답
# data=[65,85,95,65,70]
# data=input('점수는?').split()
# # print(data)
# data=map(int,data)
# for z in data :
#     if z<60 :
#         print('불합격')
#         break
# else :
#     print('합격')
#실습) 모든 점수의 합계가 300점이 넘으면 합격
s=0
data=[65,45,95,55,70]
# data=input('점수는?').split()
# data=map(int,data)
for z in data :
    s+=z
    if s>=300 :
        print('합격')
        break
else :
    print('불합격')





















