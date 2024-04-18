
# Lab 1:
 
# Task 1 :Write a python script to read id,name,maths and science marks from the console for  5 students and write
#         into text file marks.txt. Here the columns are separated  by spaces.
 
# Task 2 :Write a python script to read  marks.txt. Find total and averagee of maths and science and 
#         display  the output in the console as per format  given below
 
#         *******************************************************************
#         id   name    maths   science     Total   average
#         *******************************************************************
#         10   Doss     70        80       150     75.00
#         ******************************************************************
#         11   Aditya   80        80        160    80
#         ***********************************1********************************


# funtions2
def write_content(id, name, maths, science ):
 f1 = open(".//marks.txt", 'a')
 f1.write(f"{id} {name} {maths} {science} ")
 f1.write("\n")
 f1.close()



def read_content():
 f1 = open(".//marks.txt", 'r')
 for i in f1:
  id ,name , maths , science = i.split()
  total = int(maths) + int(science)
  print("****************************************************")
  print(f"{id}    {name}    {maths}    {science}         {total}        {total/2}")
 f1.close()



# program start
while True:
 print('\n Option 1: To Write Student Details')
 print(' Option 2: read all student information')
 print(' Option 3: exit')

 choice = input("Enter the option: ")

 if choice == '1':
  entry = int(input("Enter the number of students: "))
  for i in range(entry):
   id = input("Enter id: ")
   name = input("Enter Name: ")
   maths = input("Enter Maths Marks: ")
   science = input("Enter Science Marks: ")
   write_content(id, name, maths, science)

 elif choice == '2':
  print("****************************************************")
  print(f"id    name    maths    science    total    Average")
  read_content()
  print("****************************************************")
 elif choice == '3':
  print("Exiting Program...")
  with open(".//marks.txt", 'w'):
   pass
  break
 else:
  print("Invalid Option")

 