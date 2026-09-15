
def find_grade(marks):
    print("Student Grades")
    while marks != -1:
        if marks >= 80:
            print(f"{marks} is HD")
        elif marks >= 70:
            print(f"{marks} is D")
        elif marks >= 60:
            print(f"{marks} is  C")
        elif marks >= 50:
            print(f"{marks} is P")
        else:
            print(f"{marks} is F")
        marks= float(input("enter your marks (-1 to exit): "))
    print("Goodbye!")

find_grade(float(input("enter your marks (-1 to exit): ")))