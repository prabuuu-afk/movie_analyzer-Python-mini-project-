# input.py

def get_movies():
    movies = {}
    n = int(input("How many movies? "))

    for i in range(n):
        while True:
            movie_name = input("Enter movie name: ")
            if movie_name.isalpha():
                break
            else:
                print("Invalid! Use letters only.")

        while True:
            try:
                rating = float(input("Enter rating (0-10): "))
                if 0 <= rating <= 10:
                    break
                else:
                    print("Rating must be between 0 and 10!")
            except ValueError:
                print("Please enter a number!")

        movies[movie_name] = rating
    
    return movies      # ← very important! sends data back