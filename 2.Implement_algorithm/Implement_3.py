input_data = input()
row = int(input_data[1]) #c2를 입력 받았을 경우 input_data[1]이 2로 행이기 때문
column = int(ord(input_data[0]))-int(ord('a')) + 1 #0부터 시작하기 때문에 1을 더해줌
                            
#나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1),(-1,-1),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

#가지의 방향에 대해 각 위치로 이동이 가능한지 확인
result = 0

for step in steps:
    #이동하고자 하는 위치 확인
    next_row = row + step[0] #1
    next_column = column + step[1] #2

    #해당 위치로 이동이 가능하다면 카운트를 증가
    if next_row >= 1 and next_row <=8 and next_column >= 1 and next_column <= 8:
        result += 1
print(result)
