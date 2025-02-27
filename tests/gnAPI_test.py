import pandas as pd

import genenetworkapi.v_pre1 as gnapi


def test_list_species():
    df_test = pd.DataFrame(
        [{"FullName": "Mus musculus", "Id": 1, "Name": "mouse", "TaxonomyId": 10090}]
    )
    assert df_test.equals(gnapi.list_species("mouse"))


def test_list_groups():
    df_test = pd.DataFrame(
        [
            {
                "DisplayName": "Hybrid Rat Diversity Panel (Includes HXB/BXH)",
                "FullName": "Hybrid Rat Diversity Panel (Includes HXB/BXH)",
                "GeneticType": "None",
                "Id": 10,
                "MappingMethodId": "1",
                "Name": "HXBBXH",
                "SpeciesId": 2,
                "public": 2,
            }
        ]
    )
    groups = gnapi.list_groups("rat")
    assert df_test.loc[0].equals(groups.loc[0])


def test_get_geno():
    genos = gnapi.get_geno("BXD").iloc[:10]

    assert genos.shape == (10, 241)
    assert genos.loc[0, "Locus"] == "rsm10000000001"
    assert genos.loc[0, "Chr"] == 1
    assert genos.loc[0, "BXD2"] == "B"


def test_list_datasets():
    datasets = gnapi.list_datasets("HSNIH-Palmer")
    assert datasets.shape == (10, 11)
