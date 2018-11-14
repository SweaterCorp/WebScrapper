import urllib
from bs4 import BeautifulSoup
import requests
import csv
import urllib.request
import typing
import time
from typing import List, Tuple
import re

from Logging import Logging


def list_to_str(items):
    open_bracket = "["
    close_bracket = "]"
    str_list = [str(item) for item in items]
    array_strs = ','.join(str_list)
    return open_bracket + array_strs + close_bracket


def normalize_str(string: str, capitalize="normal", replace: Tuple[str, str] = None):
    string = string.strip().replace('\n', '')
    if(capitalize.lower() == "lower"):
        string = string.lower()
    if(capitalize.lower() == "upper"):
        string = string.upper()
    if (replace is not None):
        string = string.replace(replace[0], replace[1])
    string = re.sub(r'\s+', ' ', string)
    return string


def get_soup(url: str):
    # url = urllib.request.urlopen(url)#requests.get(url).text
    html = requests.get(url).text
    return BeautifulSoup(html, "html5lib")

def write_to_file(file_path:str, text: str):
        with open(file_path, "w") as file:
            file.write(text)

