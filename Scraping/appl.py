from flask import Flask, render_template, request
import requests
import csv
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

def scrape_amazon_reviews(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }

    all_reviews = []

    amazon_url = url

    while True:
        amazon_response = requests.get(amazon_url, headers=headers, timeout=10)

        if amazon_response.status_code == 200:
            amazon_html = amazon_response.text
            amazon_soup = bs(amazon_html, "html.parser")
            reviews = amazon_soup.find_all("div", class_="a-section review aok-relative")

            for review in reviews:
                name_elem = review.find('span', class_="a-profile-name")
                name = name_elem.text if name_elem else "No Name"

                rating_elem = review.find("i", class_="a-icon a-icon-star a-star-1 review-rating")
                rating = rating_elem.text if rating_elem else "No Rating"

                comment_elem = review.find("div", class_="a-row a-spacing-small review-data")
                comment = comment_elem.text if comment_elem else "No Comment"

                mydict = {
                    "Name": name,
                    "Rating": rating,
                    "Review": comment,
                }
                all_reviews.append(mydict)

            next_button = amazon_soup.find("li", class_="a-last")
            if next_button:
                next_page_url = next_button.find("a")
                if next_page_url:
                    next_page_url = next_page_url.get("href")
                    amazon_url = "https://www.amazon.in" + next_page_url
                else:
                    break
            else:
                break
        else:
            return 'Error: Unable to fetch Amazon page'

    return all_reviews

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Name', 'Rating', 'Review']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product_url = request.form.get('product_url')  # Get the product URL from the form
        all_reviews = scrape_amazon_reviews(product_url)
        if all_reviews:
            save_to_csv(all_reviews, 'amazon_reviews.csv')  # Save the data to a CSV file
            return render_template('results.html', reviews=all_reviews)
        else:
            return 'No reviews found.'
    return render_template("index.html")

@app.route('/reviews', methods=['GET', 'POST'])
def display_reviews():
    if request.method == 'POST':
        product_url = request.form.get('product_url')  # Get the product URL from the form
        if product_url:
            all_reviews = scrape_amazon_reviews(product_url)
            if all_reviews:
                save_to_csv(all_reviews, 'amazon_reviews.csv')  # Save the data to a CSV file
                return render_template('results.html', reviews=all_reviews)
    
    return 'No reviews found.'

if __name__ == '__main__':
    app.run(debug=True)