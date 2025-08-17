# Contribution Instructions
To contribute to this repository, please adhere to the following instructions:

1. Check out a new branch with an appropriate title. (_e.g._, 20001231_contribution_by_mcauthorsky_a_e)

2. Add the new literature files in the appropriate publication year directories.
If a publication year directory does not exist, create it yourself.
Only add officially published peer-reviewed literature relevant to computer-assisted chemical synthesis. (_i.e._, avoid adding pre-print publications)
Refer to the section outlining the [relevant literature sources](#relevant-literature-sources) for more information.
Adhere to the following literature file naming conventions:

    ```
    # One Author (Author Ęugene McAuthórśky):
    yyyymmdd_mcauthorsky_a_e.md
    
    # Two Authors (Author Ęugene McAuthórśky and Coauthor Oliver Bradshaw de Machine):
    yyyymmdd_mcauthorsky_a_e_and_de_machine_c_o_b.md
    
    # Three or More Authors (Author Ęugene McAuthórśky, Coauthor Oliver Bradshaw de Machine, and Mentor Complainson):
    yyyymmdd_mcauthorsky_a_e_et_al.md
    ```

3. Format the literature files referring to the section outlining the [formatting instructions](#formatting-instructions).

4. Once a reasonable number of literature files are added (_e.g._, ~10), create a pull request and assign a reviewer.

5. After the pull request is approved and the branch is successfully merged, delete the branch.


## Relevant Literature Sources
The relevant literature sources are as follows:

- **Conferences**:
  - [NeurIPS](https://nips.cc)
  - [ICLR](https://icml.cc)
  - [ICML](https://iclr.cc)

- **Journals**:
  - [American Chemical Society (ACS)](https://pubs.acs.org/action/doSearch)
  - [Multidisciplinary Digital Publishing Institute (MDPI)](https://mdpi.com/search)
  - [Nature](https://nature.com/search/advanced)
  - [PLOS ONE](https://journals.plos.org/plosone/search)
  - [Royal Society of Chemistry (RCS)](https://pubs.rsc.org/en/search/advancedsearch)
  - [Science](https://science.org/search/advanced)
  - [ScienceDirect](https://sciencedirect.com/search)
  - [Springer](https://link.springer.com/advanced-search)
  - [Thieme](https://thieme-connect.com/products/all/search)
  - [Wiley](https://onlinelibrary.wiley.com/search/advanced)

- **Pre-prints**:
  - [arXiv](https://arxiv.org/search/advanced)
  - [bioRxiv](https://biorxiv.org/search)
  - [ChemRxiv](https://chemrxiv.org/engage/chemrxiv/search-dashboard)

- **Others**:
  - [DSpace@MIT](https://dspace.mit.edu/discover)
  - [GitHub](https://github.com/search/advanced)
  - [PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/advanced)
  - [ResearchGate](https://researchgate.net/search.Search.html)


## Formatting Instructions
To format a literature file, please adhere to the following instructions:


### Overview (NOTE: Format as Title (i.e., Use the # symbol instead of the ### symbol.))
**Title:**
Copy the **official publication title** in this [title format converter](https://titlecaseconverter.com) with the **APA**, **Keep Words in All Caps**, and **Use Straight Quotes** options toggled on.
Convert and copy the modified title here.
(_e.g._, `Title of the Publication About a Relevant Topic`)

**Authors:**
Copy the **official publication author information** in the **Vancouver referencing format** with periods and special symbols here.
(_e.g._, `McAuthórśky, A.Ę., de Machine, C.O.B., and Complainson, M.`)

**Publication Date:**
Copy the **official publication date** in the **yyyy/mm/dd date format** here.
(_e.g._, `2000/12/31`)

**Publication Link:**
Copy the **official publication link** here.
(_e.g._, `[ACS JCIM](https://pubs.acs.org/journal/jcisd8)`)

**Alternative Links:**
Copy the **alternative links** (_e.g._, alternative publication, pre-print, web page, data source, and code) here using the **|** symbol as a delimiter with each link in a new row.
Avoid adding links to illegal sources.
If there are no alternative links, write **None**.
(_e.g._, `[arXiv](https://pubs.acs.org/journal/jcisd8) |\n[PubMed Central](https://pmc.ncbi.nlm.nih.gov)` or `None`)

**Impact:**
Add **True** or **False** here depending on whether the **official publication is impactful or not**.
(_e.g._, `True` or `False`)

**Tags:**
Add the **tags** that summarize the contents of the **official publication** here using the **-** symbol as a delimiter.
(_e.g._, `single-step-retrosynthesis, template-based, data-source`)


### Abstract (NOTE: Format as Title (i.e., Use the # symbol instead of the ### symbol.))
Copy the **official publication abstract** here separating each sentence in a new row.
(_e.g._, `The first sentence of the abstract text.\nThe second sentence of the abstract text.\n...`)


### Citation (NOTE: Format as Title (i.e., Use the # symbol instead of the ### symbol.))
Copy the **official publication citation** in the **BibTex citation format** here.
If the download of the citation file is only available in the **RIS citation format**, please convert it to the BibTex citation format using this [RIS2BibTex citation format converter](https://www.bruot.org/ris2bib).
Format the citation file using this [BibTex citation format normalizer](https://hsborges.github.io/bibtex-normalizer).
This normalizer formats the citation file using the **{ ** and ** }** delimiter symbols, but it omits them for some fields. (_e.g._, year)
Add the **{ ** and ** }** delimiter symbols wherever they are missing after the normalization.
Delete the **abstract** and **keywords** fields, if included.
Title the citation with the lowercase surname of the first author followed by the year of publication.
(_e.g._, `@article {mcauthorsky2000,\n...\n}`)
