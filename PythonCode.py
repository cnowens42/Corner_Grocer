#  Curtis Owens
#  CS 210: Programming Languages
#  Professor Ksendemir
#  December 11, 2022

'''
Project 3 summary:
The Corner Grocer needs a program that analyzes the text records they generate throughout the day. These records list
items purchased in chronological order from the time the store opens to the time it closes. They are interested in
rearranging their produce section and need to know how often items are purchased so they can create the most effective
layout for their customers. The program that the Corner Grocer is asking you to create should address the following
three requirements for a given text-based input file that contains a list of purchased items for a single day:

Produce a list of all items purchased in a given day along with the number of times each item was purchased.
Produce a number representing how many times a specific item was purchased in a given day.
Produce a text-based histogram listing all items purchased in a given day, along with a representation of the
number of times each item was purchased.

'''


import re # For regular expression operations.
import string # For common string operations.

#  Python functtion opening and reading from a file:
grocery_items = dict()
input_file = open("cornerGrocer.txt", "r")
for line in input_file:
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word in grocery_items:
            grocery_items[word] = grocery_items[word] + 1
        else:
            grocery_items[word] = 1
input_file.close()

#  Python functtion that prints each item purchased along with its quantity:
def printItemCount():
    print("\nQUANTITY OF EACH ITEM PURCHASED TODAY\n")
    for item in list(grocery_items.keys()):
        print(item, end = "")
        print(":", grocery_items[item])
    print()

#  Python functtion that prints a user specified item:
def printCount(userItem):
    userItem = userItem.capitalize()
    for item in list(grocery_items.keys()):
        if (userItem == item):
            return grocery_items[item]
    return 0

#  Python functtion creates a file and writes the items and quanitities to it:
def createFile(fileName):
    input_file = open(fileName, "w")
    for item in list(grocery_items.keys()):
        input_file.write("\n" + item + " " + str(grocery_items[item]))
    input_file.close()
    return 0