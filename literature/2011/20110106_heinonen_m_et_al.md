# Overview
**Title:**
Computing Atom Mappings for Biochemical Reactions Without Subgraph Isomorphism

**Authors:**
Heinonen, M., Lappalainen, S., Mielikäinen, T., and Rousu, J. |
Heinonen, M. et al.

**Publication Date:**
2011/01/06

**Link:**
[Mary Ann Liebert Journal of Computational Biology](https://www.liebertpub.com/doi/10.1089/cmb.2009.0216)

**Alternative Links:**
None

**Tags:**
atom-to-atom-mapping


# Abstract
The ability to trace the fate of individual atoms through the metabolic pathways is needed in many applications of systems biology and drug discovery.
However, this information is not immediately available from the most common metabolome studies and needs to be separately acquired.
Automatic discovery of correspondence of atoms in biochemical reactions is called the "atom mapping problem".
We suggest an efficient approach for solving the atom mapping problem exactly-finding mappings of minimum edge edit distance.
The algorithm is based on A* search equipped with sophisticated heuristics for pruning the search space.
This approach has clear advantages over the commonly used heuristic approach of iterative maximum common subgraph (MCS) algorithm: we explicitly minimize an objective function, and we produce solutions that typically require less manual curation.
The two methods are similar in computational resource demands.
We compare the performance of the proposed algorithm against several alternatives on data obtained from the KEGG LIGAND and RPAIR databases: greedy search, bi-partite graph matching, and the MCS approach.
Our experiments show that alternative approaches often fail in finding mappings with minimum edit distance.


# Citation
```
@article {20110106_heinonen_m_et_al,
  author       = { Markus Heinonen and Sampsa Lappalainen and Taneli Mielikäinen and Juho Rousu },
  title        = { Computing Atom Mappings for Biochemical Reactions without Subgraph Isomorphism },
  journal      = { Journal of Computational Biology },
  year         = { 2011 },
  note         = { PMID: 21210731 },
  pages        = { 43-58 },
  volume       = { 18 },
  number       = { 1 },
  doi          = { 10.1089/cmb.2009.0216 },
  url          = { https://doi.org/10.1089/cmb.2009.0216 },
  eprint       = { https://doi.org/10.1089/cmb.2009.0216 }
}
```
