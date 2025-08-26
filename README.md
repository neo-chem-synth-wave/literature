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
[![Static Badge](https://img.shields.io/badge/total-245-blue)](#timeline)
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
[![Static Badge](https://img.shields.io/badge/2018-11-orange)](#timeline)
[![Static Badge](https://img.shields.io/badge/2019-18-orange)](#timeline)
[![Static Badge](https://img.shields.io/badge/2020-23-yellow)](#timeline)
[![Static Badge](https://img.shields.io/badge/2021-29-yellow)](#timeline)
[![Static Badge](https://img.shields.io/badge/2022-33-green)](#timeline)
[![Static Badge](https://img.shields.io/badge/2023-32-green)](#timeline)
[![Static Badge](https://img.shields.io/badge/2024-33-green)](#timeline)
[![Static Badge](https://img.shields.io/badge/2025-30-green)](#timeline)

| Publication Date | Publication                                                                                                                                                                                                                     |                            Tags                             |
|:----------------:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------:|
|    2025/02/28    | [Phan, T. et al. SynTemp: Efficient Extraction of Graph-Based Reaction Rules From Large-Scale Reaction Databases](../literature/2025/20250228_phan_t_et_al.md)                                                                  |           reaction-template-extraction, syn-temp            |
|    2025/01/18    | [Zhao, P. et al. Single-Step Retrosynthesis Prediction via Multitask Graph Representation Learning](../literature/2025/20250118_zhao_p_et_al.md)                                                                                |           single-step-retrosynthesis, retro-mtgr            |
|    2025/01/30    | [Long, L. et al. Artificial Intelligence in Retrosynthesis Prediction and Its Applications in Medicinal Chemistry](../literature/2025/20250130_long_l_et_al.md)                                                                 |                         perspective                         |
|    2025/03/12    | [Bradshaw, J. et al. Challenging Reaction Prediction Models to Generalize to Novel Chemistry](../literature/2025/20250312_bradshaw_j_et_al.md)                                                                                  |             single-step-synthesis, benchmarking             |
|    2025/01/02    | [Zhang, X. et al. A Data-Driven Group Retrosynthesis Planning Model Inspired by Neurosymbolic Programming](../literature/2025/20250102_zhang_x_et_al.md)                                                                        |    single-step-retrosynthesis, multi-step-retrosynthesis    |
|    2025/03/28    | [Keto, A. et al. Improving Reaction Prediction Through Chemically Aware Transfer Learning](../literature/2025/20250328_keto_a_et_al.md)                                                                                         |            single-step-synthesis, template-based            |
|    2025/03/16    | [Kozlov, K.S. et al. Discovering Organic Reactions With a Machine-Learning-Powered Deciphering of Tera-Scale Mass Spectrometry Data](../literature/2025/20250316_kozlov_k_s_et_al.md)                                           |                    data-source, reaction                    |
|    2025/04/08    | [Shee, Y. et al. DirectMultiStep: Direct Route Generation for Multistep Retrosynthesis](../literature/2025/20250408_shee_y_et_al.md)                                                                                            | multi-step-retrosynthesis, template-free, direct-multi-step |
|    2025/04/11    | [Qiao, A. et al. Advancing Retrosynthesis With Retrieval-Augmented Graph Generation](../literature/2025/20250411_qiao_a_et_al.md)                                                                                               |       single-step-retrosynthesis, template-free, rarb       |
|    2025/05/01    | [Krzyzanowski, A. et al. Exploring BERT for Reaction Yield Prediction: Evaluating the Impact of Tokenization, Molecular Representation, and Pretraining Data Augmentation](../literature/2025/20250501_krzyzanowski_a_et_al.md) |           reaction-yield-prediction, synth-coder            |
|       ...        | [See All](/documentation/b_timeline.md)                                                                                                                                                                                         |                             ...                             |


## License Information
The contents of this repository are published under the [MIT](/LICENSE) license.
Please refer to the individual references for more details regarding the license information of external resources utilized within the repository.


## Contact
If you are interested in contributing to this research project by reporting bugs, suggesting improvements, or submitting feedback, feel free to do so using [GitHub Issues](https://github.com/neo-chem-synth-wave/literature/issues).
