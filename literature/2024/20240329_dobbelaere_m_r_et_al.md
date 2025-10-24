# Overview
**Title:**
Rxn-INSIGHT: Fast Chemical Reaction Analysis Using Bond-Electron Matrices

**Authors:**
Dobbelaere, M.R., Lengyel, I., Stevens, C.V., Van Geem, K.M. |
Dobbelaere, M.R. et al.

**Publication Date:**
2024/03/29

**Link:**
[BMC Journal of Cheminformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-024-00834-z)

**Alternative Links:**
[GitHub](https://github.com/mrodobbe/Rxn-INSIGHT) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC10980627) |
[ResearchGate](https://www.researchgate.net/publication/379407518_Rxn-INSIGHT_fast_chemical_reaction_analysis_using_bond-electron_matrices)

**Tags:**
reaction-analysis, rxn-insight


# Abstract
The challenge of devising pathways for organic synthesis remains a central issue in the field of medicinal chemistry.
Over the span of six decades, computer-aided synthesis planning has given rise to a plethora of potent tools for formulating synthetic routes.
Nevertheless, a significant expert task still looms: determining the appropriate solvent, catalyst, and reagents when provided with a set of reactants to achieve and optimize the desired product for a specific step in the synthesis process.
Typically, chemists identify key functional groups and rings that exert crucial influences at the reaction center, classify reactions into categories, and may assign them names.
This research introduces Rxn-INSIGHT, an open-source algorithm based on the bond-electron matrix approach, with the purpose of automating this endeavor.
Rxn-INSIGHT not only streamlines the process but also facilitates extensive querying of reaction databases, effectively replicating the thought processes of an organic chemist.
The core functions of the algorithm encompass the classification and naming of reactions, extraction of functional groups, rings, and scaffolds from the involved chemical entities.
The provision of reaction condition recommendations based on the similarity and prevalence of reactions eventually arises as a side application.
The performance of our rule-based model has been rigorously assessed against a carefully curated benchmark dataset, exhibiting an accuracy rate exceeding 90% in reaction classification and surpassing 95% in reaction naming.
Notably, it has been discerned that a pivotal factor in selecting analogous reactions lies in the analysis of ring structures participating in the reactions.
An examination of ring structures within the USPTO chemical reaction database reveals that with just 35 unique rings, a remarkable 75% of all rings found in nearly 1 million products can be encompassed.
Furthermore, Rxn-INSIGHT is proficient in suggesting appropriate choices for solvents, catalysts, and reagents in entirely novel reactions, all within the span of a second, utilizing nothing more than an everyday laptop.


# Citation
```
@article {20240329_dobbelaere_m_r_et_al,
  author       = { Maarten R. Dobbelaere and István Lengyel and Christian V. Stevens and Kevin M. Van Geem },
  title        = { Rxn-INSIGHT: fast chemical reaction analysis using bond-electron matrices },
  journal      = { Journal of Cheminformatics },
  year         = { 2024 },
  pages        = { 37 },
  month        = { Mar },
  volume       = { 16 },
  number       = { 1 },
  day          = { 29 },
  issn         = { 1758-2946 },
  doi          = { 10.1186/s13321-024-00834-z },
  url          = { https://doi.org/10.1186/s13321-024-00834-z }
}
```
