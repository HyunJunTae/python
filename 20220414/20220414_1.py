# s = input('??')
# count = 0
# count_list = []

# for i in s :
#     if i in 'aeiouAEIOU' :
#         count += 1
#         count_list.append(i)
#         print(i,"!!!")
#     else : 
#         print(i)

# print("모음들 : {}".format(count_list))
# print("모음 개수 : {}".format(count))

# contacts = {"Kim" : "010-1234-5678", "Park" : "010-4312-6785", "Lee" : "010-4132-7565"}

# print("1")
# for i in contacts :
#     print(i)

# print("2")
# for name in contacts :
#     print(name)

# print("3")
# for i in contacts.keys() :
#     print(i)

# print("4")
# for i in contacts.keys() :
#     print(contacts[i])

# print("5")
# for i in contacts.values() :
#     print(i)

# print("6")
# for i in contacts.items() :
#     print(i)
    
# print("7")
# for i,k in contacts.items() :
#     print(i,k)


# D = {"Austria" : [0,2,1], "Canada": [4,8,5], "China" : [5,0,1]}

# for i in D :
#     print(D)
    
# for i in D.items() :
#     print(i)

# for country, medal in D.items() :
#     print("{}의 메달 개수 : 금{}, 은{}, 동{}".format(country, medal[0], medal[1], medal[2]))
    
# for i in D.keys() :
#     print("{}의 메달 개수 : {}".format(i, D[i]))


for x in range(2,7) :
    for y in range(1,10) :
        print( "{}*{} = {}".format(x, y, x*y), end=' ' )
    print()
    
    
print("---------------------------------------------------------------------")
for x in range(2,7) :
    print( '{}*{} = {:2}'.format(x, 1 , x*1) , end=' ' )
    print( '{}*{} = {:2}'.format(x, 2 , x*2) , end=' ' )
    print( '{}*{} = {:2}'.format(x, 3 , x*3) , end=' ' )
    print( '{}*{} = {:2}'.format(x, 4 , x*4) , end=' ' )
    print( '{}*{} = {:2}'.format(x, 5 , x*5) , end=' ' )
    print( '{}*{} = {:2}'.format(x, 6 , x*6) , end=' ' )
    print( '{}*{} = {:2}'.format(x, 7 , x*7) , end=' ' )
    print( '{}*{} = {:2}'.format(x, 8 , x*8) , end=' ' )
    print( '{}*{} = {:2}'.format(x, 9 , x*9) , end=' ' )
    print()