# Overview
**Title:**
Incorporating Synthetic Accessibility in Drug Design: Predicting Reaction Yields of Suzuki Cross-Couplings by Leveraging AbbVie's 15-Year Parallel Library Data Set

**Authors:**
Raghavan, P., Rago, A.J., Verma, P., Hassan, M.M., Goshu, G.M., Dombrowski, A.W., Pandey, A., Coley, C.W., and Wang, Y. |
Raghavan, P. et al.

**Publication Date:**
2024/05/20

**Link:**
[ACS JACS](https://pubs.acs.org/doi/10.1021/jacs.4c00098)

**Alternative Links:**
[DSpace@MIT](https://dspace.mit.edu/handle/1721.1/158164) |
[GitHub](https://github.com/priyanka-rag/suzuki_yield_predict_external) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC11157529)

**Starred:**
False

**Tags:**
synthesizability, synthetic-accessibility


# Abstract
Despite the increased use of computational tools to supplement medicinal chemists’ expertise and intuition in drug design, predicting synthetic yields in medicinal chemistry endeavors remains an unsolved challenge.
Existing design workflows could profoundly benefit from reaction yield prediction, as precious material waste could be reduced, and a greater number of relevant compounds could be delivered to advance the design, make, test, analyze (DMTA) cycle.
In this work, we detail the evaluation of AbbVie’s medicinal chemistry library data set to build machine learning models for the prediction of Suzuki coupling reaction yields.
The combination of density functional theory (DFT)-derived features and Morgan fingerprints was identified to perform better than one-hot encoded baseline modeling, furnishing encouraging results.
Overall, we observe modest generalization to unseen reactant structures within the 15-year retrospective library data set.
Additionally, we compare predictions made by the model to those made by expert medicinal chemists, finding that the model can often predict both reaction success and reaction yields with greater accuracy.
Finally, we demonstrate the application of this approach to suggest structurally and electronically similar building blocks to replace those predicted or observed to be unsuccessful prior to or after synthesis, respectively.
The yield prediction model was used to select similar monomers predicted to have higher yields, resulting in greater synthesis efficiency of relevant drug-like molecules.


# Citation
```
@article {raghavan2024a,
  author       = { Priyanka Raghavan and Alexander J. Rago and Pritha Verma and Majdi M. Hassan and Gashaw M. Goshu and Amanda W. Dombrowski and Abhishek Pandey and Connor W. Coley and Ying Wang },
  title        = { Incorporating Synthetic Accessibility in Drug Design: Predicting Reaction Yields of Suzuki Cross-Couplings by Leveraging AbbVie’s 15-Year Parallel Library Data Set },
  journal      = { Journal of the American Chemical Society },
  year         = { 2024 },
  note         = { PMID: 38768950 },
  pages        = { 15070-15084 },
  volume       = { 146 },
  number       = { 22 },
  doi          = { 10.1021/jacs.4c00098 },
  url          = { https://doi.org/10.1021/jacs.4c00098 },
  eprint       = { https://doi.org/10.1021/jacs.4c00098 }
}
```
