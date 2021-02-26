from flask import Flask
from yahooquery import Ticker

app = Flask(__name__)


@app.route('/price/<ticker>')
def price(ticker):
    stock = Ticker(ticker)
    return stock.price


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
