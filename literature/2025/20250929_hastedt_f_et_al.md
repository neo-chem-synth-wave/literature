# Overview
**Title:**
MolPrice: Assessing Synthetic Accessibility of Molecules Based on Market Value

**Authors:**
Hastedt, F., Hellgardt, K., Yaliraki, S., Zhang, D., and Chanona, A.R. |
Hastedt, F. et al.

**Publication Date:**
2025/09/29

**Link:**
[BMC Journal of Cheminformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-025-01076-3)

**Alternative Links:**
[GitHub](https://github.com/OptiMaL-PSE-Lab/MolPrice)

**Tags:**
synthesizability, mol-price


# Abstract
Machine learning approaches for conceptualizing and designing in silico compounds have attracted significant attention.
However, the applicability of these compounds is often challenged by synthetic viability and cost-effectiveness.
Researchers introduced proxy-scores, known as synthethic accessiblity scoring, to quantify the ease of synthesis for virtual molecules.
Despite their utility, existing synthetic accessibility tools have notable limitations: they overlook compound purchasability, lack physical interpretability, and often rely on imperfect computer-aided synthesis planning algorithms.
We introduce MolPrice, an accurate and fast model for molecular price prediction.
Utilizing self-supervised contrastive learning, MolPrice autonomously generates price labels for synthetically complex molecules, enabling the model to generalize to molecules beyond the training distribution.
Our results show that MolPrice reliably assigns higher prices to synthetically complex molecules than to readily purchasable ones, effectively distinguishing different levels of synthetic accessibility.
Furthermore, MolPrice achieves competitive performance on literature benchmarks for synthetic accessibility.
To demonstrate its practical utility, we conduct a virtual screening case study, illustrating how MolPrice successfully identifies purchasable molecules from a large candidate library.
MolPrice bridges the gap between generative molecular design and real-world feasibility by integrating cost-awareness into synthetic accessibility assessment, making it a powerful model to accelerate molecular discovery.


# Citation
```
@article {20250929_hastedt_f_et_al,
  author       = { Friedrich Hastedt and Klaus Hellgardt and Sophia Yaliraki and Dongda Zhang and Antonio del Rio Chanona },
  title        = { MolPrice: assessing synthetic accessibility of molecules based on market value },
  journal      = { Journal of Cheminformatics },
  year         = { 2025 },
  pages        = { 150 },
  month        = { Sep },
  volume       = { 17 },
  number       = { 1 },
  day          = { 29 },
  issn         = { 1758-2946 },
  doi          = { 10.1186/s13321-025-01076-3 },
  url          = { https://doi.org/10.1186/s13321-025-01076-3 }
}
```
