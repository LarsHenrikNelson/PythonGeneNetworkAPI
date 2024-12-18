import requests

import pandas as pd

from .utils_geno import GN_URL, genofile_location_json
from .query import _check_status, _convert_to_df

# This file contains the functions to get data from gene network APIs

############################
# Functions returning list #
############################
"""                                                                                    
    list_species(species: str ="";gn_url: str =gn_url())

Returns a data frame with a list of species respresented in the
GeneNetwork database.  If the `species` string is non-empty, it will
return the information of the matched species.
"""


def list_species(species: str = "") -> pd.DataFrame:
    """
    Returns a data frame with a list of species respresented in the
    GeneNetwork database.  If the `species` string is non-empty, it will
    return the information of the matched species.

    Args:
        species (str, optional): Species on GeneNetwork. Defaults to "".

    Returns:
        pd.DataFrame: Dataframe of information retrieved from GeneNetwork
    """
    if len(species) != 0:
        url = f"{GN_URL}/species/{species}"
    else:
        url = f"{GN_URL}/species"
    res = requests.get(url)
    _check_status(res.status_code, "Species not in GeneNetwork")
    return _convert_to_df(res.json())


def list_groups(species: str = "") -> pd.DataFrame:
    """
    If `species` is not specified, then it returns all groups (segregating
    populations) represented in the GeneNetwork database.  If the string
    `species` is specified, then it returns all groups for that species.

    Args:
        species (str, optional): Species on GeneNetwork. Defaults to "".

    Returns:
        pd.DataFrame: Dataframe of information retrieved from GeneNetwork
    """
    if len(species) != 0:
        url = f"{GN_URL}/groups/{species}"
    else:
        url = f"{GN_URL}/groups"
    res = requests.get(url)
    _check_status(res.status_code, "Species not in GeneNetwork")
    return _convert_to_df(res.json())


def list_datasets(group: str) -> pd.DataFrame:
    """
    Lists all datasets available in a specified `group`.

     Args:
         group (str): Grou on GeneNetwork

     Returns:
         pd.DataFrame: Dataframe of information retrieved from GeneNetwork
    """
    url = f"{GN_URL}/datasets/{group}"
    res = requests.get(url)
    _check_status(res.status_code, "Group not in GeneNetwork")
    return _convert_to_df(res.json())


def list_geno(group: str) -> dict[str, list[str]]:
    """
    Returns a dictionary with the location name of the different geno files of
    a group, and if available some metadata such as strain of the first filial
    generation, maternal and paternal strain.
    If there exist more than one location, the default location is indicated
    by a `*`.

    Args:
        group (str): Group on GeneNetwork

    Raises:
        AttributeError: If no metadata is found

    Returns:
        dict[str, list[str]]: A dictionary of locations and metadata
    """
    # parse geno meta
    geno_url = f"{GN_URL}/genotypes/view/{group}"
    req = requests.get(geno_url)

    _check_status(req.status_code, "No metadata or could not parse json page.")

    # check if "genofile" keys exist
    json_parsed = req.json()
    if "genofile" not in json_parsed:
        raise AttributeError("genofile key not found")

    # get geno meta
    if len(json_parsed) > 1:
        meta_keys = [i for i in json_parsed.keys() if i != "genofile"]
        vmeta_geno = []
        for i in meta_keys:
            vmeta_geno.append(
                json_parsed[i] if isinstance(json_parsed[i], list) else [json_parsed[i]]
            )
        x = genofile_location_json(json_parsed)
        vmeta_geno.append(x)
        meta_keys.append("location")
        dfmeta_geno = {j: i for i, j in zip(vmeta_geno, meta_keys)}
    else:  # only location available in metadata
        vmeta_geno = genofile_location_json(json_parsed)
        dfmeta_geno = {"location": vmeta_geno}

    if len(dfmeta_geno["location"]) > 1:
        format = f"{group}.geno"  # expect ".geno" location file
        idx_default = [
            index for index, i in enumerate(dfmeta_geno["location"]) if i == format
        ]
        temp = dfmeta_geno["location"]
        for i in idx_default:
            dfmeta_geno["location"][i] = f"{temp[i]}*"
    return dfmeta_geno
