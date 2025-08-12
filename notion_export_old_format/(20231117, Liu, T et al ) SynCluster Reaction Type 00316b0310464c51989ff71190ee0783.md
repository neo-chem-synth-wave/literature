# (20231117, Liu, T. et al.) SynCluster: Reaction Type Clustering and Recommendation Framework for Synthesis Planning

Tags: chemical-data, enhancement

## Publication Overview

| **Title:**  | SynCluster: Reaction Type Clustering and Recommendation Framework for Synthesis
Planning |
| --- | --- |
| **Authors:**  | Tiantao Liu, Zheng Cao, Yuansheng Huang, Yue Wan, Jian Wu, Chang-Yu Hsieh,
Tingjun Hou, Yu Kang |
| Publication Date**:**  | 2023/11/17 |
| Publication Links: | [**ACS JACS**](https://pubs.acs.org/doi/10.1021/jacsau.3c00607) |
| Alternative Links: | **-** |
| Code Links: | [**Official GitHub Repository**](https://github.com/Yoko1030/SynCluster) |

## Publication Abstract

<aside>
ℹ️ AI-assisted synthesis planning has emerged as a valuable tool in accelerating synthetic chemistry for the discovery of new drugs and materials. The template-free approach, which showcases superior generalization capabilities, is seen as the mainstream direction in this field. However, it remains unclear whether such an end-to-end approach can achieve problem-solving performance on par with experienced chemists without fully revealing insights into the chemical mechanisms involved. Moreover, there is a lack of unified and chemically inspired frameworks for improving multitask reaction predictions in this area. In this study, we have addressed these challenges by investigating the impact of fine-grained reaction-type labels on multiple downstream tasks and propose a novel framework named SynCluster. This framework incorporates unsupervised clustering cues into the baseline models and identifies plausible chemical subspaces which is compatible with multitask extensions and can serve as model-independent indicators to effectively enhance the performance of multiple downstream tasks. In retrosynthesis prediction, SynCluster achieves significant improvements of 4.1 and 11.0% in top-1 and top-10 prediction accuracy, respectively, compared to the baseline Molecular Transformer, and achieves a notable enhancement of 13.9% in top-10 accuracy when combined with Retroformer. By incorporating simplified molecular-input line-entry system augmentation, our framework achieves higher top-10 accuracy compared to state-of-the-art sequence-based retrosynthesis models and improves over the baseline on the diversity and validity of reactants. SynCluster also achieves 94.9% top-10 accuracy in forward synthesis prediction and 51.5% top-10 Maxfrag accuracy in reagent prediction. Overall, SynCluster provides a fresh perspective with chemical interpretability and reinforcement of domain knowledge in the synthesis design. It offers a promising solution for improving the accuracy and efficiency of AI-assisted synthesis planning and bridges the gap between template-free approaches and the problem-solving abilities of experienced chemists.

</aside>