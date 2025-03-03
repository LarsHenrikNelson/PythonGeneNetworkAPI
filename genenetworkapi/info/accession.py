from pathlib import Path
from functools import lru_cache

import pandas as pd
import requests
from bs4 import BeautifulSoup

from .._utils import _download
from .probeset import convert_probeset_from_string


@lru_cache(maxsize=10)
def get_accession_info():
    data_page = "https://info.genenetwork.org/index.php"
    xx = requests.get(data_page).text
    soup = BeautifulSoup(xx, "html.parser")
    table = soup.find("table")
    rows = table.find_all("tr")
    header = rows[0]
    header_th = header.find_all("th")
    accession_dict = {}
    column_names = []
    for i in header_th[:-1]:
        accession_dict[i.text] = []
        column_names.append(i.text)
    rows = rows[1:]
    for i in rows:
        rows_th = i.find_all("td")
        for j, cname in zip(rows_th, column_names):
            accession_dict[cname].append(j.text)
    accession_df = pd.DataFrame(accession_dict)
    return accession_df


def _accession_file_names(url: str):
    tt = requests.get(url)
    soup = BeautifulSoup(tt.text, "html.parser")
    aa = soup.find_all("a")
    files = []
    for i in aa:
        if i["href"] != "../":
            temp = i["href"]
            temp_url = f"{url}{temp}"
            files.append(temp_url)
    return files


def _accession_files(urls):
    output = {}
    for i in urls:
        data = _download(i)
        df = convert_probeset_from_string(data)
        name = Path(i).stem
        output[name] = df
    return output


@lru_cache(maxsize=10)
def get_accession_data(accession_number: str | list[str]):
    if isinstance(accession_number, str):
        accession_number = [accession_number]
    files = []
    for an in accession_number:
        file_url = f"https://files.genenetwork.org/current/GN{an}/"
        i_files = _accession_file_names(file_url)
        files.extend(i_files)
    output = _accession_files(files)
    return output
