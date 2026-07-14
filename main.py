# main.py

from input import get_movies
from analysis import analyze_movies, recommend_movies
from visualizer import show_chart

movies = {}

while True:
    print("\n============================")
    print("    Movie Rating Analyzer")
    print("============================")
    print("1. Add Movies")
    print("2. Show Analysis")
    print("3. Show Recommendations")
    print("4. Show Chart")
    print("5. Exit")
    print("============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        movies=get_movies()
    elif choice == "2":
        if movies:
            analyze_movies(movies)
        else:
            print("No movies added! Add movies first")
    elif choice == "3":
        recommend_movies(movies)
    elif choice == "4":
        chart=show_chart(movies)
    elif choice == "5":
        print("Goodbye! 🎬")
        break
    else:
        print("Invalid choice! Try again.")