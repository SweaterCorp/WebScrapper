from typing import List

from Utils import list_to_str


class Size:
    russian_size: str
    other_country_size: str
    country_type: str
    is_available: bool

    def __init__(self, russian_size: str, other_country_size: str, country_type: str, is_available: bool = True):
        self.russian_size = russian_size
        self.other_country_size = other_country_size
        self.country_type = country_type
        self.is_available = is_available

    def __str__(self):
        return "(|RUS:" + self.russian_size + f" {self.country_type}:" + self.other_country_size + f"| IsAvailable: {str(self.is_available)})"


class Product:

    def __init__(self, vendor_code: str, is_available:bool, brand: str, color: str, print: str, price: str, made_in_country: str, link: str, sizes: List[Size], photos: List[str]):
        self.vendor_code = vendor_code
        self.is_available = is_available
        self.brand = brand
        self.color = color
        self.print = print
        self.price = price
        self.made_in_country = made_in_country
        self.link = link
        self.sizes = sizes
        self.photos = photos

    def to_scv_line(self):
        sizes_line = list_to_str(self.sizes)
        photos_line = list_to_str(self.photos)

        result = self.vendor_code + ";" + \
            str(self.is_available) + ";" + \
            self.brand + ";" + \
            self.color + ";" +\
            self.print+ ";" + \
            self.price + ";" +\
            self.made_in_country + ";" + \
            self.link + ";" + \
            sizes_line + ";" + \
            photos_line + ";"
        return result
