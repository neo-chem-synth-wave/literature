# (20230323, Jaume-Santero, F. et al.) Transformer Performance for Chemical Reactions: Analysis of Different Predictive and Evaluation Scenarios

Tags: review, single-step-retrosynthesis, single-step-synthesis, template-free

## Publication Overview

| **Title:**  | Transformer Performance for Chemical Reactions: Analysis of Different Predictive and
Evaluation Scenarios |
| --- | --- |
| **Authors:**  | Fernando Jaume-Santero, Alban Bornet, Alain Valery, Nona Naderi,
David V. Alvarez, Dimitrios Proios, Anthony Yazdani, Colin Bournez, Thomas Fessard,
Douglas Teodoro |
| Publication Date**:**  | 2023/03/23 |
| Publication Links: | [**ACS JCIM**](https://pubs.acs.org/doi/10.1021/acs.jcim.2c01407) |
| Alternative Links: | [**UNIGE Archive**](https://archive-ouverte.unige.ch/unige:169342) |
| Code Links: | [**Official GitHub Repository**](https://github.com/albornet/chempred_revision) |

## Publication Abstract

<aside>
ℹ️ The prediction of chemical reaction pathways has been accelerated by the development of novel machine learning architectures based on the deep learning paradigm. In this context, deep neural networks initially designed for language translation have been used to accurately predict a wide range of chemical reactions. Among models suited for the task of language translation, the recently introduced molecular transformer reached impressive performance in terms of forward-synthesis and retrosynthesis predictions. In this study, we first present an analysis of the performance of transformer models for product, reactant, and reagent prediction tasks under different scenarios of data availability and data augmentation. We find that the impact of data augmentation depends on the prediction task and on the metric used to evaluate the model performance. Second, we probe the contribution of different combinations of input formats, tokenization schemes, and embedding strategies to model performance. We find that less stable input settings generally lead to better performance. Lastly, we validate the superiority of round-trip accuracy over simpler evaluation metrics, such as top-k accuracy, using a committee of human experts and show a strong agreement for predictions that pass the round-trip test. This demonstrates the usefulness of more elaborate metrics in complex predictive scenarios and highlights the limitations of direct comparisons to a predefined database, which may include a limited number of chemical reaction pathways.

</aside>