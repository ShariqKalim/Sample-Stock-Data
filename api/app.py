from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_stock_price(ticker="ZOMATO"):
    url = f'https://www.google.com/finance/quote/{ticker}:NSE'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    myClass = "YMlKec fxKbKc"
    ans = float(soup.find(class_=myClass).text.strip()[1:].replace(',', ''))
    return ans

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_stock_price')
def get_price():
    price = get_stock_price()
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(debug=True)
