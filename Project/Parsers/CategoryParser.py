from bs4 import BeautifulSoup
from typing import List
from Project.Entities.Product import Product
from Project.Entities.Category import Category
from Project.Product.PageParser import ProductPageParser
from Project.Infrastructure.Utils import get_soup


class CategoryParser:

    def parse_category(self, url: str,  count: int, count_per_page: int = 60):
        category = Category()
        base_url = url + "/?page="
        pages = count // count_per_page

        for i in range(pages):
            url = base_url + str(i)
            category.add_products(self.__parse_table(url))
        return category

    def __parse_table(self, soup: BeautifulSoup):
        result = []
        product_parser = ProductPageParser()
        links = soup.find_all("a", {"class": "products-list-item__link link"})
        for link in links[0:10]:
            url = "https://www.lamoda.ru" + link["href"]
            product = product_parser.parse_product_page(get_soup(url))
            product.site = url
            result.append(product)
        return result
