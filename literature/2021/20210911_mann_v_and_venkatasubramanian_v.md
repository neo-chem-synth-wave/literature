# Overview
**Title:**
Retrosynthesis Prediction Using Grammar-Based Neural Machine Translation: An Information-Theoretic Approach

**Authors:**
Mann, V. and Venkatasubramanian, V.

**Publication Date:**
2021/09/11

**Link:**
[Elsevier Computers and Chemical Engineering](https://www.sciencedirect.com/science/article/abs/pii/S0098135421003112)

**Alternative Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/61270e70fc08e3dd0882aa17) |
[GitHub](https://github.com/vupil/grammarTransformerReactionPrediction) |
[ResearchGate](https://www.researchgate.net/publication/354525382_Retrosynthesis_Prediction_using_Grammar-based_Neural_Machine_Translation_An_Information-Theoretic_Approach)

**Starred:**
False

**Tags:**
single-step-retrosynthesis, template-free


# Abstract
Retrosynthetic prediction is one of the main challenges in chemical synthesis because it requires a search over the space of plausible chemical reactions that often results in complex, multi-step, branched synthesis trees for even moderately complex organic reactions.
Here, we propose an approach that performs single-step retrosynthesis prediction using SMILES grammar-based representations in a neural machine translation framework.
Information-theoretic analyses of such grammar-representations reveal that they are superior to SMILES representations and are better-suited for machine learning tasks due to their underlying redundancy and high information capacity.
We report the top-1 prediction accuracy of 43.8% (syntactic validity 95.6%) and maximal fragment (MaxFrag) accuracy of 50.4%.
Comparing our model’s performance with previous work that used character-based SMILES representations demonstrate significant reduction in grammatically invalid predictions and improved prediction accuracy.
Fewer invalid predictions for both known and unknown reaction class scenarios demonstrate the model’s ability to learn the underlying SMILES grammar efficiently.


# Citation
```
@article {mann2021a,
  author       = { Vipul Mann and Venkat Venkatasubramanian },
  title        = { Retrosynthesis prediction using grammar-based neural machine translation: An information-theoretic approach },
  journal      = { Computers & Chemical Engineering },
  year         = { 2021 },
  pages        = { 107533 },
  volume       = { 155 },
  issn         = { 0098-1354 },
  doi          = { https://doi.org/10.1016/j.compchemeng.2021.107533 },
  url          = { https://www.sciencedirect.com/science/article/pii/S0098135421003112 }
}
```
