# Overview
**Title:**
AiZynthTrain: Robust, Reproducible, and Extensible Pipelines for Training Synthesis Prediction Models

**Authors:**
Genheden, S., Norrby, P.O., and Engkvist, O.

**Publication Date:**
2023/03/23

**Publication Link:**
[ACS JCIM](https://pubs.acs.org/doi/10.1021/acs.jcim.2c01486)

**Alternative Publication Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/6380bd380949e12fc255cfea) |
[ResearchGate](https://www.researchgate.net/publication/365796363_AiZynthTrain_robust_reproducible_and_extensible_pipelines_for_training_synthesis_prediction_models) |
[Official GitHub Repository](https://github.com/MolecularAI/aizynthtrain)


# Abstract
We introduce the AiZynthTrain Python package for training synthesis models in a robust, reproducible, and extensible way. 
It contains two pipelines that create a template-based one-step retrosynthesis model and a RingBreaker model that can be straightforwardly integrated in retrosynthesis software. 
We train such models on the publicly available reaction data set from the U.S. Patent and Trademark Office (USPTO), and these are the first retrosynthesis models created in a completely reproducible end-to-end fashion, starting with the original reaction data source and ending with trained machine-learning models. 
In particular, we show that employing new heuristics implemented in the pipeline greatly improves the ability of the RingBreaker model for disconnecting ring systems. 
Furthermore, we demonstrate the robustness of the pipeline by training on a more diverse but proprietary data set. 
We envisage that this framework will be extended with other synthesis models in the future.


# Citation
```
@article {genheden2023,
  author       = { Samuel Genheden and Per-Ola Norrby and Ola Engkvist },
  title        = { AiZynthTrain: Robust, Reproducible, and Extensible Pipelines for Training Synthesis Prediction Models },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2023 },
  note         = { PMID: 36959737 },
  pages        = { 1841-1846 },
  volume       = { 63 },
  number       = { 7 },
  doi          = { 10.1021/acs.jcim.2c01486 },
  url          = { https://doi.org/10.1021/acs.jcim.2c01486 },
  eprint       = { https://doi.org/10.1021/acs.jcim.2c01486 }
}
```
