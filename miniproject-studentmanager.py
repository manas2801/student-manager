def load_students():
    try:
        with open ("students.txt","r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return[]
    
def save_student(name):
    with open("students.txt","a") as file:
        file.write(name + "\n")

students = load_students()

def add_student():
    name = input("Enter student name :")
    students.append(name)
    save_student(name)
    print("Student added!")

def show_students():
    if not students:
        print("No students found")
    else:
        print("Student list:")
        for s in students:
            print(s)

def search_student():
    name = input("Enter name to search:")
    if name in students:
        print("Student found!")
    else:
        print("Student not found ")

def delete_student():
    name = input("Enter name to delete:")
    if name in students:
        students.remove(name)

        # Rewrite the file with the updated student list
        with open("students.txt", "w") as file:
            for s in students:
                file.write(s + "\n")
        print("Student deleted")
    else:
        print("Student not found")

while True:
    print("\n1, Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    try:
        choice = input("Enter your choice: ")
    except ValueError:
        print("Invalid input. Please enter a number.")

    if choice == '1':
        add_student()
    elif choice == '2':
        show_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")