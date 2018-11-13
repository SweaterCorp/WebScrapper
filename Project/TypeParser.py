
from bs4 import BeautifulSoup
from typing import List

# from ..Entities.Type import ClothesType, BaseType
# from ..Infrastructure.Utils import normalize_str

from Type import *
from Utils import *


class TypeParser:

    # brand_types = "multifilter_brands"
    # style_types = "multifilter_property_style "
    # size_types = "multifilter_size_values "
    # color_types = "multifilter_colors"

    def parse_prints(self, soup: BeautifulSoup):
        print_types = "multifilter_print "
        return self.__parse_types(soup, print_types)

    def parse_brands(self, soup: BeautifulSoup):
        brand_types = "multifilter_brands"
        return self.__parse_types(soup, brand_types)

    def parse_styles(self, soup: BeautifulSoup):
        style_types = "multifilter_property_style "
        return self.__parse_types(soup, style_types)

    def parse_sizes(self, soup: BeautifulSoup):
        size_types = "multifilter_size_values "
        return self.__parse_types(soup, size_types)

    def parse_colors(self, soup: BeautifulSoup):
        color_types = "multifilter_colors"
        return self.__parse_types(soup, color_types)

    def __parse_types(self, soup: BeautifulSoup, class_attribute: str):
        results: List[BaseType] = []
        list = soup.find("div", {"class": f"multifilter {class_attribute}"})
        items = list.find_all("div", {"class": "multifilter-item"})
        for item in items:
            label = item.find("label")
            text = label.get_text()
            results.append(BaseType(text))
        return results

    def parse_clothes(self, soup: BeautifulSoup):
        results: List[ClothesType] = []
        table_left_column = soup.find("div", {"class": "table__left-column"})
        list = table_left_column.find(
            "div", {"class": "catalog-navigation-wrap"}).find("ul").find("ul").find_all("li")
        for item in list:
            count = item.find("span", {"class": "cat-nav-cnt"}).get_text()
            link = item.find("a", {"class": "link"})
            clothes_name = link.get_text()
            clothes_name = normalize_str(clothes_name)
            href = link["href"]
            results.append(ClothesType(clothes_name, href, count))
        return results
