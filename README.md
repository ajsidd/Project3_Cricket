# Cricket Players Directory

This is a simple Flask web application to browse cricket players based on their bowling style, batting style, and position.

## Features

- Filter players by bowling style
- Filter players by batting style
- Filter players by position

## Technologies Used

- Python
- Flask
- SQLAlchemy
- Pandas
- PostgreSQL

## Installation

### Prerequisites

- Python 3.x
- PostgreSQL

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/cricket-players-directory.git
    ```

2. Navigate to the project directory:

    ```bash
    cd cricket-players-directory
    ```

3. Install required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a PostgreSQL database named `cricket` and import the `players_data.csv` file into a table named `players_data`.

5. Update the `config.py` file with your database credentials and SportMonks API key.

6. Run the Flask application:

    ```bash
    python app.py
    ```

## Usage

- Navigate to [http://localhost:5000](http://localhost:5000) in your web browser.
- Use the links to filter players by bowling style, batting style, or position.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contributors

- [Ali Khan](https://github.com/khanali37gmail)
- [Amir Siddique](https://github.com/ajsidd)
- [Emad Kamali](https://github.com/Emadkamali)
- [Kashish Jain](https://github.com/kasheshjaiin)

