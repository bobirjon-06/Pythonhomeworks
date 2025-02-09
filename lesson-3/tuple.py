nums = tuple(input().split())
element = input()
count = nums.count(element)
print(count)

nums = tuple(map(int, input("Enter numbers: ").split()))
print(max(nums))


nums = tuple(map(int, input("Enter numbers: ").split()))
print(min(nums))

nums = tuple(input().split())
element = input()
present = False
if element in nums:
    present = True
print(present)

nums = tuple(input().split())
if len(nums)>0:
    print(nums[0])
else:
    print(False)

nums = tuple(input().split())
if len(nums)>0:
    print(nums[-1])
else:
    print(False)

nums = tuple(input().split())
print(len(nums))

first = tuple(input().split())
second = first[:3]
print(second)

first = tuple(input().split())
second = tuple(input().split())
third = first + second
print(third)

first = tuple(input().split())
element = input()
found = [num for num in first if num == element]
print(found)

nums = tuple(map(int, input().split()))
if len(nums) < 2:
    print("Not enough elements")
else:
    largest = secondl = float('-inf') 
    for num in nums:
        if num > largest:
            secondl, largest = largest, num 
        elif secondl < num < largest:
            secondl = num

    if secondl == float('-inf'):
        print("No second largest element")
    else:
        print(secondl)

nums = tuple(map(int, input().split()))

if len(nums) < 2:
    print("Not enough elements")
else:
    smallest = seconds = float('inf')

    for num in nums:
        if num < smallest:
            seconds, smallest = smallest, num 
        elif smallest < num < seconds:
            seconds = num

    if seconds == float('inf'):
        print("No second smallest element")
    else:
        print(seconds)

element = input()
singtuple = (element, )
print(singtuple)

nums = list(map(int, input().split()))
numtuple = (nums, )
print(numtuple)

nums = tuple(map(int, input().split()))
Sorted = False
if nums == tuple(sorted(nums)):
    Sorted = True

print(Sorted)

nums = tuple(map(int, input().split()))
start = int(input())
end = int(input())
subtuple = nums[start:end]
print(max(subtuple))

nums = tuple(map(int, input().split()))
start = int(input())
end = int(input())
subtuple = nums[start:end]
print(min(subtuple))

nums = tuple(input().split())
element = (input())
temp = list(nums)
if element in temp:
    temp.remove(element)
newt = tuple(temp)
print(newt)

nums = tuple(map(int, input().split()))  
size = int(input())  

newt = []  
for i in range(0, len(nums), size):  
    newt.append(nums[i:i+size])  
newt = tuple(newt)  
print(newt)  

nums = tuple(input().split())  
n = int(input())  
newt = []  
for num in nums:  
    newt.extend([num] * n)  
newt = tuple(newt)  
print(newt)  

start, end = map(int, input().split())  
nums = tuple(range(start, end + 1))  
print(nums)

first = tuple(input().split())
new = first[::-1]
print(new)

nums = tuple(input().split())
palindrome = False
if nums == nums[::-1]:
    palindrome = True
print(palindrome)

nums = tuple(map(int, input("Enter numbers: ").split()))
unique = []
seen = []
for num in nums:
    if num not in seen:
        unique.append(num)
        seen.append(num)
unique = tuple(unique)
print(unique)