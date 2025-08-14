# Overview
**Title:**
SCScore: Synthetic Complexity Learned from a Reaction Corpus

**Authors:**
Coley, C.W., Rogers, L., Green, W.H., and Jensen, K.F.

**Publication Date:**
2018/01/08

**Publication Link:**
[ACS JCIM](https://pubs.acs.org/doi/10.1021/acs.jcim.7b00622)

**Alternative Publication Links:**
[Official GitHub Repository](https://github.com/connorcoley/scscore)

# Abstract
Several definitions of molecular complexity exist to facilitate prioritization of lead compounds, to identify diversity-inducing and complexifying reactions, and to guide retrosynthetic searches. In this work, we focus on synthetic complexity and reformalize its definition to correlate with the expected number of reaction steps required to produce a target molecule, with implicit knowledge about what compounds are reasonable starting materials. 
We train a neural network model on 12 million reactions from the Reaxys database to impose a pairwise inequality constraint enforcing the premise of this definition: that on average, the products of published chemical reactions should be more synthetically complex than their corresponding reactants. 
The learned metric (SCScore) exhibits highly desirable nonlinear behavior, particularly in recognizing increases in synthetic complexity throughout a number of linear synthetic routes.


# Citation
```
@article{coley2018,
  author = "Coley, Connor W. and Rogers, Luke and Green, William H. and Jensen, Klavs F.",
  title = "SCScore: Synthetic Complexity Learned from a Reaction Corpus",
  journal = "Journal of Chemical Information and Modeling",
  volume = "58",
  number = "2",
  pages = "252-261",
  year = "2018",
  doi = "10.1021/acs.jcim.7b00622",
  note = "PMID: 29309147",
  URL = "https://doi.org/10.1021/acs.jcim.7b00622",
  eprint = "https://doi.org/10.1021/acs.jcim.7b00622"
}
```

