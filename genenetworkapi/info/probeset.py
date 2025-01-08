from pathlib import Path
from io import StringIO

import pandas as pd


def convert_probeset_from_file(filepath: str | Path):
    if isinstance(filepath, str):
        filepath = Path(filepath)
    with open(
        filepath,
        "r",
    ) as w:
        m = w.readlines()
    probe_set = convert_probeset_from_string(m)
    probe_set.to_csv(filepath.with_suffix(".csv"))
    return probe_set


def convert_probeset_from_string(data: str):
    indices = [index for index, i in enumerate(data) if i[0] == "#"]
    new_string = StringIO("".join(data[indices[1] + 2 :]))
    probe_set = pd.read_csv(new_string, header=0, sep="\t")
    probe_set = probe_set.loc[:, ~probe_set.columns.str.contains("^Unnamed")]
    return probe_set
