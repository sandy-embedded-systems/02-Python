# Convert Snake Case to Pascal Case
# Explanation: Change a snake_case string (words separated by underscores) into PascalCase (words start with uppercase, no underscores).
# Input: "my_variable_name"
# Expected Output: "MyVariableName"
def snake_to_pascal(s):
    result=""
    for word in s.split('_'):
        if word:
            result+=word[0].upper()+word[1:]
    return result
print(snake_to_pascal("my_variable_name"))

# Find the Position of a Character in the k-th Word
# Explanation: Given a list of strings, find the position of a specific character in the k-th word.
# Input: List = ["hello", "world"], k = 2, char = "r"
# Expected Output: Position: 2
def fin_pos(l,k,ch):
    return l[k].find(ch)
print(fin_pos(["Hello","World"],1,'r'))

# Mirror Image of a String
# Explanation: Reverse the string as if viewing in a mirror.
# Input: "abcd"
# Expected Output: "dcba"
s=input("Enter string:")
print("Mirrir image:",s[::-1])

# Replace Multiple Words at Once
# Explanation: Simultaneously replace several different words in a string with new ones.
# Input: String = "I like apples and bananas.", Replace: {"apples": "oranges", "bananas": "grapes"}
# Expected Output: "I like oranges and grapes."
def replace_multiple_words(text, replacements):
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text
print(replace_multiple_words("I like apples and bananas.",{"apples": "oranges", "bananas": "grapes"}))

# Remove Punctuation from a String
# Explanation: Remove all punctuation marks, keeping only letters, digits, and spaces.
# Input: "Hello, world! How are you?"
# Expected Output: "Hello world How are you"
def remove_punctuation(s):
    result=""
    for ch in s:
        if ch.isalnum() or ch.isspace():
            result+=ch
    return result
text="Hello, world! How are you?"
print(remove_punctuation(text))

# Check if Two Strings are Rotationally Equivalent
# Explanation: Check if one string can be rotated (circularly shifted) to match the other.
# Input: "abcde", "cdeab"
# Expected Output: Rotationally equivalent: Yes


# Generate a Random Binary String
# Explanation: Log Session a string of a given length containing only random 0s and 1s.
# Input: Length = 8
# Expected Output: e.g., "10101001"
import random
def rand_str(len):
    result=""
    for i in range(1,len+1):
        result+=str(random.randint(0,1))
    return result
print(rand_str(8))
# Reverse Sort a String
# Explanation: Sort the characters of the string in descending order.
# Input: "python"
# Expected Output: "ytponh"
string=input("Enter a string:")
print("reverse sorted:",sorted(string,reverse=True))

# Validate a Password String
# Explanation: Check if a password meets certain conditions (length, special characters, etc.).
# Input: "MyPass123@"
# Expected Output: Valid password: Yes
def validate(password):
    if len(password)<8: return False
    lower=upper=digit=spl=False
    for ch in password:
        if ch.islower():
            lower=True
        elif ch.isupper():
            upper=True
        elif ch.isdigit():
            digit=True
        else :spl=True
    if (lower and upper and digit and spl): return True
    else : return False
print(validate("Mypassword@2003"))

# Pad a String with Characters
# Explanation: Add extra characters (like *, space, or 0) to the left or right of a string to 
# reach a desired length.
# Input: "cat", Length = 6, Pad char = "*"
# Expected Output: "***cat"
string=input("Enter string:")
l=int(input("Enter required length:"))
ch=input("Enter pad character:")
result=(l-len(string))*ch+string
print(result)