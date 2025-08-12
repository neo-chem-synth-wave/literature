# (20210604, Somnath, V.R. et al.) Learning Graph Models for Retrosynthesis Prediction

Tags: single-step-retrosynthesis, template-based

## Publication Overview

| **Title:**  | Learning Graph Models for Retrosynthesis Prediction |
| --- | --- |
| **Authors:**  | Vignesh R. Somnath, Charlotte Bunne, Connor W. Coley, Andreas Krause, Regina Barzilay |
| Publication Date**:**  | 2021/06/04 |
| Publication Links: | [**arXiv**](https://arxiv.org/abs/2006.07038) |
| Alternative Links: | [**NeurIPS](https://proceedings.neurips.cc/paper/2021/hash/4e2a6330465c8ffcaa696a5a16639176-Abstract.html) | [OpenReview](https://openreview.net/forum?id=LyjH88yV7F)** |
| Code Links: | [**Official GitHub Repository**](https://github.com/vsomnath/graphretro) |

## Publication Abstract

<aside>
ℹ️ Retrosynthesis prediction is a fundamental problem in organic synthesis, where the task is to identify precursor molecules that can be used to synthesize a target molecule. A key consideration in building neural models for this task is aligning model design with strategies adopted by chemists. Building on this viewpoint, this paper introduces a graph-based approach that capitalizes on the idea that the graph topology of precursor molecules is largely unaltered during a chemical reaction. The model first predicts the set of graph edits transforming the target into incomplete molecules called synthons. Next, the model learns to expand synthons into complete molecules by attaching relevant leaving groups. This decomposition simplifies the architecture, making its predictions more interpretable, and also amenable to manual correction. Our model achieves a top-1 accuracy of 53.7%, outperforming previous template-free and semi-template-based methods.

</aside>