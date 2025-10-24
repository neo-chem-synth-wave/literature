# Overview
**Title:**
Bidirectional Graphormer for Reactivity Understanding: Neural Network Trained to Reaction Atom-to-Atom Mapping Task

**Authors:**
Nugmanov, R., Dyubankova, N., Gedich, A., and Wegner, J.K. |
Nugmanov, R. et al.

**Publication Date:**
2022/07/06

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.2c00344)

**Alternative Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/62348dd0a4ed957158249609) |
[GitHub](https://github.com/chython/chytorch-rxnmap)

**Tags:**
atom-to-atom-mapping, rxn-map


# Abstract
This work introduces GraphormerMapper, a new algorithm for reaction atom-to-atom mapping (AAM) based on a transformer neural network adopted for the direct processing of molecular graphs as sets of atoms and bonds, as opposed to SMILES/SELFIES sequence-based approaches, in combination with the Bidirectional Encoder Representations from Transformers (BERT) network.
The graph transformer serves to extract molecular features that are tied to atoms and bonds.
The BERT network is used for chemical transformation learning.
In a benchmarking study with IBM RxnMapper, which is the best AAM algorithm according to our previous study, we demonstrate that our AAM algorithm is superior to it on our "Golden" benchmarking data set.


# Citation
```
@article {20220706_nugmanov_r_et_al,
  author       = { Ramil Nugmanov and Natalia Dyubankova and Andrey Gedich and Joerg Kurt Wegner },
  title        = { Bidirectional Graphormer for Reactivity Understanding: Neural Network Trained to Reaction Atom-to-Atom Mapping Task },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2022 },
  note         = { PMID: 35792579 },
  pages        = { 3307-3315 },
  volume       = { 62 },
  number       = { 14 },
  doi          = { 10.1021/acs.jcim.2c00344 },
  url          = { https://doi.org/10.1021/acs.jcim.2c00344 },
  eprint       = { https://doi.org/10.1021/acs.jcim.2c00344 }
}
```
