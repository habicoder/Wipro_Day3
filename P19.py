# text files manipulation
# writig into a text file
 
f1=open("D://doss.txt" ,"w")  # w mode erases  previous contents it it exist
name=input("Enter name  ")
f1.write(name)
age=input("Enter age  ")
f1.write(" " + age)