# Program: PassedStudents (Pure Python)
data = [
    {"student_id": 1, "name": "Alice", "score": 39},
    {"student_id": 2, "name": "Bob", "score": 85},
    {"student_id": 3, "name": "Charlie", "score": 40}
]

result = [{"student_id": d["student_id"], "name": d["name"]}
          for d in data if d["score"] >= 40]

for r in result:
    print(r)
