# visualizer.py

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def show_chart(movies):
    names = list(movies.keys())
    ratings = list(movies.values())

    bars = plt.bar(names, ratings, color=["gold", "red", "skyblue"])

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.1,
            str(height),
            ha="center"
        )

    plt.title("My Movie Ratings")
    plt.xlabel("Movies")
    plt.ylabel("Rating (0-10)")
    plt.show()