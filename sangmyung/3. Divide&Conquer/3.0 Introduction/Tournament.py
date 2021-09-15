#tournament

def tournament(n, team):
    for i in range(n,n > 1,i/2):
        for j in range(0, j<i, j+2):
            win[j/2] = winner(team[j],team[j+1])
            win = team
    return win[0]
