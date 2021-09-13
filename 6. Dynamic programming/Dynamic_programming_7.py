import sys
input = sys.stdin.readline

for tc in range(int(input())):
    #금광 정보 입력
    n, m = map(int,input().split())
    array = list(map(int,input().split()))

    #다이나믹 프로그래밍을 위한 2차원 DP테이불 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m]) #쭉 입력받은 것을 2차원 배열로 담기 위한 작업 m단위로 슬라이싱해서 dp 테이블에 2차원 테이블로 넣어줄 수 있게 한다.
        index += m
    #다이나믹 프로그래밍 진행
    for j in range(1, m): #열 확인
        for i in range(n): #열마다 행 확인
            #왼쪽에서 위에서 오는 경우
            if i == 0: #인덱스가 벗어나는 경우
                left_up = 0
            else:
                left_up = dp[i-1][j-1]

            #왼쪽 아래에서 오는 경우
            if i == n - 1: #인덱스가 벗어나는 경우
                left_down = 0
            else:
                left_down = dp[i+1][j-1]

            #왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)
