marks = {
    "Ravi": 45,
    "Aman": 75,
    "Priya": 85,
    "Rahul": 30
}

def get_failed_students(marks):
    failed_students = []
    for student, mark in marks.items():
        if mark < 50:
            failed_students.append(student)
    return failed_students

result = get_failed_students(marks)
print(result)