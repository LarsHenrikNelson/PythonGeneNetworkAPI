import tempfile

import requests


def _download(url, filepath: None | str = None):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        if filepath is None:
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
