# 1
num = float(input())
num = round(num, 2)
print(num)

# 2
a = float(input())
b = float(input())
c = float(input())
print(max(a, b, c))
print(min(a, b, c))

# 3
a = float(input())
m = a*1000
cm = m*100
print(a, m, cm)

# 4
a, b = map(int,input().split())
c = max(a, b)
d = min(a, b)
ans = c//d
# r = c-(ans*d)
print(divmod(c, d))

# 5
a = int(input())
print((a*(9/5))+32)

# 6
n = int(input())
print(n-(n//10)*10)

# 7
n = int(input())
if n%2==0:
    print("Even")
else:
    print("Odd")
