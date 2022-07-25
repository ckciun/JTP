# 만약에 ~ 하면
# 조건이 Ture일 때 실행할 명령어
# 조건이 False일 때 실행할 명령어

a = False

if a:
    print('True')
    print()
else:
    print('False')
    print()
    
# and(&), or(|), not(!) 연산 가능

a = 0
b = 1

if a or b:
    print('True')
    print()
else:
    print('False')
    print()
    
# if in & if not if

if 1 in [1, 2, 3]:
    print('True')
    print()
else:
    print('False')
    print()
    
if 1 not in [1, 2, 3]:
    print('True')
    print()
else:
    print('False')
    print()
    
# elif
# 조건이 True와 False가 아닐 경우

if a:
    print('True')
    print()
elif b:
    print('elif')
    print()
else:
    print('False')
    print()

# Python의 조건부 표현식

score =70

if score >= 60:
    message = 'success'
else:
    message = 'failure'
print(message)
print()

# if문을 한 줄로 표현

message = 'success' if score >= 60 else 'failure'
print(message)
print()
