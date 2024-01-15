def calculate(x , y):
    sign = input("Enter the sign: + or - or * or /: ")
    try:
       if y == 0:
        return False, "Try again"
    except:
        pass
    if sign == "+":
        result = x + y
        return result
    elif sign == "-":
        result = x - y
        return result
    elif sign == "*":
        result = x * y
        return result
    elif sign == "/":
        result = x / y
        return result
    else:
        print("Invalid sign")
        return 0

calc = calculate(100, 20)
print("Calculating:" "",calc)