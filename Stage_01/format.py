# String Formating

a = "I eat %d apples." % 3
print(a)
print()

# Formating 하지 않은 경우

b = "I eat " + str(3) + " aplles."
print(b)
print()

# 변수 사용하기

number = 10
day = "three"
c = "I eat %d aplles. So i was sick for %s days." % (number, day)
print(c)
print()

# {}사용
# {}를 변수형식으로 사용할 경우, format 순서 상관없음,
# 변수 형식이 아닐 경우, 순차적으로 대입
# {}가 .format 인자보다 많으면 오류 발생
# .format인자가 {}에 순차적으로 대입되기 때문에
# .format인자가 {}보다 많아도 오류 발생 X

d = "I eat {} apples. So i was sick for {} days.".format(3, "three")
print(d)
print()

e = "I eat {num} aplles. So i was sick for {day} days.".format(day="three", num=3)
print(e)
print()

# Python v3.6부터 사용 가능한 Formating

name = "Python"
f = f"My name is {name}"
print(f)
print()

# 정렬과 공백
# 10칸 공백 넣기
g = "%10s" % "hi"
print(g)
print()

# 소수점 표현
# 0.2
# 0은 간격 2는 소수점 자리

h = "%0.2f" % 3.141592
print(h)
print()

