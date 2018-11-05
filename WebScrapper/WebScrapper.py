import urllib
from bs4 import BeautifulSoup
import requests
import csv
import urllib.request
import typing 
from typing import List

def parse_types(html:str, class_attribute: str):
    results = [];
    soup = BeautifulSoup(html, "html.parser");
    list = soup.find("div", {"class": f"multifilter {class_attribute}"});
    items = list.find_all("div", {"class":"multifilter-item"});
    for item in items:
        label = item.find("label")
        text = label.get_text();
        results.append(text);
    return results;

def parse_clothes(html:str):
    results = [];
    soup = BeautifulSoup(html, "html.parser");
    table_left_column = soup.find("div", {"class": "table__left-column"});
    list = table_left_column.find("div", {"class": "catalog-navigation-wrap"}).find("ul").find("ul");
    items = list.find_all("a", {"class":"link"});
    for item in items:
        text = item.get_text();
        href = item["href"];
        results.append((text, href));
    return results;

def read_html(file_path:str):
    file = open(file_path, "r", encoding="utf8")
    return file.read();

def read_csv(file_path:str):
    with open(file_path, "r", newline="") as file:
        return csv.reader(file)

def write_csv(file_path:str, rows):
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

folder = "../ParsingSites/";
types_file= "Types.html"

print_types =  "multifilter_print ";
brand_types =  "multifilter_brands";
style_types=  "multifilter_property_style ";
size_types= "multifilter_size_values "
color_types = "multifilter_colors"

html_text = read_html(folder + types_file);

prints = parse_types(html_text, print_types);
brands = parse_types(html_text, brand_types);
styles = parse_types(html_text, style_types);
sizes = parse_types(html_text, size_types);
colors = parse_types(html_text, color_types);

clothes = parse_clothes(html_text)




#a = parse_types(htmlText, brands_class)
#print(a)