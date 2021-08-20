# 반복문을 이용해서 구한 팩토리얼
def factorial_iterative(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result


# 재귀적으로 구현한 팩토리얼
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print('반복적으로 구현한 팩토리얼: ',factorial_iterative(5))
print('재귀적으로 구현한 팩토리얼: ',factorial_recursive(5))
