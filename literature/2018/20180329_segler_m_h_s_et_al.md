# Overview
**Title:**
Planning Chemical Syntheses With Deep Neural Networks and Symbolic AI

**Authors:**
Segler, M.H.S., Preuss, M., and Waller, M.P. |
Segler, M.H.S. et al.

**Publication Date:**
2018/03/29

**Link:**
[Nature](https://www.nature.com/articles/nature25978)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/1708.04202)

**Starred:**
True

**Tags:**
single-step-retrosynthesis, multi-step-retrosynthesis, template-based, fingerprint, 3n-mcts


# Abstract
To plan the syntheses of small organic molecules, chemists use retrosynthesis, a problem-solving technique in which target molecules are recursively transformed into increasingly simpler precursors.
Computer-aided retrosynthesis would be a valuable tool but at present it is slow and provides results of unsatisfactory quality.
Here we use Monte Carlo tree search and symbolic artificial intelligence (AI) to discover retrosynthetic routes.
We combined Monte Carlo tree search with an expansion policy network that guides the search, and a filter network to pre-select the most promising retrosynthetic steps.
These deep neural networks were trained on essentially all reactions ever published in organic chemistry.
Our system solves for almost twice as many molecules, thirty times faster than the traditional computer-aided search method, which is based on extracted rules and hand-designed heuristics.
In a double-blind AB test, chemists on average considered our computer-generated routes to be equivalent to reported literature routes.


# Citation
```
@article {segler2018a,
  author       = { Marwin H. S. Segler and Mike Preuss and Mark P. Waller },
  title        = { Planning chemical syntheses with deep neural networks and symbolic AI },
  journal      = { Nature },
  year         = { 2018 },
  pages        = { 604-610 },
  month        = { Mar },
  volume       = { 555 },
  number       = { 7698 },
  day          = { 01 },
  issn         = { 1476-4687 },
  doi          = { 10.1038/nature25978 },
  url          = { https://doi.org/10.1038/nature25978 }
}
```
