from flask import Flask, jsonify

from bs4 import BeautifulSoup

import requests

app = Flask(__name__)

@app.route('/price')

def get_price():

    url = "https://www.metal.com/Lithium-ion-Battery/202303240001"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    price_element = soup.find("div", {"class": "price-value"})

    if price_element:

        return jsonify({"price": price_element.text.strip()})
    else:

        return jsonify({"error": "Price not found"}), 404

@app.errorhandler(404)

def page_not_found(error):

    return jsonify({"error": "Invalid URL"}), 404

if __name__ == '__main__':
    
    app.run(debug=True)
