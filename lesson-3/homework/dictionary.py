first = dict(input().split() for _ in range(int(input("Enter number of key-value pairs: "))))  
key = input("Enter the key: ")  
value = first.get(key, "Key not found")

print(value)

first = dict(input().split() for _ in range(int(input("Enter number of key-value pairs: "))))  
key = input("Enter the key: ")
if key in first:
    print("Present")
else:
    print("Not present")

first = dict(input().split() for _ in range(int(input("Enter number of key-value pairs: "))))  
print(len(first))

first = dict(input().split() for _ in range(int(input("Enter number of key-value pairs: "))))  
keys_list = list(first.keys())
print(keys_list)

first = dict(input().split() for _ in range(int(input("Enter number of key-value pairs: "))))  
values_list = list(first.values())
print(values_list)

first = dict(input().split() for _ in range(int(input("Enter number of key-value pairs: "))))  
second = dict(input().split() for _ in range(int(input("Enter number of key-value pairs: "))))  
first.update(second)
print(first)

first = dict(input().split() for _ in range(int(input("Enter number of key-value pairs: "))))
key = input("Enter key to remove: ")
if key in first:
    first.pop(key)
else:
    print("Key not found")
print(first)

first = dict()
print(first)

first = {}
num_pairs = int(input("Enter number of key-value pairs: "))
if num_pairs > 0:
    first = dict(input().split() for _ in range(num_pairs))
empty = len(first) == 0
print(empty)

first = dict(input().split() for _ in range(int(input("Enter number of key-value pairs: "))))
key = input("Enter key to search: ")
if key in first:
    print(key, first[key])  # Print key-value pair if key exists

first = dict(input().split() for _ in range(int(input("Enter number of key-value pairs: "))))
value = input("Enter a value: ")
count = 0
for num in first.values():
    if num == value:
        count+=1
print(count)

first = dict(input().split() for _ in range(int(input("Enter number of key-value pairs: "))))
inverted = {}
for key, value in first.items():
    inverted[value] = key
print(inverted)

first = dict(input().split() for _ in range(int(input("Enter number of key-value pairs: "))))
value = input()
keys = []
for key, values in first.items():
    if values == value:
        keys.append(key)
print(keys)

keys = input("Enter keys: ").split()
values = input("Enter values: ").split()
first = dict()
for o in range(min(len(keys), len(values))):
    first[keys[i]]= values[i]
print(first)

first = dict(input().split() for _ in range(int(input("Enter number of key-value pairs: "))))
nested = False
for val in first.values():
    if isinstance(val, dict):
        nested = True
        break
print(nested)

first = {
    "person": {"name": "Jane", "age": 19},
    "job": {"title": "Doctor", "salary": 50000}
}
outer_key = input()
inner_key = input()
value = None
if outer_key in first and isinstance(first[outer_key], dict):
    if inner_key in first[outer_key]:
        value = first[outer_key][inner_key]
print(value)

first = {}
default_value = input()

n = int(input())
for _ in range(n):
    key, value = input().split()
    first[key] = value
test_key = input()
print(first.setdefault(test_key, default_value))

first = {}
n = int(input("Enter number of key-value pairs: "))
for _ in range(n):
    key, value = input().split()
    first[key] = value
unique_values = set(first.values())
print(len(unique_values))

first = {}
n = int(input("Enter number of key-value pairs: "))
for _ in range(n):
    key, value = input().split()
    first[key] = value
sorted_dict = dict(sorted(first.items()))
print(sorted_dict)

# first = {}
# n = int(input("Enter number of key-value pairs: "))
# for _ in range(n):
#     key, value = input().split()
#     first[key] = value
# sorted(first.items(), key=lambda item: item[1])
# print(sorted_dict) didnt understand this one.

filtered_dict = {k: v for k, v in first.items() if v % 2 == 0}
print(filtered_dict)  

first = dict(input().split() for _ in range(int(input("Enter number of key-value pairs: "))))
seond= dict(input().split() for _ in range(int(input("Enter number of key-value pairs: "))))
common_keys = set(first.keys()) & set(second.keys())
print(bool(common_keys))
print(common_keys)

first = dict(input().split() for _ in range(int(input("Enter number of key-value pairs: "))))
newdict = dict(first)
print(dict)

first = dict(input().split() for _ in range(int(input("Enter number of key-value pairs: "))))
first_pair = next(iter(first.items()))  
print(first_pair)
