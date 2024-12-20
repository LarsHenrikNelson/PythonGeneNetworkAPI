import pandas as pd
import requests
from bs4 import BeautifulSoup


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
