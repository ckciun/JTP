# 상속
# 기존 Class의 기능을 이어받아 새로운 기능 추가

class Fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
            
    def add(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
class MoreFourcal(Fourcal):
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result
    
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourcal(4, 5)
print(a.first, a.second)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())
print(a.pow())
print()

# Method Overriding
# 부모와 자식 Class에 동일한 함수가 있으면
# 자식 Class의 함수가 우선순위

class ChangeFourcal(Fourcal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = ChangeFourcal(4, 0)
print(a.div())
print()
