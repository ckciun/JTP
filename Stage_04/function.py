# f(x) = 2x + 3
# 수학과 다르게 입/출력 값이 없거나, 둘 중 하나만 있을수도 있다
# Form
"""
def <함수명> <매개변수>:
    수행 할 명령어
    return <리턴 값>
"""

# 입/출력 값이 모두 있는 함수

def f_sum(a, b):
    _result = a + b
    return _result

print(f_sum(1, 2))
print()

# 출력 값만 있는 함수

def f_say():
    return 'Hi'

print(f_say())
print()

# 입력 값만 있는 함수

def f_sum2(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

f_sum2(1, 2)
print()

# 입/출력 값이 모두 없는 함수

def f_say2():
    print('Hi')
    
print(f_say2())
print()

# 여러 개의 입력 값이 있는 함수

def f_multi_value(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(f_multi_value(1,2,3))
print()
# 여러 개의 출력 값이 있는 함수

def f_sum_and_mul(a, b):
    return a + b, a * b

print(f_sum_and_mul(2, 3))
print(f_sum_and_mul(2, 3)[0])
print(f_sum_and_mul(2, 3)[1])
print()

# 매개변수 기본값

def f_myself(name, age, man = True):
    print("나의 이름은 %s이고," % name)
    print("나이는 %d살입니다." % age)
    if man:
        print("나는 남자입니다.")
    else:
        print("나는 여자입니다.")
        
f_myself('Choi', 32)
print()

# 함수에서 전역 변수에 영향 주기

a = 1
def f_var(a):
    a += 1
    return a

a = f_var(a)
print(a)
print()

# 혹은

a = 1
def f_var2():
    global a
    a += 1

f_var2()
print(a)
print()

## 응용 ##
# Lamda 함수

# def add(a, b):
#     return a + b

add = lambda a, b : a + b
print(add(4, 6))
print()

l_mylist = [lambda a, b : a + b, lambda a, b : a * b]
print(l_mylist[0](3, 3))
print(l_mylist[1](3, 2))
print()
