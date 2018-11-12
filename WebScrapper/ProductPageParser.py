from bs4 import BeautifulSoup
from typing import List, Tuple
from Product import *


class ProductPageParser:

    def parse_product_page(self, soup: BeautifulSoup):
        price = self.__parse_price(soup)
        brand = self.__parse_brand(soup)
        sizes = self.__parse_sizes(soup)
        photos = self.__parse_photos(soup)

        description = self.__parse_poduct_description(soup);
        print_ = self.__parse_print(description)
        color = self.__parse_color(description)
        vendor_code = self.__parse_vendor_code(description)
        made_in_country = self.__parse_made_in_country(description)

        product = Product(vendor_code=vendor_code, brand=brand, color=color, print=print_, price=price, made_in_country=made_in_country, site = "", sizes=sizes, photos=photos)
        return product

    def __parse_price(self, soup: BeautifulSoup):
        price = soup.find("div", {"class": "ii-clothes__price-original"})
        return normalize_str(price.get_text())

    def __parse_brand(self, soup: BeautifulSoup):
        brand = soup.find("a", {"class": "ii-clothes__brand-text ii-link_primary"})
        return normalize_str(brand.get_text())

    def __parse_sizes(self, soup: BeautifulSoup):
        sizes_container = soup.find("div", {"class": "clothes__sizes-select-container"})
        select_items = sizes_container.find_all("div", {"class": "ii-select__option"})
        sizes = [normalize_str(item["data-display"]) for item in select_items]
        return sizes

    def __parse_photos(self, soup: BeautifulSoup):
        items = soup.find_all("img", {"class": "showcase__slide-image"})
        items: List[str] = [("http:"+item["src"]) for item in items]
        items: List[str] = [item.replace("imf46x66", "clothes") for item in items]
        return items

    def __parse_print(self, label_values: List[Tuple[str, str]]):
        print_pattern = "узор"
        return self.__find_value_by_pattern(label_values, print_pattern)

    def __parse_color(self, label_values: List[Tuple[str, str]]):
        color_pattern = "цвет"
        return self.__find_value_by_pattern(label_values, color_pattern)

    def __parse_vendor_code(self, label_values: List[Tuple[str, str]]):
        vendor_code_pattern = "артикул"
        return self.__find_value_by_pattern(label_values, vendor_code_pattern)

    def __parse_made_in_country(self, label_values: List[Tuple[str, str]]):
        made_in_country_pattern = "страна производства"
        return self.__find_value_by_pattern(label_values, made_in_country_pattern)

    def __find_value_by_pattern(self, label_values: List[Tuple[str, str]], pattern: str):
        for label_value in label_values:
            if(pattern in label_value[0]):
                return label_value[1]
        return ""

    def __parse_poduct_description(self, soup: BeautifulSoup):
        container: BeautifulSoup = soup.find("div", {"class": "ii-clothes__description-text"})
        container: BeautifulSoup = container.find("div", {"class": "ii-clothes__attributes"})
        complex_items: BeautifulSoup = container.find_all("div", {"class", "ii-clothes__attribute"})

        label_values: List[Tuple[str, str]] = []
        for complex_item in complex_items:
            label = complex_item.find("span", {"class": "ii-clothes__attribute-label"})
            label = normalize_str(label.get_text(), replace=(":", ""))

            value=complex_item.find("span", {"class": "ii-clothes__attribute-value"})
            value=normalize_str(value.get_text(), capitalize="lower", replace=(":", ""))

            label_values.append((label, value))
        return label_values
