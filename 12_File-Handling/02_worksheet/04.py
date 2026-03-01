'''
Group Logs by Module
Using the output from Question 3, write a function that groups log entries by their module.
For each module, output the count of log entries.
Challenge: Use dictionary comprehensions or iterative methods to build the grouped result.
'''

def group_by_module(logs):
    result={}
    for entry in logs:
        module=entry["module"]
        if module not in result:
            result[module]=0
        result[module]+=1
    return result
logs=[
{'timestamp':'2026-03-01 10:15:23','log_level':'INFO','module':'auth','message':'User login successful'}
]
print(group_by_module(logs))