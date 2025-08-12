# (20220712, Zhong, Z. et al.) Root-aligned SMILES: A Tight Representation for Chemical Reaction Prediction

Tags: single-step-retrosynthesis, single-step-synthesis, template-free

## Publication Overview

| **Title:**  | Root-aligned SMILES: A Tight Representation for Chemical Reaction Prediction |
| --- | --- |
| **Authors:**  | Zipeng Zhong, Jie Song, Zunlei Feng, Tiantao Liu, Lingxiang Jia, Shaolun Yao, Min Wu,
Tingjun Hou, Mingli Song |
| Publication Date**:**  | 2022/07/12 |
| Publication Links: | [**RSC Chemical Science**](https://pubs.rsc.org/en/content/articlelanding/2022/sc/d2sc02763a) |
| Alternative Links: | [**arXiv](https://arxiv.org/abs/2203.11444) | [ResearchGate](https://www.researchgate.net/publication/359411170_Root-aligned_SMILES_for_Molecular_Retrosynthesis_Prediction)** |
| Code Links: | [**Official GitHub Repository**](https://github.com/otori-bird/retrosynthesis) |

## Publication Abstract

<aside>
ℹ️ Chemical reaction prediction, involving forward synthesis and retrosynthesis prediction, is a fundamental problem in organic synthesis. A popular computational paradigm formulates synthesis prediction as a sequence-to-sequence translation problem, where the typical SMILES is adopted for molecule representations. However, the general-purpose SMILES neglects the characteristics of chemical reactions, where the molecular graph topology is largely unaltered from reactants to products, resulting in the suboptimal performance of SMILES if straightforwardly applied. In this article, we propose the root-aligned SMILES (R-SMILES), which specifies a tightly aligned one-to-one mapping between the product and the reactant SMILES for more efficient synthesis prediction. Due to the strict one-to-one mapping and reduced edit distance, the computational model is largely relieved from learning the complex syntax and dedicated to learning the chemical knowledge for reactions. We compare the proposed R-SMILES with various state-of-the-art baselines and show that it significantly outperforms them all, demonstrating the superiority of the proposed method.

</aside>