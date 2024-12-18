import pandas as pd

from genenetworkapi import list_species


def test_list_species():
    df_test = pd.DataFrame(
        [{"FullName": "Mus musculus", "Id": 1, "Name": "mouse", "TaxonomyId": 10090}]
    )
    assert df_test.equals(list_species("mouse"))
