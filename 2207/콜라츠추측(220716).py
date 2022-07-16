def solution(num):
    answer = 0
    
    while(answer <= 500 and num != 1) :
        if (num%2 == 0) :
            num /= 2
        elif (num%2 == 1) :
            num = num*3 + 1
        answer += 1
        
    if (answer > 500) :
        answer = -1
        
    return answer


def solution1(num) :
    
    for i in range(500) :
        if (num%2 == 0) :
            num /= 2
        elif (num%2 == 1) :
            num = num*3 + 1
            
        if (num == 1) :
            return i + 1
    
    return -1

def solution2(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1
        



num = 6
print(solution(num))