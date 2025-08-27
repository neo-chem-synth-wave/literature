# Overview
**Title:**
ReactionMap: An Efficient Atom-Mapping Algorithm for Chemical Reactions

**Authors:**
Fooshee, D., Andronico, A., and Baldi, P. |
Fooshee, D. et al.

**Publication Date:**
2013/10/25

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/ci400326p)

**Alternative Links:**
[ChemDB Chemoinformatics Portal](https://cdb.ics.uci.edu)

**Starred:**
False

**Tags:**
atom-to-atom-mapping, reaction-map


# Abstract
Large databases of chemical reactions provide new data-mining opportunities and challenges.
Key challenges result from the imperfect quality of the data and the fact that many of these reactions are not properly balanced or atom-mapped.
Here, we describe ReactionMap, an efficient atom-mapping algorithm.
Our approach uses a combination of maximum common chemical subgraph search and minimization of an assignment cost function derived empirically from training data.
We use a set of over 259,000 balanced atom-mapped reactions from the SPRESI commercial database to train the system, and we validate it on random sets of 1000 and 17,996 reactions sampled from this pool.
These large test sets represent a broad range of chemical reaction types, and ReactionMap correctly maps about 99% of the atoms and about 96% of the reactions, with a mean time per mapping of 2 s.
Most correctly mapped reactions are mapped with high confidence.
Mapping accuracy compares favorably with ChemAxon’s AutoMapper, versions 5 and 6.1, and the DREAM Web tool.
These approaches correctly map 60.7%, 86.5%, and 90.3% of the reactions, respectively, on the same data set.
A ReactionMap server is available on the ChemDB Web portal at http://cdb.ics.uci.edu.


# Citation
```
@article {fooshee2013a,
  author       = { David Fooshee and Alessio Andronico and Pierre Baldi },
  title        = { ReactionMap: An Efficient Atom-Mapping Algorithm for Chemical Reactions },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2013 },
  note         = { PMID: 24160861 },
  pages        = { 2812-2819 },
  volume       = { 53 },
  number       = { 11 },
  doi          = { 10.1021/ci400326p },
  url          = { https://doi.org/10.1021/ci400326p },
  eprint       = { https://doi.org/10.1021/ci400326p }
}
```
