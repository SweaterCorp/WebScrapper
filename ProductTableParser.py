from typing import List
from Product import Product
from ProductPageParser import *
from Utils import *

class ProductTableParser:

    def parse_table(self, soup:BeautifulSoup):
        result: List[Product] = []
        product_parser = ProductPageParser()
        links = soup.find_all("a", {"class": "products-list-item__link link"})
        for link in links[0:10]:
            url = "https://www.lamoda.ru" + link["href"]
            product = product_parser.parse_product_page(get_soup(url))
            product.site = url;
            result.append(product)
        return result;


tab = ProductTableParser();


file = open("../ParsingSites/ProductTableSample.html", "r", encoding="utf8")
html = file.read()

result = ProductTableParser().parse_table(get_soup("https://www.lamoda.ru/c/399/clothes-bluzy-rubashki/"))

a = result;
