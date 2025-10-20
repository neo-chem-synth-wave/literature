# Overview
**Title:**
A Transformer Model for Retrosynthesis

**Authors:**
Karpov, P., Godin, G., and Tetko, I.V. |
Karpov, P. et al.

**Publication Date:**
2019/09/09

*Link:**
[Springer ICANN 2019](https://link.springer.com/chapter/10.1007/978-3-030-30493-5_78)

**Alternative Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/60c7417af96a00cd49286446) |
[ResearchGate](https://www.researchgate.net/publication/335731741_A_Transformer_Model_for_Retrosynthesis)

**Tags:**
single-step-retrosynthesis


# Abstract
We describe a Transformer model for a retrosynthetic reaction prediction task.
The model is trained on 45 033 experimental reaction examples extracted from USA patents.
It can successfully predict the reactants set for 42.7% of cases on the external test set.
During the training procedure, we applied different learning rate schedules and snapshot learning.
These techniques can prevent overfitting and thus can be a reason to get rid of internal validation dataset that is advantageous for deep models with millions of parameters.
We thoroughly investigated different approaches to train Transformer models and found that snapshot learning with averaging weights on learning rates minima works best.
While decoding the model output probabilities there is a strong influence of the temperature that improves at T = 1.3 the accuracy of models up to 1–2%.


# Citation
```
@inproceedings {20190909_karpov_p_et_al,
  author       = { Pavel Karpov and Guillaume Godin and Igor V. Tetko },
  title        = { A Transformer Model for Retrosynthesis },
  booktitle    = { Artificial Neural Networks and Machine Learning - ICANN 2019: Workshop and Special Sessions },
  year         = { 2019 },
  pages        = { 817-830 },
  address      = { Cham },
  publisher    = { Springer International Publishing },
  editor       = { Tetko, Igor V. and Kůrková, Věra and Karpov, Pavel and Theis, Fabian },
  isbn         = { 978-3-030-30493-5 }
}
```
