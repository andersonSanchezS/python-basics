# Lists - arrays in Python
li: list = [1, 2, 3, 4, 5]

# Matrix - 2D array
matrix: list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# List methods
# append() - adds an element to the end of the list
li.append(6)

# insert() - adds an element at a given index
li.insert(2, 7)

# remove() - removes an element from the list
li.remove(7)

# pop() - removes an element from the list and returns it
li.pop()

# index() - returns the index of the first element with the specified value
li.index(1)

# count() - returns the number of elements with the specified value
li.count(1)

# sort() - sorts the list in ascending order
li.sort()

# sort(reverse=True) - sorts the list in descending order
li.sort(reverse=True)

# reverse() - reverses the order of the list
li.reverse()

# clear() - removes all elements from the list
li.clear()

# copy() - returns a shallow copy of the list
li_copy: list = li.copy()

# extend() - appends the contents of another iterable to the end of the list
li.extend([10, 11, 12])

# list destructuring
a, b, c = [1, 2, 3]

# list comprehension
li_comp: list = [i for i in range(10)]
li_numbers: list = [i for i in range(0, 11) if i % 2 == 0]
