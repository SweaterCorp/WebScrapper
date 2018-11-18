class BaseType:
    def __init__(self, name: str):
        self.name = name

    def to_csv_line(self):
        return self.name + ";"


class CategoryType(BaseType):
    products_table_url: str
    products_count: int

    def __init__(self, category_name: str, products_table_url: str, products_count: int):
        super(CategoryType, self).__init__(category_name)
        self.products_table_url = products_table_url
        self.products_count = products_count

    def to_csv_line(self):
        return self.name + ";" + self.products_table_url + ";" + self.products_count + ";"