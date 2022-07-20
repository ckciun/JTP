# key와 value가 한 쌍으로 묶여있는 list
# 중괄호 사용 {}
# 연관 배열(Associative array) or Hash라고 부르기도 한다
# Dictionary를 만들 때, value는 중복되어도 되지만 key는 중복되면 안된다

dic = {
    'name' : '홍길동',
    'age' : '15',
    'job' : '의적'
}

print(dic)
print(dic['name'])
print()

# Dictionary에 key 추가하기

dic['cop.'] = '활빈당'

print(dic)
print(dic['cop.'])
print()

# Dictionary에 key 삭제하기

del dic['age']
print(dic)
print()

# key만 확인하기

print(dic.keys())

# value만 확인하기

print(dic.values())

# 각 key와 value 한 쌍을 tuple 형태로 출력

print(dic.items())
print()

# For 반복문 응용

for k in dic.keys():
    print(k)
print()

for v in dic.values():
    print(v)
print()
    
for k, v in dic.items():
    print("Key : {}, Value : {}".format(k, v))
print()

## 응용 ##
# .get을 사용하면 Key가 없을경우 None 출력
print(dic.get('name'))
print(dic.get('birth'))
print(dic.get('birth','Key 없음'))
print()
# in을 통해서 Dictionary안에 key가 있는지 탐색
print('birth' in dic)
print()

# Dictionary 초기화하기

dic.clear()
print(dic)