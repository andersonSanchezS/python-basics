# Sets are a collection of unique items
# Sets are unordered

mySet: set = {"apple", "banana", "cherry"}

# Sets methods

# 1. len() - returns the number of items in the set
print(len(mySet))

# 2. add() - adds an item to the set
mySet.add("orange")

# 3. remove() - removes an item from the set
mySet.remove("banana")

# 4. discard() - removes an item from the set if it exists, otherwise it does nothing
mySet.discard("banana")

# 5. pop() - removes an item from the set and returns it
print(mySet.pop())

# 6. clear() - removes all the items from the set
mySet.clear()

# 7. copy() - creates a copy of the set
print(mySet.copy())

# 8. union() - returns a new set with all the items from both sets
print(mySet.union({"orange", "apple", "banana"}))

# 9. intersection() - returns a new set with all the items that exist in both sets
print(mySet.intersection({"orange", "apple", "banana"}))

# 10. difference() - returns a new set with all the items that exist in the first set but not in the second
print(mySet.difference({"orange", "apple", "banana"}))

# 11. symmetric_difference() - returns a new set with all the items that exist in either set but not in both
print(mySet.symmetric_difference({"orange", "apple", "banana"}))

# 12. issubset() - returns True if the set is a subset of another set, otherwise False
print(mySet.issubset({"orange", "apple", "banana"}))

# 13. issuperset() - returns True if the set is a superset of another set, otherwise False
print(mySet.issuperset({"orange", "apple", "banana"}))

# 14. isdisjoint() - returns True if the set has no items in common with another set, otherwise False
print(mySet.isdisjoint({"orange", "apple", "banana"}))

# 15. update() - updates the set with the items of another set
mySet.update({"orange", "apple", "banana"})

# 16. intersection_update() - updates the set with the items that exist in both sets
mySet.intersection_update({"orange", "apple", "banana"})

# 17. difference_update() - updates the set with the items that exist in the first set but not in the second
mySet.difference_update({"orange", "apple", "banana"})

# 18. symmetric_difference_update() - updates the set with the items that exist in either set but not in both
mySet.symmetric_difference_update({"orange", "apple", "banana"})

