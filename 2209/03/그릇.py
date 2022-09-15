g = input()
n = 10
for i in range(len(g)-1) :
    if (g[i] == g[i+1]) :   n += 5
    else  :     n += 10
print(n)