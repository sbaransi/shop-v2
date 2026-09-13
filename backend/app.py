from flask import Flask
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return {
        "project": "shop-v2",
        "status": "running"
    }


@app.route("/products")
def products():

    conn = psycopg2.connect(
        host="host.docker.internal",
        port="5433",
        database="shopdb",
        user="shopuser",
        password="shoppass"
    )

    cur = conn.cursor()

    cur.execute("SELECT * FROM products")

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [
        {
            "id": row[0],
            "name": row[1],
            "price": float(row[2])
        }
        for row in rows
    ]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
