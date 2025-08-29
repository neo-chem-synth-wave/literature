# Overview
**Title:**
ReactionT5: A Pre-trained Transformer Model for Accurate Chemical Reaction Prediction With Limited Data

**Authors:**
Sagawa, T. and Kojima, R.

**Publication Date:**
2025/08/19

**Link:**
[BMC Journal of Cheminformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-025-01075-4)

**Alternative Links:**
[GitHub](https://github.com/sagawatatsuya/ReactionT5v2) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC12366004) |
[ResearchGate](https://www.researchgate.net/publication/394681140_ReactionT5_a_pre-trained_transformer_model_for_accurate_chemical_reaction_prediction_with_limited_data)

**Starred:**
False

**Tags:**
single-step-synthesis, single-step-retrosynthesis, reaction-yield, reaction-t5


# Abstract
Accurate chemical reaction prediction is critical for reducing both cost and time in drug development.
This study introduces ReactionT5, a transformer-based chemical reaction foundation model pre-trained on the Open Reaction Database—a large publicly available reaction dataset.
In benchmarks for product prediction, retrosynthesis, and yield prediction, ReactionT5 outperformed existing models.
Specifically, ReactionT5 achieved 97.5% accuracy in product prediction, 71.0% in retrosynthesis, and a coefficient of determination of 0.947 in yield prediction.
Remarkably, ReactionT5, when fine-tuned with only a limited dataset of reactions, achieved performance on par with models fine-tuned on the complete dataset.
Additionally, the visualization of ReactionT5 embeddings illustrates that the model successfully captures and represents the chemical reaction space, indicating effective learning of reaction properties.


# Citation
```
@article {sagawa2025a,
  author       = { Tatsuya Sagawa and Ryosuke Kojima },
  title        = { ReactionT5: a pre-trained transformer model for accurate chemical reaction prediction with limited data },
  journal      = { Journal of Cheminformatics },
  year         = { 2025 },
  pages        = { 126 },
  month        = { Aug },
  volume       = { 17 },
  number       = { 1 },
  day          = { 19 },
  issn         = { 1758-2946 },
  doi          = { 10.1186/s13321-025-01075-4 },
  url          = { https://doi.org/10.1186/s13321-025-01075-4 }
}
```
