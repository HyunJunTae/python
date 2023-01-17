def solution(arr):
    answer = 0
    for i in arr :
        answer = answer + i
    return answer/len(arr)


def solutioin1(list):
    return (sum(list) / len(list))
# 리스트에서 sum, len 사용 가능.


def solution2(list):
    # 함수를 완성해서 매개변수 list의 평균값을 return하도록 만들어 보세요.
    if len(list) == 0:
        return 0 # 리스트가 비어있는 경우 예외처리.

    return sum(list) / len(list)


arr = [1,2,3,4]

print(solution(arr))





## 추가. 파이썬에소 특정 요소 개수 구할 때.
i = [1,1,3,4,5,3,3,7,6,8,9,3,2,5,9]

print(i.count(3)) #리스트i에 요소3의 개수 구할때 