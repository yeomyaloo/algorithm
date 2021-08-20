a = input()
lst = []
int_num = 0

for i in a:
    if i.isalpha(): #알파벳인 경우를 알려주는 함수
        lst.append(i)
    else:
        int_num += int(i) #문자로 숫자를 입력받았기 때문에 형변환해주어 int_num함수에 넣어준다.

lst.sort() #알파벳만 모아둔 리스트의 알파벳을 오름차순으로 정렬해준다.


#숫자가 하나라도 존재할 경우엔 가장 뒤에 삽입해주는 과정
if int_num != 0:
    lst.append(str(int_num))

print("".join(lst))
    
