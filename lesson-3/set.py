import random

first = set(input().split())
second = set(input().split()) 
new_set = first | second 
print(new_set)  

first = set(input().split())
second = set(input().split())
newset = first&second
print(newset)

first = set(input().split())
second = set(input().split()) 
newset = first - second
print(newset)

first = set(input().split())
second = set(input().split()) 
if first.issubset(second) or second.issubset(first):
    print(True)
else:
    print(False)

first = set(input().split())
element = input()
if element in first:
    print (True)
else:
    print(False)

first = set(input().split())
print(len(first))

first = list(input().split())
newset = set(first)
print(newset)

first = set(input().split())
element = input()
if element in first:
    first.remove(element)
    print(first)
else:
    print("It isnt there")

first = set(input().split())
first.clear()
print(first)

first = set(input().split())  
print(len(first) == 0)  

first = set(input().split())  
second = set(input().split())  
newset = first ^ second  
print(newset)  

first = set(input().split())  
element = input()
if element not in first:
    first.add(element)
print(first)

first = set(input().split())  
if first:
    removed = first.pop()  
    print(removed)  
else:  
    print("Set is empty")

first = set(map(int, input().split()))  
if first:
    print(max(first))  
else:  
    print("Set is empty")  

first = set(map(int, input().split()))  
if first:
    print(min(first))  
else:  
    print("Set is empty")  

first = set(map(int, input().split()))  
newset = {num for num in first if num % 2 == 0}  

print(newset)

first = set(map(int, input().split()))  
newset = {num for num in first if num % 2 == 1}  

print(newset)  

start, end = map(int, input().split())  
newset = set(range(start, end + 1))  

print(newset)  

first = list(input().split())  
second = list(input().split())  
third = set(first+second)
print(third)

first = set(input().split())  
second = set(input().split())  
if first.isdisjoint(second):
    print("No elements in common")
else:
    print("They have common elements")

first = list(input().split())
second = set(first)
third = list(second)
print(third)

first = list(input().split())  
unique_elements = set(first)  
print(len(unique_elements))

num = int(input())
start, end = map(int, input().split())
ranset = set(random.sample(range(start, end+1), num))
print(ranset)