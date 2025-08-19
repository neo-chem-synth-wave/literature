# Overview
**Title:**
Retrosynthetic Planning With Experience-Guided Monte Carlo Tree Search

**Authors:**
Hong, S., Zhuo, H.H., Jin, K., Shao, G., and Zhou, Z.

**Publication Date:**
2023/06/10

**Link:**
[Nature Communications](https://www.nature.com/articles/s42004-023-00911-8)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/2112.06028) |
[GitHub](https://github.com/jjljkjljk/EG-MCTS)

**Starred:**
False

**Tags:**
single-step-retrosynthesis, multi-step-retrosynthesis, eg-mcts


# Abstract
In retrosynthetic planning, the huge number of possible routes to synthesize a complex molecule using simple building blocks leads to a combinatorial explosion of possibilities.
Even experienced chemists often have difficulty to select the most promising transformations.
The current approaches rely on human-defined or machine-trained score functions which have limited chemical knowledge or use expensive estimation methods for guiding.
Here we propose an experience-guided Monte Carlo tree search (EG-MCTS) to deal with this problem.
Instead of rollout, we build an experience guidance network to learn knowledge from synthetic experiences during the search.
Experiments on benchmark USPTO datasets show that, EG-MCTS gains significant improvement over state-of-the-art approaches both in efficiency and effectiveness.
In a comparative experiment with the literature, our computer-generated routes mostly matched the reported routes.
Routes designed for real drug compounds exhibit the effectiveness of EG-MCTS on assisting chemists performing retrosynthetic analysis.


# Citation
```
@article {hong2023a,
  author       = { Siqi Hong and Hankz Hankui Zhuo and Kebing Jin and Guang Shao and Zhanwen Zhou },
  title        = { Retrosynthetic planning with experience-guided Monte Carlo tree search },
  journal      = { Communications Chemistry },
  year         = { 2023 },
  pages        = { 120 },
  month        = { Jun },
  volume       = { 6 },
  number       = { 1 },
  day          = { 10 },
  issn         = { 2399-3669 },
  doi          = { 10.1038/s42004-023-00911-8 },
  url          = { https://doi.org/10.1038/s42004-023-00911-8 }
}
```
