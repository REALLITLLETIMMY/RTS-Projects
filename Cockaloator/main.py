operator = input("Select *,/,+,-")
x = int(input("1st number: "))
y = int(input("2st number: "))
if operator == "+":
    print(x + y)
elif operator == "-":
    print(x - y)
elif operator == "*":
    print(x * y)
elif operator == "/":
    print(x / y)
else:
    print("x:", x, "y:" ,y,)
