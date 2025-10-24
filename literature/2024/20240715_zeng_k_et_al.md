# Overview
**Title:**
Ualign: Pushing the Limit of Template-Free Retrosynthesis Prediction With Unsupervised SMILES Alignment

**Authors:**
Zeng, K., Yang, B., Zhao, X., Zhang, Y., Nie, F., Yang, X., Jin, Y., and Xu, Y. |
Zeng, K. et al.

**Publication Date:**
2024/07/15

**Link:**
[BMC Journal of Cheminformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-024-00877-2)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/2404.00044) |
[GitHub](https://github.com/zengkaipeng/UAlign) |
[ResearchGate](https://www.researchgate.net/publication/382270476_Ualign_pushing_the_limit_of_template-free_retrosynthesis_prediction_with_unsupervised_SMILES_alignment) |
[ResearchGate (Pre-print)](https://www.researchgate.net/publication/380084278_UAlign_Pushing_the_Limit_of_Template-free_Retrosynthesis_Prediction_with_Unsupervised_SMILES_Alignment)

**Tags:**
single-step-retrosynthesis, multi-step-retrosynthesis, template-free, ualign


# Abstract
Motivation

Retrosynthesis planning poses a formidable challenge in the organic chemical industry, particularly in pharmaceuticals.
Single-step retrosynthesis prediction, a crucial step in the planning process, has witnessed a surge in interest in recent years due to advancements in AI for science.
Various deep learning-based methods have been proposed for this task in recent years, incorporating diverse levels of additional chemical knowledge dependency.

Results

This paper introduces UAlign, a template-free graph-to-sequence pipeline for retrosynthesis prediction.
By combining graph neural networks and Transformers, our method can more effectively leverage the inherent graph structure of molecules.
Based on the fact that the majority of molecule structures remain unchanged during a chemical reaction, we propose a simple yet effective SMILES alignment technique to facilitate the reuse of unchanged structures for reactant generation.
Extensive experiments show that our method substantially outperforms state-of-the-art template-free and semi-template-based approaches.
Importantly, our template-free method achieves effectiveness comparable to, or even surpasses, established powerful template-based methods.


# Citation
```
@article {20240715_zeng_k_et_al,
  author       = { Kaipeng Zeng and Bo Yang and Xin Zhao and Yu Zhang and Fan Nie and Xiaokang Yang and Yaohui Jin and Yanyan Xu },
  title        = { Ualign: pushing the limit of template-free retrosynthesis prediction with unsupervised SMILES alignment },
  journal      = { Journal of Cheminformatics },
  year         = { 2024,
  pages        = { 80 },
  month        = { Jul },
  volume       = { 16 },
  number       = { 1 },
  day          = { 15 },
  issn         = { 1758-2946 },
  doi          = { 10.1186/s13321-024-00877-2 },
  url          = { https://doi.org/10.1186/s13321-024-00877-2 }
}
```
