def calculate():
    try:
        x = int(input("Enter the first num: " ""))
        y = int(input("Enter the second num: " ""))
        sign = input("Enter the sign: + or - or * or /: ")
        new_x = int(x)
        new_y = int(y)
        new_result = 0
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

    except ValueError:
        print("Invalid input")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError:
        print("Invalid input")
    

calc = calculate()
print("Calculating:" "",calc)