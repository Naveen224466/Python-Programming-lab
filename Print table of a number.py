'''5. Program to display the table of an entered number in the following format:
2*1=2
2*2=4
………..
2*10=20'''

x=eval(input("enter a number : "))
a=range(1,11)
for i in a:
    b=x*i
    print(f"{x}*{i} = {b}")
    