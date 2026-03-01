# 1. Lost & Found in the Supermarket
# You’re managing the stock system for a small supermarket. Each item is a key, and its count is the value. A frantic customer wants to know if “apples” are still available. How will you instantly check if “apples” are on your shelf?
# Input: stock = {'apples': 14, 'bananas': 22, 'rice': 12}, query = 'apples'
# Expected Output: Yes, apples are in stock!
stock = {'apples': 14, 'bananas': 22, 'rice': 12}
query='apples'
if query in stock.keys():
    print("Yes, apples are in stock")
else : print("No stock left")


# 2. The Magic Dictionary of Hogwarts
# Every student at Hogwarts has a pet. Sometimes, a student forgets to register a pet. If someone asks 
# for Hermione’s pet, and her name isn’t registered, you must politely tell them “No record, maybe try
# another student!” Can you build this polite pet query?
# Input: pets = {'Harry': 'owl', 'Ron': 'rat'}, query = 'Hermione'
# Expected Output: No record, maybe try another student!
pets = {'Harry': 'owl', 'Ron': 'rat'}
query = 'Hermione'
if query not in pets.keys():
    print("No record, maybe try another student!")
else: print(pets[query])

# 3. The Unique Collector’s Auction
# You’re at a collector’s auction. Each lot number is a key, and the value is the type of collectible. 
# Auctioneers want to quickly know how many unique collectibles are being auctioned, not just the 
# number of lots. Can you wow them with an instant count?
# Input: auction = {'lot1': 'coin', 'lot2': 'stamp', 'lot3': 'coin', 'lot4': 'comic'}
# Expected Output: Unique collectibles: ['coin', 'stamp', 'comic']
auction = {'lot1': 'coin', 'lot2': 'stamp', 'lot3': 'coin', 'lot4': 'comic'}
lst=[]
for key in auction:
    if auction[key] not in lst:
        lst.append(auction[key])
print("Unique collections:",lst)


# 4. Robot Warehouse – Fast Inventory Sum
# A robot does inventory at the end of the day and must tell the boss the total number of items, 
# not just per item. What’s the fastest way for the robot to add up all item counts in the warehouse?
# Input: inventory = {'box': 30, 'crate': 22, 'pallet': 8}
# Expected Output: Total items in warehouse: 60
Total=0
inventory = {'box': 30, 'crate': 22, 'pallet': 8}
for key in inventory:
    Total+=inventory[key]
print("Total items in warehouse:",Total)


# 5. The Dictionary of Two Kingdoms
# The “North” kingdom and the “South” kingdom both keep ledgers of gold reserves. Suddenly
# there’s a war—when they merge, the South’s gold value should overwrite the North’s wherever the city
# names match! What do the ledgers look like after the kingdoms unite?
# Input: north = {'Winterfell': 1000, 'The Eyrie': 800}, south = {'The Eyrie': 1200, "King's Landing": 2500}
# Expected Output: {'Winterfell': 1000, 'The Eyrie': 1200, "King's Landing": 2500}
north = {'Winterfell': 1000, 'The Eyrie': 800}
south = {'The Eyrie': 1200, "King's Landing": 2500}
north.update(south)
print(north)

# 6. Secret Spy Codes
# You intercepted a list of coded messages (keys), but your team uses new code names (a mapping).
# How will you quickly rename every code to its new secret label?
# Input: codes = {'alpha': 'ok', 'beta': 'wait'}, new_labels = {'alpha': 'red', 'beta': 'blue'}
# Expected Output: {'red': 'ok', 'blue': 'wait'}
codes = {'alpha': 'ok', 'beta': 'wait'}
new_labels = {'alpha': 'red', 'beta': 'blue'}
mapped={}
for key in new_labels:
    mapped[new_labels[key]]=codes.get(key)
print(mapped)

# 7. Erase the Forbidden Spells
# You have a dictionary of spells, but some spells are now forbidden. Given a list of banned 
# spell names, wipe them from your magic book!
# Input: spells = {'fireball': 5, 'healing': 10, 'curse': 2}, banned = ['curse', 'fireball']
# Expected Output: {'healing': 10}
spells = {'fireball': 5, 'healing': 10, 'curse': 2}
banned = ['curse', 'fireball']

for spell in banned:
    if spell in spells:
        del spells[spell]
print(spells)

# 8. The Cafe’s Popular Menu
# Every order is tracked in a list. Can you build a menu board that shows how many times each item was ordered today?
# Input: orders = ['latte', 'espresso', 'latte', 'tea', 'espresso', 'latte']
# Expected Output: {'latte': 3, 'espresso': 2, 'tea': 1}
orders = ['latte', 'espresso', 'latte', 'tea', 'espresso', 'latte']
menu={}
for item in orders:
    if item in menu:
        menu[item]+=1
    else: menu[item]=1
print(menu)

# 9. Update the Employee Profile
# A nested dictionary holds employee info. An employee changed their phone number. Update it without touching the rest of their info.
# Input: profile = {'info': {'name': 'Sam', 'phone': '555-1234'}}, new_phone = '555-9999'
# Expected Output: {'info': {'name': 'Sam', 'phone': '555-9999'}}
profile = {'info': {'name': 'Sam', 'phone': '555-1234'}}
new_phone = '555-9999'
profile['info']['phone']=new_phone
print(profile)
# 10. Pairing the Guest List
# You have two lists: guest names and their seat numbers. Match each guest
# to their seat for the dinner plan!
# Input: names = ['Alice', 'Bob', 'Eve'], seats = [5, 12, 8]
# Expected Output: {'Alice': 5, 'Bob': 12, 'Eve': 8}
names = ['Alice', 'Bob', 'Eve']
seats = [5, 12, 8]
d={}
i=0
while i<len(names):
    d[names[i]]=seats[i]
    i+=1
print(d)
