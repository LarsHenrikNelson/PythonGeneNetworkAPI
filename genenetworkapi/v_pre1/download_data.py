from typing import Literal
from pathlib import Path

from .query import GN_URL
from .utils_geno import genofile_location, has_genofile_meta
from .._utils import _download


def download_geno(
    group,
    filepath: None | Path | str = None,
    format: Literal["bimbam", "rqtl2", "geno"] = "geno",
    dataset: str | None = None,
):

    if has_genofile_meta(group):
        # need to check real location of data
        vlocation = genofile_location(group)

    if len(vlocation) == 1:
        group = vlocation[0][0:-5]

    geno_url = f"{GN_URL}/genotypes/{format}/{group}"

    if format == "rqtl2":
        if dataset is not None:
            geno_url = geno_url + f"/{dataset}.zip"

    return _download(geno_url, filepath)


def download_pheno(dataset: str, filepath: None | Path | str = None):
    pheno_url = f"{GN_URL}/sample_data/{dataset}Publish"
    return _download(pheno_url, filepath)


def download_omics(dataset: str, filepath: None | Path | str = None):
    dataset_url = f"{GN_URL}/sample_data/{dataset}"
    return _download(dataset_url, filepath)
