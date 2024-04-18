'''
Task 2 :Write a python script to read  marks.txt. Find total and averagee of maths and science and 
        display  the output in the console as per format  given below
 
        *******************************************************************
        id   name    maths   science     Total   average
        *******************************************************************
        10   Doss     70        80       150     75.00
        ******************************************************************
        11   Aditya   80        80        160    80
        *******************************************************************
        

[2:50 PM] N Murugadoss (Unverified)
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
 
 
f=open("marks.txt")

print("*************************************")

print("Id  Name  Math  Scie  Total  Avg     ")

print("*************************************")
 
for rec in f:

  id,name,maths,scie=rec.split(" ")

  total=int(maths)+int(scie)

  avg=total/2.0

  print(id,name,maths,scie,total,avg)
 
  print("*************************************")
 
 
f.close()
 
 
  
