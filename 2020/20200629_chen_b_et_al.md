# Overview
**Title:**
Retro*: Learning Retrosynthetic Planning with Neural Guided A* Search

**Authors:**
Chen, B., Li, C., Dai, H., and Song, L.

**Publication Date:**
2020/06/29

**Publication Link:**
[arXiv](https://arxiv.org/abs/2006.15820)

**Alternative Publication Links:**
[ICML](https://proceedings.mlr.press/v119/chen20k.html) |
[Official GitHub Repository](https://github.com/binghong-ml/retro_star)


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
@inproceedings{chen2020,
    author = "Chen, Binghong and Li, Chengtao and Dai, Hanjun and Song, Le",
    title = "Retro*: Learning Retrosynthetic Planning with Neural Guided A* Search",
    booktitle = "Proceedings of the 37th International Conference on Machine Learning",
    pages = "1608--1616",
    year = "2020",
    editor = "III, Hal Daumé and Singh, Aarti",
    volume = "119",
    series = "Proceedings of Machine Learning Research",
    month = "13--18 Jul",
    publisher = "PMLR",
    pdf = "http://proceedings.mlr.press/v119/chen20k/chen20k.pdf",
    url = "https://proceedings.mlr.press/v119/chen20k.html",
}
```
