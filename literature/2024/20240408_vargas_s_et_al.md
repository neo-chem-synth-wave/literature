# Overview
**Title:**
High-Throughput Quantum Theory of Atoms in Molecules (QTAIM) for Geometric Deep Learning of Molecular and Reaction Properties

**Authors:**
Vargas, S., Gee, W., and Alexandrova, A. |
Vargas, S. et al.

**Publication Date:**
2024/04/08

**Link:**
[RSC Digital Discovery](https://pubs.rsc.org/en/content/articlelanding/2024/dd/d4dd00057a)

**Alternative Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/65dc25f366c13817299005ef) |
[GitHub (Data)](https://github.com/santi921/qtaim_generator) |
[GitHub (Molecular Machine Learning)](https://github.com/santi921/qtaim_embed) |
[GitHub (Reaction Property Machine Learning)](https://github.com/santi921/bondnet) |
[ResearchGate](https://www.researchgate.net/publication/379673630_High-throughput_quantum_theory_of_atoms_in_molecules_QTAIM_for_geometric_deep_learning_of_molecular_and_reaction_properties)

**Starred:**
False

**Tags:**
reaction-property


# Abstract
We present a package, generator, for geometric molecular property prediction based on topological features of quantum mechanical electron density.
Generator computes quantum theory of atoms in molecules (QTAIM) features, via density functional theory (DFT), for sets of molecules or reactions in a high-throughput manner, and compiles features into a single data structure for processing, analysis, and geometric machine learning.
An accompanying graph neural network package can be used for property prediction and allows users to readily use computed features for learning tasks.
To test the efficacy of electron density-based data for machine learning, we benchmark several datasets including QM8, QM9, LIBE, Tox21, and a Green 2022 reaction dataset.
This wide dataset diversity underscores the flexibility of QTAIM descriptors and our package.
In addition, we made our code compatible with new versions of BondNet and ChemProp architectures to allow for both reaction and molecular property prediction out-of-the-box.
To motivate the use of QTAIM features for varied prediction tasks, we also perform extensive benchmarking of our new models against several existing models as well as to our models without QTAIM features.
We show that almost universally, QTAIM features improve model performance on our algorithms, ChemProp, and BondNet.
We also determine that QTAIM can aid in generalizing model performance to out-of-domain (OOD) datasets and improve learning at smaller data regimes.
Combined, we hope that this framework could enable QTAIM-enhanced structure-to-property predictions – especially in domains with less data, including experimental or reaction-level datasets with complex underlying chemistries.


# Citation
```
@article {vargas2024a,
  author       = { Santiago Vargas and Winston Gee and Anastassia Alexandrova },
  title        = { High-throughput quantum theory of atoms in molecules (QTAIM) for geometric deep learning of molecular and reaction properties },
  journal      = { Digital Discovery },
  year         = { 2024 },
  pages        = { 987-998 },
  volume       = { 3 },
  issue        = { 5 },
  publisher    = { RSC },
  doi          = { 10.1039/D4DD00057A },
  url          = { https://dx.doi.org/10.1039/D4DD00057A }
}
```
