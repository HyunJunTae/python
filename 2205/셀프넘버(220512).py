##셀프넘버 프로그램. 첫 수 33. 다음 수는 33 + 3 + 3 = 39. 그 다음은 39 + 3 + 9 = 51. .... 이런 수가 아닌 수를 셀프넘버라고 함.
## 셀프넘버 : 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97.....



# def selfnum() :
#     a = list(range(1,10001)) # 1부터 10000까지 숫자 a에 저장
    
#     for i in a : # a 가져와서 1부터 10000까지 반복문 실행.
        
#         while i <= 10000 :
#             n_a = list(str(a[i])) # a의 숫자 i를 str로 만들어서 쪼개기. i = 301이면 n_a = ['3', '0', '1']
            
#             for j in n_a : # n_a 길이만큼, 즉 i의 자릿수만큼 반복
#                 i = i + int(j) #숫자 i에 더해주기. 이걸 하면 i가 셀프넘버 공식을 한 다음 숫자가 됨. 31 -> 39.
            
#             if i in a :
#                 a.remove(i)

#     print(a)

# selfnum()


# b = list("301")
# print(b)



a = list(range(1,10001)) # 1부터 10000까지 숫자 a에 저장

for i in a : # a 가져와서 1부터 10000까지 반복문 실행.
    
    k = i
    
    while k <= 10000 :
        n_a = list(str(a[k])) # a의 숫자 i를 str로 만들어서 쪼개기. i = 301이면 n_a = ['3', '0', '1']
        
        for j in n_a : # n_a 길이만큼, 즉 i의 자릿수만큼 반복
            k = k + int(j) #숫자 i에 더해주기. 이걸 하면 i가 셀프넘버 공식을 한 다음 숫자가 됨. 31 -> 39.
        
        if k <= 10000 and k in a :
            a.remove(k)

print(a)