# Overview
**Title:**
Root-Aligned SMILES: A Tight Representation for Chemical Reaction Prediction

**Authors:**
Zhong, Z., Song, J., Feng, Z., Liu, T., Jia, L., Yao, S., Wu, M., Hou, T., and Song, M. |
Zhong, Z. et al.

**Publication Date:**
2022/07/12

**Link:**
[RSC Chemical Science](https://pubs.rsc.org/en/content/articlelanding/2022/sc/d2sc02763a)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/2203.11444) |
[GitHub](https://github.com/otori-bird/retrosynthesis) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC9365080) |
[ResearchGate](https://www.researchgate.net/publication/361926668_Root-aligned_SMILES_A_Tight_Representation_for_Chemical_Reaction_Prediction)

**Tags:**
single-step-retrosynthesis, multi-step-retrosynthesis, template-free, r-smiles


# Abstract
Chemical reaction prediction, involving forward synthesis and retrosynthesis prediction, is a fundamental problem in organic synthesis.
A popular computational paradigm formulates synthesis prediction as a sequence-to-sequence translation problem, where the typical SMILES is adopted for molecule representations.
However, the general-purpose SMILES neglects the characteristics of chemical reactions, where the molecular graph topology is largely unaltered from reactants to products, resulting in the suboptimal performance of SMILES if straightforwardly applied.
In this article, we propose the root-aligned SMILES (R-SMILES), which specifies a tightly aligned one-to-one mapping between the product and the reactant SMILES for more efficient synthesis prediction.
Due to the strict one-to-one mapping and reduced edit distance, the computational model is largely relieved from learning the complex syntax and dedicated to learning the chemical knowledge for reactions.
We compare the proposed R-SMILES with various state-of-the-art baselines and show that it significantly outperforms them all, demonstrating the superiority of the proposed method.


# Citation
```
@article {20220712b_zhong_z_et_al,
  author       = { Zipeng Zhong and Jie Song and Zunlei Feng and Tiantao Liu and Lingxiang Jia and Shaolun Yao and Min Wu and Tingjun Hou and Mingli Song },
  title        = { Root-aligned SMILES: a tight representation for chemical reaction prediction },
  journal      = { Chem. Sci. },
  year         = { 2022 },
  pages        = { 9023-9034 },
  volume       = { 13 },
  issue        = { 31 },
  publisher    = { The Royal Society of Chemistry },
  doi          = { 10.1039/D2SC02763A },
  url          = { https://dx.doi.org/10.1039/D2SC02763A }
}
```
