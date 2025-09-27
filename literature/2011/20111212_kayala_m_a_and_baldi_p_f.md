# Overview
**Title:**
A Machine Learning Approach to Predict Chemical Reactions

**Authors:**
Kayala, M.A. and Baldi, P.F.

**Publication Date:**
2011/12/12

**Link:**
[NeurIPS 2011](https://papers.nips.cc/paper_files/paper/2011/hash/b337e84de8752b27eda3a12363109e80-Abstract.html)

**Alternative Links:**
None

**Tags:**
single-step-synthesis, template-based


# Abstract
Being able to predict the course of arbitrary chemical reactions is essential to the theory and applications of organic chemistry.
Previous approaches are not high-throughput, are not generalizable or scalable, or lack sufficient data to be effective.
We describe single mechanistic reactions as concerted electron movements from an electron orbital source to an electron orbital sink.
We use an existing rule-based expert system to derive a dataset consisting of 2,989 productive mechanistic steps and 6.14 million non-productive mechanistic steps.
We then pose identifying productive mechanistic steps as a ranking problem: rank potential orbital interactions such that the top ranked interactions yield the major products.
The machine learning implementation follows a two-stage approach, in which we first train atom level reactivity filters to prune 94.0% of non-productive reactions with less than a 0.1% false negative rate.
Then, we train an ensemble of ranking models on pairs of interacting orbitals to learn a relative productivity function over single mechanistic reactions in a given system.
Without the use of explicit transformation patterns, the ensemble perfectly ranks the productive mechanisms at the top 89.1% of the time, rising to 99.9% of the time when top ranked lists with at most four non-productive reactions are considered.
The final system allows multi-step reaction prediction.
Furthermore, it is generalizable, making reasonable predictions over reactants and conditions which the rule-based expert system does not handle.


# Citation
```
@inproceedings {20111212_kayala_m_a_and_baldi_p_f,
  author       = { Matthew Kayala and Pierre Baldi },
  title        = { A Machine Learning Approach to Predict Chemical Reactions },
  booktitle    = { Advances in Neural Information Processing Systems },
  year         = { 2011 },
  volume       = { 24 },
  pages        = {  },
  publisher    = { Curran Associates, Inc. },
  editor       = { J. Shawe-Taylor and R. Zemel and P. Bartlett and F. Pereira and K.Q. Weinberger },
  url          = { https://proceedings.neurips.cc/paper_files/paper/2011/file/b337e84de8752b27eda3a12363109e80-Paper.pdf }
}
```
