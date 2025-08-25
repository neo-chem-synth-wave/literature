# Overview
**Title:**
rBAN: Retro-Biosynthetic Analysis of Nonribosomal Peptides

**Authors:**
Ricart, E., Leclére, V., Flissi, A., Mueller, M., Pupin, M., Lisacek, F. |
Ricart, E. et al.

**Publication Date:**
2019/02/08

**Link:**
[BMC Journal of Cheminformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0335-x)

**Alternative Links:**
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC6689883) |
[rBAN](https://norine.univ-lille.fr/rban) |
[ResearchGate](https://www.researchgate.net/publication/330972010_RBAN_Retro-biosynthetic_analysis_of_nonribosomal_peptides)

**Starred:**
False

**Tags:**
single-step-retrosynthesis, rban


# Abstract
Proteinogenic and non-proteinogenic amino acids, fatty acids or glycans are some of the main building blocks of nonribsosomal peptides (NRPs) and as such may give insight into the origin, biosynthesis and bioactivities of their constitutive peptides.
Hence, the structural representation of NRPs using monomers provides a biologically interesting skeleton of these secondary metabolites.
Databases dedicated to NRPs such as Norine, already integrate monomer-based annotations in order to facilitate the development of structural analysis tools.
In this paper, we present rBAN (retro-biosynthetic analysis of nonribosomal peptides), a new computational tool designed to predict the monomeric graph of NRPs from their atomic structure in SMILES format.
This prediction is achieved through the "in silico" fragmentation of a chemical structure and matching the resulting fragments against the monomers of Norine for identification.
Structures containing monomers not yet recorded in Norine, are processed in a "discovery mode" that uses the RESTful service from PubChem to search the unidentified substructures and suggest new monomers.
rBAN was integrated in a pipeline for the curation of Norine data in which it was used to check the correspondence between the monomeric graphs annotated in Norine and SMILES-predicted graphs.
The process concluded with the validation of the 97.26% of the records in Norine, a two-fold extension of its SMILES data and the introduction of 11 new monomers suggested in the discovery mode.
The accuracy, robustness and high-performance of rBAN were demonstrated in benchmarking it against other tools with the same functionality: Smiles2Monomers and GRAPE.


# Citation
```
@article {ricart2019,
  author       = { Emma Ricart and Valérie Leclére and Areski Flissi and Markus Mueller and Maude Pupin and Frédérique Lisacek },
  title        = { rBAN: retro-biosynthetic analysis of nonribosomal peptides },
  journal      = { Journal of Cheminformatics },
  year         = { 2019 },
  pages        = { 13 },
  month        = { Feb },
  volume       = { 11 },
  number       = { 1 },
  day          = { 08 },
  issn         = { 1758-2946 },
  doi          = { 10.1186/s13321-019-0335-x },
  url          = { https://doi.org/10.1186/s13321-019-0335-x }
}
```
