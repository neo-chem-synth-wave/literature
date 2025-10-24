# Overview
**Title:**
ReactionDataExtractor: A Tool for Automated Extraction of Information From Chemical Reaction Schemes

**Authors:**
Wilary, D.M. and Cole, J.M.

**Publication Date:**
2021/09/15

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.1c01017)

**Alternative Links:**
[GitHub](https://github.com/dmw51/reactiondataextractor) |
[ReactionDataExtractor](http://www.reactiondataextractor.org)

**Tags:**
reaction-extraction, reaction-data-extractor


# Abstract
Chemical reaction schemes are commonly used for visual encapsulation of chemical information.
Figures of reaction schemes contain chemical transformations, the chemical species involved, as well as reaction conditions.
From a data-mining point of view, they constitute rich sources, densely packed with knowledge.
Yet, the challenge of automatically extracting data from them has remained largely untackled.
This work presents ReactionDataExtractor, a software tool that can be used for the automatic extraction of information from multistep reaction schemes.
Its capabilities include segmentation of reaction steps, regions containing reaction conditions, chemical diagrams, as well as optical character and structure recognition.
A combination of rules and unsupervised machine-learning approaches is used, with bespoke detection algorithms that identify arrows, structures, labels, and conditions detection algorithms.
It can be used as a low-maintenance tool for database generation capable of extracting data from large quantities of images supplied by the user.
On assessment using a self-generated evaluation set, the tool achieved precision and recall metrics of between 67% and 91% in the six core areas of data extraction.
The ReactionDataExtractor tool is released under the MIT license and is available to download from http://www.reactiondataextractor.org.


# Citation
```
@article {20210915b_wilary_d_m_and_cole_j_m,
  author       = { Damian M. Wilary and Jacqueline M. Cole },
  title        = { ReactionDataExtractor: A Tool for Automated Extraction of Information from Chemical Reaction Schemes },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2021 },
  note         = { PMID: 34525303 },
  pages        = { 4962-4974 },
  volume       = { 61 },
  number       = { 10 },
  doi          = { 10.1021/acs.jcim.1c01017 },
  url          = { https://doi.org/10.1021/acs.jcim.1c01017 },
  eprint       = { https://doi.org/10.1021/acs.jcim.1c01017 }
}
```
