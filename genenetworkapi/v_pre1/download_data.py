from .query import GN_URL
from .utils_geno import genofile_location, has_genofile_meta
from .._utils import _download


def download_geno(group, filepath: None | str = None, format: str = "geno"):

    if has_genofile_meta(group):
        # need to check real location of data
        vlocation = genofile_location(group)

    if len(vlocation) == 1:
        group = vlocation[0][0:-5]

    geno_url = f"{GN_URL}/genotypes/{group}.{format}"

    return _download(geno_url, filepath)


def download_pheno(dataset: str, filepath: None | str = None):
    pheno_url = f"{GN_URL}/sample_data/{dataset}Publish"
    return _download(pheno_url, filepath)


def download_omics(dataset: str, filepath: None | str = None):
    dataset_url = f"{GN_URL}/sample_data/{dataset}"
    return _download(dataset_url, filepath)
