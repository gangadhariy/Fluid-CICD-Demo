from flask import Flask, jsonify
import psycopg2
import os


app = Flask(__name__)


def get_db_connection():

    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )


@app.route("/")
def home():

    return jsonify(
        {
            "message": "Python API is running Successfully"
        }
    )


@app.route("/health")
def health():

    return "OK", 200


@app.route("/database")
def database():

    try:

        conn = get_db_connection()

        cursor = conn.cursor()

        cursor.execute(
            "select now();"
        )

        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return jsonify(
            {
                "database_time": str(result[0])
            }
        )

    except Exception as e:

        return jsonify(
            {
                "error": str(e)
            }
        ), 500



if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
