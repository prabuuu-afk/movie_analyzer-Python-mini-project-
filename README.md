# Movie Rating Analyzer 🎬

## Overview
Movie Rating Analyzer is a Python console-based mini project that allows users to store movie ratings, analyze them, generate recommendations, and visualize ratings using a bar chart. The project demonstrates Python fundamentals including modular programming, dictionaries, loops, functions, input validation, and data visualization with Matplotlib.

## Features
- Add multiple movies with ratings (0–10)
- Input validation for movie names and ratings
- Calculate average movie rating
- Find highest-rated and lowest-rated movies
- Recommend movies with ratings of 8 or above
- Display ratings as a bar chart

## Project Structure
```
main.py          # Menu-driven application
input.py         # Collects and validates user input
analysis.py      # Performs analysis and recommendations
visualizer.py    # Displays bar chart using Matplotlib
README.md        # Project documentation
```

## Workflow
1. Start the application by running `main.py`.
2. Select **Add Movies** and enter movie names and ratings.
3. Choose **Show Analysis** to view:
   - Average rating
   - Highest-rated movie
   - Lowest-rated movie
4. Choose **Show Recommendations** to list movies rated 8 or above.
5. Choose **Show Chart** to visualize ratings.
6. Exit the application.

## Technologies Used
- Python 3
- Matplotlib

## Concepts Demonstrated
- Modular Programming
- Functions
- Dictionaries
- Loops
- Conditional Statements
- Exception Handling
- Data Visualization

## Installation
```bash
pip install matplotlib
```

## Run
```bash
python main.py
```

## Sample Output
```text
Movie Rating Analyzer
1. Add Movies
2. Show Analysis
3. Show Recommendations
4. Show Chart
5. Exit
```

## Future Improvements
- Allow movie names with spaces and numbers.
- Save movie data to a file.
- Load previously saved movies.
- Sort movies by rating.
- Add genre and release year.
- Export analysis as a report.

## Author
Python Mini Project - Movie Rating Analyzer
