# Write a function to reverse a string.
# e.g. Giving input of string "Ivy", the function should return "yvI".
# Suppose the function name is "reverse_string".
# I can call this function like this:
#  reversed_name = reverse_string("Ivy")
# reversed_name should be "yvI" now.
#x = 0
def reverseMe(in_str):
    newStringList = []
    x = len(in_str) - 1
    while x != -1 :
        newStringList.extend(in_str[x])
        x -= 1
    return "".join(newStringList)
    

def reverse_cheating(in_str):
    newStringList = []
    newStringList.extend(in_str)
    newStringList.reverse() 
    return "".join(newStringList)

def reverse_oneline(in_str):
    return in_str[::-1]

reverse_ivy = reverse_oneline("Ivy")
print("Ivy, I reversed your name as: ", reverse_ivy)
reverse_jonathan = reverse_string("Jonathan")
print("Reverse myself is: ", reverse_jonathan)
reverse_echo = reverse_oneline("echo")
print("Reverse myself is: ", reverse_echo)