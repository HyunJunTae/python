def solution(n):
    
    answer = []
    
    for i in str(n) :
        answer.insert(0, int(i))

    return answer


def solution1(n):
    return list(map(int, reversed(str(n))))
# reversed : 순서가 있는 개체(리스트, 튜플, 문자열)를 뒤집어서 'reversed'개체로 return하는 함수.
# map : 리스트의 요소를 지정된 함수로 처리해주는 함수. 여기에선 int로 처리함.
# reversed(str(n))으로 12345를 문자열로 만들고 뒤집어서 54321 reversed 개체로 만든 후, 
# map으로 int형으로 처리해준 다음 리스트에 넣어줌.



n = int(input("Input : "))
print(solution(n))