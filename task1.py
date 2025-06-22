# create dic of student marks

name=input("Enter the student's name: ")

std={
    'Mike':45,
    'Kate':40,
    'Nick':39,
    'Riya':33
}

if name in std:
    result=std.get(name)
    print(f"{name} mark: {result}")
else:
    print("Student not found.")