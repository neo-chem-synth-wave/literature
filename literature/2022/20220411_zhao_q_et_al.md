# Overview
**Title:**
Conformational Sampling for Transition State Searches on a Computational Budget

**Authors:**
Zhao, Q., Hsu, H., and Savoie, B.M. |
Zhao, Q. et al.

**Publication Date:**
2022/04/11

**Link:**
[ACS Journal of Chemical Theory and Computation](https://pubs.acs.org/doi/full/10.1021/acs.jctc.2c00081)

**Alternative Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/61b2bdc525f39a5318d4138e) |
[GitHub](https://github.com/Savoie-Research-Group/yarp) |
[ResearchGate](https://www.researchgate.net/publication/356955599_Conformational_Sampling_for_Transition_State_Searches_on_a_Computational_Budget)

**Starred:**
False

**Tags:**
reaction-mechanism


# Abstract
Transition state searches are the basis for computationally characterizing reaction mechanisms, making them a pivotal tool in myriad chemical applications.
Nevertheless, common search algorithms are sensitive to reaction conformations, and the conformational spaces of even medium-sized reacting systems are too complex to explore with brute force.
Here, we show that it is possible to train a classifier to learn the features of reaction conformers that conduce successful transition state searches, such that optimal conformers can be down-selected before incurring the cost of a high-level transition state search.
The efficacy and transferability of this approach were tested using four distinct benchmarks comprising over three hundred individual reactions.
Neglecting conformer contributions led to qualitatively incorrect activation energy estimations for a broad range of reactions, whereas simple random forest classifiers reliably down-selected low-barrier reaction conformers for unseen reactions.
The robust performance of these machine learning classifiers mitigates cost as a factor when implementing conformational sampling into contemporary reaction prediction workflows and opens up many avenues for further improvements as transition state data grow.


# Citation
```
@article {zhao2022a,
  author       = { Qiyuan Zhao and Hsuan-Hao Hsu and Brett M. Savoie },
  title        = { Conformational Sampling for Transition State Searches on a Computational Budget },
  journal      = { Journal of Chemical Theory and Computation },
  year         = { 2022 },
  note         = { PMID: 35403426 },
  pages        = { 3006-3016 },
  volume       = { 18 },
  number       = { 5 },
  doi          = { 10.1021/acs.jctc.2c00081 },
  url          = { https://doi.org/10.1021/acs.jctc.2c00081 },
  eprint       = { https://doi.org/10.1021/acs.jctc.2c00081 }
}
```
