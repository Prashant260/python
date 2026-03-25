with open("demo.txt",'r')as f:
  text=f.read()
found = text.rfind("found")
if found==True:
  print("the word exists \n")
  