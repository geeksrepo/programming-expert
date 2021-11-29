x = "4"
y = int(x) + 4
print(type(y))
print(type(x))
print(y)

y = float("4.5") + 4
print(type(y))
print(type(x))
print(y)

y = float(4.5) + 4
print(type(y))
print(type(x))
print(y)

y = int(4.9) + 4
print(type(y))
print(type(x))
print(y)

y = bool("")
print(type(y))
print(type(x))
print(y)

y = bool(-9)
print(type(y))
print(type(x))
print(y)

y = str(-9) + "2"
print(type(y))
print(type(x))
print(y)

y = str(True) + "2"
print(type(y))
print(type(x))
print(y)

number = int(input("Enter a number: "))
result = number + 5
print("The result is", result)