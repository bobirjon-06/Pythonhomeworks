#1
nums = list(map(int, input().split()))
element = int(input("Enter the element: "))

count = 0
for num in nums:
    if num == element:
        count += 1

print(count)


nums = list(map(int, input().split()))
total = 0

for num in nums:
    total += num

print(total)

nums = list(map(int, input().split()))
largest = nums[0]

for num in nums:
    if num > largest:
        largest = num

print(largest)

nums = list(map(int, input().split()))
smallest = nums[0]
for num in nums:
    if num < smallest:
        smallest = num

print(smallest)

nums = list(map(int, input().split()))
element = int(input("Enter the element: "))
present = False
for num in nums:
    if num == element:
        present = True
        break

nums = list(map(int, input().split()))
if len(nums)<=0:
    print("The list is empty")
else:
    first = nums[0]
    print(first)

nums = list(map(int, input().split()))
if len(nums)<=0:
    print("The list is empty")
else:
    last = nums[-1]
print(last)

nums = list(map(int, input().split()))
print(nums[:3])

nums = list(map(int, input().split()))
reverse = nums[::-1]
print(reverse)

nums = list(map(int, input().split()))
sort = sorted(nums)

nums = list(map(int, input().split()))
new = []
for num in nums:
    if num not in new:
        new.append(nums)
print(new)

nums = list(map(int, input().split()))
element, order = int(input("Enter the element and its orderd: "))
nums.insert(order, element)
print(nums)

nums = list(map(int, input().split()))
element = int(input("Enter the element: "))
for num in nums:
    if element == nums[num]:
        print(num)

nums = list(map(int, input().split()))
empty = True
if len(nums)>0:
    empty = False
print(empty)

nums = list(map(int, input("Enter an integer list of numbers: ").split()))
count = 0
for num in nums:
    if num%2==0:
        count+=1
print(count)

nums = list(map(int, input("Enter an integer list of numbers: ").split()))
count = 0
for num in nums:
    if num%2!=0:
        count+=1
print(count)

nums = list(map(int, input().split()))
second = list(map(int, input().split()))
final = num+second
print(final)

nums = list(map(int, input().split()))
second = list(map(int, input().split()))
if second in nums:
    print("Yes")
else:
    print("No")

nums = list(map(int, input().split()))
element, replace = int(input("Enter the element and its replacement: "))
if element in nums:
    nums[nums.index(element)] = replace
print(nums)

nums = list(map(int, input().split()))
secondl, largest = nums[0]
for num in nums:
    if largest<num:
        secondl, largest=num
    elif num > secondl and num<largest:
        secondl = num
print(secondl)

nums = list(map(int, input().split()))
seconds, largest = nums[0]
for num in nums:
    if smallest>num:
        seconds, smallest=num
    elif num < seconds and num>smallest:
        seconds = num
print(seconds)

nums = list(map(int, input().split()))
even = []
for num in nums:
    if num % 2 == 0:
        even.append(num)

print(even)

nums = list(map(int, input().split()))
odd = []
for num in nums:
    if num % 2 != 0:
        odd.append(num)

print(odd)

nums = list(map(int, input().split()))
print(len(nums))

nums = list(map(int, input().split()))
length = len(nums)
middle = length //2
if length%2==0:
    print(nums[middle], nums[middle-11])
else:
    print(nums[middle])

nums = list(map(int, input().split()))
start = int(input())
end = int(input())
sublist = nums[start:end]
print(min(sublist))

nums = list(map(int, input().split()))
index = int(input())
print(nums.remove(index))

nums = list(map(int, input().split()))
Sorted = False
if nums == nums.sort():
    Sorted = True
print(Sorted)

nums = list(map(int, input().split()))
number = int(input())
newlist = []
for num in nums:
    for _ in range(number):
        newlist.append(num)

print(newlist)

first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = first+second
third.sort()
print(third)

nums = list(map(int, input().split()))
element = int(input())
indices = []
for num in nums:
    if num ==  element:
        indices.append(num)

print(indices)

nums = list(map(int, input().split()))
new = []
new = [nums[-1]] + nums[:-1]

print(new)

first = int(input())
second = int(input())
nums = list(range(first, second))
print (nums)

nums = list(map(int, input().split()))
total = 0
for num in nums:
    if num > 0:
        total += num

print(total)

nums = list(map(int, input().split()))
total = 0
for num in nums:
    if num < 0:
        total += num

print(total)

nums = list(map(int, input().split()))
palindrome = False
if nums == nums[::-1]:
    palindrome = True
print(palindrome)

nums = list(map(int, input("Enter numbers: ").split()))
size = int(input("Enter sublist size: "))

nested_list = [nums[i:i+size] for i in range(0, len(nums), size)]
print(nested_list)

nums = list(map(int, input("Enter numbers: ").split()))
unique = []
seen = []
for num in nums:
    if num not in seen:
        unique.append(num)
        seen.append(num)

print(unique)

