import urllib
from bs4 import BeautifulSoup
import requests
import csv
import urllib.request
import typing
from typing import List
import re


def list_to_str(items):
    open_bracket = "["
    close_bracket = "]"
    str_list = [str(item) for item in items]
    array_strs = ','.join(str_list)
    return open_bracket + array_strs + close_bracket


def normalize_str(string: str):
    string = string.strip().replace('\n', '')
    string = re.sub(r'\s+', ' ', string)
    return string
