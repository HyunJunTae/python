error = False

print("사칙연산을 입력(x 연산자 y)") # 사칙연산 입력하라고 띄우기
num = input("") #사칙연산 입력


#연산자 형식 오류 체크
L = num.split()
if len(L) != 3 :
    error = True
    
#피연산자 오류 체크
if error == False :
    a, b, c = num.split()
    if a.isdigit() == False :
        error = True
    if c.isdigit() == False :
        error = True
    # if a != int(a) and b != int(b) :
    #     error = True


#연산자 오류 체크
if error == False :
    연산자 = ["+", "-", "*", "/"]
    if b not in 연산자 :
        error = True


if error == True :
    print("잘못입력!")

if error == False:
    a = int(a)
    c = int(c)
    if b == "+" :
        print("{} {} {} = {}".format(a, b, c, a+c))
    elif b == "-" :
        print("{} {} {} = {}".format(a, b, c, a-c))
    elif b == "*" :
        print("{} {} {} = {}".format(a, b, c, a*c))
    elif b == "/" :
        print("{} {} {} = {}".format(a, b, c, a/c))