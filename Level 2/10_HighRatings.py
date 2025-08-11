# Program: HighRatings (Pure Python)
data = [
    {"movie_id": 1, "title": "Movie A", "rating": 4.4},
    {"movie_id": 2, "title": "Movie B", "rating": 4.7},
    {"movie_id": 3, "title": "Movie C", "rating": 5.0}
]

result = [{"movie_id": d["movie_id"], "title": d["title"]}
          for d in data if d["rating"] >= 4.5]

for r in result:
    print(r)
