from bs4 import BeautifulSoup
from typing import List
from Product import Product
from Category import Category
from ProductPageParser import ProductPageParser
from Utils import get_soup


class CategoryParser:

    def parse_category(self, url: str,  count: int, count_per_page: int = 60):
        category = Category()
        base_url = url + "/?page="
        pages = count // count_per_page

        for i in range(pages):
            url = base_url + str(i)
            category.add_products(self.__parse_table(get_soup(url)))
        return category

    def __parse_table(self, soup: BeautifulSoup):
        result = []
        product_parser = ProductPageParser()
        links = soup.find_all("a", {"class": "products-list-item__link link"})
        for link in links:
            url = "https://www.lamoda.ru" + link["href"]
            product = product_parser.parse_product_page(get_soup(url))
            product.link = url
            result.append(product)
        return result
