# 반복되는 변수 & 함수를 미리 정해놓은 틀
# Class 이름의 첫번째 글자는 대문자

# result1 = 0
# result2 = 0
# def add1(num):
#     global result1
#     result1 += num
#     return result1

# def add2(num):
#     global result2
#     result2 += num
#     return result2

# print(add1(3))
# print(add1(4))
# print()
# print(add2(3))
# print(add2(7))
# print()

# class Calculator:
#     def __init__(self):
#         self.result = 0
        
#     def add(self, num):
#         self.result += num
#         return self.result
    
# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print()
# print(cal2.add(3))
# print(cal2.add(7))
# print()

 # __init__ 없는 Class
class Fourcal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
        
    def add(self):
        result = self.first + self.second
        return result

a = Fourcal()
a.setdata(1, 2)
print(a.first, a.second)
print(a.add())
print()

# __init__ 있는 Class
class Fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
            
    def add(self):
        result = self.first + self.second
        return result

a = Fourcal(3, 4)
print(a.first, a.second)
print(a.add())
print()
