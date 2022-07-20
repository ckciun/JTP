# 특정 값의 True, False 여부를 판단
# 조건문에서 Ture 상태일 때 명령어 실행
# False 상태일 땐 실행하지 않음

# Python의 참과 거짓
# "Python", [1, 2, 3], 숫자 1
# 문자형이나 list등에 값이 존재할 경우 참으로 판단
# " ". [ ], ( ), { }, 숫자 0, None(타 언어의 null값)
# 자료형에 값이 없는 경우 거짓으로 판단

a = "HI"

if a:
    print(a)
print()
    
b = " "

if b:
    print(b)
print()

c = [1, 2, 3, 4]

while c:
    c.pop()
    print(c)
print()
