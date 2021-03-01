from flask import Flask
from yahooquery import Ticker

app = Flask(__name__)


@app.route('/ping')
def ping():
    return "ok"


@app.route('/price/<ticker>')
def price(ticker):
    stock = Ticker(ticker)
    return stock.price


@app.route('/holdings/<ticker>')
def holders(ticker):
    stock = Ticker(ticker)
    return stock.fund_holding_info


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
