Student_grades = {}

def add_student(name, grade):
    Student_grades[name] = grade
    print(f"Added {name} with grade: {grade}")

def update_student(name, new_grade):
    if name in Student_grades:
        Student_grades[name] = new_grade
        print(f"{name}'s grade has been updated to {new_grade}")
    else:
        print(f"{name} not found.")

def del_student(name):
    if name in Student_grades:
        del Student_grades[name]
        print(f"{name}'s record has been deleted successfully.")
    else:
        print(f"{name} not found.")

def view_students():
    if Student_grades:
        for name, grade in Student_grades.items():
            print(f"{name} - {grade}")
    else:
        print("No records found.")

def main():
    while True:
        print("\n_Student Grades Management System_")
        print("Press 1 to Add a new Student")
        print("Press 2 to Update student grades")
        print("Press 3 to Delete a student record")
        print("Press 4 to View all student records")
        print("Press 5 to Exit")

        try:
            choice = int(input("Please enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            add_student(name, grade)
        elif choice == 2:
            name = input("Enter student name: ")
            new_grade = input("Enter new student grade: ")
            update_student(name, new_grade)
        elif choice == 3:
            name = input("Enter student name: ")
            del_student(name)
        elif choice == 4:
            view_students()
        elif choice == 5:
            print("Closing the program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
