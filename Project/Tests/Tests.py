from Parsers.ProductPageParser import ProductPageParser
from Entities.Product import Product
from Infrastructure.Logging import Logging
from Infrastructure.Utils import get_soup

class Tests:
    @staticmethod
    def tes_product_page_parser():
        #file = open("../ParsingSites/ProductPageSample3.html", "r", encoding="utf8")
        #html = file.read()

        pr: Product = ProductPageParser().parse_product_page(get_soup("https://www.lamoda.ru/p/mp002xw0djjv/clothes-emi-bluza/"))

        Logging.log(pr.to_scv_line())
        print(pr.to_scv_line())
