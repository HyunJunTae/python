def solution(arr):
    
    min = arr[0]
    index = 0
    
    for i in range(1, len(arr)) :
        if (min > arr[i]) :
            min = arr[i]
            index = i
            
    arr.pop(index)
    
    if (len(arr) == 0) :
        return [-1]
    return arr


def solution1(arr) :
    
    arr.remove(min(arr))
    
    if (len(arr) == 0) :
        return [-1]
    return arr

arr = [4,1,2,3]
print(solution1(arr))