first = list(map(int, input("Enter the first list: ").split()))
second = list(map(int, input("Enter the second list: ").split()))
newset = set(first)^set(second) #conver list to a set
print("The uncommon elements are ", list(newset))

n = int(input("Enter a number: "))
for i in range(1, n):
    print(i*i)

def underscore(s):#created a function
    result = []
    count = 0
    i = 0
    while i < len(s):
        result.append(s[i])
        count+=1
        if count == 3:
            if i+1<len(s) and s[i+1]=='_': #skip to the next if underscore is already there
                i+=1
                result.append(s[i])
                if i+1<len(s) and s[i] == 'aeiouAEIOU':#skip vowels
                    i+=1
            result.append('_')
            count = 0#reset count to make sure underscore is added to the next cases
        i+=1
    return "".join(result)
s = input("Enter a string: ")
print("Your result: ", underscore(s))      

import random
randnum = random.randrange(1, 100)
found = False
count = 0 #set the counter to 0 to control that user has limited attempts
while found == False and count <=10:
    guess = int(input("Guess the number between 1 and 100: "))
    if guess > randnum:
        print("Too high!")
    elif guess < randnum:
        print("Too low!")
    else:
        print("You guessed it right!")
        break
    count+=1
    if count == 10:
        ans = input("You lost. Want to play again? ")
        if ans == 'yes' or 'y' or 'YES' or 'Y' or 'ok':
            count = 0 #reset the counter if the user wants to play again

eligible = False
while eligible == False:
    password = input("Enter a password: ")
    if len(password) > 8 and password != password.lower():
        print("Password is strong.")
        eligible = True
        break
    if len(password) <8:
        print("Password is too short!")
    elif password == password.lower():
        print("Password must contain an uppercase letter!")
    # else:
    #     print("Password is strong!")
    #     eligible = True
    # break

prime = []
for i in range(2, 101):
    is_prime = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(i)
print(prime)

import random
countC = 0  #set both counters to 0
countU = 0
while countC <5 and countU <5:
    choices = ["rock", "scissors", "paper"]
    comp = random.choice(choices)
    userinput = False
    while userinput == False:
        user = int(input("Enter 1 for rock, 2 for scissors and 3 for paper: "))
        if user not in[1, 2, 3]:
            print("Error! Enter 1, 2 or 3")
        else:
            userinput = True #handled the case where user enters smth other than 1, 2, 3
    if user == 1:
        if comp == 'rock':
            print("It's a tie")
        elif comp == 'scissors':
            countU+=1
        else:
            countC+=1
        print("Computer chose ", comp)
        print("User-Computer", countU, '-', countC)
    elif user == 2:
        if comp == 'rock':
            countC+=1
        elif comp == 'scissors':
            print("It's a tie")
        else:
            countU+=1
        print("Computer chose ", comp)
        print("User-Computer", countU, '-', countC)
    elif user == 3:
        if comp == 'rock':
            countU+=1
        elif comp == 'scissors':
            countC+=1
        else:
            print("It's a tie")
        print("Computer chose ", comp)
        print("User-Computer", countU, '-', countC)
if countC>countU:
    print("Computer won!")
else:
    print("User won!")