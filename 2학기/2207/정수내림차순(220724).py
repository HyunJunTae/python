def solution(n):
    list = []
    
    while (True) :
        num = n % 10
        list.append(num)
        
        n -= num
        n /= 10
        
        if (n == 0) :
            break

    list.sort(reverse = True)
    
    print(list)
    answer = 0
    for i in list :
        answer += i
        answer *= 10
    answer /= 10
    
    return int(answer)


def solution1(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))
# n을 str로 만들어서 list로 하나씩 끊고 sort로 정렬해서 join으로 다시 리스트에서 문자열로 합치고 int로 바꿔서 return




n = int(input("Input num : "))

print(solution(n))