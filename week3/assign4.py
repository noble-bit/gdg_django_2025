def get_grade(student_grades, student_name):
    
    try:
        return student_grades[student_name]
    except KeyError:
        return "student no found in the system"

grades = {
    
    'Nebil':99,
    'Surafel':15,
    'Manche':0

}

print(get_grade(grades, "Nebil"))
print(get_grade(grades, "Surafel"))
