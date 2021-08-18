#거스름 돈: 답안 예시

n = 1260
count = 0

array = [500,100,50,10]

for coin in array:
    count += n//coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin #나눈 값이 나머지 값으로 갈 수 있게 1260-1000 = 260인 경우를 반
print(count)
