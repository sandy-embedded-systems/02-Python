# 1. List Creation and Indexing
# Log Session a list named fruits containing "apple", "banana", and "cherry".
# Print the second item in the list.
# Change the value from "banana" to "kiwi".
# Print the updated list.
# Determine the length of the list.
fruits=["apple","banana","cherry"]
print("second:",fruits[1])
fruits[fruits.index("banana")]="kiwi"
print(fruits)
print(len(fruits))

# 2. Adding and Removing Items
# Append "orange" to the fruits list.
# Insert "mango" at the second position.
# Remove "apple" from the list.
# Use the pop() method to remove the last item.
# Clear the entire list.
l=["apple", "banana","cherry"]
l.append("orange")
l.index(1,"mango")
l.remove("apple")
print(l.pop())
l.clear()

# 3. Looping Through Lists
# Log Session a list of numbers from 1 to 5.
# Use a for loop to print each number.
# Use a while loop to print each number.
# Use list comprehension to create a new list with each number squared.
list=[1,2,3,4,5]
for ele in list:
    print(ele)
while ele in list:
    print(ele)
square=[x*2 for x in list]
print(square)

# 4. List Comprehension
# Log Session a list of fruits: "apple", "banana", "cherry", "kiwi", "mango".
# Use list comprehension to create a new list containing fruits with the letter "a".
# Convert all fruit names to uppercase using list comprehension.
# Replace "banana" with "orange" using list comprehension.
list=["apple", "banana", "cherry", "kiwi", "mango"]
new=[ele for ele in list and 'a' in ele]
print(new)
# 5. Sorting and Copying Lists
# Log Session a list of numbers: [3, 1, 4, 2, 5].
# Sort the list in ascending order.
# Sort the list in descending order.
# Copy the sorted list to a new list.
# Print both lists to verify they are separate copies.
list.clear()
list=[3, 1, 4, 2, 5]
list.sort()
print(list)
list.sort(reverse=True)
print(list)
new_list=list.copy()
print(list)
print(new_list)

# 6. Joining and Extending Lists
# Log Session two lists: list1 = ["a", "b", "c"] and list2 = [1, 2, 3].
# Concatenate the two lists into a new list.
# Use the extend() method to add list2 to list1.
# Print the final lists.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
# 7. List Methods Practice
# Log Session a list: colors = ["red", "green", "blue", "green"].
# Use the count() method to find how many times "green" appears.
# Use the index() method to find the position of "blue".
# Reverse the list using the reverse() method.
# Clear the list using the clear() method.
colors = ["red", "green", "blue", "green"]
print(colors.count("green"))
print(colors.index("blue"))
colors.remove()
print(colors)
colors.clear()
