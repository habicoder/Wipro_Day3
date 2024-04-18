'''
Write a python script to write and read the file content doss.txt.
 
option 1 : Read id , name and marks for 3 students and write into doss.txt
 
option 2 : read  all contents doss.txt and display
 
option 3 : exit
'''
 
 
while True:
  print("1. To write        ")
  print("2. To read         ")
  print("3. To exit         ")
  
  
  choice=int(input("Enter your choice:  "))
  if choice == 1:
      f1 = open("doss.txt", "w")
      for i in range(3):
          id = input("Enter Your Id: ")
          f1.write(id)
          name = input("Enter Your Name: ")
          f1.write(name)
          marks = input("Enter Your Marks: ")
          f1.write(marks)
          f1.write("\n")
          f1.close()
  elif choice == 2:
       f1 = open("doss.txt", "r")
       for i in f1:
           print(i)
       f1.close()
  elif choice == 3:
       break
