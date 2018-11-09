import typing
from typing import List


class Size:
    def __init__(self, russsian: str, international: str):
        self.russsian = russsian
        self.international = international

    def __str__(self):
        return "(rus:" + self.russsian + ", int:" + self.international + ")"


class Product:

    def __init__(self, vendor_code: str, brand: str, color: str, style: str, print: str, price: str, made_in_country: str, site: str, sizes: List[Size], photos: List[str]):
        self.vendor_code = vendor_code
        self.brand = brand
        self.color = color
        self.style = style
        self.print = print
        self.price = price
        self.made_in_country = made_in_country
        self.site = site
        self.sizes = sizes
        self.photos = photos

    def to_scv_line(self):
        sizes_line = list_to_str(self.sizes)
        photos_line = list_to_str(self.photos)

        result = self.vendor_code + ";" + \
            self.brand + ";" + \
            self.color + ";" +\
            self.style + ";" + \
            self.print+ ";" + \
            self.price + ";" +\
            self.made_in_country + ";" + \
            self.site + \
            sizes_line + ";" + \
            photos_line + ";"
        return result


def list_to_str(items):
    open_bracket = "["
    close_bracket = "]"
    str_list = [str(item) for item in items]
    array_strs = ','.join(str_list)
    return open_bracket + array_strs + close_bracket
