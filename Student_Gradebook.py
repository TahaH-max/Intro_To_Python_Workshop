students = {}

def addStudent():
    name = input("What is the Students name: ")
    grade_input = input("What are the grades? spaced out by 1: ")
    grades = list(map(float, grade_input.split()))
    students[name] = grades
    print("Student added")

def viewAllStudents():
    for name, grades in students.items():
        avg = sum(grades) / (len(grades))
        print(name, ", Grades: ", grades, ". Average: ", avg)

def searchStudent():
    name = input("What is the students name? ")
    if name in students:
        print(name, "Grades: ", students[name], ". Average: ", (sum(students[name]) / len(students[name])))
    else:
        print("Student not found.")

def updateGrades():
    name = input("What is the students name? ")
    if name in students:
        grades = students[name]
        updated = input("How would you like to update? Enter new grades space-separated: ")
        students[name] = list(map(float, updated.split()))
        print("Updated. ")
    else:
        print("Student not found")
        
def main():
    while True:
        print("\n1. Add student\n2. View all\n3. Search student\n4. Update grades\n5. Exit")
        choice = int(input("Which one? Choose a number: "))
        if choice == 1:
            addStudent()
        elif choice == 2:
            viewAllStudents()
        elif choice == 3:
            searchStudent()
        elif choice == 4:
            updateGrades()
        elif choice == 5:
            print("Goodbye")
            break
        else:
            print("Invalid entry")
main()

