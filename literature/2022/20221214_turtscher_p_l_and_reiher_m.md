# Overview
**Title:**
Pathfinder - Navigating and Analyzing Chemical Reaction Networks With an Efficient Graph-Based Approach

**Authors:**
Türtscher, P.L. and Reiher, M.

**Publication Date:**
2022/12/14

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.2c01136)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/2209.04039) |
[GitHub](https://github.com/qcscine) |
[ResearchGate](https://www.researchgate.net/publication/366305226_Pathfinder_Navigating_and_Analyzing_Chemical_Reaction_Networks_with_an_Efficient_Graph-Based_Approach)

**Starred:**
False

**Tags:**
multi-step-synthesis


# Abstract
While the field of first-principles explorations into chemical reaction space has been continuously growing, the development of strategies for analyzing resulting chemical reaction networks (CRNs) is lagging behind.
A CRN consists of compounds linked by reactions.
Analyzing how these compounds are transformed into one another based on kinetic modeling is a nontrivial task.
Here, we present the graph-optimization-driven algorithm and program Pathfinder to allow for such an analysis of a CRN.
The CRN for this work has been obtained with our open-source Chemoton reaction network exploration software.
Chemoton probes reactive combinations of compounds for elementary steps and sorts them into reactions.
By encoding these reactions of the CRN as a graph consisting of compound and reaction vertices and adding information about activation barriers as well as required reagents to the edges of the graph yields a complete graph-theoretical representation of the CRN.
Since the probabilities of the formation of compounds depend on the starting conditions, the consumption of any compound during a reaction must be accounted for to reflect the availability of reagents.
To account for this, we introduce compound costs to reflect compound availability.
Simultaneously, the determined compound costs rank the compounds in the CRN in terms of their probability to be formed.
This ranking then allows us to probe easily accessible compounds in the CRN first for further explorations into yet unexplored terrain.
We first illustrate the working principle on an abstract small CRN.
Afterward, Pathfinder is demonstrated in the example of the disproportionation of iodine with water and the comproportionation of iodic acid and hydrogen iodide.
Both processes are analyzed within the same CRN, which we construct with our autonomous first-principles CRN exploration software Chemoton [Unsleber, J. P.; J. Chem. Theory Comput. 2022, 18, 5393−5409] guided by Pathfinder.


# Citation
```
@article {turtscher2022a,
  author       = { Paul L. Türtscher and Markus Reiher },
  title        = { Pathfinder─Navigating and Analyzing Chemical Reaction Networks with an Efficient Graph-Based Approach },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2023 },
  note         = { PMID: 36515968 },
  pages        = { 147-160 },
  volume       = { 63 },
  number       = { 1 },
  doi          = { 10.1021/acs.jcim.2c01136 },
  url          = { https://doi.org/10.1021/acs.jcim.2c01136 },
  eprint       = { https://doi.org/10.1021/acs.jcim.2c01136 }
}
```
