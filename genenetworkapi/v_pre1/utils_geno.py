# import re
from io import StringIO

import requests
import pandas as pd

from .query import GN_URL


def _convert_probeset_from_string(data: str):
    index = 0
    firstline = data[index]
    while firstline[0] == "#" or firstline[0] == "@":
        index += 1
        firstline = data[index]
    new_string = StringIO("".join(data[index:]))
    probe_set = pd.read_csv(new_string, header=0, sep="\t")
    probe_set = probe_set.loc[:, ~probe_set.columns.str.contains("^Unnamed")]
    return probe_set


def parse_geno(filename: str | list[str]):
    # read the file into lines
    if not isinstance(filename, list):
        with open(filename, mode="r") as f:
            lines = f.readlines()
    else:
        lines = filename
    df = _convert_probeset_from_string(lines)
    return df


"""                                                                                    
    genofile_location(json_parsed::Dict)

Returns a vector of String containing the location of geno files for a group.

---
    genofile_location(group::String)

Returns a vector of String containing the location of geno files for a group.

"""


def genofile_location_json(json_parsed: dict):
    # check if "genofile" keys exist
    if "genofile" not in json_parsed:
        raise AttributeError("genofile key not found")

    # check number of genofile for a group
    n_genofile = len(json_parsed["genofile"])

    vlocation_genofile = []

    for i in range(n_genofile):
        if "location" in json_parsed["genofile"][i]:
            vlocation_genofile.append(json_parsed["genofile"][i]["location"])
        else:
            raise AttributeError("location key not found")

    return vlocation_genofile


def genofile_location(group: str):
    # parse geno meta
    geno_url = f"{GN_URL}/genotypes/view/{group}"
    json_parsed = requests.get(geno_url).json()

    return genofile_location_json(json_parsed)


"""                                                                                    
    has_genofile_meta(group::String; gn_url::String=gn_url())

Returns `true` if the group's genotype files possesse metadata that may contain 
alternative location of the files.
"""


def has_genofile_meta(group: str):
    geno_url = f"{GN_URL}/genotypes/view/{group}"
    status = requests.get(geno_url).status_code
    if status >= 500 and status < 600:
        return False
    else:
        return True
