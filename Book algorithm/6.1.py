#1부터 n까지의 합을 계산하는 반복함수와 재귀함수

n = int(input())
sum_n = 0
for i in range(1, n+1):
    sum_n += i

print(sum_n)
