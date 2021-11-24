import math

#소수 판별 함수(2이상의 자연수에 대해서)
def is_prime_number(x):
    
    #2부터 x의 제곱근까지 모든 수를 확인하며
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
        
    return True

