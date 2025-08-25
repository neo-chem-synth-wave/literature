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
The [generate_timeline_markdown](/scripts/generate_timeline_markdown.py) script can be utilized as follows:

```shell
python scripts/generate_timeline_markdown.py \
  --input_directory_path "../literature"
```

The [search_literature](/scripts/search_literature.py) script can be utilized as follows:

```shell
python scripts/search_literature.py \
  --input_directory_path "../literature" \
  --search_tags "single-step-retrosynthesis" "template-based"
```

All scripts are utilizing a base environment.


## Timeline
[![Static Badge](https://img.shields.io/badge/total-230-blue)](#timeline)
[![Static Badge](https://img.shields.io/badge/1966-1-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/1969-1-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/1977-1-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/1980-1-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/1993-1-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/1995-1-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2008-1-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2009-2-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2010-2-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2011-1-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2012-3-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2013-2-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2014-1-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2015-4-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2016-6-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2017-8-red)](#timeline)
[![Static Badge](https://img.shields.io/badge/2018-11-yellow)](#timeline)
[![Static Badge](https://img.shields.io/badge/2019-18-yellow)](#timeline)
[![Static Badge](https://img.shields.io/badge/2020-23-green)](#timeline)
[![Static Badge](https://img.shields.io/badge/2021-29-green)](#timeline)
[![Static Badge](https://img.shields.io/badge/2022-33-green)](#timeline)
[![Static Badge](https://img.shields.io/badge/2023-32-green)](#timeline)
[![Static Badge](https://img.shields.io/badge/2024-33-green)](#timeline)
[![Static Badge](https://img.shields.io/badge/2025-25-green)](#timeline)

|    Date    | Publication                                                                                                                                                                          |                                         Tags                                         |
|:----------:|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------:|
| 2025/08/11 | [Armstrong, D. et al. Tango*: Constrained Synthesis Planning Using Chemically Informed Value Functions](literature/2025/20250811_armstrong_d_et_al.md)                               |                   multi-step-retrosynthesis, template-free, tango*                   |
| 2025/07/31 | [Deng, Y. et al. RSGPT: A Generative Transformer Model for Retrosynthesis Planning Pre-trained on Ten Billion Datapoints](literature/2025/20250731_deng_y_et_al.md)                  |  single-step-retrosynthesis, multi-step-retrosynthesis, semi-template-based, rsgpt   |
| 2025/07/29 | [Wieczorek, E. et al. Transfer Learning for Heterocycle Retrosynthesis](literature/2025/20250729_wieczorek_e_et_al.md)                                                               |                              single-step-retrosynthesis                              |
| 2025/07/29 | [Hu, X. et al. log-RRIM: Yield Prediction via Local-to-Global Reaction Representation Learning and Interaction Modeling](literature/2025/20250729_hu_x_et_al.md)                     |                         reaction-yield-prediction, log-rrim                          |
| 2025/07/29 | [Current, S. et al. DiffER: Categorical Diffusion Ensembles for Single-Step Chemical Retrosynthesis](literature/2025/20250729_current_s_et_al.md)                                    |                    single-step-retrosynthesis, diffusion, differ                     |
| 2025/07/28 | [Liu, X. et al. Chemoenzymatic Synthesis Planning Guided by Synthetic Potential Scores](literature/2025/20250728_liu_x_et_al.md)                                                     |           single-step-retrosynthesis, multi-step-retrosynthesis, ace-retro           |
| 2025/07/14 | [Westerlund, A.M. et al. Highly Parallel Optimisation of Chemical Reactions Through Automation and Machine Intelligence](literature/2025/20250714_westerlund_a_m_et_al.md)           | single-step-retrosynthesis, multi-step-retrosynthesis, template-based, aizynthfinder |
| 2025/07/12 | [Sin, J.W. et al. Highly Parallel Optimisation of Chemical Reactions Through Automation and Machine Intelligence](literature/2025/20250712_sin_j_w_et_al.md)                         |                            reaction-optimization, minerva                            |
| 2025/07/02 | [Lan, Z. et al. Retrosynthesis Prediction via Search in (Hyper) Graph](literature/2025/20250702_lan_z_et_al.md)                                                                      |              single-step-retrosynthesis, semi-template-based, retro-sig              |
| 2025/06/25 | [Wu, J. et al. HiCLR: Knowledge-Induced Hierarchical Contrastive Learning With Retrosynthesis Prediction Yields a Reaction Foundation Model](literature/2025/20250625_wu_j_et_al.md) |                                    reaction-yield                                    |
|    ...     | [...](/documentation/b_timeline.md)                                                                                                                                                  |                                         ...                                          |


## License Information
The contents of this repository are published under the [MIT](/LICENSE) license.
Please refer to the individual references for more details regarding the license information of external resources utilized within the repository.


## Contact
If you are interested in contributing to this research project by reporting bugs, suggesting improvements, or submitting feedback, feel free to do so using [GitHub Issues](https://github.com/neo-chem-synth-wave/literature/issues).
