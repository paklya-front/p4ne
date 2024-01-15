def calculate(x = int(input("Enter the first num: " "")) , y = int(input("Enter the second num: " "")), sign = input("Enter the sign: + or - or * or /: ") ):
    #####НЕ ДОДЕЛАЛ ИСКЛЮЧЕНИЯ((((
    try:
        if x == str():
            return False, "Try again"
    except:
            ValueError
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

calc = calculate()
print("Calculating:" "",calc)