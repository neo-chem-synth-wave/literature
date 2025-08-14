# Overview
**Title:**
Unassisted Noise Reduction of Chemical Reaction Datasets

**Authors:**
Toniato, A., Schwaller, P., Cardinale, A., Geluykens, J., and Laino, T.

**Publication Date:**
2021/03/29

**Publication Link:**
[Nature Machine Intelligence](https://www.nature.com/articles/s42256-021-00319-w)

**Alternative Publication Links:**
[arXiv](https://arxiv.org/abs/2102.01399) |
[Official GitHub Repository](https://github.com/rxn4chemistry/OpenNMT-py/tree/noise_reduction)


# Abstract
Existing deep learning models applied to reaction prediction in organic chemistry can reach high levels of accuracy (>90% for natural language processing-based ones). 
With no chemical knowledge embedded other than the information learnt from reaction data, the quality of the datasets plays a crucial role in the performance of the prediction models. 
Human curation is prohibitively expensive, so unaided approaches to remove chemically incorrect entries from existing datasets are essential to improve the performance of artificial intelligence models in synthetic chemistry tasks. 
Here, we propose a machine learning-based, unassisted approach to remove chemically wrong entries from chemical reaction collections. 
We apply this method to the Pistachio collection of chemical reactions and to an open dataset, both extracted from United States Patent and Trademark Office patents. 
Our results show an improved prediction quality for models trained on the cleaned and balanced datasets. 
For retrosynthetic models, the roundtrip accuracy metric grows by 13 percentage points and the value of the cumulative Jensen-Shannon divergence decreases by 30% compared to its original record. 
The coverage remains high at 97%, and the value of the class diversity is not affected by the cleaning. 
The proposed strategy is the first unassisted rule-free technique to address automatic noise reduction in chemical datasets.


# Citation
```
@article {toniato2021,
  author       = { Alessandra Toniato and Philippe Schwaller and Cardinale Antonio and Joppe Geluykens and Teodoro Laino },
  title        = { Unassisted noise reduction of chemical reaction datasets },
  journal      = { Nat. Mach. Intell. },
  year         = { 2021 },
  pages        = { 485--494 },
  month        = { mar },
  volume       = { 3 },
  number       = { 6 },
  publisher    = { Springer Science and Business Media LLC },
  copyright    = { https://www.springernature.com/gp/researchers/text-and-data-mining },
  language     = { en }
}
```
