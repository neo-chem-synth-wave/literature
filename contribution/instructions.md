# Contribution Instructions
To contribute to this repository, please adhere to the following instructions:

1. Check out a new branch with an appropriate title. 
2. Add a new literature file(s) in the appropriate year directory.
If the appropriate year directory does not exist, please create it yourself.
Add only officially published peer-reviewed literature (_i.e._, conferences and journals) relevant to computer-assisted chemical synthesis and avoid adding literature limited to pre-prints.
For more information, please refer to the section outlining the [relevant literature sources](#relevant-literature-sources).
Adhere to the following file naming conventions:

    ```
    # One Author (Author Ęugene McAuthórśky):
    yyyymmdd_mcauthorsky_a_e.md
    
    # Two Authors (Author Ęugene McAuthórśky and Coauthor Oliver Bradshaw de Machine):
    yyyymmdd_mcauthorsky_a_e_and_de_machine_c_o_b.md
    
    # Three or More Authors (Author Ęugene McAuthórśky, Coauthor Oliver Bradshaw de Machine, and Mentor Complainson):
    yyyymmdd_mcauthorsky_a_e_et_al.md
    ```

3. Update the new literature file(s) according to the [formatting instructions](#formatting-instructions).
4. Once a reasonable number of entries are added (_e.g._, up to 10 entries for quicker reviews), please create a pull request and assign a reviewer.
5. After the pull request is approved and the branch is successfully merged, delete the branch.


## Relevant Literature Sources
Please adhere to the following relevant literature sources:

- **Conference Publications**:
  - [NeurIPS](https://nips.cc)
  - [ICLR](https://icml.cc)
  - [ICML](https://iclr.cc)
- **Journal Publications**:
  - [American Chemical Society (ACS)](https://pubs.acs.org/action/doSearch)
  - [Multidisciplinary Digital Publishing Institute (MDPI)](https://www.mdpi.com/search)
  - [Nature](https://www.nature.com/search/advanced)
  - [PLOS ONE](https://journals.plos.org/plosone/search)
  - [Royal Society of Chemistry (RCS)](https://pubs.rsc.org/en/search/advancedsearch)
  - [Science](https://www.science.org/search/advanced)
  - [ScienceDirect](https://www.sciencedirect.com/search)
  - [Springer](https://link.springer.com/advanced-search)
  - [Thieme](https://www.thieme-connect.com/products/all/search)
  - [Wiley](https://onlinelibrary.wiley.com/search/advanced)
- **Pre-print Publications**:
  - [arXiv](https://arxiv.org/search/advanced)
  - [bioRxiv](https://www.biorxiv.org/search)
  - [ChemRxiv](https://chemrxiv.org/engage/chemrxiv/search-dashboard)
- **Other Publications**:
  - [ResearchGate](https://www.researchgate.net/search.Search.html)


## Formatting Instructions
Please adhere to the following formatting instructions while structuring the literature files:

### Overview
**Title:**
Copy the official publication title in this [title format converter](https://titlecaseconverter.com) with the **APA**, **Keep Words in All Caps**, and **Use Straight Quotes** options toggled on.
(_e.g._, McAuthórśky, A.Ę., de Machine, C.O.B., and Complainson, M.)

**Authors:**
Copy the official publication author information in the **Vancouver referencing with periods and special symbols** format here.
(_e.g._, McAuthórśky, A.Ę., de Machine, C.O.B., and Complainson, M.)

**Publication Date:**
Copy the official publication date in the **yyyy/mm/dd** date format here.
(_e.g._, 2000/12/31)

**Publication Link:**
Copy the official publication link here.
(_e.g._, `[ACS JCIM](https://pubs.acs.org/journal/jcisd8)`)

**Alternative Links:**
Copy the alternative links here using the **|** symbol as a delimiter with each link in a new row.
This is important because some official publications cannot be accessed for free, but the pre-prints or, in some cases, complete manuscripts can be found elsewhere online.
Please avoid any posting any illegal sources.
The best way of checking for alternative publication links is by Googling the exact title and author information.
If there are no alternative links to be found, simply write **None**.
Even if the official publication is open source, it is still useful to add two to three alternative publication links.
For example:

```markdown
[arXiv](https://pubs.acs.org/journal/jcisd8) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov) |
[ResearchGate](https://researchgate.net)
```

**Impact:**
Add **True** or **False** depending on whether the publication is impactful or not.
(_e.g._, True)

**Tags:**
Add the tags that summarize the contents of the publication here, using the **-** as a delimiter.
(_e.g._, single-step-retrosynthesis, template-based, data-source)


### Abstract
Copy the official publication abstract text here, separating each sentence in a new row.


### Citation
Copy the official publication citation in the BibTex format here.
If the download of the citation is only available in the RIS format, please convert it to BibTex using this [RIS2BibTex citation format converter](https://www.bruot.org/ris2bib).
Format the BibTex file using this [BibTex citation format normalizer](https://hsborges.github.io/bibtex-normalizer).
This normalizer formats the file using the **{ }** symbols, but it omits it for some fields. (_e.g._, year)
Considering this, please add the **{ }** symbols wherever they are missing after normalization, and additionally delete the **abstract** and **keywords** entries.
