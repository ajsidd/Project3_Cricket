from flask import Flask, render_template, request
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)

# Database connection parameters
db_config = {
    'dbname': 'cricket',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

# Connection string for PostgreSQL
connection_string = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/players/bowling/<bowling_style>')
def get_players_by_bowling_style(bowling_style):
    # Create a SQLAlchemy engine
    engine = create_engine(connection_string)
    
    # Query the 'players_data' table for players with specific bowling style
    query = f"SELECT * FROM players_data WHERE lower(\"Bowling_Style\") = lower('{bowling_style}');"
    
    # Read data into a DataFrame
    df = pd.read_sql_query(query, engine)
    
    # Convert DataFrame to HTML table
    table_html = df.to_html(index=False, classes="table table-striped")

    return render_template('index.html', table=table_html)

@app.route('/players/batting/<batting_style>')
def get_players_by_batting_style(batting_style):
    # Create a SQLAlchemy engine
    engine = create_engine(connection_string)
    
    # Query the 'players_data' table for players with specific batting style
    query = f"SELECT * FROM players_data WHERE lower(\"Batting_Style\") = lower('{batting_style}');"
    
    # Read data into a DataFrame
    df = pd.read_sql_query(query, engine)
    
    # Convert DataFrame to HTML table
    table_html = df.to_html(index=False, classes="table table-striped")

    return render_template('index.html', table=table_html)

@app.route('/players/position/<position_name>')
def get_players_by_position(position_name):
     # Create a SQLAlchemy engine
    engine = create_engine(connection_string)

    # Convert position_name to match the format in the database
    position_name = position_name.replace('-', ' ')

    
    # Query the 'players_data' table for players with specific batting style
    query = f"SELECT * FROM players_data WHERE lower(\"Position\") = lower('{position_name}');"
    
    # Read data into a DataFrame
    df = pd.read_sql_query(query, engine)
    
    # Convert DataFrame to HTML table
    table_html = df.to_html(index=False, classes="table table-striped")

    return render_template('index.html', table=table_html)

if __name__ == '__main__':
    app.run(debug=True)
