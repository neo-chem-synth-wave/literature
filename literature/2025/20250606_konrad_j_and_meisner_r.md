# Overview
**Title:**
Smart Reaction Templating: A Graph-Based Method for Automated Molecular Dynamics Input Generation

**Authors:**
Konrad, J. and Meißner, R.

**Publication Date:**
2025/06/06

**Link:**
[ACS Journal of Chemical Information and Modeling](https://www.nature.com/articles/s41467-025-61803-0)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/2503.02678) |
[ResearchGate](https://www.researchgate.net/publication/389581087_Smart_Reaction_Templating_A_Graph-Based_Method_for_Automated_Molecular_Dynamics_Input_Generation) |
[Technical University Hamburg GitLab](https://collaborating.tuhh.de/m-29/software/templater)

**Starred:**
False

**Tags:**
reaction-template


# Abstract
Accurately modeling chemical reactions in molecular dynamics simulations requires detailed pre- and postreaction templates, often created through labor-intensive manual workflows.
This work introduces a Python-based algorithm that automates the generation of reaction templates for the LAMMPS REACTION package, leveraging graph-theoretical principles and subgraph isomorphism techniques.
By representing molecular systems as mathematical graphs, the method enables the automated identification of conserved molecular domains, reaction sites, and atom mappings, significantly reducing manual effort.
The algorithm was validated on three case studies: poly addition, poly condensation, and chain polymerization, demonstrating its ability to map conserved domains, identify reaction-initiating atoms, and resolve challenges such as symmetric reactants and indistinguishable atoms.
Additionally, the generated templates were optimized for computational efficiency by retaining only essential reactive domains, ensuring scalability and consistency in high-throughput workflows for computational chemistry, materials science, and machine learning applications.
Future work will focus on extending the method to mixed organic–inorganic systems, incorporating adaptive scoring mechanisms, and integrating quantum mechanical calculations to enhance its applicability.


# Citation
```
@article {konrad2025a,
  author       = { Julian Konrad and Robert Meißner },
  title        = { Smart Reaction Templating: A Graph-Based Method for Automated Molecular Dynamics Input Generation },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2025 },
  note         = { PMID: 40476355 },
  pages        = { 6038-6047 },
  volume       = { 65 },
  number       = { 12 },
  doi          = { 10.1021/acs.jcim.5c00445 },
  url          = { https://doi.org/10.1021/acs.jcim.5c00445 },
  eprint       = { https://doi.org/10.1021/acs.jcim.5c00445 }
}
```
