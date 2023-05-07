# Lists (a.k.a Arrays) are used to store various items in a variable, like the data of a person
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names)  # Prints all the items
names[0] = "Jon"
print(names[3])  # Prints the third item of the list
print(names[-1])  # Negative index means from last to first (-1 is mary, -2 Sam)
print(names[0:3])  # 0:3 Prints The first element, the second, the third and the fourth.
print(names)

# Lists methods
# "a".  shows you all the methods (depends on your code editor
numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # Adds 6 to the list
numbers.insert(0, -1)  # Removes the last item
# numbers.clear()  Clears the list
print(1 in numbers)  # Checks if 1 is in numbers (a boolean expression)
print(len(numbers))  # It tells how many elements are in the list
