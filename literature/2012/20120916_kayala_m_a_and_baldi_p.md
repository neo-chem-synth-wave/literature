# Overview
**Title:**
ReactionPredictor: Prediction of Complex Chemical Reactions at the Mechanistic Level Using Machine Learning

**Authors:**
Kayala, M.A. and Baldi, P.F.

**Publication Date:**
2012/09/16

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/ci3003039)

**Alternative Links:**
[ChemDB Chemoinformatics Portal](https://cdb.ics.uci.edu)

**Starred:**
False

**Tags:**
single-step-synthesis


# Abstract
Proposing reasonable mechanisms and predicting the course of chemical reactions is important to the practice of organic chemistry.
Approaches to reaction prediction have historically used obfuscating representations and manually encoded patterns or rules.
Here we present ReactionPredictor, a machine learning approach to reaction prediction that models elementary, mechanistic reactions as interactions between approximate molecular orbitals (MOs).
A training data set of productive reactions known to occur at reasonable rates and yields and verified by inclusion in the literature or textbooks is derived from an existing rule-based system and expanded upon with manual curation from graduate level textbooks.
Using this training data set of complex polar, hypervalent, radical, and pericyclic reactions, a two-stage machine learning prediction framework is trained and validated.
In the first stage, filtering models trained at the level of individual MOs are used to reduce the space of possible reactions to consider.
In the second stage, ranking models over the filtered space of possible reactions are used to order the reactions such that the productive reactions are the top ranked.
The resulting model, ReactionPredictor, perfectly ranks polar reactions 78.1% of the time and recovers all productive reactions 95.7% of the time when allowing for small numbers of errors.
Pericyclic and radical reactions are perfectly ranked 85.8% and 77.0% of the time, respectively, rising to >93% recovery for both reaction types with a small number of allowed errors.
Decisions about which of the polar, pericyclic, or radical reaction type ranking models to use can be made with >99% accuracy.
Finally, for multistep reaction pathways, we implement the first mechanistic pathway predictor using constrained tree-search to discover a set of reasonable mechanistic steps from given reactants to given products.
Webserver implementations of both the single step and pathway versions of ReactionPredictor are available via the chemoinformatics portal http://cdb.ics.uci.edu/.


# Citation
```
@article {kayala2012a,
  author       = { Matthew A. Kayala and Pierre Baldi },
  title        = { ReactionPredictor: Prediction of Complex Chemical Reactions at the Mechanistic Level Using Machine Learning },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2012 },
  note         = { PMID: 22978639 },
  pages        = { 2526-2540 },
  volume       = { 52 },
  number       = { 10 },
  doi          = { 10.1021/ci3003039 },
  url          = { https://doi.org/10.1021/ci3003039 },
  eprint       = { https://doi.org/10.1021/ci3003039 }
}
```
