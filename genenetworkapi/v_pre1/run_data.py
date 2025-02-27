import requests
from typing import Literal

import pandas as pd

from .query import GN_URL, _check_status, _convert_to_df


def run_gemma(
    db: str, trait_id: str, use_loco: bool = False, maf: float = 0.01
) -> tuple[str, pd.DataFrame]:
    loco = "true" if use_loco else "false"
    url = f"{GN_URL}/mapping?trait_id={trait_id}&db={db}&method=gemma&use_loco={loco}&maf={maf}"
    res = requests.get(url)
    _check_status(res.status_code, "DB and/or trait are not in GeneNetwork database.")
    res = res.json()
    df = _convert_to_df(res[0])
    return res[1], df


def run_rqtl(
    db: str,
    trait_id: str,
    method: Literal["hk", "em", "ehk", "imp", "mr", "mr_imp", "mr-argmax"] = "hk",
    model: Literal["normal", "binary", "2part", "np"] = "normal",
    n_perm: int = 0,
    control_marker: str = "",
    interval_mapping: bool = False,
) -> pd.DataFrame:
    method = method.lower()
    model = model.lower()

    im = "true" if interval_mapping else "false"
    url = f"{GN_URL}/mapping?trait_id={trait_id}&db={db}&method=rqtl&rqtl_method={method}&rqtl_model={model}&num_perm={n_perm}&interval_mapping={im}"
    if len(control_marker) > 0:
        url = f"{url}&control_marker={control_marker}"
    res = requests.get(url)
    _check_status(
        res.status_code, "Dataset and/or trait are not in GeneNetwork database."
    )
    df = _convert_to_df(res.json())
    return df


def run_correlation(
    trait_id: str,
    db: str,
    target_db: str,
    tp: Literal["sample", "tissue"] = "sample",
    method: Literal["pearson", "spearman"] = "pearson",
    n_result: int = 500,
) -> pd.DataFrame:
    url = f"{GN_URL}/correlation?trait_id={trait_id}&db={db}&target_db={target_db}&type={tp}&method={method}&return={n_result}"
    res = requests.get(url)
    _check_status(
        res.status_code, "Dataset, trait and/or group are not in GeneNetwork database."
    )
    df = _convert_to_df(res.json())
    return df
