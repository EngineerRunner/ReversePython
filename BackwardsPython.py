import os
import sys

try:
    random = sys.argv[1]
except:
    sys.exit("USAGE: 'BackwardsPython.py [path to file]'")
def reverse_list(listy):
    output = []
    for item in listy:
        output.insert(0,item)
    return output

def reverse_item(item):
    r = []
    for letter in item:
        r.append(letter)
    return reverse_list(r)

def full_reverse(listy):
    listy = reverse_list(listy)
    newlist = []
    for item in listy:
        newlist.append(''.join(reverse_item(item)))
    return(newlist)

with open(sys.argv[1]) as file:
    lines = [line.rstrip() for line in file]
inputlist = []
for x in lines:
    inputlist.append(x)

newlist = full_reverse(inputlist)
newlist = '\n'.join(newlist)
exec(newlist)