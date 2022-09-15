a, b = input().split()

a = list(reversed(a))
a = int("".join(a))
b = list(reversed(b))
b = int("".join(b))

print(max(a, b))