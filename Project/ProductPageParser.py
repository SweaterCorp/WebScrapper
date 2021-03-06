from bs4 import BeautifulSoup
from typing import List, Tuple
import json
from Product import Product, Size
from Logging import Logging
from Utils import get_soup, normalize_str


class ProductPageParser:

    def parse_product_page(self, soup: BeautifulSoup):
        is_available = self.__parse_product_is_available(soup)
        price = self.__parse_price(soup)
        brand = self.__parse_brand(soup)
        sizes = self.__parse_sizes(soup)
        photos = self.__parse_photos(soup)

        description = self.__parse_product_description(soup)
        print_ = self.__parse_print(description)
        color = self.__parse_color(description)
        vendor_code = self.__parse_vendor_code(description)
        made_in_country = self.__parse_made_in_country(description)

        product = Product(vendor_code=vendor_code, is_available = is_available, brand=brand, color=color, print=print_,
                          price=price, made_in_country=made_in_country, link="", sizes=sizes, photos=photos)
        return product

    def __parse_product_is_available(self, soup: BeautifulSoup):
        is_product_available = soup.find("div", {"data-in-stock": "true"})
        if (is_product_available is None):
            return False
        else:
            return True

    def __parse_price(self, soup: BeautifulSoup):
        price = self._get_price_first_way(soup)
        if(price == ""):
            price = self._get_price_second_way(soup)
        return normalize_str(price)

    def _get_price_first_way(self, soup: BeautifulSoup):
        product_price = soup.find("div", {"class": "ii-product__price"})
        if (product_price is None):
            return ""
        if(product_price.has_attr("data-original")):
            return product_price["data-original"]
        if(product_price.has_attr("data-current")):
            return product_price["data-current"]
        return ""

    def _get_price_second_way(self, soup: BeautifulSoup):
        several_price = soup.find("div", {"class": "ii-product__price ii-product__price_several"})
        if (several_price is None):
            return ""
        data_several_prices = several_price["data-several-prices"]
        return json.loads(data_several_prices)["details"][0]["value"]

    def __parse_brand(self, soup: BeautifulSoup):
        brand = soup.find("a", {"class": "ii-product__brand-text ii-link_primary"})
        return normalize_str(brand.get_text())

    def __parse_sizes(self, soup: BeautifulSoup):
        sizes_container = soup.find("div", {"class": "product__sizes-select-container"})
        select_items = sizes_container.find_all("div", {"class": "ii-select__option"})
        sizes = [self.__parse_size(item) for item in select_items]
        return sizes

    def __parse_size(self, item_size:BeautifulSoup):
        data_display:str = item_size["data-display"]
        is_available: bool = "ii-select__option_disabled" not in item_size["class"];
        sizes = data_display.split(" ")
        return Size(sizes[0], sizes[2].replace("(",""), sizes[3].replace(")",""), is_available)

    def __parse_photos(self, soup: BeautifulSoup):
        items = soup.find_all("img", {"class": "showcase__slide-image"})
        items: List[str] = [("http:"+item["src"]) for item in items]
        items: List[str] = [item.replace("imf46x66", "product") for item in items]
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

    def __parse_product_description(self, soup: BeautifulSoup):
        container: BeautifulSoup = soup.find("div", {"class": "ii-product__description-text"})
        container: BeautifulSoup = container.find("div", {"class": "ii-product__attributes"})
        complex_items: BeautifulSoup = container.find_all("div", {"class", "ii-product__attribute"})

        label_values: List[Tuple[str, str]] = []
        for complex_item in complex_items:
            label = complex_item.find("span", {"class": "ii-product__attribute-label"})
            label = normalize_str(label.get_text(), capitalize="lower", replace=(":", ""))

            value = complex_item.find("span", {"class": "ii-product__attribute-value"})
            value = normalize_str(value.get_text(), replace=(":", ""))

            label_values.append((label, value))
        return label_values

# pr: Product = ProductPageParser().parse_product_page(get_soup("https://www.lamoda.ru/p/ad005ewcjde1/clothes-adladilisik-yubka"))

# #Logging.log(pr.to_scv_line())
# print(pr.to_scv_line())



