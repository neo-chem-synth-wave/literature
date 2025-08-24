# Overview
**Title:**
Finding the K Best Synthesis Plans

**Authors:**
Fagerberg, R., Flamm, C., Kianian, R., Merkle, D., and Stadler, P.F. |
Fagerberg, R. et al.

**Publication Date:**
2018/04/05

**Link:**
[BMC Journal of Cheminformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-018-0273-z)

**Alternative Links:**
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC5887019)

**Starred:**
False

**Tags:**
multi-step-synthesis


# Abstract
In synthesis planning, the goal is to synthesize a target molecule from available starting materials, possibly optimizing costs such as price or environmental impact of the process.
Current algorithmic approaches to synthesis planning are usually based on selecting a bond set and finding a single good plan among those induced by it.
We demonstrate that synthesis planning can be phrased as a combinatorial optimization problem on hypergraphs by modeling individual synthesis plans as directed hyperpaths embedded in a hypergraph of reactions (HoR) representing the chemistry of interest.
As a consequence, a polynomial time algorithm to find the K shortest hyperpaths can be used to compute the K best synthesis plans for a given target molecule.
Having K good plans to choose from has many benefits: it makes the synthesis planning process much more robust when in later stages adding further chemical detail, it allows one to combine several notions of cost, and it provides a way to deal with imprecise yield estimates.
A bond set gives rise to a HoR in a natural way.
However, our modeling is not restricted to bond set based approaches—any set of known reactions and starting materials can be used to define a HoR.
We also discuss classical quality measures for synthesis plans, such as overall yield and convergency, and demonstrate that convergency has a built-in inconsistency which could render its use in synthesis planning questionable.
Decalin is used as an illustrative example of the use and implications of our results.


# Citation
```
@article {fagerberg2018a,
  author       = { Rolf Fagerberg and Christoph Flamm and Rojin Kianian and Daniel Merkle and Peter F. Stadler },
  title        = { Finding the K best synthesis plans },
  journal      = { Journal of Cheminformatics },
  year         = { 2018 },
  pages        = { 19 },
  month        = { Apr },
  volume       = { 10 },
  number       = { 1 },
  day          = { 05 },
  issn         = { 1758-2946 },
  doi          = { 10.1186/s13321-018-0273-z },
  url          = { https://doi.org/10.1186/s13321-018-0273-z }
}
```
