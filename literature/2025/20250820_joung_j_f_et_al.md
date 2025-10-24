# Overview
**Title:**
Electron Flow Matching for Generative Reaction Mechanism Prediction

**Authors:**
Joung, J.F., Fong, M.H., Casetti, N., Liles, J.P., Dassanayake, N.S., and Coley, C.W. |
Joung, J.F. et al.

**Publication Date:**
2025/08/20

**Link:**
[Nature](https://www.nature.com/articles/s41586-025-09426-9)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/2502.12979) |
[GitHub](https://github.com/FongMunHong/FlowER) |
[GitHub (Data)](https://github.com/jfjoung/Mechanistic_dataset)

**Tags:**
reaction-mechanism, flower


# Abstract
Central to our understanding of chemical reactivity is the principle of mass conservation1, which is fundamental for ensuring physical consistency, balancing equations and guiding reaction design.
However, data-driven computational models2,3,4,5,6,7,8,9 for tasks such as reaction product prediction rarely abide by this most basic constraint10,11,12,13.
Here we recast the problem of reaction prediction as a problem of electron redistribution using the modern deep generative framework of flow matching14,15,16, explicitly conserving both mass and electrons through the bond-electron (BE) matrix representation17,18.
Our model, FlowER, overcomes limitations inherent in previous approaches by enforcing exact mass conservation, resolving hallucinatory failure modes, recovering mechanistic reaction sequences for unseen substrate scaffolds and generalizing effectively to out-of-domain reaction classes with extremely data-efficient fine-tuning.
FlowER also enables downstream estimation of thermodynamic or kinetic feasibility and manifests a degree of chemical intuition in reaction prediction tasks.
This inherently interpretable framework represents an important step in bridging the gap between predictive accuracy and mechanistic understanding in data-driven reaction outcome prediction.


# Citation
```
@article {20250820_joung_j_f_et_al,
  author       = { Joonyoung F. Joung and Mun Hong Fong and Nicholas Casetti and Jordan P. Liles and Ne S. Dassanayake and Connor W. Coley },
  title        = { Electron flow matching for generative reaction mechanism prediction },
  journal      = { Nature },
  year         = { 2025 },
  month        = { Aug },
  day          = { 20 },
  issn         = { 1476-4687 },
  doi          = { 10.1038/s41586-025-09426-9 },
  url          = { https://doi.org/10.1038/s41586-025-09426-9 }
}
```
