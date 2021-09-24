#보글 게임판에서 단어를 찾는 재귀 호출 알고리즘
dx = {-1,-1,-1,1,1,1,0,0}
dy = {-1,0,1,-1,0,1,-1,1}
word = input()

def hasWord(y,x, word):
    #시작 위치가 범위를 벗어날 경우 무조건 실패
    if y<0 and x<0 and y>4 and x>4:
        return False

    #첫 글자가 일치하지 않으면 실패
    if board[y][x] != word[0]:
        return False

    #첫 글자가 일치하고 단어의 길이가 1인 경우 성공
    if len(word) == 1:
        return True

    #안전한 8칸 검사. 인접한 이웃이 최대 8개씩 있기 때문.
    for i in range(0, i<8):
        nextY = y + dy[i]
        nextX = x + dx[i]
        
        #문자열의 첫 문자는 일치, 첫 문자를 제외하여 재귀함수 호출
        if hasWord(nextY,nextX,word[1]):
           return True
        
    return False
