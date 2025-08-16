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
|    Date    | Publication                                                                                                                                                                                                                              |                                             Tags                                              | Impact |
|:----------:|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------:|:------:|
| 2008/03/07 | [Brenk, R. et al. Lessons Learnt From Assembling Screening Libraries for Drug Discovery for Neglected Diseases.](literature/2008/20080307_brenk_r_et_al.md)                                                                              |                                    `data-source`, `filter`                                    |        |
| 2009/02/06 | [Law, J. et al. Route Designer: A Retrosynthetic Analysis Tool Utilizing Automated Retrosynthetic Rule Generation.](literature/2009/20090206_law_j_et_al.md)                                                                             | `single-step-retrosynthesis`, `multi-step-retrosynthesis`, `template-based`, `route-designer` |        |
| 2009/06/10 | [Ertl, P. and Schuffenhauer, A. Estimation of Synthetic Accessibility Score of Drug-like Molecules based on Molecular Complexity and Fragment Contributions.](literature/2009/20090610_ertl_p_and_schuffenhauer_a.md)                    |                   `synthesizability`, `synthetic-accessibility`, `sa-score`                   | :star: |
| 2010/02/04 | [Baell, J.B. and Holloway, G.A. New Substructure Filters for Removal of Pan Assay Interference Compounds (PAINS) From Screening Libraries and for Their Exclusion in Bioassays.](literature/2010/20100204_baell_j_b_and_holloway_g_a.md) |                               `data-source`, `filter`, `pains`                                |        |
| 2010/04/28 | [Rogers, D. and Hahn, M. Extended-Connectivity Fingerprints.](literature/2010/20100428_rogers_d_hahn_m.md)                                                                                                                               |                       `compound-representation`, `fingerprint`, `ecfp`                        | :star: |
| 2012/06/04 | [Christ, C.D. et al. Mining Electronic Laboratory Notebooks: Analysis, Retrosynthesis, and Reaction Based Enumeration.](literature/2012/20120604_christ_c_d_et_al.md)                                                                    |           `reaction-extraction`, `reaction-classification`, `eln`, `retrosynthesis`           |        |
| 2012/10/09 | [Lowe, D.M. Extraction of Chemical Structures and Reactions from the Literature.](literature/2012/20121009_lowe_d_m.md)                                                                                                                  |   `reaction-extraction`, `text-mining`, `data-source`, `uspto-1976-2013`, `uspto-1976-2016`   | :star: |
| 2013/03/25 | [Carbonell, P. et al. Stereo Signature Molecular Descriptor.](literature/2013/20130325_carbonell_p_et_al.md)                                                                                                                             |                       `compound-descriptor`, `graph`, `stereochemistry`                       |        |
| 2013/10/08 | [Kraut, H. et al. Algorithm for Reaction Classification.](literature/2013/20131008_kraut_h_et_al.md)                                                                                                                                     |            `reaction-classification`, `maximum-common-substructure`, `data-source`            |        |
| 2014/12/26 | [Schneider, N. et al. Development of a Novel Fingerprint for Chemical Reactions and Its Application to Large-Scale Reaction Classification and Similarity.](literature/2014/20141226_schneider_n_et_al.md)                               |             `fingerprint`, `reaction-classification`, `data-source`, `uspto-50k`              | :star: |
| 2015/10/06 | [Schneider, N. et al. Get Your Atoms in Order - An Open-Source Implementation of a Novel and Robust Molecular Canonicalization Algorithm.](literature/2015/20151006_schneider_n_et_al.md)                                                |                             `compound-canonicalization`, `rdkit`                              | :star: |
| 2015/10/19 | [Sterling, T. and Irwin, J.J. ZINC 15 - Ligand Discovery for Everyone.](literature/2015/20151019_sterling_t_and_irwin_j_j.md)                                                                                                            |                                   `data-source`, `zinc-15`                                    | :star: |
| 2015/11/03 | [Duvenaud, D. et al. Convolutional Networks on Graphs for Learning Molecular Fingerprints.](literature/2015/20151207_duvenaud_d_et_al.md)                                                                                                |                         `compound-descriptor`, `graph`, `fingerprint`                         |        |
| 2017/04/18 | [Coley, C.W. et al. Prediction of Organic Reaction Outcomes using Machine Learning.](literature/2017/20170418_coley_c_w_et_al.md)                                                                                                        |             `single-step-synthesis`, `template-based`, `data-source`, `uspto-15k`             | :star: |
| 2017/11/16 | [Coley, C.W. et al. Computer-Assisted Retrosynthesis Based on Molecular Similarity.](literature/2017/20171116_coley_c_w_et_al.md)                                                                                                        |    `single-step-retrosynthesis`, `multi-step-retrosynthesis`, `template-based`, `retrosim`    | :star: |
| 2021/01/28 | [Schwaller, P. et al. Mapping the Space of Chemical Reactions Using Attention-Based Neural Networks.](literature/2021/20210128_schwaller_p_et_al.md)                                                                                     |       `reaction-classification`, `fingerprint`, `transformer`, `rxnfp`, `uspto-1k-tpl`        |        |
| 2021/02/03 | [Hasic, H. and Ishida, T. Single-Step Retrosynthesis Prediction Based on the Identification of Potential Disconnection Sites Using Molecular Substructure Fingerprints.](literature/2021/20210203_hasic_h_and_ishida_t.md)               |                      `single-step-retrosynthesis`, `semi-template-based`                      |        |
| 2021/04/07 | [Schwaller, P. et al. Extraction of Organic Chemistry Grammar From Unsupervised Learning of Chemical Reactions.](literature/2021/20210407_schwaller_p_et_al.md)                                                                          |                   `atom-to-atom-mapping`, `transformer-model`, `rxnmapper`                    |        |
| 2022/11/22 | [Kwon, Y. et al. Generative Modeling to Predict Multiple Suitable Conditions for Chemical Reactions.](literature/2022/20221122_kwon_y_et_al.md)                                                                                          |      `reaction-condition-prediction`, `variational-autoencoder`, `graph-neural-network`       |        |
| 2025/07/31 | [Deng, Y. et al. RSGPT: A Generative Transformer Model for Retrosynthesis Planning Pre-trained on Ten Billion Datapoints.](literature/2025/20250731_deng_y_et_al.md)                                                                     |   `single-step-retrosynthesis`, `multi-step-retrosynthesis`, `semi-template-based`, `rsgpt`   |        |


## License Information
The contents of this repository are published under the [MIT](/LICENSE) license.
Please refer to the individual references for more details regarding the license information of external resources utilized within the repository.


## Contact
If you are interested in contributing to this research project by reporting bugs, suggesting improvements, or submitting feedback, feel free to do so using [GitHub Issues](https://github.com/neo-chem-synth-wave/literature/issues).
