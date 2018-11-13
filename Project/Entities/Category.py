from typing import List
from Project.Entities.Product import Product


class Category:

    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product):
        self.products.append(product)

    def add_products(self, products: List[Product]):
        self.products.extend(products)

    @staticmethod
    def save_products_to_file(file_path: str, products: List[Product]):
        with open(file_path, "w",  encoding="utf8", newline="") as file:
            for product in products:
                file.write(product.to_scv_line()+"\n")

    def save_category_to_file(self, file_path: str):
        Category.save_products_to_file(file_path, self.products)
