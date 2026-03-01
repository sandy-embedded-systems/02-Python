# Python - Check if a given string is binary string or not
# Story: Is your note just 0s and 1s?
# Sample Input:
# note = "101010"
# Sample Output:
# Yes
# Sample Input:
# note = "1201"
# Sample Output:
# No
# Tip: What does set(note) show you?
binary=input("Enter binary string:")
check=set(binary)
if check.symmetric_difference({'1','0'}):
    print("No")
else: print("Yes")

# Python set to check if string is panagram
# Story: Does your sentence use every letter in the alphabet?
# Sample Input:
# sentence = "The quick brown fox jumps over a lazy dog"
# Sample Output:
# Yes
# Tip: Compare set of your letters with the alphabet set!
sentence=input("Enter your sentence:")
check=set()
for ch in sentence:
    if ch.isalpha():
        check.add(ch.lower())
if len(check)==26:
    print("YES")
else: print("NO")


# Python Set - Pairs of complete strings in two sets
# Story: Pick a word from each basket to make a pair that covers all 26 letters!
# Sample Input:
# A = {"abc", "defg", "xyz"}
# B = {"mnopq", "rstuv", "wxyz"}
# Tip: Try making pairs and see if all alphabet letters are used together.
A={"abc","defg","xyz"}
B={"mnopq","rstuv","wxyz"}
alphabet=set("abcdefghijklmnopqrstuvwxyz")

for a in A:
    for b in B:
        combined=set(a+b)
        if combined==alphabet:
            print("Pair:",a,b)
            
            
# Python program to check whether a given string is Heterogram or not
# Story: Does your word have only different letters, no repeats?
# Sample Input:
# word = "lamp"
# Sample Output:
# Yes
# Sample Input:
# word = "hello"
# Sample Output:
# No
# Tip: Compare len(set(word)) and len(word).
word=input("Enter your word:")
if len(set(word)) ==len(word):
    print("yes")
else: print("no")


# Python program to convert Set into Tuple and Tuple into Set
# Story: You line up your toys (tuple—order matters), then put them in a toy box (set—order doesn’t matter).
# Sample Input:
# toys_set = {"teddy", "robot", "ball"}
# Sample Output:
# ("teddy", "robot", "ball")
# Tip: What changes when you go from set to tuple and back?
# Sample input
toys_set = {"teddy", "robot", "ball"}
toys_tuple = tuple(toys_set)
print("Set to Tuple:", toys_tuple)
toys_set_again=set(toys_tuple)
print("Tuple to Set:", toys_set_again)


# Python program to convert set into a list
# Story: You pour your collection of badges (set) out into a row (list) to show your friends.
# Sample Input:
# badges = {"star", "moon", "heart"}
# Sample Output:
# ["star", "moon", "heart"]
# Tip: Does the list always come out in the same order?
badges = {"star", "moon", "heart"}
lst=list(badges)
print(lst)
print(badges)

# Python program to convert Set to String
# Story: You turn your collection of letters into a cool code word.
# Sample Input:
# letters = {"A", "B", "C"}
# Sample Output:
# "BAC"
# Tip: Set has no order—how can you make it alphabetical?
letters = {"A", "B", "C"}
print(str(letters))

# Python program to convert String to Set
# Story: Find all different letters in your name!
# Sample Input:
# myname = "samantha"
# Sample Output:
# {'s', 'a', 'm', 'n', 't', 'h'}
# Tip: It's a fast way to spot repeated letters.
myname="santhosh"
print(set(myname))

# Python - Convert a set into dictionary
# Story: Give each pet a number for your pet show.
# Sample Input:
# pets = {"dog", "cat", "fish"}
# Sample Output:
# {'dog': 0, 'cat': 1, 'fish': 2}
# Tip: Try using enumerate() to give each item a number.
# Sample input
pets = {"dog", "cat", "fish"}
pets_dict={}
for i,pet in enumerate(pets):
    pets_dict[pet]=i
print(pets_dict)

# Python program to find union of n arrays
# Story: Collect favorite colors from all your classmates—what are all the colors?
# Sample Input:
# friends_colors = [
#   ["red", "blue"],
#   ["green", "red"],
#   ["yellow", "blue"]
# ]
# Sample Output:
# {'red', 'blue', 'green', 'yellow'}
# Tip: What happens if someone likes the same color twice?
friends_colors = [
   ["red", "blue"],
   ["green", "red"],
   ["yellow", "blue"]]
unique=set()
for item in friends_colors:
    for colour in item:
        unique.add(colour)
print(unique)

# Python - Intersection of two lists
# Story: Which stickers do you and your friend both have?
# Sample Input:
# mine = ["dino", "star", "moon"]
# yours = ["star", "rocket", "moon"]
# Sample Output:
# {"star", "moon"}
# Tip: How is this different if you use a list instead of a set?
mine = ["dino", "star", "moon"]
yours = ["star", "rocket", "moon"]
print(set(mine).intersection(set(yours)))

# Python program to get all subsets of given size of a set
# Story: How many different teams of 3 can you make from 5 kids?
# Sample Input:
# kids = {"Amy", "Bob", "Cara", "Dan", "Eva"}
# size = 3
# Sample Output:
# ("Amy", "Bob", "Cara")  # one possible team
# Tip: Which Python library helps you make all teams?
kids=["Amy","Bob","Cara","Dan","Eva"]
size=3

def make_teams(arr,size,start,team):
    if len(team)==size:
        print(tuple(team))
        return
    for i in range(start,len(arr)):
        make_teams(arr,size,i+1,team+[arr[i]])

make_teams(kids,size,0,[])


# Python - Minimum number of subsets with distinct elements using Counter
# Story: You have lots of marbles. How many bags do you need so that no bag has two marbles of the same color?
# Sample Input:
# marbles = ["red", "blue", "red", "green", "blue", "red"]
# Sample Output:
# 3
# Tip: The most common color
kids=["Amy","Bob","Cara","Dan","Eva"]
size=3

def make_teams(arr,size,start,team):
    if len(team)==size:
        print(tuple(team))
        return
    for i in range(start,len(arr)):
        make_teams(arr,size,i+1,team+[arr[i]])

make_teams(kids,size,0,[])