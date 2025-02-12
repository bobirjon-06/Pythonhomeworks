def convert_cel_to_far(celcius):
    return round(celcius * 9/5+32, 2)
def convert_far_to_cel(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2)

fahrenheit = float(input("Enter a temperature in degrees F: "))
print(f"{fahrenheit}F -> {convert_far_to_cel(fahrenheit)}C")

celcius = float(input("Enter a temperature in degrees C: "))
print(f"{celcius}C -> {convert_cel_to_far(celcius)}F")

