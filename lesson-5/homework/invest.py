def invest(amount, rate, years):
    for year in range(0, years):
        amount += amount * rate
        print(f"year, {year}: ${amount:.2f} ")
pamount = float(input("Enter the initial amount: "))
annualrate = float(input("Enter percentage increase: "))
numofyears = int(input("Enter the number of years: "))
invest(pamount, annualrate, numofyears)