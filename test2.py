marks = {
    "Ravi": 45,
    "Aman": 75,
    "Priya": 85,
    "Rahul": 30
}

def get_passed_students(marks):
    passed_students = []
    for student, mark in marks.items():
        if mark >= 50:
            passed_students.append(student)
    return passed_students

result = get_passed_students(marks)
print(result)