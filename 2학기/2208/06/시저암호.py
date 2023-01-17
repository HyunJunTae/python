def solution(s, n):
    
    answer = ''
    
    for i in s :
        # 65 90 / 97 122
        # 대문자 경우
        if (65 <= ord(i) <= 90) :
            if (ord(i) + n > 90) :
                answer += chr(ord(i) - 26 + n)
            else :
                answer += chr(ord(i) + n)
        # 소문자 경우
        elif (97 <= ord(i) <= 122) :
            if (ord(i) + n > 122) :
                answer += chr(ord(i) - 26 + n)
            else :
                answer += chr(ord(i) + n)
        # 소문자 대문자 다 아닌 경우 (공백 등)
        else :
            answer += i
    
    return answer


def solution1(s, n): # 이건 내가 만든거 히힣
    
    answer = ''
    
    for i in s :
        # 65 90 / 97 122
        # 대문자 경우
        if (65 <= ord(i) <= 90) :
            answer += chr(ord(i) - 26 + n) if ord(i) + n > 90 else chr(ord(i) + n)
        # 소문자 경우
        elif (97 <= ord(i) <= 122) :
            answer += chr(ord(i) - 26 + n) if ord(i) + n > 122 else chr(ord(i) + n)
        # 소문자 대문자 다 아닌 경우 (공백 등)
        else :
            answer += i
    
    return answer


def solution2(s, n):
    answer = ''
    for i in s:
        if i:
            if i >= 'A' and i <= 'Z':
                answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
            elif i >= 'a' and i <= 'z':
                answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
            else : answer += ' '
    return answer



s = input("s : ")
n = int(input("n : "))

print(solution1(s, n))