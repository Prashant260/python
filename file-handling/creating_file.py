# creating a file .txt and adding some of the data into it.
with open("demo.txt",'+a') as f:
    f.writelines("Hi everyone")
    f.writelines("\n We are learning File I/O")
    f.writelines("\n using java.")
    f.writelines("\n i like programming in java.")
