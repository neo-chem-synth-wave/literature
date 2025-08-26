# Overview
**Title:**
Context-Driven Exploration of Complex Chemical Reaction Networks

**Authors:**
Simm, G.N. and Reiher, M.

**Publication Date:**
2017/10/30

**Link:**
[ACS Journal of Chemical Theory and Computation](https://pubs.acs.org/doi/10.1021/acs.jctc.7b00945)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/1709.02479) |
[ETH Zürich Research Collection](https://www.research-collection.ethz.ch/entities/publication/61c87d79-170d-415a-a302-a1a0f11a052e)

**Starred:**
False

**Tags:**
reaction-network


# Abstract
The construction of a reaction network containing all relevant intermediates and elementary reactions is necessary for the accurate description of chemical processes.
In the case of a complex chemical reaction (involving, for instance, many reactants or highly reactive species), the size of such a network may grow rapidly.
Here, we present a computational protocol that constructs such reaction networks in a fully automated fashion steered in an intuitive, graph-based fashion through a single graphical user interface.
Starting from a set of initial reagents new intermediates are explored through intra- and intermolecular reactions of already explored intermediates or new reactants presented to the network.
This is done by assembling reactive complexes based on heuristic rules derived from conceptual electronic-structure theory and exploring the corresponding approximate reaction path.
A subsequent path refinement leads to a minimum-energy path which connects the new intermediate to the existing ones to form a connected reaction network.
Tree traversal algorithms are then employed to detect reaction channels and catalytic cycles.
We apply our protocol to the formose reaction to study different pathways of sugar formation and to rationalize its autocatalytic nature.


# Citation
```
@article {simm2017a,
  author       = { Gregor N. Simm and Markus Reiher },
  title        = { Context-Driven Exploration of Complex Chemical Reaction Networks },
  journal      = { Journal of Chemical Theory and Computation },
  year         = { 2017 },
  note         = { PMID: 29084387 },
  pages        = { 6108-6119 },
  volume       = { 13 },
  number       = { 12 },
  doi          = { 10.1021/acs.jctc.7b00945 },
  url          = { https://doi.org/10.1021/acs.jctc.7b00945 },
  eprint       = { https://doi.org/10.1021/acs.jctc.7b00945 }
}
```
