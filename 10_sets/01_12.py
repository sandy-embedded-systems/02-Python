# Find the size of a Set in Python
# Story: You have a bag of unique toys. How many toys do you have?
# Sample Input:
# bag = {"ball", "car", "puzzle", "car", "yo-yo"}
# Sample Output:
# 4
# Tip: Remember, sets only keep one of each thing!
bag ={"ball", "car", "puzzle", "car", "yo-yo"}
print(len(bag))

# Iterate over a set in Python
# Story: You want to see every animal in your mini zoo, but the order doesn't matter.
# Sample Input:
# animals = {"lion", "tiger", "bear"}
# Tip: The order may change every time. When is this helpful?
animals = {"lion", "tiger", "bear"}
for item in animals:
    print(item)
    
# Python - Maximum and Minimum in a Set
# Story: You played some games. What’s your best and worst score?
# Sample Input:
# scores = {3, 7, 10, 2, 9}
# Sample Output:
# Max: 10
# Min: 2
scores = {3, 7, 10, 2, 9}
print("Max:",max(scores),"\nMin:",min(scores),end="")

# Tip: What Python functions can help you find biggest and smallest?
# Python - Remove items from Set
# Story: You want to take out an old toy from your toy box.
# Sample Input:
# toys = {"robot", "car", "doll"}
# # remove "doll"
# Sample Output:
# {"robot", "car"}
toys ={"robot", "car", "doll"}
toys.remove('doll')
print(toys)


# Tip: What’s the difference between remove and discard if the item isn't there?
# Python - Check if two lists have at-least one element common
# Story: You and your friend want to see if you both like any of the same cartoons.
# Sample Input:
# my_favs = ["Tom", "Jerry", "Ben 10"]
# friend_favs = ["Powerpuff", "Jerry", "Scooby"]
# Sample Output:
# Yes! "Jerry" is common.
# Tip: Which set operation shows what you both like?
my_favs = ["Tom", "Jerry", "Ben 10"]
friend_favs = ["Powerpuff", "Jerry", "Scooby"]
common=set(my_favs).intersection(set(friend_favs))
print(f"Yes! {common} is common")

# Python program to find common elements in three lists using sets
# Story: Three friends want to pick a movie everyone likes. Which ones do they all like?
# Sample Input:
# a = ["Toy Story", "Frozen", "Moana"]
# b = ["Moana", "Coco", "Frozen"]
# c = ["Frozen", "Moana", "Up"]
# Sample Output:
# ["Frozen", "Moana"]
# Tip: Can you use set.intersection for this?
a = ["Toy Story", "Frozen", "Moana"]
b = ["Moana", "Coco", "Frozen"]
c = ["Frozen", "Moana", "Up"]
common_items=set(set(a).intersection(set(b))).intersection(set(c))
print(common_items)

# Python - Find missing and additional values in two lists
# Story: You compared last week's and this week's homework lists. What's missing and what's new?
# Sample Input:
# old_hw = ["math", "science", "art"]
# new_hw = ["math", "history", "science"]
# Sample Output:
# Missing: art
# Additional: history
# Tip: What set difference shows what you forgot?
old_hw = ["math", "science", "art"]
new_hw = ["math", "history", "science"]
res=set(set(old_hw)-set(new_hw))

# Python program to find the difference between two lists
# Story: What games do you want to play this week that you didn't play last week?
# Sample Input:
# last_week = ["hide", "seek", "tag"]
# this_week = ["hide", "seek", "jump", "run"]
# Sample Output:
# ["jump", "run"]
# Tip: Use set subtraction: A - B!
last_week = ["hide", "seek", "tag"]
this_week = ["hide", "seek", "jump", "run"]
print(list(set(this_week)-set(last_week)))

# Python Set difference to find lost element from a duplicated array
# Story: You had four marbles yesterday, now one is missing. Which one?
# Sample Input:
# yesterday = [1, 2, 3, 4]
# today = [1, 4, 2]
# Sample Output:
# 3
# Tip: What does set(yesterday) - set(today) give you?
yesterday = [1, 2, 3, 4]
today = [1, 4, 2]
if len(yesterday)>len(today):
    print(*(set(yesterday)-set(today)))
else: print(set(today)-set(yesterday))

# Python program to count number of vowels using sets in given string
# Story: You want to count the vowels in your secret code message.
# Sample Input:
# msg = "hello world"
# Sample Output
# 3
# Tip: Vowels can be put in a set for quick checking!
msg=input("Enter a string:")
vowels=set("aeiou")
cnt=0
for ch in msg:
    if ch in vowels:
        cnt+=1
print(cnt)

# Concatenated string with uncommon characters in Python
# Story: You and your friend invent two words. Make a mashup with only letters not shared by both.
# Sample Input:
# word1 = "apple"
# word2 = "orange"
# Sample Output:
# "plrgn"
# Tip: What does set(word1) ^ set(word2) do?
word1 = "apple"
word2 = "orange"
sym_diff=set(word1)^ set(word2)
result="".join(sym_diff)
print(result)

# Python - Program to accept the strings which contains all vowels
# Story: Find all words that have a, e, i, o, and u!
# Sample Input:
# words = ["education", "python", "sequoia"]
# Sample Output:
# 1
words = ["education", "python", "sequoia"]
vowel_s=set("aeiou")
cnt=0
for word in words:
    if vowel_s.issubset(set(word.lower())):
        cnt+=1
print(cnt)
