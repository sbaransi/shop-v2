from flask import Flask
from flask_cors import CORS
import psycopg2
from flask import request

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
        host="postgres",
        port="5432",
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

@app.route("/products", methods=["POST"])
def create_product():

    data = request.json

    conn = psycopg2.connect(
        host="host.docker.internal",
        port="5433",
        database="shopdb",
        user="shopuser",
        password="shoppass"
    )

    cur = conn.cursor()

    cur.execute(
        "INSERT INTO products (name, price) VALUES (%s, %s)",
        (data["name"], data["price"])
    )

    conn.commit()

    cur.close()
    conn.close()

    return {"message": "Product created"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
