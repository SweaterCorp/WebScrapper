import urllib
from bs4 import BeautifulSoup
import requests
import csv
import urllib.request
import typing
from typing import List, Tuple
import re

from CategoryParser import *



categories:List[Tuple[str,str]] = [
("blouses_shirts","https://www.lamoda.ru/c/399/clothes-bluzy-rubashki/"),
("trousers","https://www.lamoda.ru/c/401/clothes-bryuki-shorty-kombinezony/"),
("outerwear","https://www.lamoda.ru/c/357/clothes-verkhnyaya-odezhda/"),
("jumpers_sweaters_cardigans","https://www.lamoda.ru/c/371/clothes-trikotazh/"),
("jeans","https://www.lamoda.ru/c/397/clothes-d-insy/"),
("jackets_suits","https://www.lamoda.ru/c/367/clothes-pidzhaki-zhaketi/"),
("dresses","https://www.lamoda.ru/c/369/clothes-platiya/"),
("tracksuits","https://www.lamoda.ru/c/415/clothes-kostyumy/"),
("hoodies_sweatshirts","https://www.lamoda.ru/c/2474/clothes-tolstovki-olimpiyki/"),
("tops","https://www.lamoda.ru/c/2627/clothes-topy/"),
("t_shirts_polo","https://www.lamoda.ru/c/2478/clothes-futbolki/"),
("shorts","https://www.lamoda.ru/c/2485/clothes-shorty/"),
("skirts","https://www.lamoda.ru/c/423/clothes-yubki/")
]

def main():
   print(categories)

   test_category = categories[1]
   parser = CategoryParser()
   category = parser.parse_category(test_category[1],60)
   category.save_category_to_file("./Data/" + test_category[0]+".csv")
 

   
   print(test_category)


if __name__ == "__main__":
    main()











# def read_html(file_path: str):
#     file = open(file_path, "r", encoding="utf8")
#     return file.read()


# def read_csv(file_path: str, delimeter=";"):
#     with open(file_path, "r",  encoding="utf8", newline="") as file:
#         return file.read()


# def write_csv(file_path: str, rows):
#     with open(file_path, "w",  encoding="utf8", newline="") as file:
#         for row in rows:
#             file.write(row+"\n")


# def types_to_csv_lines(rows, delimeter=";"):
#     return [(row+delimeter) for row in rows]


# def clothes_to_csv_lines(rows, delimeter=";"):
#     results = []
#     for row in rows:
#         line = delimeter.join(map(str, (str(item)for item in row))) + delimeter
#         results.append(line)
#     return results





# https://www.lamoda.ru/c/399/clothes-bluzy-rubashki/?page=2

# 60 на странице вещей


# def parse_clothes_item(html:str):

    # http://a.lmcdn.ru/clothes/O/V/OV001EWBRUQ2_6867434_1_v2.jpg
    # http://a.lmcdn.ru/img46x66/O/V/OV001EWBRUQ2_6867434_1_v2.jpg
    #


#url = "https://www.lamoda.ru/p/ov001ewbruq2/clothes-ovs-dzhinsy/";
# html = requests.get(url).text;#urllib.request.urlopen(url).read();
# with open("../ParsingSites/Model.html", "w",  encoding="utf8", newline="") as file:
#    file.write(html)

#a = parse_types(htmlText, brands_class)
# print(a)




# def parse_types():
#     sites_folder = "../ParsingSites/"
#     data_folder = "../Data/"
#     types_file = "Types.html"

    

#     html_text = read_html(sites_folder + types_file)

#     prints = parse_types(html_text, print_types)
#     brands = parse_types(html_text, brand_types)
#     styles = parse_types(html_text, style_types)
#     sizes = parse_types(html_text, size_types)
#     colors = parse_types(html_text, color_types)

#     clothes = parse_clothes_list(html_text)

#     write_csv(data_folder + "Prints.csv", types_to_csv_lines(prints))
#     write_csv(data_folder + "Brands.csv", types_to_csv_lines(brands))
#     write_csv(data_folder + "Styles.csv", types_to_csv_lines(styles))
#     write_csv(data_folder + "Sizes.csv", types_to_csv_lines(sizes))
#     write_csv(data_folder + "Colors.csv", types_to_csv_lines(colors))

#     write_csv(data_folder + "Clothes.csv", clothes_to_csv_lines(clothes))