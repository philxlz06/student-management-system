students = []

def add_student():  
    name=input("Enter student name: ")
    student_id=input("Enter student ID: ")
    grade= input("Enter student grade: ")

    student={
        "name": name,
        "id": student_id,
        "grade": grade
    }

    students.append(student)
    print("Student added sucessfully\n")

def view_student():
    if not students:
        print("No students found.\n")
        return
    
    print("\n All students:")
    for student in students:
        print(f" Name: {student['name']}, ID: {student['id']},Grade: {student['grade']}")
        print()

def search_student():
    search_id = input("Enter student ID to search: ")
    found = False

    for student in students:
        if student["id"] == search_id:
            print(f"\n Found student - Name: {student['name']}, Grade: {student['grade']}\n")
            found= True
            break
    
    if not found:
        print("Student not found \n ")

def delete_student():
    delete_id = input("Enter student ID to delete: ")
    for i,student in enumerate(students):
        if student["id"] == delete_id:
            del students[i]
            print(" Student deleted sucessfully \n")
            return
    print("Student not found\n")


def main():
    while True:
        print("==== STudent Management System====")
        print("1. Add student")
        print("2. View ALL students")
        print("3. Search Student by ID")
        print("4. Delete Student")
        print("5. Exit")

        choice =input("Enter your choice (1-5): ")

        if choice =="1":
            add_student()
        elif choice=="2":
            view_student()
        elif choice =="3":
            search_student()
        elif choice=="4":
            delete_student()
        elif choice=="5":
            print("GOODBYE")
            break
        else:
            print("Invalid choice. Please try again\n")

if __name__=="__main__":
    main()

