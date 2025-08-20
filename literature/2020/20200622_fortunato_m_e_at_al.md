# Overview
**Title:**
Data Augmentation and Pretraining for Template-Based Retrosynthetic Prediction in Computer-Aided Synthesis Planning

**Authors:**
Fortunato, M.E., Coley, C.W., Barnes, B.C., and Jensen, K.F. |
Fortunato, M.E. et al.

**Publication Date:**
2020/06/22

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.0c00403)

**Alternative Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/60c747d9bb8c1a47e43dab76) |
[DSpace@MIT](https://dspace.mit.edu/handle/1721.1/134636) |
[GitLab](https://gitlab.com/mefortunato/template-relevance)

**Starred:**
False

**Tags:**
single-step-retrosynthesis, multi-step-retrosynthesis, template-based, optimization


# Abstract
This work presents efforts to augment the performance of data-driven machine learning algorithms for reaction template recommendation used in computer-aided synthesis planning software.
Often, machine learning models designed to perform the task of prioritizing reaction templates or molecular transformations are focused on reporting high-accuracy metrics for the one-to-one mapping of product molecules in reaction databases to the template extracted from the recorded reaction.
The available templates that get selected for inclusion in these machine learning models have been previously limited to those that appear frequently in the reaction databases and exclude potentially useful transformations.
By augmenting open-access data sets of organic reactions with explicitly calculated template applicability and pretraining a template-relevance neural network on this augmented applicability data set, we report an increase in the template applicability recall and an increase in the diversity of predicted precursors.
The augmentation and pretraining effectively teaches the neural network an increased set of templates that could theoretically lead to successful reactions for a given target.
Even on a small data set of well-curated reactions, the data augmentation and pretraining methods resulted in an increase in top-1 accuracy, especially for rare templates, indicating that these strategies can be very useful for small data sets.


# Citation
```
@article {fortunato2020a,
  author       = { Michael E. Fortunato and Connor W. Coley and Brian C. Barnes and Klavs F. Jensen },
  title        = { Data Augmentation and Pretraining for Template-Based Retrosynthetic Prediction in Computer-Aided Synthesis Planning },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2020 },
  note         = { PMID: 32568548 },
  pages        = { 3398-3407 },
  volume       = { 60 },
  number       = { 7 },
  doi          = { 10.1021/acs.jcim.0c00403 },
  url          = { https://doi.org/10.1021/acs.jcim.0c00403 },
  eprint       = { https://doi.org/10.1021/acs.jcim.0c00403 }
}
```
