# Print Superscript and Subscript in String Output
# Explanation: Show part of the string as superscript or subscript, for math or scientific notation.
# Input: "E = mc2" (display 2 as superscript)
# Expected Output: "E = mc²"
text="E=mc2"
text=text.replace("2","²")
print(text)

# Check for Pangram
# Explanation: Verify if a string contains every letter of the alphabet at least once.
# Input: "The quick brown fox jumps over the lazy dog"
# Expected Output: Is pangram: Yes
s="The quick brown fox jumps over the lazy dog"
s=s.lower()
alphabet="abcdefghijklmnopqrstuvwxyz"
flag=True
for ch in alphabet:
    if ch not in s:
        flag=False
        break
if flag:
    print("Is pangram: Yes")
else:
    print("Is pangram: No")
    
# Sort List of Dates Given as Strings
# Explanation: Sort dates given as strings in chronological order.
# Input: ["2021-05-21", "2019-01-12", "2020-12-15"]
# Expected Output: ['2019-01-12', '2020-12-15', '2021-05-21']
dates=["2021-05-21","2019-01-12","2020-12-15"]
dates.sort()
print(dates)


# Split String into Groups of n Characters
# Explanation: Divide a string into equal-sized chunks.
# Input: "abcdefgh", n = 3
# Expected Output: ['abc', 'def', 'gh']
s="abcdefgh"
n=3
result=[]
for i in range(0,len(s),n):
    result.append(s[i:i+n])
print(result)


# Extract Indices of Substring Matches
# Explanation: Find all starting positions of a substring in a string.
# Input: String = "abracadabra", Substring = "abra"
# Expected Output: [0, 7]
def find_substring_indices(s, sub):
    indices=[]
    start=0
    while True:
        pos=s.find(sub,start)
        if pos==-1:
            break
        indices.append(pos)
        start=pos+1
    return indices
print(find_substring_indices("Hello llo i am llo",'llo'))
    
# Remove After a Substring
# Explanation: Remove everything after a given substring in a string.
# Input: String = "abcdeFGhiJK", Substring = "FG"
# Expected Output: "abcdeFG"
def rem(string,sub):
    idx=string.find(sub)
    idx+=len(sub)
    string=string[:idx]
    return string
# Remove Redundant Substrings from a List
# Explanation: From a list of strings, remove repeated substring patterns.
# Input: ["hellohello", "w
# orld", "testtesttest"]
# Expected Output: ["hello", "world", "test"]
words=["hellohello","world","testtesttest"]
result=[]
for w in words:
    found=False
    for i in range(1,len(w)//2+1):
        part=w[:i]
        if part*(len(w)//len(part))==w:
            result.append(part)
            found=True
            break
    if not found:
        result.append(w)
print(result)


# Filter Strings with a Combination of k Substrings
# Explanation: From a list, select only the strings that contain all of a set of k substrings.
# Input: List = ["applebanana", "apple", "banana", "applebananacherry"], Substrings = ["apple", "banana"]
# Expected Output: ["applebanana", "applebananacherry"]
lst=["applebanana","apple","banana","applebananacherry"]
subs=["apple","banana"]
subs_set=set(subs)
result=[]
for item in lst:
    present=set()
    for s in subs_set:
        if s in item:
            present.add(s)
    if present==subs_set:
        result.append(item)
print(result)