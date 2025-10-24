# Overview
**Title:**
DirectMultiStep: Direct Route Generation for Multistep Retrosynthesis

**Authors:**
Shee, Y., Morgunov, A., Li, H., and Batista, V.S. |
Shee, Y. et al.

**Publication Date:**
2025/04/08

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.4c01982)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/2405.13983) |
[DirectMultiStep](https://directmultistep.com) |
[GitHub](https://github.com/batistagroup/DirectMultiStep) |
[ResearchGate](https://www.researchgate.net/publication/380820896_DirectMultiStep_Direct_Route_Generation_for_Multi-Step_Retrosynthesis)

**Tags:**
multi-step-retrosynthesis, template-free, direct-multi-step


# Abstract
Traditional computer-aided synthesis planning (CASP) methods rely on iterative single-step predictions, leading to exponential search space growth that limits efficiency and scalability.
We introduce a series of transformer-based models that leverage a mixture of experts approach to directly generate multistep synthetic routes as a single string, conditionally predicting each transformation based on all preceding ones.
Our DMS Explorer XL model, which requires only target compounds as input, outperforms state-of-the-art methods on the PaRoutes dataset with 1.9x and 3.1x improvements in Top-1 accuracy on the n1 and n5 test sets, respectively.
Providing additional information, such as the desired number of steps and starting materials, enables both a reduction in model size and an increase in accuracy, highlighting the benefits of incorporating more constraints into the prediction process.
The top-performing DMS-Flex (Duo) model scores 25–50% higher on Top-1 and Top-10 accuracies for both n1 and n5 sets.
Additionally, our models successfully predict routes for the FDA-approved drugs not included in the training data, demonstrating strong generalization capabilities.
While the limited diversity of the training set may affect performance on less common reaction types, our multistep-first approach presents a promising direction toward fully automated retrosynthetic planning.


# Citation
```
@article {20250408b_shee_y_et_al,
  author       = { Yu Shee and Anton Morgunov and Haote Li and Victor S. Batista },
  title        = { DirectMultiStep: Direct Route Generation for Multistep Retrosynthesis },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2025 },
  note         = { PMID: 40197023 },
  pages        = { 3903-3914 },
  volume       = { 65 },
  number       = { 8 },
  doi          = { 10.1021/acs.jcim.4c01982 },
  url          = { https://doi.org/10.1021/acs.jcim.4c01982 },
  eprint       = { https://doi.org/10.1021/acs.jcim.4c01982 }
}
```
