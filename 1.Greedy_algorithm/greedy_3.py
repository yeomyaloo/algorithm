data = input()

#첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)): #1부터 data 길이까지
    num = int(data[i])

    #두 수 중에서 하나라도 0또는 1인 경우는 곱하기보다는 더하기 수행을 해주는 것이 낫다.
    if num <= 1 or result <=1:
        result += num
    else:
        result *= num
print(result)
