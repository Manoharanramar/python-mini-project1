from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Prices
PRICES = {
    "popcorn": 120,
    "drink": 80,
    "nachos": 100,
    "combo": 250
}

@app.route('/')
def home():
    return "Snack Booking API"

@app.route('/book-snacks', methods=['POST'])
def book_snacks():
    data = request.json  # assuming JSON from frontend

    popcorn = int(data.get('popcorn', 0))
    drink = int(data.get('drink', 0))
    nachos = int(data.get('nachos', 0))
    combo = int(data.get('combo', 0))

    total = (popcorn * PRICES['popcorn'] +
             drink * PRICES['drink'] +
             nachos * PRICES['nachos'] +
             combo * PRICES['combo'])

    booking = {
        "items": {
            "popcorn": popcorn,
            "drink": drink,
            "nachos": nachos,
            "combo": combo
        },
        "total": total
    }

    return jsonify({"message": "Snacks booked!", "booking": booking})


if __name__ == '__main__':
    app.run(debug=True)
