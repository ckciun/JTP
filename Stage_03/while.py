# 반복문
# 같은 명령을 여러번 수행해야 할 경우 사용
# 조건이 True일 경우 계속해서 반복 수행
# 조건이 False일 경우 중지

_count = 0
while _count < 10:
    print(_count)
    _count += 1
    if _count == 10:
        print('Stop')
print()

# break
# 조건이 True여도 특정 조건을 만족했을 경우 반복 중지

_num = 0
while _num < 100:
    print(_num)
    _num += 1
    if _num == 6:
        print('Stop')
        break
print()

# continue
# 반복 수행 중 continue를 만나면 즉시 반복 시작 부분으로 돌아감

_a = 0
while _a < 10:
    _a += 1
    if _a % 2 == 0:
        continue
    print(_a)
print()
