from bs4 import BeautifulSoup
from requests import get
import lxml

def get_product_info(url):
    headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0",
        "Accept-Language" : "en",
    }
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()

    rate = soup.select_one(selector="#acrPopover").getText()
    rate = float(rate.strip().split()[0])

    rating = soup.select_one(selector="#acrCustomerReviewText").getText()
    j = ""
    for i in (rating.strip().split()[0]).split(','):
        j = j+i
    rating = int(j)

    price = soup.select_one(selector="#priceblock_ourprice").getText()
    price = float(price.strip().split()[0][1:])

    image = soup.find("img", id="landingImage")["data-a-dynamic-image"].split('"')[1]

    return (name, price, rate, rating, image)

if __name__ == '__main__':
    url = "https://www.amazon.com/Colorfulkoala-Womens-Waisted-Leggings-Pockets/dp/B07G54GS2T/"
    print(get_product_info(url))
