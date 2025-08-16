# Overview
**Title:**
RSGPT: A Generative Transformer Model for Retrosynthesis Planning Pre-trained on Ten Billion Datapoints

**Authors:**
Deng, Y., Zhao, X., Sun, H., Chen, Y., Wang, X., Xue, X., Li, L., Song, J., Hsieh, C., Hou, T., Pan, X., Alomar, T.S., Ji, X., and Wang, X.

**Publication Date:**
2025/07/31

**Publication Link:**
[Nature Communications](https://www.nature.com/articles/s41467-025-62308-6)

**Alternative Links:**
[GitHub](https://github.com/jogjogee/RSGPT) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC12314115) |
[ResearchGate](https://www.researchgate.net/publication/394173109_RSGPT_a_generative_transformer_model_for_retrosynthesis_planning_pre-trained_on_ten_billion_datapoints)

**Impact:**
False

**Tags:**
single-step-retrosynthesis, multi-step-retrosynthesis, semi-template-based, rsgpt


# Abstract
Retrosynthesis planning is a crucial task in organic synthesis, and deep-learning methods have enhanced and accelerated this process.
With the advancement of the emergence of large language models, the demand for data is rapidly increasing.
However, available retrosynthesis data are limited to only millions.
Therefore, we pioneer the utilization of the template-based algorithm to generate chemical reaction data, resulting in the production of over 10 billion reaction datapoints.
A generative pretrained transformer model is subsequently developed for template-free retrosynthesis planning by pre-training on 10 billion generated data.
Inspired by the strategies of large language models, we introduce reinforcement learning to capture the relationships among products, reactants, and templates more accurately.
Experiments demonstrate that our model achieves state-of-the-art performance on the benchmark, with a Top-1 accuracy of 63.4%, substantially outperforming previous models.


# Citation
```
@article {deng2025,
  author       = { Yafeng Deng and Xinda Zhao and Hanyu Sun and Yu Chen and Xiaorui Wang and Xi Xue and Liangning Li and Jianfei Song and Chang-Yu Hsieh and Tingjun Hou and Xiandao Pan and Taghrid Saad Alomar and Xiangyang Ji and Xiaojian Wang },
  title        = { RSGPT: a generative transformer model for retrosynthesis planning pre-trained on ten billion datapoints },
  journal      = { Nature Communications },
  year         = { 2025 },
  pages        = { 7012 },
  month        = { Jul },
  volume       = { 16 },
  number       = { 1 },
  day          = { 31 },
  issn         = { 2041-1723 },
  doi          = { 10.1038/s41467-025-62308-6 },
  url          = { https://doi.org/10.1038/s41467-025-62308-6 }
}
```
