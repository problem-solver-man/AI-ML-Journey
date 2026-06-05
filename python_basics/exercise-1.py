"""
==================== Problem Statement ====================

Create a program that:

Takes 5 student names.
Takes their marks.
Stores them in a dictionary.

Prints:
    • Highest marks
    • Lowest marks
    • Average marks
    • Pass/Fail status

"""

def getStudentMarks(num):
    """
    Takes input for 'n' student name and marks and returns
    a dict with names as keys and marks as values.
    e.g. students = {
        "Name1": 0
        "Name2": 1
    }
    """
    students = {}

    for i in range(num):
        name = input(f"Enter the student name {i + 1}: ")
        marks = float(input("Enter the marks: "))
        students[name] = marks
        print()
    
    print(f"Name and marks of {num} students recorded successfully.")
    print()

    return students



def showResult(dictionary):
    """
    Takes a dict as param and shows the result.
    """
    print(dictionary)
    print(f"Highest marks = {max(dictionary.values())}")
    print(f"Lowest marks = {min(dictionary.values())}")
    print(f"Average marks = {sum(dictionary.values()) / len(dictionary.values())}")
    print()

    for name, marks in dictionary.items():
        if marks >= 40:
            status = "Pass"
        else:
            status = "Fail"
        
        print(f"{name} {marks} {status}")


if __name__ == "__main__":
    data = getStudentMarks(2)
    showResult(data)