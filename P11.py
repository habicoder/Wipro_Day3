# [11:24 AM] N Murugadoss (Unverified)
# Write a python script to write and read the file content doss.txt.
 
# option 1 : Read id , name and marks for 3 students and write into doss.txt
 
# option 2 : read  all contents doss.txt and display
 
# option 3 : exit
 
 

# funtions
def write_content(id, name, marks):
 f1 = open(".//doss.txt", 'a')
 f1.write(f"{id} {name} {marks}")
 f1.write("\n")
 f1.close()



def read_content():
 f1 = open(".//doss.txt", 'r')
 for i in f1:
  print(i.strip())
 f1.close()



# program start
while True:
 print('\n Option 1: Write id , name and marks for 3 students')
 print(' Option 2: read all student information')
 print(' Option 3: exit')

 choice = input("Enter the option: ")

 if choice == '1':
  for i in range(3):
   id = input("Enter id: ")
   name = input("Enter Name: ")
   marks = int(input("Enter marks: "))
   write_content(id, name, marks)

 elif choice == '2':
  read_content()
 elif choice == '3':
  print("Exiting Program...")
  break

 