# 🎬 Movie Rating Analyzer

A simple Python mini project that allows users to enter movie names and ratings, analyze the collected data, generate recommendations, and visualize ratings using Matplotlib.

This project is completely menu-driven and demonstrates the use of Python functions, modules, lists, dictionaries, loops, conditional statements, and data visualization.

---

# 📌 Project Objective

The objective of this project is to collect movie ratings from users and provide useful insights through analysis and graphical visualization.

The project is divided into multiple modules, where each menu option performs a different task.

---

# ✨ Features

The project provides **5 main functionalities**:

## 1. Get Movies from User

This option allows users to enter movie details.

### Tasks Performed
- Accept movie names.
- Accept ratings for each movie.
- Validate the entered rating.
- Store all movie information.
- Allow multiple movie entries.

---

## 2. Show Analysis

This option analyzes all the movies entered by the user.

### Analysis Includes

- Total number of movies
- Average rating
- Highest-rated movie
- Lowest-rated movie

This helps users understand the overall performance of the entered movie collection.

---

## 3. Show Recommendations

Based on movie ratings, the program recommends movies.

### Recommendation Logic

- Movies with higher ratings are recommended.
- Lower-rated movies are not recommended.

This gives users a quick list of the best movies from their collection.

---

## 4. Show Chart (Matplotlib)

This option creates a graphical representation of movie ratings.

### Chart Details

- X-axis → Movie Names
- Y-axis → Ratings
- Bar Chart using Matplotlib
- Easy visualization of rating comparisons

---

## 5. Exit

Terminates the application safely.

---

# 📂 Project Structure

```
Movie_Rating_Analyzer/
│
├── main.py              # Main menu and program execution
├── input.py             # Handles movie input from users
├── analysis.py          # Performs movie analysis
├── visualizer.py        # Displays charts using Matplotlib
├── README.md
```

---

# 🔄 Project Workflow

```
                START
                   │
                   ▼
          Display Main Menu
                   │
     ┌─────────────┼──────────────┐
     │             │              │
     ▼             ▼              ▼

1. Get Movies   2. Show      3. Show
   from User     Analysis   Recommendations
     │             │              │
     └──────┬──────┴──────┬───────┘
            │             │
            ▼             ▼
     4. Show Chart (Matplotlib)
            │
            ▼
        5. Exit Program
```

---

# 🛠 Technologies Used

- Python 3
- Matplotlib

---

# 📚 Python Concepts Used

- Functions
- Modules
- Lists
- Dictionaries
- Loops
- Conditional Statements
- User Input
- Exception Handling
- Data Analysis
- Data Visualization

---

# ▶️ How to Run

### Step 1

Install Python 3.

### Step 2

Install Matplotlib

```bash
pip install matplotlib
```

### Step 3

Run the project

```bash
python main.py
```

---

# 📋 Sample Menu

```
========= Movie Rating Analyzer =========

1. Get Movies from User
2. Show Analysis
3. Show Recommendations
4. Show Chart
5. Exit

Enter your choice:
```

---

# 📊 Example

### Input

```
Movie : Interstellar
Rating : 9.5

Movie : Avatar
Rating : 8

Movie : Titanic
Rating : 7
```

### Analysis

```
Total Movies : 3

Average Rating : 8.17

Highest Rated Movie :
Interstellar (9.5)

Lowest Rated Movie :
Titanic (7.0)
```

### Recommendation

```
Recommended Movies

⭐ Interstellar
⭐ Avatar
```

### Chart

A Matplotlib bar chart is displayed showing movie ratings.

---

# 🚀 Future Enhancements

- Save movie data to a file
- Load previous movie data
- Search movies
- Delete movies
- Update ratings
- Sort movies by rating
- Pie chart visualization
- Export analysis report

---

# 👨‍💻 Author

**Naveen prabu**

Python Mini Project

---

# 📄 License

This project is created for educational purposes and learning Python programming.