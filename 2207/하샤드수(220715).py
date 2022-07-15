def solution(x):
    
    a = x
    h_num = 0
    
    while True : # 13
        h_num = h_num + (x % 10)
        x = x - (x % 10)
        if (x == 0) :
            break
        x = x / 10
        
    if ((a % h_num) == 0) : 
        answer = True
    else :
        answer = False
        
    return answer


def solution1(x) :
    for i in str(x) :
        h_num = h_num + int(i)
    return x % h_num == 0    
## 정수 x를 str(x)를 해서 문자열로 바꿔준 후 다시 int(x)로 정수로 바꿔서 한 자리씩 더해주기.

def solution2(x) :
    return x % sum([int(i) for i in str(x)]) == 0
## str(x)를 해서 만든 문자열에서 한 자리씩 가져와서 리스트를 만든 후 sum 함수로 원소 다 더해주고 ~~~~~~~.


print(solution(int(input())))