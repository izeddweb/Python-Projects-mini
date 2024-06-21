import requests
from bs4 import BeautifulSoup

# url of the website you want to scrape
urlToScrape = "https://books.toscrape.com/"


response = requests.get(urlToScrape)


soup = BeautifulSoup(response.content, "html.parser")

links = soup.find_all("article")

for link in links:
    title = link.h3.a["title"]
    rating = link.p["class"][1]
    price = link.find("p", class_="price_color")

    print(" the title of book is :  " + title)
    print(" the rating of book is :  " + rating + " stars")
    print(" the price is : " + price.text)
    print(" --------")



