# Literature
[![Static Badge](https://img.shields.io/badge/Institute%20of%20Science%20Tokyo-%231C3177?style=flat)](https://www.isct.ac.jp)
[![Static Badge](https://img.shields.io/badge/Elix%2C%20Inc.-%235EB6B3?style=flat)](https://www.elix-inc.com)
[![Static Badge](https://img.shields.io/badge/Faculty%20of%20Electrical%20Engineering-%23275D91?style=flat)](https://www.etf.unsa.ba)

Welcome to the computer-assisted chemical synthesis **literature** research project !!!


## Utilization
The purpose of the [scripts](/scripts) directory is to illustrate how to search the available computer-assisted chemical synthesis literature.
The [search_literature](/scripts/search_literature.py) script can be utilized as follows:

```shell
# Get the available template-based single-step retrosynthesis literature.
python scripts/download_extract_and_format_data.py \
  --literature_directory_path "literature" \
  --search_tags "single-step-retrosynthesis" "template-based"
```


## Publication Timeline
|    Date    | Publication                                                                                                                                                                                                                |                                           Tags                                            | Impact |
|:----------:|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------:|:------:|
| 1993/02/01 | [Ugi, I. et al. Computer-assisted Solution of Chemical Problems - The Historical Development and the Present State of the Art of a New Discipline of Chemistry.](literature/1993/19930201_ugi_i_et_al.md)                  |                                    `review`, `history`                                    |        |
| 2009/06/10 | [Ertl, P. and Schuffenhauer, A. Estimation of Synthetic Accessibility Score of Drug-like Molecules based on Molecular Complexity and Fragment Contributions.](literature/2009/20090610_ertl_p_and_schuffenhauer_a.md)      |                              `synthesizability`, `sa-score`                               | :star: |
| 2012/10/09 | [Lowe, D.M. Extraction of Chemical Structures and Reactions from the Literature.](literature/2012/20121009_lowe_d_m.md)                                                                                                    |                    `data-source`, `uspto-1976-2013`, `uspto-1976-2016`                    | :star: |
| 2017/04/18 | [Coley, C.W. et al. Prediction of Organic Reaction Outcomes using Machine Learning.](literature/2017/20170418_coley_c_w_et_al.md)                                                                                          |           `single-step-synthesis`, `template-based`, `data-source`, `uspto-15k`           |        |
| 2017/11/16 | [Coley, C.W. et al. Computer-assisted Retrosynthesis based on Molecular Similarity.](literature/2017/20171116_coley_c_w_et_al.md)                                                                                          |  `single-step-retrosynthesis`, `multi-step-retrosynthesis`, `template-based`, `retrosim`  | :star: |
| 2021/01/28 | [Schwaller, P. et al. Mapping the Space of Chemical Reactions using Attention-based Neural Networks.](literature/2021/20210128_schwaller_p_et_al.md)                                                                       |     `reaction-classification`, `fingerprint`, `transformer`, `rxnfp`, `uspto-1k-tpl`      |        |
| 2021/02/03 | [Hasic, H. and Ishida, T. Single-step Retrosynthesis Prediction based on the Identification of Potential Disconnection Sites using Molecular Substructure Fingerprints.](literature/2021/20210203_hasic_h_and_ishida_t.md) |                    `single-step-retrosynthesis`, `semi-template-based`                    |        |
| 2021/04/07 | [Schwaller, P. et al. Extraction of Organic Chemistry Grammar from Unsupervised Learning of Chemical Reactions.](literature/2021/20210407_schwaller_p_et_al.md)                                                            |                 `atom-to-atom-mapping`, `transformer-model`, `rxnmapper`                  |        |
| 2022/11/22 | [Kwon, Y. et al. Generative Modeling to Predict Multiple Suitable Conditions for Chemical Reactions.](literature/2022/20221122_kwon_y_et_al.md)                                                                            |    `reaction-condition-prediction`, `variational-autoencoder`, `graph-neural-network`     |        |
| 2025/07/31 | [Deng, Y. et al. RSGPT: A Generative Transformer Model for Retrosynthesis Planning Pre-trained on Ten Billion Datapoints.](literature/2025/20250731_deng_y_et_al.md)                                                       | `single-step-retrosynthesis`, `multi-step-retrosynthesis`, `semi-template-based`, `rsgpt` |        |


## License Information
The contents of this repository are published under the [MIT](/LICENSE) license.
Please refer to the individual references for more details regarding the license information of external resources utilized within the repository.


## Contact
If you are interested in contributing to this research project by reporting bugs, suggesting improvements, or submitting feedback, feel free to do so using [GitHub Issues](https://github.com/neo-chem-synth-wave/literature/issues).
