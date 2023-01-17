def solution(n, m):
    answer = []
    
    if(n > m) : # n이 더 작게, m이 더 크게 만들기.
        a = n
        n = m
        m = a
    
    # 최대공약수
    for i in range(m,0,-1) :
        if (n%i == 0 and m%i == 0) :
            answer.append(i)
            break
    
    #최소공배수
    a = m
    while(a%n != 0) :
        a += m
    answer.append(a)
    
    return answer



def solution1(a, b):
    c, d = max(a, b), min(a, b) # max, min을 이용해 a, b 중 큰 값, 작은 값을 각각 c, d에 저장.
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t # 유클리드 호제법
    answer = [c, int(a*b/c)]

    return answer



# 8 12
# 8 16 24
# 12 24



n = 8
m = 12
print(solution(n,m))














# for i in range(10,1,-1) :
#     print(i)