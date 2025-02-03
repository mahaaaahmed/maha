def displayValues(name, age, height, is_student):
    print(name)
    print(age)
    print(height)
    print(is_student)

name = input("Please enter a name: ")
age = int(input("Please enter an age: "))
height = float(input("Please enter a height: "))
is_student = bool(input("Please enter whether or not you are a student: "))


displayValues(name,age,height,is_student)
