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
    return render_template('index2.html')

@app.route('/filtered-players', methods=['GET', 'POST'])
def filtered_players():
    engine = create_engine(connection_string)

    bowling_style = request.form.get('bowling_style')
    batting_style = request.form.get('batting_style')
    position_name = request.form.get('position_name')

    filters = []
    if bowling_style:
        filters.append(f"\"Bowling_Style\" = '{bowling_style}'")
    if batting_style:
        filters.append(f"\"Batting_Style\" = '{batting_style}'")
    if position_name:
        position_name = position_name.replace('-', ' ')
        filters.append(f"\"Position\" = '{position_name}'")

    if filters:
        where_clause = " AND ".join(filters)
        query = f"SELECT * FROM players_data WHERE {where_clause};"

        df = pd.read_sql_query(query, engine)
        table_html = df.to_html(index=False, classes="table table-striped")
    else:
        table_html = "Please select at least one filter."

    return render_template('index2.html', table=table_html)

if __name__ == '__main__':
    app.run(debug=True)
