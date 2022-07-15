price1 = 2000
price2 = 3000
price3 = 3500


f=open("C:/Users/user/OneDrive/바탕 화면/Python/기인프 과제/daily.txt", 'r') #판매량 file
s= f.readlines() #리스트
for num in s : #한 줄씩 가져옴
    num = num.split()
    a = int(num[0])
    latte = int(num[1])
    capu= int(num[2])
    total = a * price1
    total = total + latte*price2
    total = total + capu*price3
print('월매출액은 {}원'.format(total))
f.close() 