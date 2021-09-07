#1부터 n까지의 합을 계산하는 반복함수와 재귀함수

def recursiveSum(n):
    if n == 1:
        return 1
    else:
        return n+recursiveSum(n-1)
    
n = int(input())

print(recursiveSum(n))
