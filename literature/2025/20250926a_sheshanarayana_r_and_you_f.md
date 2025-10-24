# Overview
**Title:**
Rethinking Retrosynthesis: Curriculum Learning Reshapes Transformer-Based Small-Molecule Reaction Prediction

**Authors:**
Sheshanarayana, R. and You, F.

**Publication Date:**
2025/09/26

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.5c01508)

**Alternative Links:**
None

**Tags:**
single-step-retrosynthesis


# Abstract
Retrosynthesis prediction remains a central challenge in computational chemistry, particularly when models must generalize to rare or structurally complex reactions.
We present a curriculum learning (CL) framework that reshapes model training by systematically controlling reaction difficulty during learning, directly addressing the challenge of chemical generalization.
In contrast to conventional generative approaches that treat all training reactions uniformly, our method introduces reactions in a chemically informed progression, gradually exposing the model to increasingly complex transformations based on synthetic accessibility, ring complexity, and molecular size.
This difficulty-aware pacing allows the model to better capture reaction conditionality, preserve chemical plausibility, and avoid failure modes commonly observed in rare or underrepresented transformations.
Applied across three transformer-based architectures─ChemBERTa + DistilGPT2, ReactionT5v2, and BART─the framework yields substantial performance gains.
Notably, the largest improvements are observed in the BART model, which lacks any chemical domain pretraining: CL improves its top-1 accuracy from 27.0% to 75.9% (+48.9%).
The remainder of our evaluations use ChemBERTa + DistilGPT2 as a representative pretrained model.
In low-data regimes with only 50% of the training data, CL increases top-1 accuracy from 16.9% to 46.6% (+29.7%).
Under scaffold-based splits, CL improves top-1 accuracy by up to 29%, and in structurally dissimilar settings (Tanimoto similarity <0.4), CL boosts top-1 accuracy from 18.2% to 69.4% (+51.2%), demonstrating strong robustness to distributional shifts.
These improvements are achieved without auxiliary labels, templates, or reaction class supervision.
Looking forward, this CL framework may aid retrosynthetic route planning for pharmaceutical intermediates, catalysts, polymers, and functional materials.


# Citation
```
@article {20250926a_sheshanarayana_r_and_you_f,
  author       = { Rahul Sheshanarayana and Fengqi You },
  title        = { Rethinking Retrosynthesis: Curriculum Learning Reshapes Transformer-Based Small-Molecule Reaction Prediction },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 0 },
  note         = { PMID: 41001729 },
  pages        = { null },
  volume       = { 0 },
  number       = { 0 },
  doi          = { 10.1021/acs.jcim.5c01508 },
  url          = { https://doi.org/10.1021/acs.jcim.5c01508 },
  eprint       = { https://doi.org/10.1021/acs.jcim.5c01508 }
}
```
