# (20191021, Chen, B. et al.) Learning to Make Generalizable and Diverse Predictions for Retrosynthesis

Tags: single-step-retrosynthesis, template-free

## Publication Overview

| **Title:**  | Learning to Make Generalizable and Diverse Predictions for Retrosynthesis |
| --- | --- |
| **Authors:**  | Benson Chen, Tianxiao Shen, Tommi S. Jaakkola, Regina Barzilay |
| Publication Date**:**  | 2019/10/21 |
| Publication Links: | [**arXiv**](https://arxiv.org/abs/1910.09688) |
| Alternative Links: | [**OpenReview**](https://openreview.net/forum?id=BygfrANKvB) |
| Code Links: | [**Official GitHub Repository](https://github.com/iclr-2020-retro/retro_smiles_transformer)**  |

## Publication Abstract

<aside>
ℹ️ We propose a new model for making generalizable and diverse retrosynthetic reaction predictions. Given a target compound, the task is to predict the likely chemical reactants to produce the target. This generative task can be framed as a sequence-to-sequence problem by using the SMILES representations of the molecules. Building on top of the popular Transformer architecture, we propose two novel pre-training methods that construct relevant auxiliary tasks (plausible reactions) for our problem. Furthermore, we incorporate a discrete latent variable model into the architecture to encourage the model to produce a diverse set of alternative predictions. On the 50k subset of reaction examples from the United States patent literature (USPTO-50k) benchmark dataset, our model greatly improves performance over the baseline, while also generating predictions that are more diverse.

</aside>

## Remarks and Comments

<aside>
💬 *Written on **2022/07/18** by **Haris Hasić**.*
****
This paper has been rejected from **ICLR 2020**, and it seems that the authors did not officially publish it anywhere else.

</aside>