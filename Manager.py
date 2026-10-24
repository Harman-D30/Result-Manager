students={}
print("\n -----Welcome to the Result Manager System-----")
while True:
    print("\n    You have 4 options   ")
    print("1. You can add students result")
    print("2. You can view student result")
    print("3. You can check student result")
    print("4. You can exit Result Manager System")

    choice=input("\n Enter your choice(1,2,3,4): ")

    # For adding student

    if choice == "1":
        student_name=input("\n Enter the name of student (add only letters) : ")
        student_marks=int(input("Enter the marks of student (add only numbers) : "))
        students[student_name]=student_marks
        print(f"\n --Added the result of {student_name}--")


    # for viewing result

    elif choice == "2":
        if  not students:
            print("\n ---Students result do not exist---")

        else:
            print("\n-----Result-----")
            for student_name,student_marks in students.items():
                print(student_name,":",student_marks)
            print("---You can see result of all students---")   

    # for checking result

    elif choice == "3":
        student_name=input("Enter the name of student (add only letters) : ")

        if student_name not in students:
            print("\n ---Student do not exist in results---")

        else:
            student_marks = students[student_name]
            
            if student_marks>=27:
                print(f"\n {student_name} has passed with {student_marks}")
            
            elif student_marks<27:
                print(f"\n {student_name} has failed with {student_marks}")
        

    # for exiting 

    elif choice == "4":
        print("\n -----exiting-----")
        print("\n -----Thank You!-----")
        break

    # for invalid option
    else:
        print("\n ---option is invalid---")
        print("     ---Try again---")

