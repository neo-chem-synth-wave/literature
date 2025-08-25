# Overview
**Title:**
Ambit-SMIRKS: A Software Module for Reaction Representation, Reaction Search and Structure Transformation

**Authors:**
Kochev, N., Avramova, S., and Jeliazkova, N. |
Kochev, N. et al.

**Publication Date:**
2018/08/20

**Link:**
[BMC Journal of Cheminformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-018-0295-6)

**Alternative Links:**
[ambit](https://ambit.sourceforge.net/smirks.html) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC6102164) |
[ResearchGate](https://www.researchgate.net/publication/327130573_Ambit-SMIRKS_a_software_module_for_reaction_representation_reaction_search_and_structure_transformation)

**Starred:**
False

**Tags:**
reaction-descriptor, ambit-smirks


# Abstract
Ambit-SMIRKS is an open source software, enabling structure transformation via the SMIRKS language and implemented as an extension of Ambit-SMARTS.
As part of the Ambit project it builds on top of The Chemistry Development Kit (The CDK).
Ambit-SMIRKS provides the following functionalities: parsing of SMIRKS linear notations into internal reaction (transformation) representations based on The CDK objects, application of the stored reactions against target (reactant) molecules for actual transformation of the target chemical objects, reaction searching, stereo information handling, product post-processing, etc.
The transformations can be applied on various sites of the reactant molecule in several modes: single, non-overlapping, non-identical, non-homomorphic or externally specified list of sites utilizing efficient substructure searching algorithm.
Ambit-SMIRKS handles the molecules stereo information and supports basic chemical stereo elements implemented in The CDK library.
The full SMARTS logical expressions syntax for reactions specification is supported, including recursive SMARTS expressions as well as additional syntax extensions.
Since its initial development for the purpose of metabolite generation within Toxtree, the Ambit-SMIRKS module was used in various chemoinformatics projects, both developed by the authors of the package and by external teams.
We show several use cases of the Ambit-SMIRKS software including standardization of large chemical databases and pathway transformation database and prediction.
Ambit-SMIRKS is distributed as a Java library under LGPL license.
More information on use cases and applications, including download links is available at http://ambit.sourceforge.net/smirks.


# Citation
```
@article {kochev2018,
  author       = { Nikolay Kochev and Svetlana Avramova and Nina Jeliazkova },
  title        = { Ambit-SMIRKS: a software module for reaction representation, reaction search and structure transformation },
  journal      = { Journal of Cheminformatics },
  year         = { 2018 },
  pages        = { 42 },
  month        = { Aug },
  volume       = { 10 },
  number       = { 1 },
  day          = { 20 },
  issn         = { 1758-2946 },
  doi          = { 10.1186/s13321-018-0295-6 },
  url          = { https://doi.org/10.1186/s13321-018-0295-6 }
}
```
