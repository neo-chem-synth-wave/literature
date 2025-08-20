# Overview
**Title:**
Investigating the Reliability and Interpretability of Machine Learning Frameworks for Chemical Retrosynthesis

**Authors:**
Hastedt, F., Bailey, R.M., Hellgardt, K., Yaliraki, S.N., del Rio Chanona, E.A., and Zhang, D. |
Hastedt, F. et al.

**Publication Date:**
2024/05/23

**Link:**
[RSC Digital Discovery](https://pubs.rsc.org/en/content/articlelanding/2024/dd/d4dd00007b)

**Alternative Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/65c6369ee9ebbb4db9fef015) |
[Elsevier Computer Aided Chemical Engineering](https://www.sciencedirect.com/science/article/abs/pii/B978044328824150452X) |
[GitHub](https://github.com/OptiMaL-PSE-Lab/EvalRetro) |
[ResearchGate](https://www.researchgate.net/publication/377329027_Investigating_the_Reliability_and_Interpretability_of_Machine_Learning_Frameworks_for_Chemical_Retrosynthesis)

**Starred:**
False

**Tags:**
analysis


# Abstract
Machine learning models for chemical retrosynthesis have attracted substantial interest in recent years.
Unaddressed challenges, particularly the absence of robust evaluation metrics for performance comparison, and the lack of black-box interpretability, obscure model limitations and impede progress in the field.
We present an automated benchmarking pipeline designed for effective model performance comparisons.
With an emphasis on user-friendly design, we aim to streamline accessibility and facilitate utilisation within the research community.
Additionally, we suggest and perform a new interpretability study to uncover the degree of chemical understanding acquired by retrosynthesis models.
Our results reveal that frameworks based on chemical reaction rules yield the most diverse, chemically valid, and feasible reactions, whereas purely data-driven frameworks suffer from unfeasible and invalid predictions.
The interpretability study emphasises that incorporating reaction rules not only enhances model performance but also improves interpretability.
For simple molecules, we show that Graph Neural Networks identify relevant functional groups in the product molecule, offering model interpretability.
Sequence-to-sequence Transformers are not found to provide such an explanation.
As the molecule and reaction mechanism grow more complex, both data-driven models propose unfeasible disconnections without offering a chemical rationale.
We stress the importance of incorporating chemically meaningful descriptors within deep-learning models.
Our study provides valuable guidance for the future development of retrosynthesis frameworks.


# Citation
```
@article {hastedt2024a,
  author       = { Friedrich Hastedt and Rowan M. Bailey and Klaus Hellgardt and Sophia N. Yaliraki and Ehecatl Antonio del Rio Chanona and Dongda Zhang },
  title        = { Investigating the reliability and interpretability of machine learning frameworks for chemical retrosynthesis },
  journal      = { Digital Discovery },
  year         = { 2024 },
  pages        = { 1194-1212 },
  volume       = { 3 },
  issue        = { 6 },
  publisher    = { RSC },
  doi          = { 10.1039/D4DD00007B },
  url          = { https://dx.doi.org/10.1039/D4DD00007B }
}
```
