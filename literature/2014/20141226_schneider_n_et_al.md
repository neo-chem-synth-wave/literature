# Overview
**Title:**
Development of a Novel Fingerprint for Chemical Reactions and Its Application to Large-Scale Reaction Classification and Similarity

**Authors:**
Schneider, N., Lowe, D.M., Sayle, R.A., and Landrum, G.A. |
Schneider, N. et al.

**Publication Date:**
2014/12/26

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/ci5006614)

**Alternative Links:**
[ACS Journal of Chemical Information and Modeling Correction Notice](https://pubs.acs.org/doi/10.1021/acs.jcim.5b00046)

**Starred:**
True

**Tags:**
reaction-descriptor, reaction-classification, fingerprint, data-source, uspto-50k


# Abstract
Fingerprint methods applied to molecules have proven to be useful for similarity determination and as inputs to machine-learning models.
Here, we present the development of a new fingerprint for chemical reactions and validate its usefulness in building machine-learning models and in similarity assessment.
Our final fingerprint is constructed as the difference of the atom-pair fingerprints of products and reactants and includes agents via calculated physicochemical properties.
We validated the fingerprints on a large data set of reactions text-mined from granted United States patents from the last 40 years that have been classified using a substructure-based expert system.
We applied machine learning to build a 50-class predictive model for reaction-type classification that correctly predicts 97% of the reactions in an external test set.
Impressive accuracies were also observed when applying the classifier to reactions from an in-house electronic laboratory notebook.
The performance of the novel fingerprint for assessing reaction similarity was evaluated by a cluster analysis that recovered 48 out of 50 of the reaction classes with a median F-score of 0.63 for the clusters.
The data sets used for training and primary validation as well as all python scripts required to reproduce the analysis are provided in the Supporting Information.


# Citation
```
@article {schneider2014a,
  author       = { Nadine Schneider and Daniel M. Lowe and Roger A. Sayle and Gregory A. Landrum },
  title        = { Development of a Novel Fingerprint for Chemical Reactions and Its Application to Large-Scale Reaction Classification and Similarity },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2015 },
  note         = { PMID: 25541888 },
  pages        = { 39-53 },
  volume       = { 55 },
  number       = { 1 },
  doi          = { 10.1021/ci5006614 },
  url          = { https://doi.org/10.1021/ci5006614 },
  eprint       = { https://doi.org/10.1021/ci5006614 }
}
```
