import io
from pathlib import Path
import zipfile
import tempfile
from functools import lru_cache


import requests


@lru_cache(maxsize=30)
def _download(url, filepath: None | str = None):
    if filepath is not None:
        filepath = Path(filepath)
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        url = Path(url)
        if url.suffix == ".zip":
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall(filepath / f"{url.stem}.zip")
        elif filepath is None:
            with tempfile.TemporaryFile() as fp:
                for chunk in r.iter_content(chunk_size=8192):
                    fp.write(chunk)
                fp.seek(0)
                output = fp.readlines()
        else:
            with open(filepath, "wb") as fp:
                for chunk in r.iter_content(chunk_size=8192):
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    # if chunk:
                    fp.write(chunk)
                fp.seek(0)
                output = fp.readlines()
    output = [x.decode("ascii", errors="ignore") for x in output]
    return output
