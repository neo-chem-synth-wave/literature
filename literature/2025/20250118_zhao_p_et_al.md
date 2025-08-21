# Overview
**Title:**
Single-Step Retrosynthesis Prediction via Multitask Graph Representation Learning

**Authors:**
Zhao, P., Wei, X., Wang, Q., Wang, Q., Li, J., Shang, J., Lu, C., and Shi, J. |
Zhao, P. et al.

**Publication Date:**
2025/01/18

**Link:**
[Nature Communications](https://www.nature.com/articles/s41467-025-56062-y)

**Alternative Links:**
[GitHub](https://github.com/zpczaizheli/Retro-MTGR) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC11742932) |
[ResearchGate](https://www.researchgate.net/publication/370370868_Single-step_retrosynthesis_prediction_by_leveraging_commonly_preserved_substructures) |
[ResearchGate (Pre-print)](https://www.researchgate.net/publication/373725811_Retro-MTGR_Molecule_Retrosynthesis_Prediction_via_Multi-Task_Graph_Representation_Learning) |
[ResearchSquare](https://www.researchsquare.com/article/rs-3205328/v1)

**Starred:**
False

**Tags:**
single-step-retrosynthesis, retro-mtgr


# Abstract
Inferring appropriate synthesis reaction (i.e., retrosynthesis) routes for newly designed molecules is vital.
Recently, computational methods have produced promising single-step retrosynthesis predictions.
However, template-based methods are limited by the known synthesis templates; template-free methods are weakly interpretable; and semi template-based methods are deficient with regard to utilizing the associations between chemical entities.
To address these issues, this paper leverages the intra-associations between synthons, the inter-associations between synthons and leaving groups (LGs), and the intra-associations between LGs.
It develops a multitask graph representation learning model for single-step retrosynthesis prediction (Retro-MTGR) to solve reaction centre deduction and LG identification simultaneously.
A comparison with 16 state-of-the-art methods first demonstrates the superiority of Retro-MTGR.
Then, its robustness and scalability and the contributions of its crucial components are validated.
More importantly, it can determine whether a bond can be a reaction centre and what LGs are appropriate for a given synthon, respectively.
The answers reflect underlying chemical synthesis rules, especially opposite electrical properties between chemical entities (e.g., reaction sites, synthons, and LGs).
Finally, case studies demonstrate that the retrosynthesis routes inferred by Retro-MTGR are promising for single-step synthesis reactions.
The code and data of this study are freely available at https://doi.org/10.5281/zenodo.14346324.


# Citation
```
@article {zhao2025,
  author       = { Peng-Cheng Zhao and Xue-Xin Wei and Qiong Wang and Qi-Hao Wang and Jia-Ning Li and Jie Shang and Cheng Lu and Jian-Yu Shi },
  title        = { Single-step retrosynthesis prediction via multitask graph representation learning },
  journal      = { Nature Communications },
  year         = { 2025 },
  pages        = { 814 },
  month        = { Jan },
  volume       = { 16 },
  number       = { 1 },
  day          = { 18 },
  issn         = { 2041-1723 },
  doi          = { 10.1038/s41467-025-56062-y },
  url          = { https://doi.org/10.1038/s41467-025-56062-y }
}
```
