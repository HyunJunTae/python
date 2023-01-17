

##for i in range(10) :
##    print("Hello, World")
##
##
##
##
##list_1 = ['철수', '영희', '채린']
##for i in list_1 :
##    print("{}는 1반입니다".format(i))
##
##
##
##
##msg1 = "onggibot"
##for i in msg1 :
##    print(i)
##for i in msg1 :
##    print(i, end="")




##dict1 = {'옹기봇' : '010-1234-5678', '고추걸' : '010-3333-4444',
##         '김치워리어' : '010-9999-9999'}
##print(dict1)
##print(dict1.keys())
##print(dict1.values())
##print(dict1.items())
##
##for i in dict1 :
##    print(i, end=" ")
##print()
##
##for i in dict1.keys() :
##    print(i, end=" ")
##print()
##
##for i in dict1.values() :
##    print(i, end=" ")
##print()
##
##for i in dict1 :
##    print(dict1[i], end=" ")
##print()
##
##for i in dict1.items() :
##    print(i, end=" ")
##print()
##
##for i, k in dict1.items() :
##    print(i, k, end=" ")
##print()



##medal = { '한국' : [12,13,14], '일본' : [123,345,456],
##         '중국' : [1,2,3] }
##
##for i, k in medal.items() :
##    print("{}의 메달 개수 : 금{}개, 은{}개, 동{}개".format(i, k[0], k[1], k[2]))
##
##
##
##for i in medal.values() :
##    hap = i[0] + i[1] + i[2]
##    i.append(hap)
##    i[0] = 0
##    i[1] = 0
##    i[2] = 0
##print(medal)




##password = input("Input password : ")
##while password != "peace" :
##    password = input("Input password : ")
##print("로그인 성공")
##
##
##
##password = input("Input password : ")
##while True :
##    password = input("Input password : ")
##    if password == "peace" :
##        print("로그인 성공")
##        break





##s = "aiueoAIUEO"
##letter = input("Input letter : ")
##result = ""
##for i in letter :
##    if i not in s :
##        result = result + i
##
##print(result)
##        
##
##add = []
##add2 = 0
##for i in range(1, 101) :
##    if i % 3 != 0 :
##        add.append(i)
##        add2 = add2 + i
##
##print(add, add2)



##add = 0
##for i in range(1, 101) :
##    add = add + i
##    if add > 100 :
##        break
##print(add)
    














def gprint(score) :

    if score > 90 :
        print("A")
    elif 90 >= score > 80 :
        print('B')
    elif 80 >= score > 70 :
        print('C')
    elif 70 >= score > 60 :
        print('D')
    else :
        print("F")

score1= 95
gprint(score1)


scores = [100, 95, 85, 75, 65, 55, 45]

for i in scores :
    gprint(i)









    
