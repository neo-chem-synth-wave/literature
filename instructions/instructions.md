# Contribution Instructions
**Step 1.** Check out a new branch with an appropriate title.

**Step 2.** Add a new file(s) in the appropriate year directory.
If the appropriate year directory does not exist, please add it yourself.
Please add only officially published peer-reviewed literature. (_i.e._, conferences and journals)
Stick to the following file naming convention:
```
# One Author (Author Ęugene McAuthórśky):
yyyymmdd_mcauthorsky_a_e.md

# Two Authors (Author Ęugene McAuthórśky and Coauthor Oliver Bradshaw de Machine):
yyyymmdd_mcauthorsky_a_e_and_de_machine_c_o_b.md

# Three or More Authors (Author Ęugene McAuthórśky, Coauthor Oliver Bradshaw de Machine, and Mentor Complainson):
yyyymmdd_mcauthorsky_a_e_et_al.md
```

**Step 3.** Update the new file(s) according to the [formatting instructions](#formatting-instructions).

**Step 4.** Once a reasonable number of entries are added (_e.g._, around ten for quicker reviews), please create a pull request for merging the branch, and assign a reviewer.

**Step 5.** After the branch is successfully merged, please delete the branch.

You can either modify the format of the [existing literature](notion_export_old_format) or add new entries, but please keep the literature relevant to computer-assisted chemical synthesis. 


# Formatting Instructions
# Overview
**Title:**
Copy the official publication title here.

**Authors:**
Copy the official publication author information in the **Vancouver** referencing format here.
(_e.g._, McAuthórśky, A.Ę., de Machine, C.O.B., and Complainson, M.)

**Publication Date:**
Copy the official publication date in the **yyyy/mm/dd** date format here.
(_e.g._, 0000/12/31)

**Publication Link:**
Copy the official publication link here.
(_e.g._, `[ACS JCIM](https://pubs.acs.org/journal/jcisd8)`)

**Alternative Publication Links:**
Copy the alternative publication links here using the | symbol as a delimiter.
This is important because a lot of official publications cannot be accessed for free, but the pre-prints or, in some cases, complete manuscripts can be found elsewhere online.
The best way of checking for alternative publication links is by Googling the exact title.
If there are no alternative links to be found, omit this section altogether.
Even if the official publication is open source, it is still useful to add two to three alternative publication links.
Please avoid any posting any illegal sources.
(_e.g._, `[arXiv](https://pubs.acs.org/journal/jcisd8)` | `[PubMed Central](https://pmc.ncbi.nlm.nih.gov)` | `[ResearchGate](https://researchgate.net)`)


# Abstract
Copy the official publication abstract text here.
Please separate each sentence in a new row, so the document is readable even in the raw form.


# Citation
Copy the official publication citation in the BibTex format here.
Please use the "" instead of the {} symbols as delimiters, and omit the abstract and keywords fields.
Indent every row instead of the first and last with a tab space.
Title the citation with the surname of the first author followed by the year.
If duplicates occur, distinguish them by adding a, b, c, etc. ordered by publication date.
If a site does not offer the BibTex format, please download the available format (_e.g._, RIS) and convert it to BibTex using this [converter](https://www.bruot.org/ris2bib).
(_e.g._, `@article{mcauthorsky0000 ... }`)
