from flask import Flask, render_template, request
import requests
import csv
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

def scrape_amazon_reviews(url, num_pages):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }

    all_reviews = []

    for page in range(1, num_pages + 1):
        page_url = f"{url}&pageNumber={page}"
        amazon_response = requests.get(page_url, headers=headers, timeout=10)

        if amazon_response.status_code == 200:
            amazon_html = amazon_response.text
            amazon_soup = bs(amazon_html, "html.parser")
            reviews = amazon_soup.find_all("div", class_="a-section review aok-relative")

            for review in reviews:
                name_elem = review.find('span', class_="a-profile-name")
                name = name_elem.text if name_elem else "No Name"

                rating_elem = review.find("i", class_="a-icon a-icon-star a-star-2 review-rating")
                rating = rating_elem.text if rating_elem else "No Rating"

                comment_elem = review.find("div", class_="a-row a-spacing-small review-data")
                comment = comment_elem.text if comment_elem else "No Comment"

                mydict = {
                    "Name": name,
                    "Rating": rating,
                    "Review": comment,
                }
                all_reviews.append(mydict)
        else:
            print(f'Error: Unable to fetch Amazon page - Status Code: {amazon_response.status_code}')

    return all_reviews

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product_url = request.form.get('product_url') 
        num_pages = int(request.form.get('num_pages'))  

        all_reviews = scrape_amazon_reviews(product_url, num_pages)
        if all_reviews:
            filename = 'amazon_reviews5.csv'

            with open(filename, mode='x', newline='', encoding='utf-8') as csv_file:
                fieldnames = ['Name', 'Rating', 'Review']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(all_reviews)

            return render_template('results.html', reviews=all_reviews)
        else:
            return 'No reviews found.'
    return render_template("index.html")

@app.route('/reviews', methods=['GET', 'POST'])
def display_reviews():
    if request.method == 'POST':
        product_url = request.form.get('product_url')  
        num_pages = int(request.form.get('num_pages'))  

        if product_url:
            all_reviews = scrape_amazon_reviews(product_url, num_pages)
            if all_reviews:
                return render_template('results.html', reviews=all_reviews)
        else:
            return 'No reviews found.'

    return 'No reviews found.'

if __name__ == '__main__':
    app.run(debug=True)
