# 1
print("Enter your name and the year of birth: ")
name = input()
year = int(input())
print("Your age is: ", 2025-year)

# 2
s = "LMaasleitbtui"
print(s[::2])
print(s[1::2])

# 3
s = input()
print(len(s), s.upper(), s.lower())

# 4
s = input()
if s == s[::-1]:
    print("Yes")
else:
    print("no")

# 5
print(sum(1 for x in s if x.lower() in "uieoa"))
print(sum(1 for x in s if x.lower() not in "uieoa" and x.isalpha()))

# 6
first = input()
second = input()
if first in second:
    print("Yes")
elif second in first:
    print("Yes")
else:
    print("No")

# 7
print("Enter a sentence: ")
s = input()
print("Enter a word to replace: ")
s1 = input()
print("Enter a word to replace with: ")
s2 = input()
print(s.replace(s1, s2))

# 8
s= input()
print(s[0])
print(s[-1])

# 9
s = input()
print(s[::-1])

# 10
print (len(input("Enter a sentence: " ).split()))

# 11
s = input()
if any(char.isdigit() for char in s):
    print("Yes")
else:
    print("No")

# 12
s = input().split()
a = "-"
res = a.join(s)
print (res)

# 13
s = input()
ans = s.replace(" ", "")
print (ans)

# 14
s1 = input()
s2 = input()

if s1 == s2:
    print("Yes")
else:
    print("No")

# 15
s = input("Enter a sentence: ")
w = s.split()
ans = ''.join(word[0].upper() for word in w)
print (ans)

# 16
s = input("enter a string: ")
c = input("enter a character: ")
ans = s.replace(c, "")
print (ans)

# 17
s = input("enter a string: ")
w = "aeiouAEOIU"
ans = ''.join('*' if char in w else char for char in s)

# 18
s = input()
w = s.split()
print(w[0])
print(w[-1])