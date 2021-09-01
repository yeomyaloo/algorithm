#피보나치 함수(Fibonacci Function)을 재귀함수로 구현

def fibo(x):
    #재귀함수가 무한루프를 돌지 않고 언제 멈출지에 대해서 명시해주는 것. 
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)
print(fibo(4))
