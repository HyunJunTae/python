def test(score) :
    if score >= 90 :
        return 0
        
    elif 90 > score >= 80 :
        return 1
        
    elif 80 > score >= 70 :
        return 2
        
    elif 70 > score >= 60 :
        return 3

    else :
        return 4
        

list = [0,0,0,0,0]


for i in range(10) :
    score = int(input("성적을 입력하세요 : "))
    a = test(score)
    list[a] = list[a] + 1

  
print("90점 이상",list[0],"명")
print("80점 이상",list[1],"명")
print("70점 이상",list[2],"명")
print("60점 이상",list[3],"명")
print("그 외",list[4],"명")
    
