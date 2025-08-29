# Literature
[![Static Badge](https://img.shields.io/badge/Institute%20of%20Science%20Tokyo-%231C3177?style=flat)](https://www.isct.ac.jp)
[![Static Badge](https://img.shields.io/badge/Elix%2C%20Inc.-%235EB6B3?style=flat)](https://www.elix-inc.com)
[![Static Badge](https://img.shields.io/badge/Faculty%20of%20Electrical%20Engineering%2C%20University%20of%20Sarajevo-%23275D91?style=flat)](https://www.etf.unsa.ba)

Welcome to the computer-assisted chemical synthesis **literature** research project !!!

Over the past decade, computer-assisted chemical synthesis has re-emerged as a prominent research subject.
Even though the idea of utilizing computers to assist chemical synthesis has existed for nearly as long as computers themselves, the inherent complexity repeatedly exceeded the available resources.
However, recent machine learning approaches have exhibited the potential to break this tendency.
While learning about such approaches may seem daunting at first, access to a concise and up-to-date overview of the state-of-the-art literature is the consensus foundation for furthering understanding and expertise, especially for novice researchers.
Consequently, the primary objective of the Literature research project is to systematically curate and facilitate access to relevant computer-assisted chemical synthesis literature.


## Utilization
The purpose of the [scripts](/scripts) directory is to illustrate how to utilize the available computer-assisted chemical synthesis literature.
The [generate_markdown_content](/scripts/generate_markdown_content.py) script can be utilized as follows:

```shell
python scripts/generate_markdown_content.py \
  --input_directory_path "../literature" \
  --markdown_content "timeline"
```

The [search_literature](/scripts/search_literature.py) script can be utilized as follows:

```shell
python scripts/search_literature.py \
  --input_directory_path "../literature" \
  --search_tags "single-step-retrosynthesis" "template-based"
```

All scripts are utilizing a base environment.


## Timeline
[![Static Badge](https://img.shields.io/badge/total-280-white)](#timeline)
[![Static Badge](https://img.shields.io/badge/1966-1-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/1969-1-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/1977-1-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/1980-1-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/1993-1-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/1995-1-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2007-2-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2008-2-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2009-2-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2010-3-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2011-3-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2012-4-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2013-3-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2014-1-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2015-4-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2016-7-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2017-11-orange)](#timeline)
[![Static Badge](https://img.shields.io/badge/2018-11-orange)](#timeline)
[![Static Badge](https://img.shields.io/badge/2019-20-yellow)](#timeline)
[![Static Badge](https://img.shields.io/badge/2020-23-yellow)](#timeline)
[![Static Badge](https://img.shields.io/badge/2021-31-green)](#timeline)
[![Static Badge](https://img.shields.io/badge/2022-34-green)](#timeline)
[![Static Badge](https://img.shields.io/badge/2023-32-green)](#timeline)
[![Static Badge](https://img.shields.io/badge/2024-40-blue)](#timeline)
[![Static Badge](https://img.shields.io/badge/2025-41-blue)](#timeline)

| Publication Date | Publication                                                                                                                                                                                                   |                                       Tags                                        |
|:----------------:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------:|
|    2025/08/26    | [Mastrolorito, F. et al. Enhancing Deep Chemical Reaction Prediction With Advanced Chirality and Fragment Representation](/literature/2025/20250826_mastrolorito_f_et_al.md)                                  |                   single-step-synthesis, frag-smiles4reactions                    |
|    2025/08/21    | [Genheden, S. and Howell, G.P. Measuring the Efficiency of Synthetic Routes and Transformations Using Vectors Derived From Similarity and Complexity](/literature/2025/20250821_genheden_s_and_howell_g_p.md) |                      multi-step-retrosynthesis, optimization                      |
|    2025/08/20    | [Joung, J.F. et al. Electron Flow Matching for Generative Reaction Mechanism Prediction](/literature/2025/20250820_joung_j_f_et_al.md)                                                                        |                            reaction-mechanism, flower                             |
|    2025/08/19    | [Xu, L. et al. A Unified Pre-trained Deep Learning Framework for Cross-Task Reaction Performance Prediction and Synthesis Planning](/literature/2025/20250819_xu_l_et_al.md)                                  |      single-step-retrosynthesis, multi-step-retrosynthesis, rxn-graphformer       |
|    2025/08/19    | [Sagawa, T. and Kojima, R. ReactionT5: A Pre-trained Transformer Model for Accurate Chemical Reaction Prediction With Limited Data](/literature/2025/20250819_sagawa_t_and_kojima_r.md)                       |  single-step-synthesis, single-step-retrosynthesis, reaction-yield, reaction-t5   |
|    2025/08/14    | [Xue, X. et al. Bidirectional Chemical Intelligent Net: A Unified Deep Learning–Based Framework for Predicting Chemical Reaction](/literature/2025/20250814_xue_x_et_al.md)                                   |    single-step-synthesis, single-step-retrosynthesis, template-free, bici-net     |
|    2025/08/11    | [Armstrong, D. et al. Tango*: Constrained Synthesis Planning Using Chemically Informed Value Functions](/literature/2025/20250811_armstrong_d_et_al.md)                                                       |                 multi-step-retrosynthesis, template-free, tango*                  |
|    2025/08/08    | [Cong, S. et al. Graph-Sequence Enhanced Transformer for Template-Free Prediction of Natural Product Biosynthesis](/literature/2025/20250808_ceng_s_et_al.md)                                                 |               single-step-retrosynthesis, template-free, gset-retro               |
|    2025/08/05    | [Zhu, L. et al. M2Echem: A Multilevel Dual Encoder-Based Model for Predicting Organic Chemistry Reactions](/literature/2025/20250805_zhu_l_et_al.md)                                                          |                  single-step-synthesis, template-free, m2e-chem                   |
|    2025/07/31    | [Deng, Y. et al. RSGPT: A Generative Transformer Model for Retrosynthesis Planning Pre-trained on Ten Billion Datapoints](/literature/2025/20250731_deng_y_et_al.md)                                          | single-step-retrosynthesis, multi-step-retrosynthesis, semi-template-based, rsgpt |
|       ...        | [See All](/documentation/b_timeline.md)                                                                                                                                                                       |                                        ...                                        |


## License Information
The contents of this repository are published under the [MIT](/LICENSE) license.
Please refer to the individual references for more details regarding the license information of external resources utilized within the repository.


## Contact
If you are interested in contributing to this research project by reporting bugs, suggesting improvements, or submitting feedback, feel free to do so using [GitHub Issues](https://github.com/neo-chem-synth-wave/literature/issues).
