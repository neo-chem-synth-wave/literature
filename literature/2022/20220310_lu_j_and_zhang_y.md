# Overview
**Title:**
Unified Deep Learning Model for Multitask Reaction Predictions With Explanation

**Authors:**
Lu, J. and Zhang, Y.

**Publication Date:**
2022/03/10

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.1c01467)

**Alternative Links:**
[GitHub](https://github.com/HelloJocelynLu/t5chem) |
[Multi-task Reaction Predictions](https://yzhang.hpc.nyu.edu/T5Chem) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC8960360)

**Tags:**
multi-task, template-free, t5-chem


# Abstract
There is significant interest and importance to develop robust machine learning models to assist organic chemistry synthesis.
Typically, task-specific machine learning models for distinct reaction prediction tasks have been developed.
In this work, we develop a unified deep learning model, T5Chem, for a variety of chemical reaction predictions tasks by adapting the "Text-to-Text Transfer Transformer" (T5) framework in natural language processing (NLP).
On the basis of self-supervised pretraining with PubChem molecules, the T5Chem model can achieve state-of-the-art performances for four distinct types of task-specific reaction prediction tasks using four different open-source data sets, including reaction type classification on USPTO_TPL, forward reaction prediction on USPTO_MIT, single-step retrosynthesis on USPTO_50k, and reaction yield prediction on high-throughput C–N coupling reactions.
Meanwhile, we introduced a new unified multitask reaction prediction data set USPTO_500_MT, which can be used to train and test five different types of reaction tasks, including the above four as well as a new reagent suggestion task.
Our results showed that models trained with multiple tasks are more robust and can benefit from mutual learning on related tasks.
Furthermore, we demonstrated the use of SHAP (SHapley Additive exPlanations) to explain T5Chem predictions at the functional group level, which provides a way to demystify sequence-based deep learning models in chemistry.
T5Chem is accessible through https://yzhang.hpc.nyu.edu/T5Chem.


# Citation
```
@article {20220310_lu_j_and_zhang_y,
  author       = { Jieyu Lu and Yingkai Zhang },
  title        = { Unified Deep Learning Model for Multitask Reaction Predictions with Explanation },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2022 },
  note         = { PMID: 35266390 },
  pages        = { 1376-1387 },
  volume       = { 62 },
  number       = { 6 },
  doi          = { 10.1021/acs.jcim.1c01467 },
  url          = { https://doi.org/10.1021/acs.jcim.1c01467 },
  eprint       = { https://doi.org/10.1021/acs.jcim.1c01467 }
}
```
