# 구구단 만들기
""" 
함수 이름은?
    gugu

입력 받는 값은?
    1자리 숫자
    
출력 하는 값은?
    9개

결과 형식은?
    리스트 형식 
"""

n = int(input())

def gugu(n):
    #print(n)
    result = []
    # result.append(n * 1)
    # result.append(n * 2)
    # result.append(n * 3)
    # result.append(n * 4)
    # result.append(n * 5)
    # result.append(n * 6)
    # result.append(n * 7)
    # result.append(n * 8)
    # result.append(n * 9)
    i = 1
    while i < 10:
        result.append(n * i)
        i += 1
    return result

#print(gugu(2))
print(gugu(n))
