import os
import psycopg2

from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'


@app.route('/hobbies', methods=['GET'])
def hobbies():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM hobbies')
    hobbies = cur.fetchall()

    cur.close()
    conn.close()

    just_hobbies = list(map(lambda e: e[1], hobbies))
    return just_hobbies


def get_db_connection():
    return psycopg2.connect(host=os.getenv('DB_HOST', 'localhost'),
                            port=os.getenv('DB_PORT', '5432'),
                            database=os.getenv('DB_DATABASE', 'postgres'),
                            user=os.getenv('DB_USER', 'postgres'),
                            password=os.getenv('DB_PASSWORD', 'postgres'))