# 전체 게시물 숫자와 한 페이지에 표시될 게시물 갯수를 입력했을 때
# 필요한 페이지 수를 출력
""" 
함수 이름
    totalpage
    
입력 받는 값
    전체 게시물 수 = m
    한 페이지에 표시될 게시물 수 = n
    
출력 하는 값
    총 페이지 수
 """
 
def totalpage(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1
 
print(totalpage(5, 10))
print(totalpage(15, 10))
print(totalpage(25, 10))
print(totalpage(30, 10))