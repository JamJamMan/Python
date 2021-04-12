#딕셔너리 {}로함
# data={'a':10,'b':20,'c':30,'d':40}
# print(data['a'])


# data={'홍길동':20,'이순신':45}
# print(data['홍길동'],'살')
#
# data={'홍길동':[20,165.5],'이순신':45}
# print(data['홍길동'][0],'살',data['홍길동'][1],'cm')
# data={'홍길동':{'나이':20,'키':165.5},'이순신':45}
# print(data['홍길동']['나이'],'살',data['홍길동']['키'],'cm')
#
# data={1:['홍길동',20,165.5],2:['이순신',45,170.5]}
# print(data[2][0])
#
# #딕셔너리에 데이터 추가
# data={}
# data['홍길동']=20
# data['이순신']=[45,170.8]
# print(data)

#실습)컴퓨터언어를 입력받아 딕셔너리에 저장
#{'backend':'java','frontend':'html5'}
# lang={}
# back=input('backend언어는?')
# lang['backend']=back
# front=input('frontend언어는?')
# lang['frontend']=front
# print(lang)

#
data={1:'고질라',2:'귀멸의칼날',3:'더박스'}
print(list(data.keys()))
print(list(data.values())[2])


#set : 중복데이터 허용불가
asia ={'한국','중국','일본'}
asia.add('베트남')
asia.add('중국')
asia.remove('일본')
asia.update({'한국','홍콩','태국'})
print(asia)














