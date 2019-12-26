from typing import List, Dict
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


def campaigns() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'majidDB'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM campaigns LIMIT 100')

    results = [{"CAMPAIGN_NAME": CAMPAIGN_TYPE}
               for (CAMPAIGN_NAME, CAMPAIGN_TYPE, *other) in cursor]

    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return jsonify({'campaigns': campaigns()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
