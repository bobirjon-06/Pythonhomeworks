# 1
u = input()
p = input()
is_true = bool(u) and bool (p)
if is_true:
    print("Accepted")

# 2
a = int(input())
b = int(input())
equal = (a == b)
if equal:
    print("They're equal")
else:
    print("Nah")

# 3
a = int(input())
pos = (a > 0)
ev = (a%2==0)
if pos and ev:
    print("Yes")
else:
    print("Nah")

# 4

a = int(input())
b = int(input())
c = int(input())

are_different = (a!=b) and (a!=c) and (b!=c)
if are_different:
    print("Yes")
else:
    print("No")

# 5
s = input()
s1 = input()
isTrue = (len(s) == len(s1))
if isTrue:
    print("Yes")
else:
    print("nah")

# 6
num = int(input())
isTrue = (num % 3 == 0) and (num % 5 == 0)
if isTrue:
    print("Yes")
else:
    print("Nah")

# 7
a = int(input())
b = int(input())

isTrue = (a+b>50)
if isTrue:
    print("Yes")
else:
    print("Nah")

# 8
a = int(input())
isTrue = (a>=10) and (a<=20)
if isTrue:
    print("Yes")
else:
    print("Nah")