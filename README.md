# Data Analysis Project

## Overview
This project analyzes clickstream data to extract business insights, such as:
- Unique users
- Most visited pages
- Peak traffic times

## Features
- Data cleaning and preparation
- Data visualization with traffic patterns by hour
- Insights into user behavior

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/data-analysis.git
   cd data-analysis
   ```

2. Create and activate virtual environment
- On Linux/MacOS
    ```
    python3 -m venv env
    source env/bin/activate
    ```

3. Install dependencies

    ```
    pip install -r requirements.txt
    ```

4. Run project
    ```
    python src/main.py
    ```

## Requirements.txt
- After installing new dependencies, update requirements.txt to keep it in sync with the environment:
    ```
    pip freeze > requirements.txt
    ```

## Roadmap
- Implement advanced analytics (e.g., cohort analysis, heatmaps)
- Develop an interactive web dashboard (future front-end integration)
- Add API support for real-time data analysis