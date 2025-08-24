# Overview
**Title:**
DiffER: Categorical Diffusion Ensembles for Single-Step Chemical Retrosynthesis

**Authors:**
Current, S., Chen, Z., Adu-Ampratwum, D., Ning, X., and Parthasarathy, S. |
Current, S. et al.

**Publication Date:**
2025/07/29

**Link:**
[BMC Journal of Cheminformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-025-01056-7)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/2505.23721) |
[GitHub](https://github.com/sfcurre/DiffER) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC12309231) |
[ResearchGate](https://www.researchgate.net/publication/394099687_DiffERdocumentclass12ptminimal_usepackageamsmath_usepackagewasysym_usepackageamsfonts_usepackageamssymb_usepackageamsbsy_usepackagemathrsfs_usepackageupgreek_setlengthoddsidemargin-69pt_begindocumentt)

**Starred:**
False

**Tags:**
single-step-retrosynthesis, diffusion, differ


# Abstract
Methods for automatic chemical retrosynthesis have found recent success through the application of models traditionally built for natural language processing, primarily through transformer neural networks.
These models have demonstrated significant ability to translate between the SMILES encodings of chemical products and reactants, but are constrained as a result of their autoregressive nature.
We propose DiffER, an alternative template-free method for single-step retrosynthesis prediction in the form of categorical diffusion, which allows the entire output SMILES sequence to be predicted in unison.
We construct an ensemble of diffusion models which achieves state-of-the-art performance for top-1 accuracy and competitive performance for top-3, top-5, and top-10 accuracy among template-free methods.
We prove that DiffER is a strong baseline for a new class of template-free model and is capable of learning a variety of synthetic techniques used in laboratory settings.


# Citation
```
@article {current2025a,
  author       = { Sean Current and Ziqi Chen and Daniel Adu-Ampratwum and Xia Ning and Srinivasan Parthasarathy },
  title        = { DiffER: categorical diffusion ensembles for single-step chemical retrosynthesis },
  journal      = { Journal of Cheminformatics },
  year         = { 2025 },
  pages        = { 112 },
  month        = { Jul },
  volume       = { 17 },
  number       = { 1 },
  day          = { 29 },
  issn         = { 1758-2946 },
  doi          = { 10.1186/s13321-025-01056-7 },
  url          = { https://doi.org/10.1186/s13321-025-01056-7 }
}
```
