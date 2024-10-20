from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_stock_price(ticker="ZOMATO"):
    url = f'https://www.google.com/finance/quote/{ticker}:NSE'
    try:
        response = requests.get(url, timeout=3)  # Set a 3-second timeout
        soup = BeautifulSoup(response.text, 'html.parser')
        myClass = "YMlKec fxKbKc"
        ans = float(soup.find(class_=myClass).text.strip()[1:].replace(',', ''))
        return ans
    except requests.exceptions.Timeout:
        return "Timeout Error"
    except Exception as e:
        return str(e)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_stock_price')
def get_price():
    price = get_stock_price()
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(debug=True)
