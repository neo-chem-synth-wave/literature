# Overview
**Title:**
PaRoutes: Towards a Framework for Benchmarking Retrosynthesis Route Predictions

**Authors:**
Genheden, S. and Bjerrum, E.

**Publication Date:**
2022/07/12

**Link:**
[RSC Digital Discovery](https://pubs.rsc.org/en/content/articlelanding/2022/dd/d2dd00015f)

**Alternative Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/621c86f3c3e9da4f737b0047) |
[GitHub](https://github.com/MolecularAI/PaRoutes) |
[ResearchGate](https://www.researchgate.net/publication/361964793_PaRoutes_towards_a_framework_for_benchmarking_retrosynthesis_route_predictions)

**Starred:**
False

**Tags:**
multi-step-retrosynthesis, template-based, pa-routes


# Abstract
We introduce a framework for benchmarking multi-step retrosynthesis methods, i.e. route predictions, called PaRoutes.
The framework consists of two sets of 10,000 synthetic routes extracted from the patent literature, a list of stock compounds, and a curated set of reactions on which one-step retrosynthesis models can be trained.
PaRoutes also comes with scripts to compute route quality and route diversity, quantities that are important for comparing methods.
As an illustration of the framework, we compare three template-based methods implemented in the AiZynthFinder software: Monte Carlo tree search (MCTS), Retro*, and a depth-first proof-number search (DFPN) algorithm.
It is found that DFPN is inferior to both MCTS and Retro* and cannot be recommended in its current implementation.
MCTS and Retro* are on a par with regard to search speed and the ability to find routes in which all starting material is in stock.
However, MCTS outperforms Retro* when it comes to route quality and route diversity.
MCTS more easily recovers the reference routes and tends to find a diverse set of solutions for a greater portion of the targets.
Having showcased the benchmark for template-based methods, we discuss potential issues and caveats needed when adapting the framework for other methods,.e.g., template-free methods or expert systems.
We will continue to update and expand the application of PaRoutes, and we also encourage practitioners and developers to adapt PaRoutes to their algorithms as we envisage that the framework could become the community standard to compare retrosynthesis route predictions.
PaRoutes is available at https://github.com/MolecularAI/PaRoutes.


# Citation
```
@article {genheden2022a,
  author       = { Samuel Genheden and Esben Bjerrum },
  title        = { PaRoutes: towards a framework for benchmarking retrosynthesis route predictions },
  journal      = { Digital Discovery },
  year         = { 2022 },
  pages        = { 527-539 },
  volume       = { 1 },
  issue        = { 4 },
  publisher    = { RSC },
  doi          = { 10.1039/D2DD00015F },
  url          = { https://dx.doi.org/10.1039/D2DD00015F }
}
```
