# Overview
**Title:**
Learning Symmetry-Aware Atom Mapping in Chemical Reactions Through Deep Graph Matching

**Authors:**
Astero, M. and Rousu, J.

**Publication Date:**
2024/04/22

**Link:**
[BMC Journal of Cheminformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-024-00841-0)

**Alternative Links:**
[GitHub](https://github.com/maryamastero/Atom-matching-network) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC11036715) |
[ResearchGate](https://www.researchgate.net/publication/380002503_Learning_symmetry-aware_atom_mapping_in_chemical_reactions_through_deep_graph_matching)

**Starred:**
False

**Tags:**
atom-to-atom-mapping, amnet


# Abstract
Accurate atom mapping, which establishes correspondences between atoms in reactants and products, is a crucial step in analyzing chemical reactions.
In this paper, we present a novel end-to-end approach that formulates the atom mapping problem as a deep graph matching task.
Our proposed model, AMNet (Atom Matching Network), utilizes molecular graph representations and employs various atom and bond features using graph neural networks to capture the intricate structural characteristics of molecules, ensuring precise atom correspondence predictions.
Notably, AMNet incorporates the consideration of molecule symmetry, enhancing accuracy while simultaneously reducing computational complexity.
The integration of the Weisfeiler-Lehman isomorphism test for symmetry identification refines the model's predictions.
Furthermore, our model maps the entire atom set in a chemical reaction, offering a comprehensive approach beyond focusing solely on the main molecules in reactions.
We evaluated AMNet's performance on a subset of USPTO reaction datasets, addressing various tasks, including assessing the impact of molecular symmetry identification, understanding the influence of feature selection on AMNet performance, and comparing its performance with the state-of-the-art method.
The result reveals an average accuracy of 97.3% on mapped atoms, with 99.7% of reactions correctly mapped when the correct mapped atom is within the top 10 predicted atoms.


# Citation
```
@article {astero2024a,
  author       = { Maryam Astero and Juho Rousu },
  title        = { Learning symmetry-aware atom mapping in chemical reactions through deep graph matching },
  journal      = { Journal of Cheminformatics },
  year         = { 2024 },
  pages        = { 46 },
  month        = { Apr },
  volume       = { 16 },
  number       = { 1 },
  day          = { 22 },
  issn         = { 1758-2946 },
  doi          = { 10.1186/s13321-024-00841-0 },
  url          = { https://doi.org/10.1186/s13321-024-00841-0 }
}
```
