#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
import requests
from bs4 import BeautifulSoup

# decoration
print(stylize("\n---- | Get current Ethereum price | ----\n", fg("red")))

# class
class Scraper:
    def __init__(self):
        self.url = "https://www.coindesk.com/price/ethereum"

    # output magic method
    def __repr__(self):
        price = stylize(self.scrape(self.url), fg("red"))
        return f"Current Ethereum price is: {price} $\n"

    # methods
    def scrape(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        result = soup.find(class_="price-large")
        contents = [i for i in result]

        return contents[1]

# main execution
if __name__ == "__main__":
    print(Scraper())
