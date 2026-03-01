# Check if a String is a Palindrome or Symmetrical
# Explanation: A palindrome reads the same forwards and backwards (e.g., "madam"). A symmetrical string has matching halves.
# Input: "madam"
# Expected Output:
def ispalindrome(string):
    if string==string[::-1]:
        print("palindrome")
    else: print("Not a palindrome")
    if string[:len(string)/2]==string[len(string)+1:]:
        print("symmatric")
    else:print("not symmetric")

# Find the Length of a String
# Explanation: Count the total characters (including spaces) in a string.
# Input: "hello world"
# Expected Output: Length: 11
def lenOfstr(str):
    cnt=0
    for ch in str:
        cnt+=1
    return cnt
print(lenOfstr("Hello world"))


# Reverse Words in a String
# Explanation: Reverse the order of words in a sentence, not the letters.
# Input: "I love Python"
# Expected Output: "Python love I"
def reverse_words(s):
    words = s.split()
    return " ".join(words[::-1])
print(reverse_words("Hello world i"))

# Remove the i-th Character from a String
# Explanation: Remove the character at a given index in a string (starting from 0).
# Input: String = "Python", i = 2
# Expected Output: "Pythn"
def remove_ith_char(s, i):
    if i < 0 or i >= len(s):
        return s   # or raise ValueError("Invalid index")
    return s[:i] + s[i+1:]
print(remove_ith_char("Hello world",5))

# Count Vowels in a String Using Sets
# Explanation: Find how many vowels (a, e, i, o, u) are in the string, using sets for efficiency.
# Input: "education"
# Expected Output: Vowels Count: 
def cntVowels(s):
    cnt=0
    for i in s:
        if i in "aeoiou":
            cnt+=1
    return cnt
print(cntVowels("Hello"))

# Eliminate Duplicate Characters from a String
# Explanation: Log Session a new string containing only the first occurrence of each character.
# Input: "programming"
# Expected Output: "progamin"
def remove_duplicates(s):
    result=""
    for ch in s:
        if ch not in result:
            result+=ch
    return result
print(remove_duplicates("Hello"))

# Identify the Least Frequent Character in a String
# Explanation: Find the character(s) that occur(s) the fewest times in a string.
# Input: "statistics"
# Expected Output: Least frequent character: 'a'
def least_freq_char(s):
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    min_count=min(freq.values())
    for ch in s:
        if freq[ch]==min_count:
            return ch
print(least_freq_char("Hello"))

# Find the Maximum Frequency Character
# Explanation: Determine which character appears most frequently in the string.
# Input: "banana"
# Expected Output: Maximum frequency character: 'a'
def max_freq_char(s):
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    max_count=max(freq.values())
    for ch in s:
        if freq[ch]==max_count:
            return ch
print(max_freq_char("Hello"))

# Check if a String Contains Special Characters
# Explanation: Check if the string contains characters other than letters or numbers.
# Input: "Hello@123"
# Expected Output: Contains special character: Yes
def contains_special_char(s):
    for ch in s:
        if not ch.isalnum():
            return True
    return False
print(contains_special_char("Hello@222"))

# Generate Random Strings Until a Target String is Formed
# Explanation: Keep generating random strings until you produce the target string.
# Input: Target = "abc"
# Expected Output: Randomly generated 'abc' after N attempts (N will vary)
import random
target="abc"
letters="abcdefghijklmnopqrstuvwxyz"
attempts=0
while True:
    attempts+=1
    guess=""
    for i in range(len(target)):
        guess+=random.choice(letters)
    if guess==target:
        print("Target found:",guess)
        print("Attempts:",attempts)
        break
    
# Check If a String is a Binary String
# Explanation: Test if the string contains only '0' and '1'.
# Input: "101101"
# Expected Output: Is binary string: Yes
def check_binary(s):
    for ch in s:
        if ch!='1' or ch!='0': return False
    return True
print(check_binary("10200111"))

# Find Close Matches for a String in a List
# Explanation: Find list entries that are similar to the given word (helpful for typo correction).
# Input: Target = "apple", List = ["apply", "apples", "ape", "maple"]
# Expected Output: Close matches: ['apply', 'apples']
target="apple"
words=["apply","apples","ape","maple"]
matches=[]
for word in words:
    diff=abs(len(word)-len(target))
    same=0
    for i in range(min(len(word),len(target))):
        if word[i]==target[i]:
            same+=1
    if diff<=1 and same>=len(target)-1:
        matches.append(word)
print("Close matches:",matches)


# Find Uncommon Words Between Two Strings
# Explanation: List words present in only one of the two strings.
# Input: "red blue green", "blue yellow red"
# Expected Output: Uncommon words: ['green', 'yellow']
def uncommon_words(s1, s2):
    words1=set(s1.split())
    words2=set(s2.split())
    result=list(words1.symmetric_difference(words2))
    return result
print(uncommon_words("blue yellow red","red blue green"))

# Swap Commas and Dots in a String
# Explanation: Replace commas with dots and dots with commas.
# Input: "23,45.89,78.90"
# Expected Output: "23.45,89.78,90"
def swap_commas_dots(s):
    s=s.replace(",","#") 
    s=s.replace(".",",")
    s=s.replace("#",".")
    return s

swap_commas_dots("23,45.89,78.90")
# Generate All Permutations of a String
# Explanation: List all possible ways to rearrange the characters.
# Input: "abc"
# Expected Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
def permutations(s):
    if len(s)==1:
        return [s]
    result=[]
    for i in range(len(s)):
        current_char=s[i]
        remaining=s[:i]+s[i+1:]
        for p in permutations(remaining):
            result.append(current_char+p)
    return result

print(permutations("abc"))