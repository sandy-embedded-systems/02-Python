# Detect URLs Within a String
# Explanation: Extract all URLs from the string.
# Input: "Check this link: https://openai.com and http://github.com"
# Expected Output: URLs found: ['https://openai.com', 'http://github.com']
import re
text="Check this link: https://openai.com and http://github.com"
urls=re.findall(r'https?://\S+',text)
print("URLs found:",urls)


# Execute Code Stored in a String
# Explanation: Run the code present in the string (useful but risky if input is untrusted).
# Input: "print(5+2)"
# Expected Output: 7
code="print(5+2)"
exec(code)


# Print the Middle Character of a String
# Explanation: Display the character(s) at the center of the string.
# Input: "python"
# Expected Output: Middle character: 't' and 'h'
def middle_character(s):
    n=len(s)
    mid=n//2
    if n%2==0:
        return s[mid-1:mid+1]
    else:
        return s[mid]
print(middle_character("Bitsilica"))

# Convert Integer to String and Vice Versa
# Explanation: Change a number to a string, and a string of digits to an integer.
# Input: Integer = 123, String = "456"
# Expected Output:
# Integer to string: '123'
# String to integer: 456
def convert(num):
    if isinstance(num,int):
        return str(num)
    else: return int(num)
print("int ro str:",convert(3333))
print("str to int",convert("1234"))

# Split a String into a List of Characters
# Explanation: Break the string into individual characters.
# Input: "dog"
# Expected Output: ['d', 'o', 'g']
def str_to_list(s):
    return list(s)
print(str_to_list("Hello"))

# Convert a List or Tuple of Characters to a String
# Explanation: Combine list/tuple elements into a single string.
# Input: ['p', 'y', 't', 'h', 'o', 'n']
# Expected Output: "python"
def convert_list(l):
    return "".join(l)
print(convert_list(['h','e','l','l','o']))

# Sort a List of Strings Alphabetically
# Explanation: Arrange the list of strings in lexicographical order.
# Input: ["pear", "apple", "banana"]
# Expected Output: ['apple', 'banana', 'pear']
def sort_list(l):
    return l.sort()
print(sort_list(["banana","mango","apple"]))

# Convert a String to a Set (Unique Characters)
# Explanation: Keep only unique characters from the string.
# Input: "balloon"
# Expected Output: {'b', 'a', 'l', 'o', 'n'}
string="Programming world"
string=set(string)
print(string)

# Generate All Valid IP Addresses from a String
# Explanation: Given a string of digits, form all possible valid IP addresses.
# Input: "25525511135"
# Expected Output: ['255.255.11.135', '255.255.111.35']
s="25525511135"
result=[]
n=len(s)
for i in range(1,4):
    for j in range(i+1,i+4):
        for k in range(j+1,j+4):
            if k<n:
                p1=s[:i]
                p2=s[i:j]
                p3=s[j:k]
                p4=s[k:]
                if int(p1)<=255 and int(p2)<=255 and int(p3)<=255 and int(p4)<=255:
                    if(str(int(p1))==p1 and str(int(p2))==p2 and str(int(p3))==p3 and str(int(p4))==p4):
                        result.append(p1+"."+p2+"."+p3+"."+p4)
print(result)


# Convert Numeric Words to Actual Numbers
# Explanation: Replace words like 'one', 'two' with their numeric equivalents.
# Input: "I have one apple and two oranges."
# Expected Output: "I have 1 apple and 2 oranges."
def convert_numeric_words(sentence):
    word_to_number={
        "zero":"0","one":"1","two":"2","three":"3",
        "four":"4","five":"5","six":"6",
        "seven":"7","eight":"8","nine":"9",
        "ten":"10"
    }
    words=sentence.split()
    result=[]
    for word in words:
        clean_word=word.lower().strip(".,!?")
        if clean_word in word_to_number:
            number=word_to_number[clean_word]
            result.append(word.replace(clean_word,number))
        else:
            result.append(word)
    return " ".join(result)
print(convert_numeric_words("I have onve apple and two oranges"))

# Find the Location of a Word in a String
# Explanation: Find the index where a word first appears in the string.
# Input: String = "welcome to python", Word = "python"
# Expected Output: Position: 11
def position(s,word):
    return s.find(word)
print(position("Hello world","world"))

# Frequency of Consecutive Characters
# Explanation: Count how many times each character repeats in sequence.
# Input: "aabccddd"
# Expected Output: {'a': 2, 'b': 1, 'c': 2, 'd': 3}
def consecutive_frequency(s):
    if not s:
        return {}
    result={}
    count=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count+=1
        else:
            result[s[i-1]]=count
            count=1
    result[s[-1]]=count
    return result
print(consecutive_frequency("aabccddd"))

# Rotate a String by k Positions
# Explanation: Shift characters in the string to the right by k positions.
# Input: String = "hello", k = 2
# Expected Output: "lohel"
def rotate_string(s, k):
    if len(s)==0:
        return s
    k=k%len(s)   
    return s[-k:]+s[:-k]
print(rotate_string("Hello",3))

# Example
print(rotate_string("hello", 2))
# Minimum Rotations to Get the Original String
# Explanation: Count the rotations needed for a string to return to its original form.
# Input: "abcde"
# Expected Output: 5
def min_rotations_to_original(s):
    original=s
    rotated=s
    count=0
    while True:
        rotated=rotated[1:]+rotated[0]
        count+=1
        if rotated==original:
            return count
print(min_rotations_to_original("Hello"))

# Count Frequency of Words in String (Short Form)
# Explanation: Show how many times each word appears.
# Input: "apple apple orange"
# Expected Output: {'apple': 2, 'orange': 1}
def word_frequency(s):
    freq={}
    for word in s.split():
        freq[word]=freq.get(word, 0)+1
    return freq
print(word_frequency("apple apple orange"))