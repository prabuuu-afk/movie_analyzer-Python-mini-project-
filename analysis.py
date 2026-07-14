# analysis.py

def analyze_movies(movies):
    ratings = list(movies.values())
    avg = round(sum(ratings) / len(ratings), 2)
    best = max(movies, key=lambda m: movies[m])
    worst = min(movies, key=lambda m: movies[m])

    print("\n--- Movie Analysis ---")
    print(f"Average Rating : {avg}")
    print(f"Highest Rated  : {best} ({movies[best]})")
    print(f"Lowest Rated   : {worst} ({movies[worst]})")


def recommend_movies(movies):
    print("\n--- Recommended Movies (Rating ≥ 8) ---")
    found = False
    for mov, rate in movies.items():
        if rate >= 8:
            print(f"{mov} : {rate} ⭐")
            found = True
    if not found:
        print("No recommendations found.")