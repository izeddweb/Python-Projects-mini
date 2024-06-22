
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all("article")

# Prepare a list to store book information
book_info_list = []

# Iterate through each article to extract title, rating, and price
for article in articles:
    title = article.h3.a["title"]
    rating = article.p["class"][1]
    price = article.find("p", class_="price_color").text

    # Format the book information
    book_info = f"Title: {title}\n Rating: {rating} stars \nPrice: {price} \n"
    book_info_list.append(book_info)

# Define the file name where you want to save the output
output_file = "output-Project-2.txt"

# Write the extracted content to a text file
with open(output_file, "w") as file:
    for book_info in book_info_list:
        file.write(book_info + "\n")

print(f" success to saved to {output_file}")
