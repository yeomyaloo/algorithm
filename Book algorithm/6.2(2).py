def pick(n, picked,toPick):
    ##기저 사례: 더 고를 원소가 없을때 고른 원소출력
    if(toPick==0):
        print(picked)
        return
    ## picked마지막숫자 참고하여 고를수있는 가장 작은 번호를 계산한다

    try:
        smallest = picked[-1] +1
    except:
        smallest = 1

    ##이 단계에서 원소 하나를 고른다
    for next in range(smallest,n):
        picked.append(next)
        pick(n,picked, toPick-1)
        del picked[-1]
    
pick(5,[],2)
