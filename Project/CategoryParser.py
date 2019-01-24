from bs4 import BeautifulSoup
from typing import List
from Product import Product
from Category import Category
from ProductPageParser import ProductPageParser
from Utils import get_soup

import time
from threading import Thread
from datetime import datetime


class CategoryParser:

    def parse_category(self, url: str, category_name: str, offset: int = 0, count: int = 60, count_per_page: int = 60):
        
        base_url = url + "/?page="
        start_page = offset // count_per_page + 1
        pages = start_page + count // count_per_page

        for i in range(start_page, pages):
            time.sleep(10)
            print("====================================")
            print("Страница чтения: " + str(i) + " из " + str(pages - 1))
            url = base_url + str(i)
            category = Category()
            category.add_products(self.__parse_table(get_soup(url)))
            now = datetime.now()
            time_now = "{}.{}.{}_{}.{}.{}".format(now.day, now.month, now.year, now.hour, now.minute, now.second)
            file_name = "page_" + str(i) + "_count_" + str(len(category.products)) + "_time_" + time_now + "_.csv"
            save_file_url = "./Data/" + category_name + "/" + file_name
            category.save_category_to_file(save_file_url)
            print("Сохранен файл c таблицей: " + file_name)
            print("====================================")
            print("")

    def __parse_table(self, soup: BeautifulSoup):
        result = []
        product_parser = ProductPageParser()
        links = soup.find_all("a", {"class": "products-list-item__link link"})
        i = 0
        links_count = len(links)
        for link in links:
            time.sleep(3)
            i = i + 1
            url = "https://www.lamoda.ru" + link["href"]
            print("----------------- " + str(i) + ") Читается продукт " + str(i) + " из " + str(links_count) + ": " + url)
            product = product_parser.parse_product_page(get_soup(url))
            product.link = url
            result.append(product)
        return result
