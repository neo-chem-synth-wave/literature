# Contribution Instructions
To contribute to this repository, please adhere to the following instructions:

1. **Check out a new branch** with an appropriate name.

2. **Add the new files** in the appropriate **publication year directories**.
If a publication year directory does not exist, create it yourself.
Prioritize literature from the [contribution wishlist](/contribution/wishlist.md).
Only add officially published peer-reviewed literature relevant to computer-assisted chemical synthesis.
Refer to the subsection outlining the [relevant literature sources](#relevant-literature-sources) for more information.
Adhere to the following file naming conventions:

    ```
    # One Author (e.g., Author Ęugene McAuthórśky):
    yyyymmdd_mcauthorsky_a_e.md

    # Two Authors (e.g., Author Ęugene McAuthórśky and Coauthor Oliver Bradshaw de Machine):
    yyyymmdd_mcauthorsky_a_e_and_de_machine_c_o_b.md

    # Three or More Authors (e.g., Author Ęugene McAuthórśky, Coauthor Oliver Bradshaw de Machine, and Mentor Complainson):
    yyyymmdd_mcauthorsky_a_e_et_al.md
    ```

3. **Format the new files** in accordance with the subsection outlining the [formatting instructions](#formatting-instructions).

4. Once a reasonable number of new files (_e.g._, ~10) are added, **create a pull request and assign a reviewer**.

5. After the pull request is approved by the assigned reviewer and the branch is successfully merged, **delete the branch**.


## Relevant Literature Sources
The relevant literature sources are as follows:

- **Conferences**:
  - [Association for the Advancement of Artificial Intelligence (AAAI) Conference on Artificial Intelligence](https://aaai.org/conference/aaai)
  - [Conference on Neural Information Processing Systems (NeurIPS)](https://nips.cc)
  - [International Joint Conferences on Artificial Intelligence (IJCAI)](https://ijcai.org)
  - [International Conference on Learning Representations (ICLR)](https://icml.cc)
  - [International Conference on Machine Learning (ICML)](https://iclr.cc)

- **Journals**:
  - [American Chemical Society (ACS)](https://pubs.acs.org/action/doSearch)
  - [Multidisciplinary Digital Publishing Institute (MDPI)](https://mdpi.com/search)
  - [Nature](https://nature.com/search/advanced)
  - [Public Library of Science (PLOS)](https://journals.plos.org/plosone/search)
  - [Royal Society of Chemistry (RSC)](https://pubs.rsc.org/en/search/advancedsearch)
  - [Science](https://science.org/search/advanced)
  - [Elsevier ScienceDirect](https://sciencedirect.com/search)
  - [Springer](https://link.springer.com/advanced-search)
  - [Thieme](https://thieme-connect.com/products/all/search)
  - [Wiley](https://onlinelibrary.wiley.com/search/advanced)

- **Pre-prints**:
  - [arXiv](https://arxiv.org/search/advanced)
  - [bioRxiv](https://biorxiv.org/search)
  - [ChemRxiv](https://chemrxiv.org/engage/chemrxiv/search-dashboard)

- **Others**:
  - [Academia](https://academia.edu)
  - [CORE](https://core.ac.uk)
  - [DSpace@MIT](https://dspace.mit.edu/discover)
  - [GitHub](https://github.com/search/advanced)
  - [PubMed Central](https://ncbi.nlm.nih.gov/pmc/advanced)
  - [ResearchGate](https://researchgate.net/search.Search.html)


## Formatting Instructions
While formatting a new file, please adhere to the following instructions:


### Overview
**Title:**
Format the **official title** using this [title format converter](https://titlecaseconverter.com) with the **APA**, **Keep Words in All Caps**, and **Use Straight Quotes** options toggled on.
Replace any em dash (_i.e._, **—**) and curly quotation (_i.e._, **‘’** and **“”**) symbols with hyphen (_i.e._, **-**) and straight quotation (_i.e._, **''** and **""**) symbols, respectively. 
For example:

```markdown
# Overview
**Title:**
A Relevant Computer-Assisted Chemical Synthesis Topic: The 'Official' Title
```

**Authors:**
Write the long and short versions of the **official author information** in the **Vancouver referencing format including periods and special symbols** here using the **' |\n'** symbol combination as a delimiter.
The short official author is formatted as follows: **McAuthórśky, A.Ę.**, **McAuthórśky, A.Ę. and de Machine, C.O.B.**, and **McAuthórśky, A.Ę. et al.** in the case of one, two, and three or more authors, respectively.
For example:

```markdown
**Authors:**
McAuthórśky, A.Ę., de Machine, C.O.B., and Complainson, M. |
McAuthórśky, A.Ę. et al.
```

**Publication Date:**
Write the **official publication date** in the **yyyy/mm/dd date format** here.
For example:

```markdown
**Publication Date:**
2000/12/31
```

**Link:**
Copy the **official link** here.
For example:

```markdown
**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/journal/jcisd8)
```

**Alternative Links:**
Write the **alternative links** (_e.g._, alternative, pre-print, web page, data source, code, etc.) here using the **' |\n'** symbol combination as a delimiter.
Avoid adding links to illegal sources.
If there are no alternative links, write **None**.
For example:

```markdown
**Alternative Links:**
[arXiv](https://arxiv.org) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov) |
[ResearchGate](https://researchgate.net)
```

**Starred:**
Write **True** or **False** here depending on whether **the literature is starred or not**, respectively.
For example:

```markdown
**Starred:**
True
```

**Tags:**
Write **the tags that summarize the official contents** here using the **' ,'** symbol combination as a delimiter.
Use the hyphen instead of the space symbols for tags with more than one word.
For example:

```markdown
**Tags:**
single-step-retrosynthesis, multi-step-retrosynthesis, template-based
```


### Abstract
Write the **official abstract** here, separating each sentence in a new row.
Replace any unrecognized and curly quotation symbols with appropriate alternative and straight quotation symbols, respectively. 
For example:

```markdown
# Abstract
The first sentence of the official abstract text.
The 'second' sentence of the official abstract text.
The "third" sentence of the official abstract text.
...
```


### Citation
Copy the **official citation** in the **BibTex format** here.
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
