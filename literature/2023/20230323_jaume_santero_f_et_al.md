# Overview
**Title:**
Transformer Performance for Chemical Reactions: Analysis of Different Predictive and Evaluation Scenarios

**Authors:**
Jaume-Santero, F., Bornet, A., Valery, A., Naderi, N., Alvarez, D.V., Proios, D., Yazdani, A., Bournez, C., Fessard, T., and Teodoro, D. |
Jaume-Santero, F. et al.

**Publication Date:**
2023/03/23

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.2c01407)

**Alternative Links:**
[GitHub](https://github.com/albornet/chempred_revision) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC10091402) |
[University of Genève](https://archive-ouverte.unige.ch/unige:169342)

**Tags:**
single-step-synthesis, multi-step-synthesis, single-step-retrosynthesis, multi-step-retrosynthesis, analysis


# Abstract
The prediction of chemical reaction pathways has been accelerated by the development of novel machine learning architectures based on the deep learning paradigm.
In this context, deep neural networks initially designed for language translation have been used to accurately predict a wide range of chemical reactions.
Among models suited for the task of language translation, the recently introduced molecular transformer reached impressive performance in terms of forward-synthesis and retrosynthesis predictions.
In this study, we first present an analysis of the performance of transformer models for product, reactant, and reagent prediction tasks under different scenarios of data availability and data augmentation.
We find that the impact of data augmentation depends on the prediction task and on the metric used to evaluate the model performance.
Second, we probe the contribution of different combinations of input formats, tokenization schemes, and embedding strategies to model performance.
We find that less stable input settings generally lead to better performance.
Lastly, we validate the superiority of round-trip accuracy over simpler evaluation metrics, such as top-k accuracy, using a committee of human experts and show a strong agreement for predictions that pass the round-trip test.
This demonstrates the usefulness of more elaborate metrics in complex predictive scenarios and highlights the limitations of direct comparisons to a predefined database, which may include a limited number of chemical reaction pathways.


# Citation
```
@article {20230323_jaume_santero_f_et_al,
  author       = { Fernando Jaume-Santero and Alban Bornet and Alain Valery and Nona Naderi and David Vicente Alvarez and Dimitrios Proios and Anthony Yazdani and Colin Bournez and Thomas Fessard and Douglas Teodoro },
  title        = { Transformer Performance for Chemical Reactions: Analysis of Different Predictive and Evaluation Scenarios },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2023 },
  note         = { PMID: 36952584 },
  pages        = { 1914-1924 },
  volume       = { 63 },
  number       = { 7 },
  doi          = { 10.1021/acs.jcim.2c01407 },
  url          = { https://doi.org/10.1021/acs.jcim.2c01407 },
  eprint       = { https://doi.org/10.1021/acs.jcim.2c01407 }
}
```
