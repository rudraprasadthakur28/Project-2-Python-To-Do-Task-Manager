marks = {
    "Ravi": 45,
    "Aman": 75,
    "Priya": 85,
    "Rahul": 30
}

def count_passed_students(marks):
    count = 0
    for student, mark in marks.items():
        if mark >= 50:
            count +=1
    return count

result = count_passed_students(marks)
print(result)