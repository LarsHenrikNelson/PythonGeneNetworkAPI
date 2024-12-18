import requests

from .utils_geno import GN_URL
from .query import _convert_to_df, _check_status


def info_dataset(dataset: str, trait: str = ""):
    if len(trait) != 0:
        url = f"{GN_URL}/dataset/{dataset}/{trait}"
    else:
        url = f"{GN_URL}/dataset/{dataset}"
    res = requests.get(url)
    _check_status(res.status_code, "Dataset not in GeneNetwork")
    return _convert_to_df(res.json())


def info_pheno(group: str, trait: str = ""):
    if len(trait) == 0:
        url = f"{GN_URL}/traits/{group}Publish.json"
    else:
        url = f"{GN_URL}/trait/{group}/{trait}"
    res = requests.get(url)
    _check_status(res.status_code, "Group and/or trait not in GeneNetwork")
    return _convert_to_df(res.json())
