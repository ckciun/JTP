# 파일 읽고 쓰기
# r = 읽기 모드 - 파일을 읽기
# w = 쓰기 모드 - 파일에 내용을 쓰기 
# a = 추가 모드 - 파일의 마지막에 새로운 내용을 추가

# 어떤 동작을 수행하던 열었던 파일은 반드시 닫아줘야 함

## 쓰기 모드
# 기존 파일에 내용 덮어쓰기
# 절대 경로
# macOS f = open('/Users/~/test.txt', 'w')
# Windows f = open('C:\~)
# 상대 경로(현재 작성중인 스크립트 파일이 들어있는 Directory에 자동으로 생성
# f = open('test.txt', 'w', encoding='UTF-8')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()
# 기존 파일 마지막에 내용 추가하기
# 'w' 대신 'a' 사용

## 읽기 모드
# 한 줄 읽기
# f = open('test.txt', 'r', encoding='UTF-8')
# line = f.readline() # 1줄씩 읽는 함수
# print(line)
# f.close()

# 여러 줄 읽기
# 반복문 활용
# f = open('test.txt', 'r', encoding='UTF-8')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# f.close()

# 함수 활용
# f = open('test.txt', 'r', encoding='UTF-8')
# _lines = f.readlines()
# for line in _lines:
#     print(line, end="") #공백 제거
#     # end="" or strip("\n")
# f.close()

# readline(s)는 파일을 한 줄 씩 읽어서
# List 형식으로 저장
# List 형식이 아닌 파일을 통째로 읽어오는 방법
f = open('test.txt', 'r', encoding='UTF-8')
data = f.read()
print(data)
f.close()

# 파일 open 후 close 하지 않는 방법
with open('test2.txt', 'w') as f:
    f.write("Welcome To Python!")