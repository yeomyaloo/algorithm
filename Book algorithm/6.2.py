#n개의 원소 중 m개를 고른는 모든 조합을 찾는 알고리즘

def loop(n):
    lst= []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for m in range(k+1,n):
                    lst.append([i,j,k,m])
    print(lst)


n= int(input())
loop(n)

