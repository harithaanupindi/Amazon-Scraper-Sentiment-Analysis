# from bs4 import BeautifulSoup as bs
# import requests

# def get_product_url():
#     with open('templates/index.html', 'r') as f:
#         soup = bs(f)
#     return soup

# get_product_url()


def get_review_url(product_url):
    temp = list(product_url.rstrip('/').rpartition('/'))
    last = temp[2]
    first = temp[0].replace("/dp","").rstrip('/')
    middle='product-reviews'
    review_url = "/".join([first, middle, last])
    return review_url

def get_pages(product_url: str, training_data: bool) -> list:
    """
    Return list of pages from product url
    """
    # sortby = ["helpful", "recent"]
    # ratings = ["one_star", ...]
    pages = []
    sort_method = "recent"
    for page in range(1, 11):
        suffix = f"/ref=cm_cr_arp_d_viewopt_srt?sortBy={sort_method}&pageNumber={page}"
        if training_data:
            suffix += "&filterByStar={rating}"
            sort_method = "helpful"
        pages.append(get_review_url(product_url) + suffix)
    return pages

get_pages("https://www.amazon.in/Apple-iPhone-13-256-GB/dp/B09V4MXBSN/", training_data=False)
# def get_reviews(review_url):
#     ...

    
# response = requests.get(amazon_html)

# amazon_soup = bs(response.text)
# print(amazon_soup)



# amazon_soup = bs(amazon_html, "html.parser")
# print(amazon_soup)
# reviews = amazon_soup.find_all("div", class_="a-section review aok-relative")
# print(reviews)

# amazon_product_url = "/Apple-iPhone-13-128GB-Green/dp/B09V4B6K53/ref=sr_1_3?crid=1CFHNFPG6EFCO&keywords=iphone+13&qid=1698917065&sprefix=%2Caps%2C186&sr=8-3"
# amazon_product_url = "https://www.amazon.in" + amazon_product_url.partition('/ref')[0]
# print(amazon_product_url)

