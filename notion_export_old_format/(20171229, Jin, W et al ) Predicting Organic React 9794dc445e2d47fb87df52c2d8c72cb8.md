# (20171229, Jin, W. et al.) Predicting Organic Reaction Outcomes with Weisfeiler-Lehman Network

Tags: single-step-synthesis, template-based

## Publication Overview

| **Title:**  | Predicting Organic Reaction Outcomes with Weisfeiler-Lehman Network |
| --- | --- |
| **Authors:**  | Wengong Jin, Connor W. Coley, Regina Barzilay, Tommi Jaakkola |
| Publication Date**:**  | 2017/12/29 |
| Publication Links: | [**arXiv**](https://arxiv.org/abs/1709.04555) |
| Alternative Links: | [**NeurIPS**](https://proceedings.neurips.cc/paper/2017/hash/ced556cd9f9c0c8315cfbe0744a3baf0-Abstract.html) |
| Code Links: | [**Official GitHub Repository**](https://github.com/wengong-jin/nips17-rexgen) |

## Publication Abstract

<aside>
ℹ️ The prediction of organic reaction outcomes is a fundamental problem in computational chemistry. Since a reaction may involve hundreds of atoms, fully exploring the space of possible transformations is intractable. The current solution utilizes reaction templates to limit the space, but it suffers from coverage and efficiency issues. In this paper, we propose a template-free approach to efficiently explore the space of product molecules by first pinpointing the reaction center -- the set of nodes and edges where graph edits occur. Since only a small number of atoms contribute to reaction center, we can directly enumerate candidate products. The generated candidates are scored by a Weisfeiler-Lehman Difference Network that models high-order interactions between changes occurring at nodes across the molecule. Our framework outperforms the top-performing template-based approach with a 10\% margin, while running orders of magnitude faster. Finally, we demonstrate that the model accuracy rivals the performance of domain experts.

</aside>