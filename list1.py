'''1. Create a program that will keep track of items for a shopping list. The program should keep asking for new 
items until nothing is entered (no input followed by enter/return key). The program should then display 
the full shopping list.'''

itm=input("enter comma seperated item: ")
list=itm.split(",")
print("final shopping list",list)

