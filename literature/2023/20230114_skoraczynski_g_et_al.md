# Overview
**Title:**
Critical Assessment of Synthetic Accessibility Scores in Computer-Assisted Synthesis Planning

**Authors:**
Skoraczyński, G., Kitlas, M., Miasojedow, B., and Gambin, A. |
Skoraczyński, G. et al.

**Publication Date:**
2023/01/14

**Link:**
[BMC Journal of Cheminformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-023-00678-z)

**Alternative Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/6366a53fecdad5512dfbd055) |
[GitHub](https://github.com/grzsko/ASAP) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC9840255) |
[ResearchGate](https://www.researchgate.net/publication/367149981_Critical_assessment_of_synthetic_accessibility_scores_in_computer-assisted_synthesis_planning)

**Tags:**
synthesizability, synthetic-accessibility, analysis


# Abstract
Modern computer-assisted synthesis planning tools provide strong support for this problem. However, they are still limited by computational complexity.
This limitation may be overcome by scoring the synthetic accessibility as a pre-retrosynthesis heuristic.
A wide range of machine learning scoring approaches is available, however, their applicability and correctness were studied to a limited extent.
Moreover, there is a lack of critical assessment of synthetic accessibility scores with common test conditions.
In the present work, we assess if synthetic accessibility scores can reliably predict the outcomes of retrosynthesis planning.
Using a specially prepared compounds database, we examine the outcomes of the retrosynthetic tool AiZynthFinder.
We test whether synthetic accessibility scores: SAscore, SYBA, SCScore, and RAscore accurately predict the results of retrosynthesis planning.
Furthermore, we investigate if synthetic accessibility scores can speed up retrosynthesis planning by better prioritizing explored partial synthetic routes and thus reducing the size of the search space.
For that purpose, we analyze the AiZynthFinder partial solutions search trees, their structure, and complexity parameters, such as the number of nodes, or treewidth.
We confirm that synthetic accessibility scores in most cases well discriminate feasible molecules from infeasible ones and can be potential boosters of retrosynthesis planning tools.
Moreover, we show the current challenges of designing computer-assisted synthesis planning tools.
We conclude that hybrid machine learning and human intuition-based synthetic accessibility scores can efficiently boost the effectiveness of computer-assisted retrosynthesis planning, however, they need to be carefully crafted for retrosynthesis planning algorithms.
The source code of this work is publicly available at https://github.com/grzsko/ASAP.


# Citation
```
@article {20230114_skoraczynski_g_et_al,
  author       = { Grzegorz Skoraczyński and Mateusz Kitlas and Błażej Miasojedow and Anna Gambin },
  title        = { Critical assessment of synthetic accessibility scores in computer-assisted synthesis planning },
  journal      = { Journal of Cheminformatics },
  year         = { 2023 },
  pages        = { 6 },
  month        = { Jan },
  volume       = { 15 },
  number       = { 1 },
  day          = { 14 },
  issn         = { 1758-2946 },
  doi          = { 10.1186/s13321-023-00678-z },
  url          = { https://doi.org/10.1186/s13321-023-00678-z }
}
```
