# 수학의 집합을 Python으로 구현한 자료형
# 각 집합의 값은 중복될 수 없다
# 정해진 순서(index)가 없다

# list를 set()형태로 만들거나
# 값을 중괄호{}로 감싼다

a = set([1, 2, 3])
b = {1, 2, 3}

print(a)
print(b)
print()

## 응용 ##
# list의 중복되는 값을 삭제

l = [1, 1, 2, 2, 3, 3]
newlist = list(set(l))
# set에선 중복되는 값을 허용하지 않기 때문에,
# 값이 중복되는 list를 set 자료형으로 만들고,
# 중복 된 값이 지워진 set 자료형을 다시 list 자료형으로 변경
print(newlist)
print()

# 교집합
# 두 집합의 값 중 겹치는 값만 출력
s1 = set([1, 2, 3, 4, 5, 6])
s2 = {4, 5, 6, 7, 8, 9}
print(s1 & s2)
print(s1.intersection(s2))
print()

# 합집합
# 두 집합의 값을 합한 결과 출력
# 이 때도, set의 특성상 중복되는 값은 출력되지 않음
print(s1 | s2)
print(s1.union(s2))
print()

# 차집합
# 두 집합의 값 중 기준이 되는 집합의 값을 제외한 값을 제거
# 이 때, 교집합 값도 제거된다
print(s1 - s2)
print(s1.difference(s2))
print()

# set에 값 추가하기
# 하나의 값만 추가할 경우
s1.add(7)
print(s1)
# 여러 개의 값을 추가할 경우
s1.update([8,9])
print(s1)
print()

# 값 제거하기
s1.remove(9)
print(s1)