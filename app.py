from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def books():

    books = [

        {"name": "Python Basics", "price": 25},
        {"name": "Flask Guide", "price": 30},
        {"name": "HTML Book", "price": 20},
        {"name": "CSS Master", "price": 22},
        {"name": "JavaScript Pro", "price": 35}

    ]

    total_price = 0

    for b in books:
        total_price += b["price"]

    average_price = total_price / len(books)

    expensive = max(books, key=lambda x: x["price"])
    cheap = min(books, key=lambda x: x["price"])

    return render_template(
        "index.html",
        books=books,
        average_price=average_price,
        expensive=expensive,
        cheap=cheap
    )


if __name__ == "__main__":
    app.run(debug=True)
