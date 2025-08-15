# Overview
**Title:**
Retrosynthesis Prediction with an Interpretable Deep Learning Framework based on Molecular Assembly Tasks

**Authors:**
Wang, Y., Pang, C., Wang, Y., Jin, J., Zhang, J., Zeng, X., Su, R., Zou, Q., and Wei, L.

**Publication Date:**
2023/10/03

**Publication Link:**
[Nature Communications](https://www.nature.com/articles/s41467-023-41698-5)

**Alternative Publication Links:**
[ResearchGate](https://www.researchgate.net/publication/374418524_Retrosynthesis_prediction_with_an_interpretable_deep-learning_framework_based_on_molecular_assembly_tasks) |
[Official GitHub Repository](https://github.com/wangyu-sd/RetroExplainer)


# Abstract
Automating retrosynthesis with artificial intelligence expedites organic chemistry research in digital laboratories. 
However, most existing deep-learning approaches are hard to explain, like a “black box” with few insights. 
Here, we propose RetroExplainer, formulizing the retrosynthesis task into a molecular assembly process, containing several retrosynthetic actions guided by deep learning. 
To guarantee a robust performance of our model, we propose three units: a multi-sense and multi-scale Graph Transformer, structure-aware contrastive learning, and dynamic adaptive multi-task learning. 
The results on 12 large-scale benchmark datasets demonstrate the effectiveness of RetroExplainer, which outperforms the state-of-the-art single-step retrosynthesis approaches. 
In addition, the molecular assembly process renders our model with good interpretability, allowing for transparent decision-making and quantitative attribution. 
When extended to multi-step retrosynthesis planning, RetroExplainer has identified 101 pathways, in which 86.9% of the single reactions correspond to those already reported in the literature. 
As a result, RetroExplainer is expected to offer valuable insights for reliable, high-throughput, and high-quality organic synthesis in drug development.


# Citation
```
@article {wang2023,
  author       = { Yu Wang and Chao Pang and Yuzhe Wang and Junru Jin and Jingjie Zhang and Xiangxiang Zeng and Ran Su and Quan Zou and Leyi Wei },
  title        = { Retrosynthesis prediction with an interpretable deep-learning framework based on molecular assembly tasks },
  journal      = { Nature Communications },
  year         = { 2023 },
  pages        = { 6155 },
  month        = { Oct },
  volume       = { 14 },
  number       = { 1 },
  day          = { 03 },
  issn         = { 2041-1723 },
  doi          = { 10.1038/s41467-023-41698-5 },
  url          = { https://doi.org/10.1038/s41467-023-41698-5 }
}
```
