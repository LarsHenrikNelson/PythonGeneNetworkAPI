from pathlib import Path
from io import StringIO

import pandas as pd


def convert_probeset(filepath: str | Path):
    if isinstance(filepath, str):
        filepath = Path(filepath)
    with open(
        filepath,
        "r",
    ) as w:
        m = w.readlines()
    indices = [index for index, i in enumerate(m) if i[0] == "#"]
    new_string = StringIO("".join(m[indices[1] + 2 :]))
    probe_set = pd.read_csv(new_string, header=0, sep="\t")
    probe_set = probe_set.drop(columns=["Unnamed: 2"])
    probe_set.to_csv(filepath.with_suffix(".csv"))
    return probe_set
