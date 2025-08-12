# (20220726, Tu, Z. and Coley, C.W.) Permutation Invariant Graph-to-Sequence Model for Template-free Retrosynthesis and Reaction Prediction

Tags: single-step-retrosynthesis, single-step-synthesis, template-free

## Publication Overview

| **Title:**  | Permutation Invariant Graph-to-Sequence Model for Template-free Retrosynthesis and Reaction Prediction |
| --- | --- |
| **Authors:**  | Zhengkai Tu, Connor W. Coley |
| Publication Date**:**  | 2022/07/26 |
| Publication Links: | [**ACS JCIM**](https://pubs.acs.org/doi/10.1021/acs.jcim.2c00321) |
| Alternative Links: | [**arXiv](https://arxiv.org/abs/2110.09681) | [OpenReview](https://openreview.net/forum?id=LLHwQh9zEb)** |
| Code Links: | [**Official GitHub Repository**](https://github.com/coleygroup/Graph2SMILES) |

## Publication Abstract

<aside>
ℹ️ Synthesis planning and reaction outcome prediction are two fundamental problems in computer-aided organic chemistry for which a variety of data-driven approaches have emerged. Natural language approaches that model each problem as a SMILES-to-SMILES translation lead to a simple end-to-end formulation, reduce the need for data preprocessing, and enable the use of well-optimized machine translation model architectures. However, SMILES representations are not efficient for capturing information about molecular structures, as evidenced by the success of SMILES augmentation to boost empirical performance. Here, we describe a novel Graph2SMILES model that combines the power of Transformer models for text generation with the permutation invariance of molecular graph encoders that mitigates the need for input data augmentation. In our encoder, a directed message passing neural network (D-MPNN) captures local chemical environments, and the global attention encoder allows for long-range and intermolecular interactions, enhanced by graph-aware positional embedding. As an end-to-end architecture, Graph2SMILES can be used as a drop-in replacement for the Transformer in any task involving molecule(s)-to-molecule(s) transformations, which we empirically demonstrate leads to improved performance on existing benchmarks for both retrosynthesis and reaction outcome prediction.

</aside>