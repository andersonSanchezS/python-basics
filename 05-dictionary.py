# Dictionaries are a collection of key-value pairs.
colors: dict = {"amarillo": "yellow", "azul": "blue", "verde": "green"}

# Dictionaries methods

# 1. len() - returns the number of items in the dictionary
print(len(colors))

# 2. keys() - returns a list of all the keys
print(colors.keys())

# 3. values() - returns a list of all the values
print(colors.values())

# 4. items() - returns a list of all the key-value pairs
print(colors.items())

# 5. get() - returns the value of the key
print(colors.get("amarillo"))

# 6. setdefault() - returns the value of the key if it exists, otherwise it sets the key-value pair and returns the
# value
print(colors.setdefault("rojo", "red"))

# 7. pop() - removes the key-value pair and returns the value
print(colors.pop("amarillo"))

# 8. popitem() - removes the last key-value pair and returns it
print(colors.popitem())

# 9. clear() - removes all the key-value pairs
colors.clear()

# 10. update() - updates the dictionary with the key-value pairs of another dictionary
colors.update({"amarillo": "yellow", "azul": "blue", "verde": "green"})

# 11. fromkeys() - creates a new dictionary with the specified keys and value
print(dict.fromkeys(["amarillo", "azul", "verde"], "red"))

# 12. copy() - creates a copy of the dictionary
print(colors.copy())

# 13. has_key() - returns True if the dictionary has the key, otherwise False
print(colors.has_key("amarillo"))

# 14. has_value() - returns True if the dictionary has the value, otherwise False
print(colors.has_value("yellow"))

