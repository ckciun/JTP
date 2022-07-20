# 특정 값을 Memory의 임의 주소에 저장한다

a = [1, 2, 3]

b = a

a[1] = 4

print(a)
print(b)
print(id(a))
print(id(b))
print(a is b) # a와 b가 같은 Memory 주소를 바라보고 있는지 확인
print()
# b에 a의 Memory 주소를 할당했기 때문에
# a의 값을 수정하면 b의 값도 동일하게 바뀐다

# Memory 주소가 아닌 변수의 값만 복사
# 동일 객체가 아니기 때문에 c 변수의 값을 변경해도 d 변수의 값은 변경되지 않는다
# Slicing이 아닌 Copy Library 사용해도 동일한 효과
# import copy
c = [1, 2, 3, 4]
d = c[:]
# d = copy(c)

print(c)
print(d)
print(id(c))
print(id(d))
print(c is d)
print()

c[1] = 4
print(c)
print(d)
print()

## 응용 ##
# 여러 변수 한 번에 만들기
e, f = ('Hello', 'World!')
# (e, f) = ('Hello', 'World!')
# (e, f) = 'Hello', 'World!'
# 괄호 생략 가능
# Tuple 말고 List 형식으로도 가능
print(e)
print(f)
print()

# 여러 변수에 같은 값 넣기

g = h = 'Python'
print(g)
print(h)
print(id(g))
print(id(h))
print(g is h)

## Python에서만 가능한 기능 ##
# 두 변수의 값을 서로 바꿀 때, 
i = 3
j = 5
tmp = j
j = i
i = tmp
print(i)
print(j)
print()

# Python 에서는
k = 3
l = 5
k, l = l, k
print(k)
print(l)
print()
