def solution(n):
    answer = ''
    count = 0
    for i in range(n) :
        if (count == 0) :
            answer += '수'
            count += 1
        else :
            answer += '박'
            count -= 1
        
    return answer

def solution1(n): # 내가만듬
    answer = ''
    for i in range(int(n/2)) :
        answer += '수박'
    if (n%2==1) :
        answer += '수'
    return answer

def solution2(n): # 내가만듬
    return '수박'*int((n/2)) if n%2 == 0 else '수박'*int((n/2)) + '수'

def solution3(n):
    return "수박"*(n//2) + "수"*(n%2)


def solution4(n):
    s = "수박" * n
    return s[:n]
    


n = int(input("n : "))
print(solution1(n))

