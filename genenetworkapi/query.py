import pandas as pd
import requests

GN_URL = "https://genenetwork.org/api/v_pre1"


def check_gn():
    status = requests.get("https://genenetwork.org/api/v_pre1/").status_code
    if status == 200:
        print("GeneNetwork is alive.")
    else:
        print("Not successful.")
    return status


def _convert_to_df(json: dict | list):
    if isinstance(json, dict):
        json = [json]
    return pd.DataFrame(json)


def _check_status(status, error_text):
    if status >= 500 and status < 600:
        raise AttributeError(error_text)
