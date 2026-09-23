marks = {
    "Ravi": 45,
    "Aman": 75,
    "Priya": 85,
    "Rahul": 30
}

def get_result_report(marks):
    top_students = {}
    for student, mark in marks.items():
        if mark >= 80:
            top_students[student] = "Excellent"
        elif mark >= 50:
            top_students[student] = "Pass"
        else:
            top_students[student] = "Fail"
    return top_students

result = get_result_report(marks)
print(result)