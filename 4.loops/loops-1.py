#loops are the function which is used to do something again and again

a="suhani"
L=[1,2,3,4,5,6,7,8,9]
L1=[]
L2=[]
for i in a :
  print(i)

#to print the string in uppercase each word one by one
for i in a :
  print(i.upper())

# to print only odd numbers only :
for i in L :
  if (i%2 == 0) :
    L1.append(i)
  else: 
    continue
print("L1= ",L1)

#to print a list of elements with addition of 2 in each element
for i in L :
  print(i+2)

# to print the addition of elements in the list
m=0
for i in L:
  m=i+m
print ("sum of all the elements are : ",m)
    
