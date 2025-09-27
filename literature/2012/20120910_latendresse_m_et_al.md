# Overview
**Title:**
Accurate Atom-Mapping Computation for Biochemical Reactions

**Authors:**
Latendresse, M., Malerich, J.P., Travers, M., and Karp, P.D. |
Latendresse, M. et al.

**Publication Date:**
2012/09/10

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/ci3002217)

**Alternative Links:**
None

**Tags:**
atom-to-atom-mapping


# Abstract
The complete atom mapping of a chemical reaction is a bijection of the reactant atoms to the product atoms that specifies the terminus of each reactant atom.
Atom mapping of biochemical reactions is useful for many applications of systems biology, in particular for metabolic engineering where synthesizing new biochemical pathways has to take into account for the number of carbon atoms from a source compound that are conserved in the synthesis of a target compound.
Rapid, accurate computation of the atom mapping(s) of a biochemical reaction remains elusive despite significant work on this topic.
In particular, past researchers did not validate the accuracy of mapping algorithms.
We introduce a new method for computing atom mappings called the minimum weighted edit-distance (MWED) metric.
The metric is based on bond propensity to react and computes biochemically valid atom mappings for a large percentage of biochemical reactions.
MWED models can be formulated efficiently as Mixed-Integer Linear Programs (MILPs).
We have demonstrated this approach on 7501 reactions of the MetaCyc database for which 87% of the models could be solved in less than 10 s.
For 2.1% of the reactions, we found multiple optimal atom mappings.
We show that the error rate is 0.9% (22 reactions) by comparing these atom mappings to 2446 atom mappings of the manually curated Kyoto Encyclopedia of Genes and Genomes (KEGG) RPAIR database.
To our knowledge, our computational atom-mapping approach is the most accurate and among the fastest published to date.
The atom-mapping data will be available in the MetaCyc database later in 2012; the atom-mapping software will be available within the Pathway Tools software later in 2012.


# Citation
```
@article {20120910_latendresse_m_et_al,
  author       = { Mario Latendresse and Jeremiah P. Malerich and Mike Travers and Peter D. Karp },
  title        = { Accurate Atom-Mapping Computation for Biochemical Reactions },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2012 },
  note         = { PMID: 22963657 },
  pages        = { 2970-2982 },
  volume       = { 52 },
  number       = { 11 },
  doi          = { 10.1021/ci3002217 },
  url          = { https://doi.org/10.1021/ci3002217 },
  eprint       = { https://doi.org/10.1021/ci3002217 }
}
```
