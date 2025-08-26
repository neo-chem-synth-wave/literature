# Overview
**Title:**
SynCoTrain: A Dual Classifier PU-Learning Framework for Synthesizability Prediction

**Authors:**
Amariamir, S., George, J., and Benner, P. |
Amariamir, S. et al.

**Publication Date:**
2025/03/27

**Link:**
[RSC Digital Discovery](https://pubs.rsc.org/en/content/articlelanding/2025/dd/d4dd00394b)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/2411.12011) |
[GitHub](https://github.com/BAMeScience/SynCoTrainMP) |
[ResearchGate](https://www.researchgate.net/publication/390246824_SynCoTrain_a_dual_classifier_PU-learning_framework_for_synthesizability_prediction) |
[ResearchGate (Pre-print)](https://www.researchgate.net/publication/385944576_SynCoTrain_A_Dual_Classifier_PU-learning_Framework_for_Synthesizability_Prediction)

**Starred:**
False

**Tags:**
synthesizability, syn-co-train


# Abstract
Material discovery is a cornerstone of modern science, driving advancements in diverse disciplines from biomedical technology to climate solutions.
Predicting synthesizability, a critical factor in realizing novel materials, remains a complex challenge due to the limitations of traditional heuristics and thermodynamic proxies.
While stability metrics such as formation energy offer partial insights, they fail to account for kinetic factors and technological constraints that influence synthesis outcomes.
These challenges are further compounded by the scarcity of negative data, as failed synthesis attempts are often unpublished or context-specific.
We present SynCoTrain, a semi-supervised machine learning model designed to predict the synthesizability of materials.
SynCoTrain employs a co-training framework leveraging two complementary graph convolutional neural networks: SchNet and ALIGNN.
By iteratively exchanging predictions between classifiers, SynCoTrain mitigates model bias and enhances generalizability.
Our approach uses Positive and Unlabeled (PU) learning to address the absence of explicit negative data, iteratively refining predictions through collaborative learning.
The model demonstrates robust performance, achieving high recall on internal and leave-out test sets.
By focusing on oxide crystals, a well-characterized material family with extensive experimental data, we establish SynCoTrain as a reliable tool for predicting synthesizability while balancing dataset variability and computational efficiency.
This work highlights the potential of co-training to advance high-throughput materials discovery and generative research, offering a scalable solution to the challenge of synthesizability prediction.


# Citation
```
@article {amariamir2025a,
  author       = { Sasan Amariamir and Janine George and Philipp Benner },
  title        = { SynCoTrain: a dual classifier PU-learning framework for synthesizability prediction },
  journal      = { Digital Discovery },
  year         = { 2025 },
  pages        = { 1437-1448 },
  volume       = { 4 },
  issue        = { 6 },
  publisher    = { RSC },
  doi          = { 10.1039/D4DD00394B },
  url          = { https://dx.doi.org/10.1039/D4DD00394B }
}
```
