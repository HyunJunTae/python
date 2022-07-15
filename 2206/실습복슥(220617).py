

##이름, 성 = input("영문이름?(이름 성) : ").split(" ")
##년, 월, 일 = input("생일? (yyyy/mm/dd) : ").split("/")
##
##
##
##아이디 = 성[-1]
##
##for i in range(1, (len(이름)) ) :
##    아이디 = 아이디 + 이름[i]
##            
##비밀번호 = 'mm' + 년[3] + 월 + 일




##medals= [ ['Austria',0,2,1], ['Canada',4,8,5], ['China',5,0,1],
##['France',0,4,5], [ 'Germany',1,1,2], ['Japan',1,1,0],
##['Korea',5,3,1], ['Norway',4,4,7], ['Russia',4,6,4],
##['Viet Nam',1,1,5] ]
##
##
##for i in medals :
##    i.append(i[1]+i[2]+i[3])
##
##for i in medals :
##    print(i)
##print("")
##print(medals)
    



##print("문제2")
##
##print("입력하세요")
##a = input("")
##b = "~!@#$%^&*-_+=(){}[]:;?.,<>"
##c = ""
##
##
##for i in a:
##    if i not in b :
##        c = c + i
##    if i in b :
##        c = c + " "
##
##
##print("**특수문자를 공백으로 바꾼 새 문자열")
##print(c)
##
##
##d = c.split(" ")
##
##f = []
##
##for i in d :
##    if i != "" :
##        f.append(i)
##
##e = {}
##
##
##
##for i in f :
##    if i not in e :
##        e[i] = 1
##    else :
##        e[i] = e[i] + 1
##
##
##print("** 단어별 빈도수")
##for i, j in e.items() :
##    print("{:10}{:2}".format(i, j))








# 실습6

##menu = {"그린티라떼" : 3000, "모카라떼" : 3500,
##        "아메리카노" : 2000, "카페라떼" : 2500 }
##
##a = "adsaf"
##
##while (a != "") :
##    a = input("메뉴 : ")
##
##    if a == "" :
##        break
##
##    elif a in menu :
##        print("{}원".format(menu[a]))
##    elif a not in menu :
##        print("없는 메뉴!")





f=open("C:/Users/user/OneDrive/바탕 화면/Python/기인프 데이터/data.txt", 'r')
a = f.read()
print("**읽은 문자열")
print(a)

b = "~!@#$%^&*-_+=(){}[]:;?.,<>"

c = ""
for i in a :
    if i not in b :
        c = c + i
    elif i in b :
        c = c + " "
print("**새 문자열") 
print(c)

d = c.split(" ")

e = []
for i in d :
    if i != "" :
        e.append(i)

f = {}

for i in e :
    if i not in f :
        f[i] = 1
    elif i in f :
        f[i] = f[i] + 1

print("**단어별 빈도수")
for i, j in f.items() :
    print("{:10}{:2}".format(i,j))
























