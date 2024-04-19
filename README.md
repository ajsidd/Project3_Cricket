# Cricket Players App

A simple Flask web application to display and filter cricket players based on their bowling style, batting style, and position.

## Features

- Filter players by bowling style
- Filter players by batting style
- Filter players by position

## Technologies Used

- Flask
- SQLAlchemy
- pandas
- psycopg2
- HTML/CSS

## Installation

### Prerequisites

- Python 3.x
- PostgreSQL

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/cricket-players-directory.git
    ```

2. Navigate to the project directory:
    ```bash
    cd cricket-players-directory
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the PostgreSQL database:
    - Update `db_config` in `app.py` with your PostgreSQL credentials.

5. Run the Flask application:
    ```bash
    python app.py
    ```

## Usage

- Visit [http://localhost:5000](http://localhost:5000) to access the application.
- Use the provided links to filter players based on bowling style, batting style, or position.

## Contributors

- [Ali Khan](https://github.com/khanali37gmail)
- [Amir Siddique](https://github.com/ajsidd)
- [Emad Kamali](https://github.com/Emadkamali)
- [Kashish Jain](https://github.com/kasheshjaiin)
