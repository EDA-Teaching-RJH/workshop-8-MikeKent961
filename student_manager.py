def addStudent(name, age, grade):
    with open("students.txt", "a") as file:
        file.write(f"{name}, {age}, {grade}\n")

def displayStudents():
    with open("students.txt", "r") as file:
        studentList = file.readlines()
        return studentList
  
def findStudent(name):
    displayStudents()
    for i in displayStudents():
        if i.split(",")[0] == name:
            return i.split(",")

def testManager():
    addStudent("Jack", 12, "D")
    addStudent("Nick", 63, "A")
    print(displayStudents)
    assert findStudent("Jack") == ['Jack', ' 12', ' D\n']
    assert findStudent("Nick") == ['Nick', ' 63', ' A\n']


def main():
    userChoice = ""
    while userChoice != "quit":
        userChoice = input("What would you like to do?\nadd\ndisplay\nsearch\nquit\nEnter here: ").lower()

        if userChoice == "add":
            name = input("What is student name?: ")
            age = int(input("What is the age of the student?: "))
            grade = input("What grade does the student have?: ")
            addStudent(name, age, grade)
            print("")

        elif userChoice == "display":
            for i in displayStudents():
                print(i)

        elif userChoice == "search":
            find = input("What is the name of the student you are searching for?: ").lower().capitalize()
            found = findStudent(find)
            print(found)
            print(f"Name: {found[0]}\nAge: {found[1]}\nGrade: {found[2]}")

        


main()