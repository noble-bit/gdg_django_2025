grades = {
    "John": "A",
    "Sara": "B",
    "Musa": "A"
}


inverted = {}

for student, grade in grades.items():
    if grade not in inverted:
        inverted[grade] = [student]  
    else:
        inverted[grade].append(student)  

print(inverted)



