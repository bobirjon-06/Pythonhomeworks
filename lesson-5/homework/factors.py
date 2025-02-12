def factors(integer):
    for num in range(1, integer+1):
        if(integer%num == 0):
            print(num, " is a factor of ", integer)
number = int(input("Enter a postive integer: "))
while number <= 0:
    number = int(input("Enter a postive integer: "))
factors(number)