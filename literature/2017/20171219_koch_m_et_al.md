# Overview
**Title:**
Molecular Structures Enumeration and Virtual Screening in the Chemical Space With RetroPath2.0

**Authors:**
Koch, M., Duigou, T., Carbonell, P., and Faulon, J. |
Koch, M. et al.

**Publication Date:**
2017/12/19

**Link:**
[BMC Journal of Cheminformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-017-0252-9)

**Alternative Links:**
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC5736515) |
[ResearchGate](https://www.researchgate.net/publication/321912129_Molecular_structures_enumeration_and_virtual_screening_in_the_chemical_space_with_RetroPath20) |
[ResearchGate (Pre-print)](https://www.researchgate.net/publication/345712064_Molecular_structures_enumeration_and_virtual_screening_in_the_chemical_space_with_RetroPath20)

**Tags:**
multi-step-synthesis


# Abstract
Background

Network generation tools coupled with chemical reaction rules have been mainly developed for synthesis planning and more recently for metabolic engineering.
Using the same core algorithm, these tools apply a set of rules to a source set of compounds, stopping when a sink set of compounds has been produced.
When using the appropriate sink, source and rules, this core algorithm can be used for a variety of applications beyond those it has been developed for.

Results

Here, we showcase the use of the open source workflow RetroPath2.0.
First, we mathematically prove that we can generate all structural isomers of a molecule using a reduced set of reaction rules.
We then use this enumeration strategy to screen the chemical space around a set of monomers and predict their glass transition temperatures, as well as around aminoglycosides to search structures maximizing antibacterial activity.
We also perform a screening around aminoglycosides with enzymatic reaction rules to ensure biosynthetic accessibility.
We finally use our workflow on an E. coli model to complete E. coli metabolome, with novel molecules generated using promiscuous enzymatic reaction rules.
These novel molecules are searched on the MS spectra of an E. coli cell lysate interfacing our workflow with OpenMS through the KNIME Analytics Platform.

Conclusion

We provide an easy to use and modify, modular, and open-source workflow.
We demonstrate its versatility through a variety of use cases including molecular structure enumeration, virtual screening in the chemical space, and metabolome completion.
Because it is open source and freely available on MyExperiment.org, workflow community contributions should likely expand further the features of the tool, even beyond the use cases presented in the paper.


# Citation
```
@article {20171227_wang_l_et_al,
  author       = { Mathilde Koch and Thomas Duigou and Pablo Carbonell and Jean-Loup Faulon },
  title        = { Molecular structures enumeration and virtual screening in the chemical space with RetroPath2.0 },
  journal      = { Journal of Cheminformatics },
  year         = { 2017 },
  pages        = { 64 },
  month        = { Dec },
  volume       = { 9 },
  number       = { 1 },
  day          = { 19 },
  issn         = { 1758-2946 },
  doi          = { 10.1186/s13321-017-0252-9 },
  url          = { https://doi.org/10.1186/s13321-017-0252-9 }
}
```
