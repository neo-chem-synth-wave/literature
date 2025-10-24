# Overview
**Title:**
Challenging Reaction Prediction Models to Generalize to Novel Chemistry

**Authors:**
Bradshaw, J., Zhang, A., Mahjour, B., Graff, D.E., Segler, M.H.S., and Coley, C.W. |
Bradshaw, J. et al.

**Publication Date:**
2025/03/12

**Link:**
[ACS Central Science](https://pubs.acs.org/doi/10.1021/acscentsci.5c00055)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/2501.06669) |
[GitHub (Data)](https://github.com/john-bradshaw/rxn-splits) |
[GitHub (Model)](https://github.com/john-bradshaw/rxn-lm)

**Tags:**
single-step-synthesis, benchmarking


# Abstract
Deep learning models for anticipating the products of organic reactions have found many use cases, including validating retrosynthetic pathways and constraining synthesis-based molecular design tools.
Despite compelling performance on popular benchmark tasks, strange and erroneous predictions sometimes ensue when using these models in practice.
The core issue is that common benchmarks test models in an in-distribution setting, whereas many real-world uses for these models are in out-of-distribution settings and require a greater degree of extrapolation.
To better understand how current reaction predictors work in out-of-distribution domains, we report a series of more challenging evaluations of a prototypical SMILES-based deep learning model.
First, we illustrate how performance on randomly sampled data sets is overly optimistic compared to performance when generalizing to new patents or new authors.
Second, we conduct time splits that evaluate how models perform when tested on reactions published years after those in their training set, mimicking real-world deployment.
Finally, we consider extrapolation across reaction classes to reflect what would be required for the discovery of novel reaction types.
This panel of tasks can reveal the capabilities and limitations of today’s reaction predictors, acting as a crucial first step in the development of tomorrow's next-generation models capable of reaction discovery.


# Citation
```
@article {20250312_bradshaw_j_et_al,
  author       = { John Bradshaw and Anji Zhang and Babak Mahjour and David E. Graff and Marwin H. S. Segler and Connor W. Coley },
  title        = { Challenging Reaction Prediction Models to Generalize to Novel Chemistry },
  journal      = { ACS Central Science },
  year         = { 2025 },
  pages        = { 539-549 },
  volume       = { 11 },
  number       = { 4 },
  doi          = { 10.1021/acscentsci.5c00055 },
  url          = { https://doi.org/10.1021/acscentsci.5c00055 },
  eprint       = { https://doi.org/10.1021/acscentsci.5c00055 }
}
```
