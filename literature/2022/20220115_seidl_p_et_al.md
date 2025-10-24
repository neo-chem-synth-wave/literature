# Overview
**Title:**
Improving Few- and Zero-Shot Reaction Template Prediction Using Modern Hopfield Networks

**Authors:**
Seidl, P., Renz, P., Dyubankova, N., Neves, P., Verhoeven, J., Wegner, J.K., Segler, M.H.S., Hochreiter, S., and Klambauer, G. |
Seidl, P. et al.

**Publication Date:**
2022/01/15

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.1c01065)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/2104.03279) |
[GitHub](https://github.com/ml-jku/mhn-react) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC9092346) |
[Johannes Kepler University Linz Library ePub Repository](https://epub.jku.at/obvulioa/content/titleinfo/8307162)

**Tags:**
single-step-retrosynthesis, template-based, mhn-react


# Abstract
Finding synthesis routes for molecules of interest is essential in the discovery of new drugs and materials.
To find such routes, computer-assisted synthesis planning (CASP) methods are employed, which rely on a single-step model of chemical reactivity.
In this study, we introduce a template-based single-step retrosynthesis model based on Modern Hopfield Networks, which learn an encoding of both molecules and reaction templates in order to predict the relevance of templates for a given molecule.
The template representation allows generalization across different reactions and significantly improves the performance of template relevance prediction, especially for templates with few or zero training examples.
With inference speed up to orders of magnitude faster than baseline methods, we improve or match the state-of-the-art performance for top-k exact match accuracy for k ≥ 3 in the retrosynthesis benchmark USPTO-50k.
Code to reproduce the results is available at github.com/ml-jku/mhn-react.


# Citation
```
@article {20220115_seidl_p_et_al,
  author       = { Philipp Seidl and Philipp Renz and Natalia Dyubankova and Paulo Neves and Jonas Verhoeven and Jörg K. Wegner and Marwin Segler and Sepp Hochreiter and Günter Klambauer },
  title        = { Improving Few- and Zero-Shot Reaction Template Prediction Using Modern Hopfield Networks },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2022 },
  note         = { PMID: 35034452 },
  pages        = { 2111-2120 },
  volume       = { 62 },
  number       = { 9 },
  doi          = { 10.1021/acs.jcim.1c01065 },
  url          = { https://doi.org/10.1021/acs.jcim.1c01065 },
  eprint       = { https://doi.org/10.1021/acs.jcim.1c01065 }
}
```
