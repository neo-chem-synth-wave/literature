# Overview
**Title:**
A Data-Driven Group Retrosynthesis Planning Model Inspired by Neurosymbolic Programming

**Authors:**
Zhang, X., Lin, H., Zhang, M., Zhou, Y., and Ma, J. |
Zhang, X. et al.

**Publication Date:**
2025/01/02

**Link:**
[Nature Communications](https://www.nature.com/articles/s41467-024-55374-9)

**Alternative Links:**
[GitHub](https://github.com/osu-zxf/DreamRetroer) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC11695995)

**Starred:**
False

**Tags:**
single-step-retrosynthesis, multi-step-retrosynthesis


# Abstract
Deep generative models have garnered significant attention for their efficiency in drug discovery, yet the synthesis of proposed molecules remains a challenge.
Retrosynthetic planning, a part of computer-assisted synthesis planning, addresses this challenge by recursively decomposing molecules using symbolic rules and machine-trained scoring functions.
However, current methods often treat each molecule independently, missing the opportunity to utilize shared synthesis patterns and repeat pathways, which may contribute from known synthesis routes to newly emerging, similar molecules, a notable challenge with AI-generated small molecules.
Our investigation reveals reusable synthesis patterns that augment the reaction template library, resulting in progressively decreasing marginal inference time as the algorithm processes more molecules.
Nevertheless, expanding the library enlarges the search space, necessitating investigation into methods for effectively prediction of reactions in retrosynthesis search.
Inspired by human learning, our algorithm, akin to neurosymbolic programming, builds upon commonly used multi-step concepts such as cascade and complementary reactions and can evolve from practical experiences, enhancing the prediction model for fundamental and compositional reaction templates.
The evolutionary process involves wake, abstraction, and dreaming phases, alternatively extending the reaction template library and refining models for more efficient retrosynthesis.
Our algorithm outperforms existing methods, discovers chemistry patterns, and significantly reduces inference time in retrosynthetic planning for a group of similar molecules, showcasing its potential in validating results from generative models.


# Citation
```
@article {zhang2025a,
  author       = { Xuefeng Zhang and Haowei Lin and Muhan Zhang and Yuan Zhou and Jianzhu Ma },
  title        = { A data-driven group retrosynthesis planning model inspired by neurosymbolic programming },
  journal      = { Nature Communications },
  year         = { 2025 },
  pages        = { 192 },
  month        = { Jan },
  volume       = { 16 },
  number       = { 1 },
  day          = { 02 },
  issn         = { 2041-1723 },
  doi          = { 10.1038/s41467-024-55374-9 },
  url          = { https://doi.org/10.1038/s41467-024-55374-9 }
}
```
