a, b, c = map(int, input().split())
d = a*b-c
if(d<0) :
    print(0)
else :
    print(d)
    
# a,b,c=map(int,input().split());print(max(0,a*b-c))