from io import StringIO
import pandas as pd

from .download_data import download_geno, download_pheno, download_omics
from .utils_geno import parse_geno


def get_geno(group: str, filepath: None | str = None, format="geno"):
    geno_file = download_geno(group, filepath=filepath, format=format)
    df = parse_geno(geno_file)
    return df


def get_pheno(dataset: str, filepath: None | str = None) -> pd.DataFrame:
    """
    Returns a given `trait` in a `group`.

    Args:
        dataset (str): _description_
        filepath (None | str, optional): Filepath to save file to
        otherwise saves to a temporary file that is discarded when
        function returns.

    Returns:
        pd.DataFrame: Dataframe of omics data retrieved from GeneNetwork
    """
    pheno_file = download_pheno(dataset, filepath)
    tempstring = "".join(pheno_file)
    stringbytes = StringIO(tempstring)
    df = pd.read_csv(stringbytes, header=0, sep=",")
    return df


def get_omics(dataset: str) -> pd.DataFrame:
    """
    Returns the omic phenotypes for a given dataset.

    Args:
        dataset (str): Dataset to query

    Returns:
        pd.DataFrame: Dataframe of omics data retrieved from GeneNetwork

    """
    omics_file = download_omics(dataset)
    tempstring = "".join(omics_file)
    stringbytes = StringIO(tempstring)
    df = pd.read_csv(stringbytes, header=0, sep=",")
    return df
