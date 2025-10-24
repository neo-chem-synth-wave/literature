# Overview
**Title:**
Reinforcement Learning Optimization of Reaction Routes on the Basis of Large, Hybrid Organic Chemistry-Synthetic Biological, Reaction Network Data

**Authors:**
Zhang, C. and Lapkin, A.A.

**Publication Date:**
2023/07/05

**Publication Link:**
[RSC Reaction Chemistry & Engineering](https://pubs.rsc.org/en/content/articlelanding/2023/re/d2re00406b)

**Alternative Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/61e53beceab6ef20aae41719) |
[University of Cambridge Apollo Repository](https://www.repository.cam.ac.uk/items/76787786-0c75-4916-8952-c763d74842f0)

**Tags:**
multi-step-retrosynthesis, optimization


# Abstract
Computer-assisted synthesis planning (CASP) accelerates the development of organic synthesis routes of complex functional molecules.
CASP tools are generally developed on the basis of rules or data of synthetic chemistry, which include some enzymatic reactions.
However, synthetic biology offers a new degree of freedom through the potential to engineer new synthetic steps.
In this work, we present a method to hybridize conventional organic synthetic and synthetic biological reaction datasets to guide synthesis planning.
A section of organic reactions from the Reaxys® database was combined with metabolic reactions from the KEGG database to create a hybrid dataset.
The combined dataset was used to assemble synthetic pathways from multiple building blocks to a target molecule.
The route assembly was performed using reinforcement learning, which was adapted to 'learn the values' of molecular structures in synthesis planning and to develop a value network to suggest near-optimal multi-step synthesis route choices from the pool of the available reactions.
To quantify the added value of synthetic biological reaction transformations in the hybrid routes, three value network 'decision-makers' were developed from the organic, biological and hybrid reaction pools.
The near-optimal synthetic routes planned from the three reaction pools were evaluated and compared to discuss the benefits of the hybrid synthetic chemical plus synthetic biological reaction decision space in reaction route optimization.


# Citation
```
@article {20230705a_zhang_c_and_lapkin_a_a,
  author       = { Chonghuan Zhang and Alexei A. Lapkin },
  title        = { Reinforcement learning optimization of reaction routes on the basis of large, hybrid organic chemistry–synthetic biological, reaction network data },
  journal      = { React. Chem. Eng. },
  year         = { 2023 },
  pages        = { 2491-2504 },
  volume       = { 8 },
  issue        = { 10 },
  publisher    = { The Royal Society of Chemistry },
  doi          = { 10.1039/D2RE00406B },
  url          = { https://dx.doi.org/10.1039/D2RE00406B }
}
```
