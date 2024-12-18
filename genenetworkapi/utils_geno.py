import re
from io import StringIO

import requests
import pandas as pd

from .query import GN_URL


def parse_geno(filename: str | list[str]):
    # read the file into lines
    if not isinstance(filename, list):
        with open(filename, mode="r") as f:
            lines = f.readlines()
    else:
        lines = filename

    # which lines have # as first character
    firstpound = [bool(re.match(r"^#", x)) for x in lines]

    # which lines have @ as first character
    firstat = [bool(re.match(r"^@", x)) for x in lines]

    # find the first index where the difference is less than 0
    endcomment = [i or j for i, j in zip(firstpound, firstat)]
    header = [index for index, val in enumerate(endcomment) if not val][0]

    tempstring = "".join(lines)
    stringbytes = StringIO(tempstring)
    df = pd.read_csv(stringbytes, header=header, sep="\t")

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
