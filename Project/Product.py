from typing import List

from Utils import list_to_str


class Size:
    def __init__(self, russian: str, international: str):
        self.russian = russian
        self.international = international

    def __str__(self):
        return "(rus:" + self.russian + ", int:" + self.international + ")"


class Product:

    def __init__(self, vendor_code: str, brand: str, color: str, print: str, price: str, made_in_country: str, site: str, sizes: List[str], photos: List[str]):
        self.vendor_code = vendor_code
        self.brand = brand
        self.color = color
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
            self.print+ ";" + \
            self.price + ";" +\
            self.made_in_country + ";" + \
            self.site + \
            sizes_line + ";" + \
            photos_line + ";"
        return result
