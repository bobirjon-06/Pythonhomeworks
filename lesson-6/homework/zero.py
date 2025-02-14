def check(function):
    def wrap(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return function(a, b)
    return wrap

@check
def div(a, b):
    return a / b

a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))
print("Output:", div(a, b))