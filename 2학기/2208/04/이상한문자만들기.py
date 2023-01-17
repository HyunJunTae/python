def solution(s):

    answer = ''
    count = 0
    for i in s :
        
        if i == ' ' :
            count = 0
            answer = answer + i
            continue
        
        if count%2 == 0 and 97<=ord(i)<=122 : # 짝수자리를 대문자로
            answer = answer + chr(ord(i)-32)
        elif count%2 == 1 and 65<=ord(i)<=90 : # 홀수자리를 소문자로
            answer = answer + chr(ord(i)+32)
        else : # 안바꿔도 되는 애면 그대로
            answer = answer + i
            
        count = count + 1            
    
    return answer



def solution1(s):
    res = []
    for x in s.split(' '):
        word = ''
        for i in range(len(x)):
            c = x[i].upper() if i % 2 == 0 else x[i].lower()
            word = word + c
        res.append(word) 
    print(res)
    return ' '.join(res)
# 문자열도 인덱스로 접근 가능. upper lower 사용. join으로 리스트들을 문자열로 이어주기. 빈칸 한 칸씩 띄워서.

def solution11(s):
    res = ""
    for x in s.split(' '):
        for i in range(len(x)):
            c = x[i].upper() if i % 2 == 0 else x[i].lower()
            res = res + c
        res = res + " "
    return res

def solution2(s):
    answer = ''
    for word in s.split(" "):
        n = ''
        for i in range(len(word)):
            if i%2 == 0 :
                n += word[i].upper()
            else :
                n += word[i].lower()
        answer += (n + " ")
    return answer[0:-1]



s = "a b c  d   e    f     gabc de"
print(s)

print(solution1(s))



# a = "a b c  d   e    f     gabc"
# print(a.split())
# print(a.split(' '))
### 스플릿으로 쪼갤 때 빈칸 포함할건지 안할건지 선택 가능.