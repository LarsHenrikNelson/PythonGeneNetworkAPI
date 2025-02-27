# GeneNetworkAPI

Provides access to the [GeneNetwork](http://genenetwork.org) database
and analysis functions using the [GeneNetwork REST
API](https://github.com/genenetwork/gn-docs/blob/master/api/GN2-REST-API.md).

Karl Broman wrote the
[GNapi](https://github.com/kbroman/GNapi/blob/main/README.md) R
package for providing access to GeneNetwork from R.  This package
follows the structure and function of that package closely.

## Note on terminology

GeneNetwork collects data on genetically segregating populations
(called _groups_) in a number of _species_ including humans.  Most of
the phenotype data is "omic" data which are organized as _datasets_. 

## Import genenetworkapi


```python
import genenetworkapi.v_pre1 as gnapi
```

## Check connection
To check if the website is responding properly:


```python
gnapi.check_gn()
```

    GeneNetwork is alive.
    




    200



## Get species list
Which species have data on them?


```python
gnapi.list_species()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FullName</th>
      <th>Id</th>
      <th>Name</th>
      <th>TaxonomyId</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mus musculus</td>
      <td>1</td>
      <td>mouse</td>
      <td>10090</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Rattus norvegicus</td>
      <td>2</td>
      <td>rat</td>
      <td>10116</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Arabidopsis thaliana</td>
      <td>3</td>
      <td>arabidopsis</td>
      <td>3702</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Homo sapiens</td>
      <td>4</td>
      <td>human</td>
      <td>9606</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Hordeum vulgare</td>
      <td>5</td>
      <td>barley</td>
      <td>4513</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Fly (Drosophila melanogaster dm6)</td>
      <td>6</td>
      <td>drosophila</td>
      <td>7227</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Macaca mulatta</td>
      <td>7</td>
      <td>monkey</td>
      <td>9544</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Glycine max</td>
      <td>8</td>
      <td>soybean</td>
      <td>3847</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Solanum lycopersicum</td>
      <td>9</td>
      <td>tomato</td>
      <td>4081</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Populus trichocarpa</td>
      <td>10</td>
      <td>poplar</td>
      <td>3689</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Oryzias latipes (Japanese medaka)</td>
      <td>11</td>
      <td>medaka</td>
      <td>8090</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Bat (Glossophaga soricina)</td>
      <td>12</td>
      <td>bat</td>
      <td>27638</td>
    </tr>
  </tbody>
</table>
</div>



To get information on a single species:


```python
gnapi.list_species("rat")
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FullName</th>
      <th>Id</th>
      <th>Name</th>
      <th>TaxonomyId</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rattus norvegicus</td>
      <td>2</td>
      <td>rat</td>
      <td>10116</td>
    </tr>
  </tbody>
</table>
</div>



## List groups for a species
Since the information is organized by segregating population
("group"), it is useful to get a list for a particular species you
might be interested in.


```python
gnapi.list_groups("rat")
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>DisplayName</th>
      <th>FullName</th>
      <th>GeneticType</th>
      <th>Id</th>
      <th>MappingMethodId</th>
      <th>Name</th>
      <th>SpeciesId</th>
      <th>public</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Hybrid Rat Diversity Panel (Includes HXB/BXH)</td>
      <td>Hybrid Rat Diversity Panel (Includes HXB/BXH)</td>
      <td>None</td>
      <td>10</td>
      <td>1</td>
      <td>HXBBXH</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>UIOWA SRxSHRSP F2</td>
      <td>UIOWA SRxSHRSP F2</td>
      <td>intercross</td>
      <td>24</td>
      <td>1</td>
      <td>SRxSHRSPF2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NIH Heterogeneous Stock (RGSMC 2013)</td>
      <td>NIH Heterogeneous Stock (RGSMC 2013)</td>
      <td>None</td>
      <td>42</td>
      <td>1</td>
      <td>HSNIH-RGSMC</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NIH Heterogeneous Stock (Palmer)</td>
      <td>NIH Heterogeneous Stock (Palmer)</td>
      <td>None</td>
      <td>55</td>
      <td>None</td>
      <td>HSNIH-Palmer</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NWU WKYxF344 F2 Behavior</td>
      <td>NWU WKYxF344 F2 Behavior</td>
      <td>intercross</td>
      <td>82</td>
      <td>3</td>
      <td>NWU_WKYxF344_F2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>HIV-1Tg and Control</td>
      <td>HIV-1Tg and Control</td>
      <td>None</td>
      <td>83</td>
      <td>1</td>
      <td>HIV-1Tg</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>HRDP-HXB/BXH Brain Proteome</td>
      <td>HRDP-HXB/BXH Brain Proteome</td>
      <td>None</td>
      <td>87</td>
      <td>1</td>
      <td>HRDP_HXB-BXH-BP</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>HRDP-HXB/BXH Metabolome</td>
      <td>HRDP-HXB/BXH Metabolome</td>
      <td>None</td>
      <td>98</td>
      <td>1</td>
      <td>HRDP_HXB-BXH-Metb</td>
      <td>2</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



You can see the type of population it is.  Note the short name
(`Name`) as that will be used in queries involving that population
(group).

## Get genotypes for a group
To get the genotypes of a group:


```python
gnapi.get_geno("BXD").iloc[:10]
```
    
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Chr</th>
      <th>Locus</th>
      <th>cM</th>
      <th>Mb</th>
      <th>BXD1</th>
      <th>BXD2</th>
      <th>BXD5</th>
      <th>BXD6</th>
      <th>BXD8</th>
      <th>BXD9</th>
      <th>...</th>
      <th>BXD077xBXD062F1</th>
      <th>BXD083xBXD045F1</th>
      <th>BXD087xBXD100F1</th>
      <th>BXD065bxBXD055F1</th>
      <th>BXD102xBXD077F1</th>
      <th>BXD102xBXD73bF1</th>
      <th>BXD170xBXD172F1</th>
      <th>BXD172xBXD197F1</th>
      <th>BXD197xBXD009F1</th>
      <th>BXD197xBXD170F1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>rsm10000000001</td>
      <td>0.00</td>
      <td>3.001490</td>
      <td>B</td>
      <td>B</td>
      <td>D</td>
      <td>D</td>
      <td>D</td>
      <td>B</td>
      <td>...</td>
      <td>D</td>
      <td>H</td>
      <td>B</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>B</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>rs31443144</td>
      <td>0.11</td>
      <td>3.010274</td>
      <td>B</td>
      <td>B</td>
      <td>D</td>
      <td>D</td>
      <td>D</td>
      <td>B</td>
      <td>...</td>
      <td>D</td>
      <td>H</td>
      <td>B</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>B</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>rs6269442</td>
      <td>0.21</td>
      <td>3.492195</td>
      <td>B</td>
      <td>B</td>
      <td>D</td>
      <td>D</td>
      <td>D</td>
      <td>B</td>
      <td>...</td>
      <td>D</td>
      <td>H</td>
      <td>B</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>B</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>rs32285189</td>
      <td>0.32</td>
      <td>3.511204</td>
      <td>B</td>
      <td>B</td>
      <td>D</td>
      <td>D</td>
      <td>D</td>
      <td>B</td>
      <td>...</td>
      <td>D</td>
      <td>H</td>
      <td>B</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>B</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>rs258367496</td>
      <td>0.43</td>
      <td>3.659804</td>
      <td>B</td>
      <td>B</td>
      <td>D</td>
      <td>D</td>
      <td>D</td>
      <td>B</td>
      <td>...</td>
      <td>D</td>
      <td>H</td>
      <td>B</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>B</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1</td>
      <td>rs32430919</td>
      <td>0.53</td>
      <td>3.777023</td>
      <td>B</td>
      <td>B</td>
      <td>D</td>
      <td>D</td>
      <td>D</td>
      <td>B</td>
      <td>...</td>
      <td>D</td>
      <td>H</td>
      <td>B</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>B</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1</td>
      <td>rs36251697</td>
      <td>0.64</td>
      <td>3.812265</td>
      <td>B</td>
      <td>B</td>
      <td>D</td>
      <td>D</td>
      <td>D</td>
      <td>B</td>
      <td>...</td>
      <td>D</td>
      <td>H</td>
      <td>B</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>B</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1</td>
      <td>rs30658298</td>
      <td>0.75</td>
      <td>4.430623</td>
      <td>B</td>
      <td>B</td>
      <td>D</td>
      <td>D</td>
      <td>D</td>
      <td>B</td>
      <td>...</td>
      <td>D</td>
      <td>H</td>
      <td>B</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>B</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1</td>
      <td>rs31879829</td>
      <td>0.85</td>
      <td>4.518714</td>
      <td>B</td>
      <td>B</td>
      <td>D</td>
      <td>D</td>
      <td>D</td>
      <td>B</td>
      <td>...</td>
      <td>D</td>
      <td>H</td>
      <td>B</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>B</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1</td>
      <td>rs36742481</td>
      <td>0.96</td>
      <td>4.776319</td>
      <td>B</td>
      <td>B</td>
      <td>D</td>
      <td>D</td>
      <td>D</td>
      <td>B</td>
      <td>...</td>
      <td>D</td>
      <td>H</td>
      <td>B</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>B</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 241 columns</p>
</div>



Currently, we only support the `.geno` format which returns a data
frame of genotypes with rows as marker and columns as individuals.

## List datasets for a group

To list the (omic) datasets available for a group, you have to use the
name as listed in the group list for a species:




```python
gnapi.list_datasets("HSNIH-Palmer")
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AvgID</th>
      <th>CreateTime</th>
      <th>DataScale</th>
      <th>FullName</th>
      <th>Id</th>
      <th>Long_Abbreviation</th>
      <th>ProbeFreezeId</th>
      <th>ShortName</th>
      <th>Short_Abbreviation</th>
      <th>confidentiality</th>
      <th>public</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>24</td>
      <td>Mon, 27 Aug 2018 00:00:00 GMT</td>
      <td>log2</td>
      <td>HSNIH-Palmer Nucleus Accumbens Core RNA-Seq (A...</td>
      <td>860</td>
      <td>HSNIH-Rat-Acbc-RSeq-Aug18</td>
      <td>347</td>
      <td>HSNIH-Palmer Nucleus Accumbens Core RNA-Seq (A...</td>
      <td>HSNIH-Rat-Acbc-RSeq-0818</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>24</td>
      <td>Sun, 26 Aug 2018 00:00:00 GMT</td>
      <td>log2</td>
      <td>HSNIH-Palmer Infralimbic Cortex RNA-Seq (Aug18...</td>
      <td>861</td>
      <td>HSNIH-Rat-IL-RSeq-Aug18</td>
      <td>348</td>
      <td>HSNIH-Palmer Infralimbic Cortex RNA-Seq (Aug18...</td>
      <td>HSNIH-Rat-IL-RSeq-0818</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>24</td>
      <td>Sat, 25 Aug 2018 00:00:00 GMT</td>
      <td>log2</td>
      <td>HSNIH-Palmer Lateral Habenula RNA-Seq (Aug18) ...</td>
      <td>862</td>
      <td>HSNIH-Rat-LHB-RSeq-Aug18</td>
      <td>349</td>
      <td>HSNIH-Palmer Lateral Habenula RNA-Seq (Aug18) ...</td>
      <td>HSNIH-Rat-LHB-RSeq-0818</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>24</td>
      <td>Fri, 24 Aug 2018 00:00:00 GMT</td>
      <td>log2</td>
      <td>HSNIH-Palmer Prelimbic Cortex RNA-Seq (Aug18) ...</td>
      <td>863</td>
      <td>HSNIH-Rat-PL-RSeq-Aug18</td>
      <td>350</td>
      <td>HSNIH-Palmer Prelimbic Cortex RNA-Seq (Aug18) ...</td>
      <td>HSNIH-Rat-PL-RSeq-0818</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24</td>
      <td>Thu, 23 Aug 2018 00:00:00 GMT</td>
      <td>log2</td>
      <td>HSNIH-Palmer Orbitofrontal Cortex RNA-Seq (Aug...</td>
      <td>864</td>
      <td>HSNIH-Rat-VoLo-RSeq-Aug18</td>
      <td>351</td>
      <td>HSNIH-Palmer Orbitofrontal Cortex RNA-Seq (Aug...</td>
      <td>HSNIH-Rat-VoLo-RSeq-0818</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>24</td>
      <td>Fri, 14 Sep 2018 00:00:00 GMT</td>
      <td>log2</td>
      <td>HSNIH-Palmer Nucleus Accumbens Core RNA-Seq (A...</td>
      <td>868</td>
      <td>HSNIH-Rat-Acbc-RSeqlog2-Aug18</td>
      <td>347</td>
      <td>HSNIH-Palmer Nucleus Accumbens Core RNA-Seq (A...</td>
      <td>HSNIH-Rat-Acbc-RSeqlog2-0818</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>24</td>
      <td>Fri, 14 Sep 2018 00:00:00 GMT</td>
      <td>log2</td>
      <td>HSNIH-Palmer Infralimbic Cortex RNA-Seq (Aug18...</td>
      <td>869</td>
      <td>HSNIH-Rat-IL-RSeqlog2-Aug18</td>
      <td>348</td>
      <td>HSNIH-Palmer Infralimbic Cortex RNA-Seq (Aug18...</td>
      <td>HSNIH-Rat-IL-RSeqlog2-0818</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>24</td>
      <td>Fri, 14 Sep 2018 00:00:00 GMT</td>
      <td>log2</td>
      <td>HSNIH-Palmer Lateral Habenula RNA-Seq (Aug18) ...</td>
      <td>870</td>
      <td>HSNIH-Rat-LHB-RSeqlog2-Aug18</td>
      <td>349</td>
      <td>HSNIH-Palmer Lateral Habenula RNA-Seq (Aug18) ...</td>
      <td>HSNIH-Rat-LHB-RSeqlog2-0818</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>24</td>
      <td>Fri, 14 Sep 2018 00:00:00 GMT</td>
      <td>log2</td>
      <td>HSNIH-Palmer Prelimbic Cortex RNA-Seq (Aug18) ...</td>
      <td>871</td>
      <td>HSNIH-Rat-PL-RSeqlog2-Aug18</td>
      <td>350</td>
      <td>HSNIH-Palmer Prelimbic Cortex RNA-Seq (Aug18) ...</td>
      <td>HSNIH-Rat-PL-RSeqlog2-0818</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>24</td>
      <td>Fri, 14 Sep 2018 00:00:00 GMT</td>
      <td>log2</td>
      <td>HSNIH-Palmer Orbitofrontal Cortex RNA-Seq (Aug...</td>
      <td>872</td>
      <td>HSNIH-Rat-VoLo-RSeqlog2-Aug18</td>
      <td>351</td>
      <td>HSNIH-Palmer Orbitofrontal Cortex RNA-Seq (Aug...</td>
      <td>HSNIH-Rat-VoLo-RSeqlog2-0818</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



## Get sample data for a group

This gives you a matrix with rows as individuals/samples/strains and
columns as "clinical" (non-omic) phenotypes.  The number after the
underscore is the phenotype number (to be used later).  Some data may
be missing.


```python
gnapi.get_pheno("HSNIH-Palmer").iloc[81:100]
``` 

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>HSR_10001</th>
      <th>HSR_10002</th>
      <th>HSR_10003</th>
      <th>HSR_10004</th>
      <th>HSR_10005</th>
      <th>HSR_10006</th>
      <th>HSR_10007</th>
      <th>HSR_10008</th>
      <th>HSR_10009</th>
      <th>...</th>
      <th>HSR_10499</th>
      <th>HSR_10500</th>
      <th>HSR_10501</th>
      <th>HSR_10502</th>
      <th>HSR_10503</th>
      <th>HSR_10504</th>
      <th>HSR_10505</th>
      <th>HSR_10506</th>
      <th>HSR_10507</th>
      <th>HSR_10508</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>81</th>
      <td>00072AAC0D</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>82</th>
      <td>00072AC972</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>83</th>
      <td>00077E61DC</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>84</th>
      <td>00077E61EC</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>85</th>
      <td>00077E61F3</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>86</th>
      <td>00077E61F5</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>87</th>
      <td>00077E6204</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>88</th>
      <td>00077E6207</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>89</th>
      <td>00077E6299</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>90</th>
      <td>00077E62CD</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>91</th>
      <td>00077E62D2</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>92</th>
      <td>00077E633D</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>93</th>
      <td>00077E634B</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>94</th>
      <td>00077E63D9</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>95</th>
      <td>00077E641E</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>96</th>
      <td>00077E6433</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>97</th>
      <td>00077E64B3</td>
      <td>8672.990234</td>
      <td>86.414001</td>
      <td>4762.080078</td>
      <td>63.416</td>
      <td>24076.119141</td>
      <td>87.117996</td>
      <td>84.0</td>
      <td>43.57</td>
      <td>6614.970215</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>98</th>
      <td>00077E64BA</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>99</th>
      <td>00077E64C1</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
  </tbody>
</table>
<p>19 rows × 509 columns</p>
</div>



To obtain omics phenotypes, you can utilize the `get_omics()` function, which provides a matrix with individuals/samples/strains as rows and omic phenotypes as columns. This function requires the input of a short abbreviation representing the available (omic) datasets for a particular group. To obtain the short abbreviation, you can refer to the section titled "List datasets for a group" and use the `list_dataset()` function.
For instance, if you want to acquire the phenotype matrix corresponding to "HSNIH-Palmer Infralimbic Cortex RNA-Seq (Aug18) rlog," you would use its respective short abbreviation.


```python
gnapi.get_omics("HSNIH-Rat-IL-RSeq-0818")
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>ENSRNOG00000000001</th>
      <th>ENSRNOG00000000007</th>
      <th>ENSRNOG00000000008</th>
      <th>ENSRNOG00000000009</th>
      <th>ENSRNOG00000000010</th>
      <th>ENSRNOG00000000012</th>
      <th>ENSRNOG00000000017</th>
      <th>ENSRNOG00000000021</th>
      <th>ENSRNOG00000000024</th>
      <th>...</th>
      <th>ENSRNOG00000062292</th>
      <th>ENSRNOG00000062293</th>
      <th>ENSRNOG00000062297</th>
      <th>ENSRNOG00000062299</th>
      <th>ENSRNOG00000062300</th>
      <th>ENSRNOG00000062301</th>
      <th>ENSRNOG00000062302</th>
      <th>ENSRNOG00000062303</th>
      <th>ENSRNOG00000062304</th>
      <th>ENSRNOG00000062307</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>00071F4FAF</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>1</th>
      <td>00071F6771</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>2</th>
      <td>00071F768E</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>3</th>
      <td>00071F95F9</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>4</th>
      <td>00071FB160</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>6166</th>
      <td>00077E840E</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>6167</th>
      <td>00077E9879</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>6168</th>
      <td>00077E9920</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>6169</th>
      <td>00077E9D84</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <th>6170</th>
      <td>00077E949D</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>...</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
  </tbody>
</table>
<p>6171 rows × 32624 columns</p>
</div>



underscore is the phenotype number (to be used later).  Some data may
be missing.

## Get information about traits

To get information on a particular (non-omic) trait use the group name
and the trait number:


```python
gnapi.info_dataset(dataset="HSNIH-Palmer", trait="10308")
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>dataset_type</th>
      <th>description</th>
      <th>id</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>phenotype</td>
      <td>Central nervous system, behavior: Reaction tim...</td>
      <td>10308</td>
      <td>reaction_time_pint1_5</td>
    </tr>
  </tbody>
</table>
</div>



## Summary information on traits

Get a list of the maximum LRS for each trait and position.


```python
gnapi.info_pheno(group="HXBBXH").iloc[:10]
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Additive</th>
      <th>Authors</th>
      <th>Chr</th>
      <th>Description</th>
      <th>Id</th>
      <th>LRS</th>
      <th>Locus</th>
      <th>Mb</th>
      <th>Mean</th>
      <th>PubMedID</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.049997</td>
      <td>Pravenec M, Zidek V, Musilova A, Simakova M, K...</td>
      <td>8</td>
      <td>Original post publication description: insulin...</td>
      <td>10001</td>
      <td>16.283131</td>
      <td>rsRn10010063</td>
      <td>27.969673</td>
      <td>0.18364</td>
      <td>12016513.0</td>
      <td>2002</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.092636</td>
      <td>Pravenec M, Zidek V, Musilova A, Simakova M, K...</td>
      <td>14</td>
      <td>Original post publication description: insulin...</td>
      <td>10002</td>
      <td>10.977678</td>
      <td>rs63915446</td>
      <td>0.439058</td>
      <td>0.28140</td>
      <td>12016513.0</td>
      <td>2002</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.601890</td>
      <td>Pravenec M, Zidek V, Musilova A, Simakova M, K...</td>
      <td>20</td>
      <td>Original post publication description: glucose...</td>
      <td>10003</td>
      <td>13.651471</td>
      <td>rsRn10018260</td>
      <td>0.117740</td>
      <td>6.34948</td>
      <td>12016513.0</td>
      <td>2002</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.992576</td>
      <td>Pravenec M, Zidek V, Musilova A, Simakova M, K...</td>
      <td>8</td>
      <td>Original post publication description: glucose...</td>
      <td>10004</td>
      <td>13.152060</td>
      <td>rsRn10010761</td>
      <td>109.713893</td>
      <td>7.08640</td>
      <td>12016513.0</td>
      <td>2002</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.008542</td>
      <td>Pravenec M, Zidek V, Musilova A, Simakova M, K...</td>
      <td>8</td>
      <td>Original post publication description: insulin...</td>
      <td>10005</td>
      <td>18.589521</td>
      <td>rsRn10010063</td>
      <td>27.969673</td>
      <td>0.02916</td>
      <td>12016513.0</td>
      <td>2002</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-0.035521</td>
      <td>Pravenec M, Zidek V, Musilova A, Simakova M, K...</td>
      <td>8</td>
      <td>Original post publication description: insulin...</td>
      <td>10006</td>
      <td>13.389624</td>
      <td>rsRn10010217</td>
      <td>48.384095</td>
      <td>0.04080</td>
      <td>12016513.0</td>
      <td>2002</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.413279</td>
      <td>Pravenec M, Zidek V, Musilova A, Simakova M, K...</td>
      <td>2</td>
      <td>Original post publication description: glucose...</td>
      <td>10007</td>
      <td>10.034807</td>
      <td>rsRn10002250</td>
      <td>61.977051</td>
      <td>6.64560</td>
      <td>12016513.0</td>
      <td>2002</td>
    </tr>
    <tr>
      <th>7</th>
      <td>-0.936806</td>
      <td>Pravenec M, Zidek V, Musilova A, Simakova M, K...</td>
      <td>3</td>
      <td>Original post publication description: glucose...</td>
      <td>10008</td>
      <td>13.249384</td>
      <td>rsRn10004899</td>
      <td>146.548904</td>
      <td>9.14200</td>
      <td>12016513.0</td>
      <td>2002</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1.239130</td>
      <td>Pravenec M, Zidek V, Musilova A, Simakova M, K...</td>
      <td>7</td>
      <td>Original post publication description: glucose...</td>
      <td>10009</td>
      <td>12.081519</td>
      <td>rsRn10009060</td>
      <td>28.357297</td>
      <td>8.57000</td>
      <td>12016513.0</td>
      <td>2002</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1.298196</td>
      <td>Pravenec M, Zidek V, Musilova A, Simakova M, K...</td>
      <td>7</td>
      <td>Original post publication description: glucose...</td>
      <td>10010</td>
      <td>10.594786</td>
      <td>rsRn10009060</td>
      <td>28.357297</td>
      <td>8.38132</td>
      <td>12016513.0</td>
      <td>2002</td>
    </tr>
  </tbody>
</table>
</div>



You could also specify a group and a trait number or a dataset and a probename.


```python
gnapi.info_pheno(dataset="BXD", trait="10001")
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>additive</th>
      <th>id</th>
      <th>locus</th>
      <th>lrs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.394444</td>
      <td>4</td>
      <td>rs48756159</td>
      <td>13.497491</td>
    </tr>
  </tbody>
</table>
</div>




```python
gnapi.info_pheno(group="HC_M2_0606_P", trait="1436869_at")
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>additive</th>
      <th>alias</th>
      <th>chr</th>
      <th>description</th>
      <th>id</th>
      <th>locus</th>
      <th>lrs</th>
      <th>mb</th>
      <th>mean</th>
      <th>name</th>
      <th>p_value</th>
      <th>se</th>
      <th>symbol</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.214088</td>
      <td>HHG1; HLP3; HPE3; SMMCI; Dsh; Hhg1</td>
      <td>5</td>
      <td>sonic hedgehog (hedgehog)</td>
      <td>99602</td>
      <td>rs8253327</td>
      <td>12.771128</td>
      <td>28.457155</td>
      <td>9.279091</td>
      <td>1436869_at</td>
      <td>0.306</td>
      <td>None</td>
      <td>Shh</td>
    </tr>
  </tbody>
</table>
</div>



## Analysis commands


### GEMMA

- db (required) - Dataset name for the trait below (Short_Abbreviation listed when you query for datasets)
- trait_id (required) - ID form trait being mapped
- use_loco - Whether to use LOCO (leave one chromosome out) method (default = False)
- maf - minor allele frequency (default = 0.01)


```python
name, df = gnapi.run_gemma(db="BXDPublish", trait_id="10015", use_loco=True)
print(name)
print(df.iloc[:10])
```

    BXD_GWA_U07BSX
             Mb  additive chr  lod_score            name   p_value
    0  3.001490  0.496897   1   0.548219  rsm10000000001  0.282996
    1  3.010274  0.496897   1   0.548219      rs31443144  0.282996
    2  3.492195  0.496897   1   0.548219       rs6269442  0.282996
    3  3.511204  0.496897   1   0.548219      rs32285189  0.282996
    4  3.659804  0.496897   1   0.548219     rs258367496  0.282996
    5  3.777023  0.496897   1   0.548219      rs32430919  0.282996
    6  3.812265  0.496897   1   0.548219      rs36251697  0.282996
    7  4.430623  0.496897   1   0.548219      rs30658298  0.282996
    8  4.518714  0.496897   1   0.548219      rs31879829  0.282996
    9  4.776319  0.496897   1   0.548219      rs36742481  0.282996
    

### R/qtl

This function performs a one-dimensional genome scan.  The arguments
are

- db (required) - Dataset name for trait below (Short_Abbreviation listed
  when you query for datasets)
- trait_id (required) - ID for trait being mapped
- method - Corresponds to the "method" option for the R/qtl scanone function (default = hk; Options: hk, ehk, em, imp, mr, mr-imp mr-argmax)
- model - corresponds to the "model" option for the R/qtl scanone function normal (default = normal, Options: normal, binary, 2-part, np) 
- n_perm - number of permutations (default = 0)
- control_marker - Name of marker to use as control; this relies on
  the user knowing the name of the marker they want to use as a
  covariate
- interval_mapping - Whether to use interval mapping (default = False)


```python
gnapi.run_rqtl(db="BXDPublish", trait_id="10015").iloc[:10]
```


### Correlation

This function correlates a trait in a dataset against all traits in a
target database.

- db (required) - DB name for the trait above (this is the Short_Abbreviation listed when you query for datasets)
- trait_id (required) - ID for trait used for correlation
- target_db (required) - Target DB name to be correlated against
- tp - (default = sample; Option: sample, tissue)
- method - (default = pearson; Options: pearson, spearman)
- return - Number of results to return (default = 500)


```python
gnapi.run_correlation(
    trait_id="1427571_at", db="HC_M2_0606_P", target_db="BXDPublish"
).iloc[:10]
```

    https://genenetwork.org/api/v_pre1/correlation?trait_id=1427571_at&db=HC_M2_0606_P&target_db=BXDPublish&type=sample&method=pearson&return=500
    

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#_strains</th>
      <th>p_value</th>
      <th>sample_r</th>
      <th>trait</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6</td>
      <td>0.004805</td>
      <td>-0.942857</td>
      <td>20511</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>0.004805</td>
      <td>-0.942857</td>
      <td>20724</td>
    </tr>
    <tr>
      <th>2</th>
      <td>12</td>
      <td>0.000018</td>
      <td>-0.923362</td>
      <td>13536</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>0.006807</td>
      <td>0.892857</td>
      <td>10157</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7</td>
      <td>0.006807</td>
      <td>-0.892857</td>
      <td>20392</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>0.018845</td>
      <td>0.885714</td>
      <td>20479</td>
    </tr>
    <tr>
      <th>6</th>
      <td>12</td>
      <td>0.000189</td>
      <td>-0.875658</td>
      <td>12762</td>
    </tr>
    <tr>
      <th>7</th>
      <td>12</td>
      <td>0.000246</td>
      <td>0.868653</td>
      <td>12760</td>
    </tr>
    <tr>
      <th>8</th>
      <td>7</td>
      <td>0.013697</td>
      <td>-0.857143</td>
      <td>20559</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>0.002220</td>
      <td>-0.842424</td>
      <td>10925</td>
    </tr>
  </tbody>
</table>
</div>


