#3. Write a Python program to append text to a file and display the text.
f=open("E:\File H\hell.txt",'a')
f.write("                   ---:SECOND STUDENT DETAIL:---     \n\n\n")
n=input("enter name: ")
sec=input("enter sec: ")
col=input("enter college name: ")
roll=eval(input("enter university roll no: "))
a=f"NAME: {n}\nSECTION: {sec}\nCOLLEGE: {col}\nUNIVERSITY ROLL NO.: {roll}"
f.write(a)
f.write("\n")
print("your data is sucessfully saved.")
f.close()

