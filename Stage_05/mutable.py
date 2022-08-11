# Immutable
# 변하지 않는 자료형
# 정수, 실수, 문자열, 튜플

# ex)
a = 1
def vartest(a):
    a = a + 1
    
vartest(a)
print(a)
# result = 1

# Mutable
# 변할 수 있는 자료형
# 리스트,딕셔너리, 집합

# ex)
b = [1, 2, 3]
def vartest2(b):
    b = b.append(4)
    
vartest2(b)
print(b)
# result = [1, 2, 3, 4]