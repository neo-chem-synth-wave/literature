# Overview
**Title:**
RDCanon: A Python Package for Canonicalizing the Order of Tokens in SMARTS Queries

**Authors:**
Mahjour, B.A. and Coley, C.W.

**Publication Date:**
2024/03/15

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.4c00138)

**Alternative Links:**
[GitHub](https://github.com/coleygroup/rdcanon)

**Tags:**
reaction-pattern, rdcanon


# Abstract
SMARTS is a widely used language in cheminformatics for defining substructural queries for database lookups, reaction templates for chemical transformations, and other applications.
As an extension to SMILES, many SMARTS patterns can represent the same query.
Despite this, no canonicalization algorithm invariant of the line notation sequence or atomic numbering is publicly available.
Here, we introduce RDCanon, an open-source Python package that can be used to standardize SMARTS queries.
RDCanon is designed to ensure that the sequence of atomic queries remains consistent for all graphs representing the same substructure query and to ensure a canonical sequence of primitives within each individual atom query; furthermore, the algorithm can be applied to canonicalize the order of reactants, agents, and products and their atom map numbers in reaction SMARTS templates.
As part of its canonicalization algorithm, RDCanon provides a mechanism in which the canonicalized SMARTS is optimized for speed against specific molecular databases.
Several case studies are provided to showcase improved efficiency in substructure matching and retrosynthetic analysis.


# Citation
```
@article {20240315_mahjour_b_a_and_coley_c_w,
  author       = { Babak A. Mahjour and Connor W. Coley },
  title        = { RDCanon: A Python Package for Canonicalizing the Order of Tokens in SMARTS Queries },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2024 },
  note         = { PMID: 38488634 },
  pages        = { 2948-2954 },
  volume       = { 64 },
  number       = { 8 },
  doi          = { 10.1021/acs.jcim.4c00138 },
  url          = { https://doi.org/10.1021/acs.jcim.4c00138 },
  eprint       = { https://doi.org/10.1021/acs.jcim.4c00138 }
}
```
