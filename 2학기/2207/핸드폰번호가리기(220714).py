# def solution(phone_number):
    
#     answer = ''
    
#     for i in range(len(phone_number) - 4) : # 01043687666
#         answer += '*'
    
#     answer += phone_number[len(phone_number)-4 : len(phone_number)]
        
#     return answer


# phone_number = input()

# print(solution(phone_number))




hyebin = "01072440039"

print(hyebin[-4:])

# 싱기한데요?
############ 문자열 인덱스 음수로 사용 가능



def solution(phone_number) :
    return '*'*(len(phone_number)-4) + phone_number[-4:]



s = "01012345678"

print(solution(s))