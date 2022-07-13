# Loops

# For loop
for i in range(10):
    print(i)

# While loop
i = 0
while i < 10:
    print(i)
    i += 1

# For loop with a list
numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    print(i)

# For loop with a dictionary
colors: dict = {"amarillo": "yellow", "azul": "blue", "verde": "green"}
for i in colors:
    print(i)

# Foreach loop
for i in colors:
    print(colors[i])

# For loop with a string
string: str = "Hello World"
for i in string:
    print(i)

# For loop with a tuple
tuple: tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in tuple:
    print(i)

# For loop with a range
for i in range(10):
    print(i)

# For loop with a range and a step
for i in range(10, 20, 2):
    print(i)
