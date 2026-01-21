# git config --global user.name "sadiksha karki"

#git init
#git add .
#git commit -m "your message"
#create repository in github
#copy paste git code from github

import requests
from bs4 import BeautifulSoup
import json

url = "http://books.toscrape.com/"

def scrape(url):
    response = requests.get(url)

    if response.status_code != 200:
        return

    # set encoding explicitly
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    book_list = []   # this will store all books

    for book in books:
        title = book.h3.a['title']
        price = book.find("p", class_="price_color").text

        book_data = {
            "title": title,
            "price": price
        }

        book_list.append(book_data)

    # Convert Python list to JSON
    json_data = json.dumps(book_list, indent=4, ensure_ascii=False)

    print(json_data)

    # Save JSON to file
    with open("books.json", "w", encoding="utf-8") as f:
        f.write(json_data)

scrape(url)
