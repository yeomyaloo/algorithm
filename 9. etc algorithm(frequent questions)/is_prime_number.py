#소수 판별 함수(1은 소수가 아니기때문에 2이상의 자연수부터)
def is_prime_number(x):

    #2부터  x-1 까지 모든 수를 확인하면서 소수 판별 진행
    for i in range(2,x):

        #x가 해당 수로 나누어 떨어지는 경우 소수가 아니기에 False 리턴해준다.
        if x%i == 0:
            return False

    #자기 자신과 1로만 나누어지는 수이기 때문에 소수 True 리턴
    return True

