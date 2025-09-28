# Overview
**Title:**
Global Reactivity Models Are Impactful in Industrial Synthesis Applications

**Authors:**
Neves, P., McClure, K., Verhoeven, J., Dyubankova, N., Nugmanov, R., Gedich, A., Menon, S., Shi, Z., and Wegner, J.K. |
Neves, P. et al.

**Publication Date:**
2023/02/11

**Link:**
[BMC Journal of Cheminformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-023-00685-0)

**Alternative Links:**
[BMC Journal of Cheminformatics Correction](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-023-00705-z) |
[GitHub](https://github.com/PauloNeves-Git/BEE) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC9921076) |
[ResearchGate](https://www.researchgate.net/publication/364208399_Global_Reactivity_Models_are_Impactful_in_Industrial_Synthesis_Applications)

**Tags:**
other


# Abstract
Artificial Intelligence is revolutionizing many aspects of the pharmaceutical industry.
Deep learning models are now routinely applied to guide drug discovery projects leading to faster and improved findings, but there are still many tasks with enormous unrealized potential.
One such task is the reaction yield prediction.
Every year more than one fifth of all synthesis attempts result in product yields which are either zero or too low.
This equates to chemical and human resources being spent on activities which ultimately do not progress the programs, leading to a triple loss when accounting for the cost of opportunity in time wasted.
In this work we pre-train a BERT model on more than 16 million reactions from 4 different data sources, and fine tune it to achieve an uncertainty calibrated global yield prediction model.
This model is an improvement upon state of the art not just from the increase in pre-train data but also by introducing a new embedding layer which solves a few limitations of SMILES and enables integration of additional information such as equivalents and molecule role into the reaction encoding, the model is called BERT Enriched Embedding (BEE).
The model is benchmarked on an open-source dataset against a state-of-the-art synthesis focused BERT showing a near 20-point improvement in r2 score.
The model is fine-tuned and tested on an internal company data benchmark, and a prospective study shows that the application of the model can reduce the total number of negative reactions (yield under 5%) ran in Janssen by at least 34%.
Lastly, we corroborate the previous results through experimental validation, by directly deploying the model in an ongoing drug discovery project and showing that it can also be used successfully as a reagent recommender due to its fast inference speed and reliable confidence estimation, a critical feature for industry application.


# Citation
```
@article {20230211_neves_p_et_al,
  author       = { Paulo Neves and Kelly McClure and Jonas Verhoeven and Natalia Dyubankova and Ramil Nugmanov and Andrey Gedich and Sairam Menon and Zhicai Shi and J{\"o}rg K. Wegner },
  title        = { Global reactivity models are impactful in industrial synthesis applications },
  journal      = { Journal of Cheminformatics },
  year         = { 2023 },
  pages        = { 20 },
  month        = { Feb },
  volume       = { 15 },
  number       = { 1 },
  day          = { 11 },
  issn         = { 1758-2946 },
  doi          = { 10.1186/s13321-023-00685-0 },
  url          = { https://doi.org/10.1186/s13321-023-00685-0 }
}
```
