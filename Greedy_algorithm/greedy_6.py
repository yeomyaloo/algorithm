h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k): #시, 분, 초를 전부 더해버리고 그 안에 3이 들어있나 체크하는 
                count += 1
print(count)
