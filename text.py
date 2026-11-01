def opperation(op):
    return op in ("+","-","*","/")
def calculator(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "error: division by zero not exist"
        return num1 / num2
    else:
        return "error: invalid operator"
def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    op = input("Enter the operator (+, -, *, /): ")

    if opperation(op):
        result = calculator(num1, num2, op)
        if isinstance(result, str):
            print(result)
        else:
            print(f"The result of this operation is: {round(result, 2)}")
    else:
        print("error: invalid operation")
main()

finally:
    print("Thank you for using the calculator.")