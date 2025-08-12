# (20141226, Schneider, N. et al.) Development of a Novel Fingerprint for Chemical Reactions and Its Application to Large-scale Reaction Classification and Similarity

Tags: chemical-data, enhancement

## Publication Overview

| **Title:**  | Development of a Novel Fingerprint for Chemical Reactions and Its Application to
Large-scale Reaction Classification and Similarity |
| --- | --- |
| **Authors:**  | Nadine Schneider, Daniel M. Lowe, Roger A. Sayle, Gregory A. Landrum |
| Publication Date**:**  | 2014/12/26 |
| Publication Links: | [**ACS JCIM](https://pubs.acs.org/doi/10.1021/ci5006614) | [ACS JCIM Correction Notice](https://pubs.acs.org/doi/10.1021/acs.jcim.5b00046)** |
| Alternative Links: | - |
| Code Links: | - |

## Publication Abstract

<aside>
ℹ️ Fingerprint methods applied to molecules have proven to be useful for similarity determination and as inputs to machine-learning models. Here, we present the development of a new fingerprint for chemical reactions and validate its usefulness in building machine-learning models and in similarity assessment. Our final fingerprint is constructed as the difference of the atom-pair fingerprints of products and reactants and includes agents via calculated physicochemical properties. We validated the fingerprints on a large data set of reactions text-mined from granted United States patents from the last 40 years that have been classified using a substructure-based expert system. We applied machine learning to build a 50-class predictive model for reaction-type classification that correctly predicts 97% of the reactions in an external test set. Impressive accuracies were also observed when applying the classifier to reactions from an in-house electronic laboratory notebook. The performance of the novel fingerprint for assessing reaction similarity was evaluated by a cluster analysis that recovered 48 out of 50 of the reaction classes with a median F-score of 0.63 for the clusters. The data sets used for training and primary validation as well as all python scripts required to reproduce the analysis are provided in the Supporting Information.

</aside>

## Remarks and Comments

<aside>
💬 *Written on **2022/09/15** by **Haris Hasić**.*
****
The correction is about fixing affiliations and references.

</aside>

<aside>
💬 *Written on **2022/09/15** by **Haris Hasić**.*
****
This publication introduces the Reaction Difference Fingerprint or RDFP descriptors and demonstrates their usability within a chemical reaction class classification setting. These descriptors are useful when dealing with chemical reactions, but the use case not so much. Namely, to classify chemical reaction data, entries need to have pre-assigned class labels, which is very hard or sometimes impossible to do, given the size and complexity of the chemical reaction space.

</aside>