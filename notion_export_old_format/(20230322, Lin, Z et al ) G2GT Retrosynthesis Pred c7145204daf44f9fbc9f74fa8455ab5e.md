# (20230322, Lin, Z. et al.) G2GT: Retrosynthesis Prediction with Graph-to-Graph Attention Neural Network and Self-Training

Tags: single-step-retrosynthesis, template-free

## Publication Overview

| **Title:**  | G2GT: Retrosynthesis Prediction with Graph-to-Graph Attention Neural Network and
Self-Training |
| --- | --- |
| **Authors:**  | Zaiyun Lin, Shiqiu Yin, Lei Shi, Wenbiao Zhou, Yingsheng J. Zhang |
| Publication Date**:**  | 2023/03/22 |
| Publication Links: | [**ACS JCIM**](https://pubs.acs.org/doi/10.1021/acs.jcim.2c01302) |
| Alternative Links: | [**arXiv**](https://arxiv.org/abs/2204.08608) |
| Code Links: | [**Official GitHub Repository**](https://github.com/Anonnoname/G2GT_2) |

## Publication Abstract

<aside>
ℹ️ Retrosynthesis prediction, the task of identifying reactant molecules that can be used to synthesize product molecules, is a fundamental challenge in organic chemistry and related fields. To address this challenge, we propose a novel graph-to-graph transformation model, G2GT. The model is built on the standard transformer structure and utilizes graph encoders and decoders. Additionally, we demonstrate the effectiveness of self-training, a data augmentation technique that utilizes unlabeled molecular data, in improving the performance of the model. To further enhance diversity, we propose a weak ensemble method, inspired by reaction-type labels and ensemble learning. This method incorporates beam search, nucleus sampling, and top-k sampling to improve inference diversity. A simple ranking algorithm is employed to retrieve the final top-10 results. We achieved new state-of-the-art results on both the USPTO-50K data set, with a top-1 accuracy of 54%, and the larger more challenging USPTO-Full data set, with a top-1 accuracy of 49.3% and competitive top-10 results. Our model can also be generalized to all other graph-to-graph transformation tasks. Data and code are available at: [https://github.com/Anonnoname/G2GT_2](https://github.com/Anonnoname/G2GT_2).

</aside>