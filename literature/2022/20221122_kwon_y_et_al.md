# Overview
**Title:**
Generative Modeling to Predict Multiple Suitable Conditions for Chemical Reactions

**Authors:**
Kwon, Y., Kim, S., Choi, Y., and Kang, S. |
Kwon, Y. et al.

**Publication Date:**
2022/11/22

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.2c01085)

**Alternative Links:**
[GitHub](https://github.com/seokhokang/reaction_condition_vae)

**Starred:**
False

**Tags:**
reaction-condition-determination


# Abstract
In synthesis planning, it is important to determine suitable reaction conditions such that a chemical reaction proceeds as intended.
Recent research attempts based on machine learning have proven to be effective in recommending reaction elements for specific categories regarding critical chemical context and operating conditions.
However, existing methods can only make a single prediction per reaction and do not directly provide a complete specification of the reaction elements as the prediction.
Therefore, their achievable performance is limited.
In this study, we propose a generative modeling approach to predict multiple different reaction conditions for a chemical reaction, each of which fully specifies critical reaction elements such that these elements can be directly used as a feasible reaction condition.
We formulate the problem of predicting reaction conditions as sampling from a generative distribution.
We model the distribution by introducing a variational autoencoder augmented with a graph neural network and learn it from a reaction dataset.
For a query reaction, multiple predictions can be obtained by repeated sampling from the distribution.
Through experimental investigation on the reaction datasets of four major types of cross-coupling reactions, we demonstrate that the proposed method significantly outperforms existing methods in retrieving ground-truth reaction conditions.


# Citation
```
@article {kwon2022a,
  author       = { Youngchun Kwon and Sun Kim and Youn-Suk Choi and Seokho Kang },
  title        = { Generative Modeling to Predict Multiple Suitable Conditions for Chemical Reactions },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2022 },
  note         = { PMID: 36413480 },
  pages        = { 5952-5960 },
  volume       = { 62 },
  number       = { 23 },
  doi          = { 10.1021/acs.jcim.2c01085 },
  url          = { https://doi.org/10.1021/acs.jcim.2c01085 },
  eprint       = { https://doi.org/10.1021/acs.jcim.2c01085 }
}
```
