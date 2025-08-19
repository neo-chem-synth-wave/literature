# Overview
**Title:**
Efficient Retrosynthetic Planning With MCTS Exploration Enhanced A* Search

**Authors:**
Zhao, D., Tu, S., and Xu, L. |
Zhao, D. et al.

**Publication Date:**
2024/03/07

**Link:**
[Nature Communications Chemistry](https://www.nature.com/articles/s42004-024-01133-2)

**Alternative Links:**
[GitHub](https://github.com/CMACH508/MEEA) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC10920677) |
[ResearchGate](https://www.researchgate.net/publication/378802747_Efficient_retrosynthetic_planning_with_MCTS_exploration_enhanced_A_search)

**Starred:**
False

**Tags:**
single-step-retrosynthesis, multi-step-retrosynthesis, template-based, meea*


# Abstract
Retrosynthetic planning, which aims to identify synthetic pathways for target molecules from starting materials, is a fundamental problem in synthetic chemistry.
Computer-aided retrosynthesis has made significant progress, in which heuristic search algorithms, including Monte Carlo Tree Search (MCTS) and A* search, have played a crucial role.
However, unreliable guiding heuristics often cause search failure due to insufficient exploration.
Conversely, excessive exploration also prevents the search from reaching the optimal solution.
In this paper, MCTS exploration enhanced A* (MEEA*) search is proposed to incorporate the exploratory behavior of MCTS into A* by providing a look-ahead search.
Path consistency is adopted as a regularization to improve the generalization performance of heuristics. Extensive experimental results on 10 molecule datasets demonstrate the effectiveness of MEEA*.
Especially, on the widely used United States Patent and Trademark Office (USPTO) benchmark, MEEA* achieves a 100.0% success rate.
Moreover, for natural products, MEEA* successfully identifies bio-retrosynthetic pathways for 97.68% test compounds.


# Citation
```
@article {zhao2024a,
  author       = { Dengwei Zhao and Shikui Tu and Lei Xu },
  title        = { Efficient retrosynthetic planning with MCTS exploration enhanced A* search },
  journal      = { Communications Chemistry },
  year         = { 2024 },
  pages        = { 52 },
  month        = { Mar },
  volume       = { 7 },
  number       = { 1 },
  day          = { 07 },
  issn         = { 2399-3669 },
  doi          = { 10.1038/s42004-024-01133-2 },
  url          = { https://doi.org/10.1038/s42004-024-01133-2 }
}
```
