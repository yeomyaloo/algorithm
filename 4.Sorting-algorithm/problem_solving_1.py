#두 배열의 원소 교체
n, k = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort() #오름차순 정렬수행
b.sort(reverse = True) #내림차순 정렬수행


#첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a)) # 배열 A의 모든 원소의 합을 출력
