# Overview
**Title:**
Investigations into the Efficiency of Computer-Aided Synthesis Planning

**Authors:**
Hartog, P.B.R., and Westerlund, A.M., Tetko, I.V., and Genheden, S. |
Hartog, P.B.R. et al.

**Publication Date:**
2025/01/31

**Link:**
[ACS Journal of Medicinal Chemistry](https://pubs.acs.org/doi/10.1021/acs.jcim.4c01821)

**Alternative Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/67078fc2cec5d6c142c33dfc) |
[GitHub](https://github.com/PeterHartog/fast-retro) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC11863376)

**Starred:**
False

**Tags:**
single-step-retrosynthesis, multi-step-retrosynthesis, fast-retro


# Abstract
The efficiency of machine learning (ML) models is crucial to minimize inference times and reduce the carbon footprints of models deployed in production environments.
Current models employed in retrosynthesis to generate a synthesis route from a target molecule to purchasable compounds are prohibitively slow.
The model operates in a single-step fashion in a tree search algorithm by predicting reactant molecules given a product molecule as input.
In this study, we investigate the ability of alternative transformer architectures, knowledge distillation (KD), and simple hyper-parameter optimization to decrease inference times of the Chemformer model.
Initially, we assess the ability of closely related transformer architectures and conclude that these models under-performed when using KD.
Additionally, we investigate the effects of feature-based and response-based KD together with hyper-parameters optimized based on inference sample time and model accuracy.
We find that although reducing model size and improving single-step speed are important, our results indicate that multi-step search efficiency is more significantly influenced by the diversity and confidence of single-step models.
Based on this work, further research should use KD in combination with other techniques, as multi-step speed continues to prevent proper integration of synthesis planning.
However, in Monte Carlo-based (MC) multi-step retrosynthesis, other factors play a crucial role in balancing exploration and exploitation during the search process, often outweighing the direct impact of single-step model speed and carbon footprints.


# Citation
```
@article {hartog2025a,
  author       = { Peter B.R. Hartog and Annie M. Westerlund and Igor V. Tetko and Samuel Genheden },
  title        = { Investigations into the Efficiency of Computer-Aided Synthesis Planning },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2025 },
  note         = { PMID: 39889203 },
  pages        = { 1771-1781 },
  volume       = { 65 },
  number       = { 4 },
  doi          = { 10.1021/acs.jcim.4c01821 },
  url          = { https://doi.org/10.1021/acs.jcim.4c01821 },
  eprint       = { https://doi.org/10.1021/acs.jcim.4c01821 }
}
```
