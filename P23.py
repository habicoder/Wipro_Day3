'''
Lab 1:
 
Task 1 :Write a python script to read id,name,maths and science marks from the console for  5 students and write
        into text file marks.txt. Here the columns are separated  by spaces.
 

        '''

f=open("marks.txt","w")
for i in range(3):
    id=input("Enter id   ")
    name=input("Enter name  ")
    maths=input("Maths Marks")
    scie=input("Science Marks")
    f.write(id+" "+name+" "+maths+" "+scie)
    f.write("\n")
f.close()
