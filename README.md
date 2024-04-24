# Cricket Players Filter App

This Flask application allows users to filter cricket players based on various criteria like bowling style, batting style, and position. The application uses a PostgreSQL database to store player data and SQLAlchemy for database interaction. The application is deployed on AWS Elastic Beanstalk.

## Versions

- **app.py**: This version of the application uses separate routes for filtering by bowling style, batting style, and position.
- **app2.py**: This version uses a single route with radio buttons for multiple filters and a submit button to run the query.

## Features

- **Filter by Bowling Style**: Filter players by their bowling style.
- **Filter by Batting Style**: Filter players by their batting style.
- **Filter by Position**: Filter players by their playing position.
- **Responsive Design**: The application UI is designed to be responsive using Bootstrap.

## Prerequisites

- Python 3.x
- AWS account (for deployment)

## Installation

1. Clone the repository:
   \```bash
   git clone https://github.com/kasheshjaiin/cricket-players-filter.git
   cd cricket-players-filter
   \```

2. Install the required Python packages:
   \```bash
   pip install -r requirements.txt
   \```

3. Set up environment variables:
   - `DB_ENDPOINT`: PostgreSQL endpoint
   - `DB_PASSWORD`: PostgreSQL password

## Configuration

The application uses environment variables to configure the database connection. Set the following environment variables before running the application:

\```bash
export DB_ENDPOINT=your_postgresql_endpoint
export DB_PASSWORD=your_postgresql_password
\```

## Usage

### app.py

Run the `app.py` using the following command:

\```bash
python app.py
\```

Navigate to `http://localhost:5000` to access the application.

### app2.py

Run the `app2.py` using the following command:

\```bash
python app2.py
\```

Navigate to `http://localhost:5000` to access the application.

## Deployment on AWS

The application is deployed on AWS Elastic Beanstalk. To deploy the application:

1. Create an AWS Elastic Beanstalk environment.
2. Configure the environment with the necessary environment variables (`DB_ENDPOINT` and `DB_PASSWORD`).
3. Deploy the application using `eb deploy`.

## Troubleshooting

- If you encounter any issues related to database connectivity or queries, check the database connection parameters and ensure the PostgreSQL server is running.
- Make sure to set the correct environment variables before running or deploying the application.


## Contributors

- [Ali Khan](https://github.com/khanali37gmail)
- [Amir Siddiqui](https://github.com/ajsidd)
- [Emad Kamali](https://github.com/Emadkamali)
- [Kashish Jain](https://github.com/kasheshjaiin)
