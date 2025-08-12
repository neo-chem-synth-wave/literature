# (20200303, Lin, K. et al.) Automatic Retrosynthetic Route Planning using Template-free Models

Tags: single-step-retrosynthesis, synthesis-route-planning, template-free

## Publication Overview

| **Title:**  | Automatic Retrosynthetic Route Planning using Template-free Models |
| --- | --- |
| **Authors:**  | Kangjie Lin, Youjun Xu, Jianfeng Pei, Luhua Lai |
| Publication Date**:**  | 2020/03/03 |
| Publication Links: | [**RSC Chemical Science**](https://pubs.rsc.org/en/content/articlelanding/2020/sc/c9sc03666k) |
| Alternative Links: | [**arXiv](https://arxiv.org/abs/1906.02308) | [ResearchGate](https://www.researchgate.net/publication/339651598_Automatic_Retrosynthetic_Route_Planning_Using_Template-Free_Models)** |
| Code Links: | [**Official GitHub Repository**](https://github.com/PKUMDL-AI/AutoSynRoute) |

## Publication Abstract

<aside>
ℹ️ Retrosynthetic route planning can be considered a rule-based reasoning procedure. The possibilities for each transformation are generated based on collected reaction rules, and then potential reaction routes are recommended by various optimization algorithms. Although there has been much progress in computer-assisted retrosynthetic route planning and reaction prediction, fully data-driven automatic retrosynthetic route planning remains challenging. Here we present a template-free approach that is independent of reaction templates, rules, or atom mapping, to implement automatic retrosynthetic route planning. We treated each reaction prediction task as a data-driven sequence-to-sequence problem using the multi-head attention-based Transformer architecture, which has demonstrated power in machine translation tasks. Using reactions from the United States patent literature, our end-to-end models naturally incorporate the global chemical environments of molecules and achieve remarkable performance in top-1 predictive accuracy (63.0%, with the reaction class provided) and top-1 molecular validity (99.6%) in one-step retrosynthetic tasks. Inspired by the success rate of the one-step reaction prediction, we further carried out iterative, multi-step retrosynthetic route planning for four case products, which was successful. We then constructed an automatic data-driven end-to-end retrosynthetic route planning system (AutoSynRoute) using Monte Carlo tree search with a heuristic scoring function. AutoSynRoute successfully reproduced published synthesis routes for the four case products. The end-to-end model for reaction task prediction can be easily extended to larger or customer-requested reaction databases. Our study presents an important step in realizing automatic retrosynthetic route planning.

</aside>