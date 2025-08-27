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
[![Static Badge](https://img.shields.io/badge/total-255-blue)](#timeline)
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
[![Static Badge](https://img.shields.io/badge/2017-10-orange)](#timeline)
[![Static Badge](https://img.shields.io/badge/2018-11-orange)](#timeline)
[![Static Badge](https://img.shields.io/badge/2019-20-yellow)](#timeline)
[![Static Badge](https://img.shields.io/badge/2020-23-yellow)](#timeline)
[![Static Badge](https://img.shields.io/badge/2021-30-green)](#timeline)
[![Static Badge](https://img.shields.io/badge/2022-33-green)](#timeline)
[![Static Badge](https://img.shields.io/badge/2023-32-green)](#timeline)
[![Static Badge](https://img.shields.io/badge/2024-33-green)](#timeline)
[![Static Badge](https://img.shields.io/badge/2025-35-green)](#timeline)

| Publication Date | Publication                                                                                                                                                                         |                                   Tags                                   |
|:----------------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------:|
|    2025/01/18    | [Zhao, P. et al. Single-Step Retrosynthesis Prediction via Multitask Graph Representation Learning](/literature/2025/20250118_zhao_p_et_al.md)                                      |                  single-step-retrosynthesis, retro-mtgr                  |
|    2025/01/29    | [Mastrolorito, F. et al. fragSMILES as a Chemical String Notation for Advanced Fragment and Chirality Representation](/literature/2025/20250129_mastrolorito_f_et_al.md)            |                    compound-description, frag-smiles                     |
|    2025/01/30    | [Long, L. et al. Artificial Intelligence in Retrosynthesis Prediction and Its Applications in Medicinal Chemistry](/literature/2025/20250130_long_l_et_al.md)                       |                               perspective                                |
|    2025/01/02    | [Zhang, X. et al. A Data-Driven Group Retrosynthesis Planning Model Inspired by Neurosymbolic Programming](/literature/2025/20250102_zhang_x_et_al.md)                              |          single-step-retrosynthesis, multi-step-retrosynthesis           |
|    2025/01/31    | [Hartog, P.B.R. et al. Investigations into the Efficiency of Computer-Aided Synthesis Planning](/literature/2025/20250131_hartog_p_b_r_et_al.md)                                    |    single-step-retrosynthesis, multi-step-retrosynthesis, fast-retro     |
|    2025/02/28    | [Phan, T. et al. SynTemp: Efficient Extraction of Graph-Based Reaction Rules From Large-Scale Reaction Databases](/literature/2025/20250228_phan_t_et_al.md)                        |                  reaction-template-extraction, syn-temp                  |
|    2025/03/02    | [Yin, X. et al. Syn-MolOpt: A Synthesis Planning-Driven Molecular Optimization Method Using Data-Derived Functional Reaction Templates](/literature/2025/20250302_yin_x_et_al.md)   | single-step-synthesis, multi-step-synthesis, template-based, syn-mol-opt |
|    2025/03/12    | [Bradshaw, J. et al. Challenging Reaction Prediction Models to Generalize to Novel Chemistry](/literature/2025/20250312_bradshaw_j_et_al.md)                                        |                   single-step-synthesis, benchmarking                    |
|    2025/03/02    | [Gao, W. et al. Revealing the Relationship Between Publication Bias and Chemical Reactivity With Contrastive Learning](/literature/2025/20250302_gao_w_et_al.md)                    |                              data-analysis                               |
|    2025/03/16    | [Kozlov, K.S. et al. Discovering Organic Reactions With a Machine-Learning-Powered Deciphering of Tera-Scale Mass Spectrometry Data](/literature/2025/20250316_kozlov_k_s_et_al.md) |                          data-source, reaction                           |
|       ...        | [See All](/documentation/b_timeline.md)                                                                                                                                             |                                   ...                                    |


## License Information
The contents of this repository are published under the [MIT](/LICENSE) license.
Please refer to the individual references for more details regarding the license information of external resources utilized within the repository.


## Contact
If you are interested in contributing to this research project by reporting bugs, suggesting improvements, or submitting feedback, feel free to do so using [GitHub Issues](https://github.com/neo-chem-synth-wave/literature/issues).
