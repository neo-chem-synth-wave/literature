# Contribution Instructions
To contribute to this repository, please adhere to the following instructions:

1. **Check out a new branch** with an appropriate title.

2. **Add the new literature files** in the appropriate **publication year directories**.
If a publication year directory does not exist, create it yourself.
Prioritize literature from the [contribution wishlist](/contribution/wishlist.md).
Only add officially published peer-reviewed literature relevant to computer-assisted chemical synthesis.
Refer to the subsection outlining the [relevant literature sources](#relevant-literature-sources) for more information.
Adhere to the following literature file naming conventions:

    ```
    # One Author (e.g., Author Ęugene McAuthórśky):
    yyyymmdd_mcauthorsky_a_e.md

    # Two Authors (e.g., Author Ęugene McAuthórśky and Coauthor Oliver Bradshaw de Machine):
    yyyymmdd_mcauthorsky_a_e_and_de_machine_c_o_b.md

    # Three or More Authors (e.g., Author Ęugene McAuthórśky, Coauthor Oliver Bradshaw de Machine, and Mentor Complainson):
    yyyymmdd_mcauthorsky_a_e_et_al.md
    ```

3. **Format the new literature files** in accordance with the subsection outlining the [formatting instructions](#formatting-instructions).

4. Once a reasonable number of new literature files (_e.g._, ~10) are added, **create a pull request and assign a reviewer**. 

5. After the pull request is approved and the branch is successfully merged, **delete the branch**.


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
  - [PubMed Central](https://ncbi.nlm.nih.gov/pmc/advanced)
  - [ResearchGate](https://researchgate.net/search.Search.html)


## Formatting Instructions
While formatting a new literature file, please adhere to the following instructions:


### Overview
**Title:**
Copy the **official publication title** in this [title format converter](https://titlecaseconverter.com) with the **APA**, **Keep Words in All Caps**, and **Use Straight Quotes** options toggled on.
Convert and copy the modified title here.
For example:

```markdown
# Overview
**Title:**
Title of a Publication About a Relevant Computer-Assisted Chemical Synthesis Topic
```

**Authors:**
Copy the **official publication author information** in the **Vancouver referencing format** with periods and special symbols here.
For example:

```markdown
**Authors:**
McAuthórśky, A.Ę., de Machine, C.O.B., and Complainson, M.
```

**Publication Date:**
Copy the **official publication date** in the **yyyy/mm/dd date format** here.
For example:

```markdown
**Publication Date:**
2000/12/31
```

**Publication Link:**
Copy the **official publication link** here.
For example:

```markdown
**Publication Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/journal/jcisd8)
```

**Alternative Links:**
Copy the **alternative links** (_e.g._, alternative publication, pre-print, web page, data source, code, etc.) here using the **|** symbol as a delimiter.
Write each link in a new row.
Avoid adding links to illegal sources.
If there are no alternative links, write **None**.
For example:

```markdown
**Alternative Links:**
[arXiv](https://arxiv.org) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov) |
[ResearchGate](https://researchgate.net)
```

**Impact:**
Write **True** or **False** here depending on whether the **official publication is impactful or not**.
For example:

```markdown
**Impact:**
True
```

**Tags:**
Write the **tags that summarize the contents of the official publication** here using the **-** symbol as a delimiter.
For example:

```markdown
**Tags:**
single-step-retrosynthesis, multi-step-retrosynthesis, template-based
```


### Abstract
Copy the **official publication abstract** here.
Write each sentence in a new row.
Remove any unrecognized symbols and curly quotation (_i.e._, **‘’** and **“”**) symbols.
For example:

```markdown
# Abstract
The first sentence of the abstract text.
The second sentence of the abstract text containing the 'curly quotation symbols'.
The third sentence of the abstract text containing the "curly quotation symbols".
...
```


### Citation
Copy the **official publication citation** in the **BibTex format** here.
If the download of the citation is only available in the **RIS format**, please convert it to the **BibTex format** using this [RIS2BibTex citation format converter](https://www.bruot.org/ris2bib).
Format the citation using this [BibTex citation format normalizer](https://hsborges.github.io/bibtex-normalizer).
This normalizer formats the citation using the **{** and **}** symbols as delimiters, but it omits them for some fields. (_e.g._, year, volume, number, etc.)
Add the **{** and **}** symbols as delimiters wherever they are missing after the formatting.
Delete the **abstract** and **keywords** fields, if originally included.
Title the citation with the **lowercase surname of the first author followed by the year of publication**.
For example:

````markdown
# Citation
```
@article {mcauthorsky2000,
  author       = { ... },
  title        = { ... },
  journal      = { ... },
  year         = { ... },
  ...,
  url          = { ... }
}
```
````
