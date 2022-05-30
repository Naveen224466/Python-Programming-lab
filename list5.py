#5. Sort the list by the length of string elements.

a=input("enter comma seperated list: ")
lst=a.split(",")
lst.sort(key=len)  #on the basis if length
print(lst)
