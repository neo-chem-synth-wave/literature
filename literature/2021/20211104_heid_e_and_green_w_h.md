# Overview
**Title:**
Machine Learning of Reaction Properties via Learned Representations of the Condensed Graph of Reaction

**Authors:**
Heid, E. and Green, W.H.

**Publication Date:**
2021/11/04

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.1c00975)

**Alternative Links:**
[GitHub](https://github.com/chemprop/chemprop) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC9092344) |
[ResearchGate](https://www.researchgate.net/publication/355935524_Machine_Learning_of_Reaction_Properties_via_Learned_Representations_of_the_Condensed_Graph_of_Reaction)

**Tags:**
reaction-representation


# Abstract
The estimation of chemical reaction properties such as activation energies, rates, or yields is a central topic of computational chemistry.
In contrast to molecular properties, where machine learning approaches such as graph convolutional neural networks (GCNNs) have excelled for a wide variety of tasks, no general and transferable adaptations of GCNNs for reactions have been developed yet.
We therefore combined a popular cheminformatics reaction representation, the so-called condensed graph of reaction (CGR), with a recent GCNN architecture to arrive at a versatile, robust, and compact deep learning model.
The CGR is a superposition of the reactant and product graphs of a chemical reaction and thus an ideal input for graph-based machine learning approaches.
The model learns to create a data-driven, task-dependent reaction embedding that does not rely on expert knowledge, similar to current molecular GCNNs.
Our approach outperforms current state-of-the-art models in accuracy, is applicable even to imbalanced reactions, and possesses excellent predictive capabilities for diverse target properties, such as activation energies, reaction enthalpies, rate constants, yields, or reaction classes.
We furthermore curated a large set of atom-mapped reactions along with their target properties, which can serve as benchmark data sets for future work.
All data sets and the developed reaction GCNN model are available online, free of charge, and open source.


# Citation
```
@article {20211104_heid_e_and_green_w_h,
  author       = { Esther Heid and William H. Green },
  title        = { Machine Learning of Reaction Properties via Learned Representations of the Condensed Graph of Reaction },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2022 },
  note         = { PMID: 34734699 },
  pages        = { 2101-2110 },
  volume       = { 62 },
  number       = { 9 },
  doi          = { 10.1021/acs.jcim.1c00975 },
  url          = { https://doi.org/10.1021/acs.jcim.1c00975 },
  eprint       = { https://doi.org/10.1021/acs.jcim.1c00975 }
}
```
