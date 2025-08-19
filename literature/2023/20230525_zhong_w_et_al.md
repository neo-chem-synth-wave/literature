# Overview
**Title:**
Retrosynthesis Prediction Using an End-to-End Graph Generative Architecture for Molecular Graph Editing

**Authors:**
Zhong, W., Yang, Z., and Chen, C.Y. |
Zhong, W. et al.

**Publication Date:**
2023/05/25

**Publication Link:**
[Nature Communications](https://www.nature.com/articles/s41467-023-38851-5)

**Alternative Links:**
[GitHub](https://github.com/Jamson-Zhong/Graph2Edits) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC10209957) |
[ResearchGate](https://www.researchgate.net/publication/371040452_Retrosynthesis_prediction_using_an_end-to-end_graph_generative_architecture_for_molecular_graph_editing)

**Starred:**
False

**Tags:**
single-step-retrosynthesis, semi-template-based, graph2edits


# Abstract
Retrosynthesis planning, the process of identifying a set of available reactions to synthesize the target molecules, remains a major challenge in organic synthesis.
Recently, computer-aided synthesis planning has gained renewed interest and various retrosynthesis prediction algorithms based on deep learning have been proposed.
However, most existing methods are limited to the applicability and interpretability of model predictions, and further improvement of predictive accuracy to a more practical level is still required.
In this work, inspired by the arrow-pushing formalism in chemical reaction mechanisms, we present an end-to-end architecture for retrosynthesis prediction called Graph2Edits.
Specifically, Graph2Edits is based on graph neural network to predict the edits of the product graph in an auto-regressive manner, and sequentially generates transformation intermediates and final reactants according to the predicted edits sequence.
This strategy combines the two-stage processes of semi-template-based methods into one-pot learning, improving the applicability in some complicated reactions, and also making its predictions more interpretable.
Evaluated on the standard benchmark dataset USPTO-50k, our model achieves the state-of-the-art performance for semi-template-based retrosynthesis with a promising 55.1% top-1 accuracy.


# Citation
```
@article {zhong2023a,
  author       = { Weihe Zhong and Ziduo Yang and Calvin Yu-Chian Chen },
  title        = { Retrosynthesis prediction using an end-to-end graph generative architecture for molecular graph editing },
  journal      = { Nature Communications },
  year         = { 2023 },
  pages        = { 3009 },
  month        = { May },
  volume       = { 14 },
  number       = { 1 },
  day          = { 25 },
  issn         = { 2041-1723 },
  doi          = { 10.1038/s41467-023-38851-5 },
  url          = { https://doi.org/10.1038/s41467-023-38851-5 }
}
```
