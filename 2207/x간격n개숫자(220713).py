def solution(x, n) :
    
    answer = []
    a = x
    
    for i in range(n) :
        answer.append(x)
        x = x + a
        
    return answer

x, n = map(int, input().strip().split())

print(solution(x, n))