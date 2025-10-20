# Overview
**Title:**
Retro*: Learning Retrosynthetic Planning With Neural Guided A* Search

**Authors:**
Chen, B., Li, C., Dai, H., and Song, L. |
Chen, B. et al.

**Publication Date:**
2020/07/13

**Link:**
[ICML 2020](https://proceedings.mlr.press/v119/chen20k.html)

**Alternative Links:**
[ACM Digital Library](https://dl.acm.org/doi/10.5555/3524938.3525088) |
[arXiv](https://arxiv.org/abs/2006.15820) |
[GitHub](https://github.com/binghong-ml/retro_star)

**Tags:**
single-step-retrosynthesis, multi-step-retrosynthesis, template-based, retro*


# Abstract
Retrosynthetic planning is a critical task in organic chemistry which identifies a series of reactions that can lead to the synthesis of a target product.
The vast number of possible chemical transformations makes the size of the search space very big, and retrosynthetic planning is challenging even for experienced chemists.
However, existing methods either require expensive return estimation by rollout with high variance, or optimize for search speed rather than the quality.
In this paper, we propose Retro*, a neural-based A*-like algorithm that finds high-quality synthetic routes efficiently.
It maintains the search as an AND-OR tree, and learns a neural search bias with off-policy data.
Then guided by this neural network, it performs best-first search efficiently during new planning episodes.
Experiments on benchmark USPTO datasets show that, our proposed method outperforms existing state-of-the-art with respect to both the success rate and solution quality, while being more efficient at the same time.


# Citation
```
@inproceedings {20200713a_chen_b_et_al,
  author       = { Binghong Chen and Chengtao Li and Hanjun Dai and Le Song },
  title        = { Retro*: Learning Retrosynthetic Planning with Neural Guided A* Search },
  booktitle    = { Proceedings of the 37th International Conference on Machine Learning },
  year         = { 2020 },
  volume       = { 119 },
  series       = { Proceedings of Machine Learning Research },
  pages        = { 1608-1616 },
  month        = { 13-18 Jul },
  publisher    = { PMLR },
  editor       = { III, Hal Daumé and Singh, Aarti },
  pdf          = { https://proceedings.mlr.press/v119/chen20k/chen20k.pdf },
  url          = { https://proceedings.mlr.press/v119/chen20k.html }
}
```
