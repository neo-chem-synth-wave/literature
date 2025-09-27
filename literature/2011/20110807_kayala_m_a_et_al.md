# Overview
**Title:**
Learning to Predict Chemical Reactions

**Authors:**
Kayala, M.A., Azencott, C., Chen, J.H., and Baldi, P. |
Kayala, M.A. et al.

**Publication Date:**
2011/08/07

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/abs/10.1021/ci200207y)

**Alternative Links:**
[ChemDB Chemoinformatics Portal](https://cdb.ics.uci.edu) |
[Europe PMC](https://europepmc.org/article/med/21819139) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC3193800)

**Tags:**
single-step-synthesis


# Abstract
Being able to predict the course of arbitrary chemical reactions is essential to the theory and applications of organic chemistry.
Approaches to the reaction prediction problems can be organized around three poles corresponding to: (1) physical laws; (2) rule-based expert systems; and (3) inductive machine learning.
Previous approaches at these poles, respectively, are not high throughput, are not generalizable or scalable, and lack sufficient data and structure to be implemented.
We propose a new approach to reaction prediction utilizing elements from each pole.
Using a physically inspired conceptualization, we describe single mechanistic reactions as interactions between coarse approximations of molecular orbitals (MOs) and use topological and physicochemical attributes as descriptors.
Using an existing rule-based system (Reaction Explorer), we derive a restricted chemistry data set consisting of 1,630 full multistep reactions with 2,358 distinct starting materials and intermediates, associated with 2,989 productive mechanistic steps and 6.14 million unproductive mechanistic steps.
And from machine learning, we pose identifying productive mechanistic steps as a statistical ranking, information retrieval problem: given a set of reactants and a description of conditions, learn a ranking model over potential filled-to-unfilled MO interactions such that the top-ranked mechanistic steps yield the major products.
The machine learning implementation follows a two-stage approach, in which we first train atom level reactivity filters to prune 94.00% of nonproductive reactions with a 0.01% error rate.
Then, we train an ensemble of ranking models on pairs of interacting MOs to learn a relative productivity function over mechanistic steps in a given system.
Without the use of explicit transformation patterns, the ensemble perfectly ranks the productive mechanism at the top 89.05% of the time, rising to 99.86% of the time when the top four are considered.
Furthermore, the system is generalizable, making reasonable predictions over reactants and conditions which the rule-based expert does not handle.
A web interface to the machine learning based mechanistic reaction predictor is accessible through our chemoinformatics portal (http://cdb.ics.uci.edu) under the Toolkits section.


# Citation
```
@article {20110807_kayala_m_a_et_al,
  author       = { Matthew A. Kayala and Chlo{\'e}-Agathe Azencott and Jonathan H. Chen and Pierre Baldi },
  title        = { Learning to Predict Chemical Reactions },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2011 },
  note         = { PMID: 21819139 },
  pages        = { 2209-2222 },
  volume       = { 51 },
  number       = { 9 },
  doi          = { 10.1021/ci200207y },
  url          = { https://doi.org/10.1021/ci200207y },
  eprint       = { https://doi.org/10.1021/ci200207y }
}
```
