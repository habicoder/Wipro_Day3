while True:
    print("\nEnter your choice:")
    print("1. To write")
    print("2. To read")
    print("3. To exit")
    choice = int(input())
 
    if choice == 1:
        f1=open("E://habi.txt" ,"w")
        for _ in range(3):
                read_id = input("Enter readid: ")
                name = input("Enter name: ")
                marks = input("Enter Marks: ")
                f1.write("Read ID:"+ read_id)
                f1.write("\n")
                f1.write("NAME:" + name)
                f1.write("\n")
                f1.write("Marks:" + marks)
                f1.write("\n")
        print("Data written to habi.txt successfully.")
    elif choice == 2:
        f1=open ("E://doss.txt")
        for i in f1:
            print(i)
    elif choice == 3:
        print("Exiting")
        break
    else:
        print("Please enter a valid option.")