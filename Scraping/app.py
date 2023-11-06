from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
import logging
import csv

app = Flask(__name__)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}


@app.route("/", methods=['GET'])
def homepage():
    return render_template("index.html")

@app.route("/reviews", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            url = request.form['url']
            response = requests.get(url, headers=headers, allow_redirects=True)
            if response.status_code == 200:
                soup = bs(response.text, "html.parser")
                reviews = []

                # Modify this to extract reviews based on the structure of the webpage
                for review in soup.find_all('div', class_="_2c2kV-"):
                    name = review.find('span', class_="_2sc7ZR _2V5EHH").text
                    rating = review.find('span', class_="_3LWZlK _1BLPMq").text
                    comment = review.find('div', class_="t-ZTKy").text

                    mydict = {
                        "Name": name,
                        "Rating": rating,
                        "Comment": comment,
                    }
                    reviews.append(mydict)

                filename = "reviews.csv"
                with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
                    fieldnames = ['Name', 'Rating', 'Comment']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(reviews)

                return render_template('results.html', reviews=reviews)
            else:
                return 'Failed to retrieve the page - Status Code: {}'.format(response.status_code)
        except Exception as e:
            logging.error(e)
            return 'Something went wrong'
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
