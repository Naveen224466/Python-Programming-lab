'''write a python program to reverse each word of entered sentence.'''

a=input("enter a sentence: ")
a=a[::-1]
out=a.split()[::-1]
res=' '.join(out)
print(res)   




    
  
