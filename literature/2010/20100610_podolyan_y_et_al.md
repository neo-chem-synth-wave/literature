# Overview
**Title:**
Assessing Synthetic Accessibility of Chemical Compounds Using Machine Learning Methods

**Authors:**
Podolyan, Y., Walters, M.A., and Karypis, G. |
Podolyan, Y. et al.

**Publication Date:**
2010/06/10

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/ci900301v)

**Alternative Links:**
None

**Tags:**
synthesizability


# Abstract
With de novo rational drug design, scientists can rapidly generate a very large number of potentially biologically active probes.
However, many of them may be synthetically infeasible and, therefore, of limited value to drug developers.
On the other hand, most of the tools for synthetic accessibility evaluation are very slow and can process only a few molecules per minute.
In this study, we present two approaches to quickly predict the synthetic accessibility of chemical compounds by utilizing support vector machines operating on molecular descriptors.
The first approach, RSsvm, is designed to identify the compounds that can be synthesized using a specific set of reactions and starting materials and builds its model by training on the compounds identified as synthetically accessible or not by retrosynthetic analysis.
The second approach, DRsvm, is designed to provide a more general assessment of synthetic accessibility that is not tied to any set of reactions or starting materials.
The training set compounds for this approach are selected from a diverse library based on the number of other similar compounds within the same library.
Both approaches have been shown to perform very well in their corresponding areas of applicability with the RSsvm achieving a receiver operator characteristic score of 0.952 in cross-validation experiments and the DRsvm achieving a score of 0.888 on an independent set of compounds.
Our implementations can successfully process thousands of compounds per minute.


# Citation
```
@article {20100610_podolyan_y_et_al,
  author       = { Yevgeniy Podolyan and Michael A. Walters and George Karypis },
  title        = { Assessing Synthetic Accessibility of Chemical Compounds Using Machine Learning Methods },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2010 },
  pages        = { 979-991 },
  volume       = { 50 },
  number       = { 6 },
  doi          = { 10.1021/ci900301v },
  url          = { https://doi.org/10.1021/ci900301v },
  eprint       = { https://doi.org/10.1021/ci900301v }
}
```
