students = [
    {"student_id": 1, "name": "Alice", "score": 88},
    {"student_id": 2, "name": "Bob", "score": 70},
    {"student_id": 3, "name": "Charlie", "score": 92}
]

high_scorers = [
    {"student_id": s["student_id"], "name": s["name"]}
    for s in students if s["score"] > 75
]

for s in high_scorers:
    print(s)
