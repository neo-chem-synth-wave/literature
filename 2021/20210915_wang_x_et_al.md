# Overview
**Title:**
RetroPrime: A Diverse, Plausible and Transformer-based Method for Single-Step Retrosynthesis Predictions

**Authors:**
Wang, X., Li, Y., Qiu, J., Chen, G., Liu, H., Liao, B., Hsieh, C.Y., and Yao, X.

**Publication Date:**
2021/09/15

**Publication Link:**
[Elsevier Chemical Engineering](https://www.sciencedirect.com/science/article/abs/pii/S1385894721014303)

**Alternative Publication Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/60c752960f50db62a63979ee) |
[Official GitHub Repository](https://github.com/wangxr0526/RetroPrime)


# Abstract
Retrosynthesis prediction is a crucial task for organic synthesis. 
In this work, we propose a single-step template-free and Transformer-based method dubbed RetroPrime, integrating chemists’ retrosynthetic strategy of (1) decomposing a molecule into synthons then (2) generating reactants by attaching leaving groups. 
These two stages are accomplished with versatile Transformer models, respectively. 
RetroPrime achieves the Top-1 accuracy of 64.8% and 51.4%, when the reaction type is known and unknown, respectively, in the USPTO-50 K dataset. 
And the Top-1 accuracy is close to the state-of-the-art transformer-based method in the large dataset USPTO-full. 
It is known that outputs of the Transformer-based retrosynthesis model tend to suffer from insufficient diversity and high chemical implausibility. 
These problems may limit the potential of Transformer-based methods in real practice, yet few works address both issues simultaneously. 
RetroPrime is designed to tackle these challenges.


# Citation
```
@article {wang2021,
  author       = { Xiaorui Wang and Yuquan Li and Jiezhong Qiu and Guangyong Chen and Huanxiang Liu and Benben Liao and Chang-Yu Hsieh and Xiaojun Yao },
  title        = { RetroPrime: A Diverse, plausible and Transformer-based method for Single-Step retrosynthesis predictions },
  journal      = { Chemical Engineering Journal },
  year         = { 2021 },
  pages        = { 129845 },
  volume       = { 420 },
  issn         = { 1385-8947 },
  doi          = { https://doi.org/10.1016/j.cej.2021.129845 },
  url          = { https://www.sciencedirect.com/science/article/pii/S1385894721014303 }
}
```
