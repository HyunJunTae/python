#20221627 태현준 중간시험

print("*****문제1*****") #문제1 표시

print("사칙연산을 입력(x 연산자 y)") # 사칙연산 입력하라고 띄우기
num = input("") #사칙연산 입력
items = num.split() #입력받은 사칙연산 분할하여 리스트로 만들기
items.append(0) #리스트 마지막에 0 추가

if items[3] == 0 : #리스트 마지막이 0이면
    if items[1] == '+' : # 연산자가 + 이면
        print("{}{}{}={}".format(items[0], items[1], items[2], int(items[0]) + int(items[2]))) # +값으로 출력
    elif items[1] == '-' : # 연산자가 -이면
        print("{}{}{}={}".format(items[0], items[1], items[2], int(items[0]) - int(items[2]))) # -값으로 출력
    elif items[1] == '*' : #연산자가 *이면
        print("{}{}{}={}".format(items[0], items[1], items[2], int(items[0]) * int(items[2]))) # *값으로 출력
    elif items[1] == '/' : #연산자가 /이면
        print("{}{}{}={:.3f}".format(items[0], items[1], items[2], int(items[0]) / int(items[2]))) # /값으로 출력
    else : #그 외에는
        print("잘못 입력!!") #잘못 입력!! 출력
else : #그 외에는
    print("잘못 입력!!") #잘못 입력!! 출력



print("*****문제2*****") #문제2 표시

a = ( (202201, '최양업', '010-1234-4500'), (202202, '정약용', '010-2230-6540'), (202203, '김대건', '010-3232-7788') ) #튜플 만들기

dict = {a[0][0] : a[0][2], a[1][0] : a[1][2], a[2][0] : a[2][2]} # 튜플 이용해서 사전 개체 만들기

dict[a[0][0]] = "010-1234-4500 4.3" #사전 0번항 value 수정
dict[a[1][0]] = "010-2230-6540 3.9" #사전 1번항 value 수정
dict[a[2][0]] = "010-3232-7788 4.25" #사전 2번항 value 수정

b, c, d, e = input("").split() #학번 이름 전화번호 학점 입력받은 후 split으로 분할

dict[b] = d + " " + e #분할한 것들을 사전에 추가

print(dict) #사전 출력