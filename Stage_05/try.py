# 오류가 발생했을 경우 수행할 동작을 정의

################################
#try:
    # 오류가 발생할 수 있는 구문
#except Exception as e:
    # 오류 발생
#else:
    # 오류가 발생하지 않음
#finally:
    #무조건 마지막에 실행
################################

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

# ex)
# try:
#     f = open('none', 'r')
# except Exception as e:
#       # Error 이름을 모를경우 Exception 사용
#       # Exception이 모든 Error를 포괄
#     print(str(e))
#       # 오류 회피
#       # Pass도 가능
# else:
#     data = f.read()
#     print(data)
# finally:
#     f.close()

## Error 발생시키기
# 값을 변형시켜서 사용해야 할 경우에
# 고의로 Error를 유발시킴

# ex)
class Bird:
    def fly(self):
        raise NotImplementedError
    
class Eagle(Bird):
    def fly(self):
        print("Eagle")
eagle = Eagle()
eagle.fly()
