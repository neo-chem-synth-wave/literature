# Overview
**Title:**
Learning to Make Generalizable and Diverse Predictions for Retrosynthesis

**Authors:**
Chen, B., Shen, T., Jaakkola, T.S., and Barzilay, R.

**Publication Date:**
2019/10/21

**Publication Link:**
[arXiv](https://arxiv.org/abs/1910.09688)

**Alternative Publication Links:**
[OpenReview](https://openreview.net/forum?id=BygfrANKvB) |
[Official GitHub Repository](https://github.com/iclr-2020-retro/retro_smiles_transformer)


# Abstract
We propose a new model for making generalizable and diverse retrosynthetic reaction predictions. 
Given a target compound, the task is to predict the likely chemical reactants to produce the target. 
This generative task can be framed as a sequence-to-sequence problem by using the SMILES representations of the molecules. 
Building on top of the popular Transformer architecture, we propose two novel pre-training methods that construct relevant auxiliary tasks (plausible reactions) for our problem. 
Furthermore, we incorporate a discrete latent variable model into the architecture to encourage the model to produce a diverse set of alternative predictions. 
On the 50k subset of reaction examples from the United States patent literature (USPTO-50k) benchmark dataset, our model greatly improves performance over the baseline, while also generating predictions that are more diverse.


# Citation
```
@misc{chen2019,
    title = "Learning to Make Generalizable and Diverse Predictions for Retrosynthesis", 
    author = "Benson Chen and Tianxiao Shen and Tommi S. Jaakkola and Regina Barzilay",
    year = "2019",
    eprint = "1910.09688",
    archivePrefix = "arXiv",
    primaryClass = "cs.LG",
    url = "https://arxiv.org/abs/1910.09688", 
}
```
