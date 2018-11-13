class BaseType:
    def __init__(self, name: str):
        self.name = name

    def to_csv_line(self):
        return self.name + ";"


class ClothesType(BaseType):
    clothes_table_url: str
    clothes_count: int

    def __init__(self, clothes_name: str, clothes_table_url: str, clothes_count: int):
        super(ClothesType, self).__init__(clothes_name)
        self.clothes_table_url = clothes_table_url
        self.clothes_count = clothes_count

    def to_csv_line(self):
        return self.name + ";" + self.clothes_table_url + ";" + self.clothes_count + ";"
