# Overview
**Title:**
State-of-the-Art Augmented NLP Transformer Models for Direct and Single-Step Retrosynthesis

**Authors:**
Tetko, I.V., Karpov, P., Deursen, R.V., and Godin, G. |
Tetko, I.V. et al.

**Publication Date:**
2020/11/04

**Link:**
[Nature Communications](https://www.nature.com/articles/s41467-020-19266-y)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/2003.02804) |
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/60c7417af96a00cd49286446) |
[GitHub](https://github.com/bigchem/synthesis) |
[ResearchGate](https://www.researchgate.net/publication/346496604_State-of-the-art_augmented_NLP_transformer_models_for_direct_and_single-step_retrosynthesis)

**Starred:**
True

**Tags:**
single-step-retrosynthesis, template-free


# Abstract
We investigated the effect of different training scenarios on predicting the (retro)synthesis of chemical compounds using text-like representation of chemical reactions (SMILES) and Natural Language Processing (NLP) neural network Transformer architecture.
We showed that data augmentation, which is a powerful method used in image processing, eliminated the effect of data memorization by neural networks and improved their performance for prediction of new sequences.
This effect was observed when augmentation was used simultaneously for input and the target data simultaneously.
The top-5 accuracy was 84.8% for the prediction of the largest fragment (thus identifying principal transformation for classical retro-synthesis) for the USPTO-50k test dataset, and was achieved by a combination of SMILES augmentation and a beam search algorithm.
The same approach provided significantly better results for the prediction of direct reactions from the single-step USPTO-MIT test set.
Our model achieved 90.6% top-1 and 96.1% top-5 accuracy for its challenging mixed set and 97% top-5 accuracy for the USPTO-MIT separated set.
It also significantly improved results for USPTO-full set single-step retrosynthesis for both top-1 and top-10 accuracies.
The appearance frequency of the most abundantly generated SMILES was well correlated with the prediction outcome and can be used as a measure of the quality of reaction prediction.


# Citation
```
@article {tetko2020a,
  author       = { Igor V. Tetko and Pavel Karpov and Ruud Van Deursen and Guillaume Godin },
  title        = { State-of-the-art augmented NLP transformer models for direct and single-step retrosynthesis },
  journal      = { Nature Communications },
  year         = { 2020 },
  pages        = { 5575 },
  month        = { Nov },
  volume       = { 11 },
  number       = { 1 },
  day          = { 04 },
  issn         = { 2041-1723 },
  doi          = { 10.1038/s41467-020-19266-y },
  url          = { https://doi.org/10.1038/s41467-020-19266-y }
}
```
