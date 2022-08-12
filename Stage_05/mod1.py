# module 1

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

# __name__
# 다른 Python 실행 파일에서 해당 모듈을 실행할 때가 아닌
# 모듈 자체적으로 실행할 때만 동작하는 명령
# __name__ == "__main__" 인 이유는
# Module을 Import하면 해당 Module 실행 파일의 이름을 가져오기 때문
# 즉 "__main__" 는 자기 자신을 의미함

if __name__ == "__main__":
    print(add(2, 4))
    print(sub(8, 7))
    print(mul(2, 4))
    print(div(6, 3))