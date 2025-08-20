# Overview
**Title:**
Machine Learning in Computer-Aided Synthesis Planning

**Authors:**
Coley, C.W., Green, W.H., and Jensen, K.F. |
Coley, C.W. et al.

**Publication Date:**
2018/05/01

**Link:**
[ACS Accounts of Chemical Research](https://pubs.acs.org/doi/10.1021/acs.accounts.8b00087)

**Alternative Links:**
None

**Starred:**
False

**Tags:**
single-step-synthesis, multi-step-synthesis, single-step-retrosynthesis, multi-step-retrosynthesis


# Abstract
Computer-aided synthesis planning (CASP) is focused on the goal of accelerating the process by which chemists decide how to synthesize small molecule compounds.
The ideal CASP program would take a molecular structure as input and output a sorted list of detailed reaction schemes that each connect that target to purchasable starting materials via a series of chemically feasible reaction steps.
Early work in this field relied on expert-crafted reaction rules and heuristics to describe possible retrosynthetic disconnections and selectivity rules but suffered from incompleteness, infeasible suggestions, and human bias.
With the relatively recent availability of large reaction corpora (such as the United States Patent and Trademark Office (USPTO), Reaxys, and SciFinder databases), consisting of millions of tabulated reaction examples, it is now possible to construct and validate purely data-driven approaches to synthesis planning.
As a result, synthesis planning has been opened to machine learning techniques, and the field is advancing rapidly.

In this Account, we focus on two critical aspects of CASP and recent machine learning approaches to both challenges.
First, we discuss the problem of retrosynthetic planning, which requires a recommender system to propose synthetic disconnections starting from a target molecule.
We describe how the search strategy, necessary to overcome the exponential growth of the search space with increasing number of reaction steps, can be assisted through a learned synthetic complexity metric.
We also describe how the recursive expansion can be performed by a straightforward nearest neighbor model that makes clever use of reaction data to generate high quality retrosynthetic disconnections.
Second, we discuss the problem of anticipating the products of chemical reactions, which can be used to validate proposed reactions in a computer-generated synthesis plan (i.e., reduce false positives) to increase the likelihood of experimental success.
While we introduce this task in the context of reaction validation, its utility extends to the prediction of side products and impurities, among other applications.
We describe neural network-based approaches that we and others have developed for this forward prediction task that can be trained on previously published experimental data.

Machine learning and artificial intelligence have revolutionized a number of disciplines, not limited to image recognition, dictation, translation, content recommendation, advertising, and autonomous driving.
While there is a rich history of using machine learning for structure–activity models in chemistry, it is only now that it is being successfully applied more broadly to organic synthesis and synthesis design.
As reported in this Account, machine learning is rapidly transforming CASP, but there are several remaining challenges and opportunities, many pertaining to the availability and standardization of both data and evaluation metrics, which must be addressed by the community at large.


# Citation
```
@article {coley2018b,
  author       = { Connor Coley W. and William H. Green and Klavs F. Jensen },
  title        = { Machine Learning in Computer-Aided Synthesis Planning },
  journal      = { Accounts of Chemical Research },
  year         = { 2018 },
  note         = { PMID: 29715002 },
  pages        = { 1281-1289 },
  volume       = { 51 },
  number       = { 5 },
  doi          = { 10.1021/acs.accounts.8b00087 },
  url          = { https://doi.org/10.1021/acs.accounts.8b00087 },
  eprint       = { https://doi.org/10.1021/acs.accounts.8b00087 }
}
```
