with open("demo.txt","r")as f :
 text=f.read()
 update_text= text.replace("java","python")
 
  

with open("demo.txt", "w") as f:
 f.write(update_text)
 

   
   