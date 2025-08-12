# (20230919, Yan, Y. et al.) RPBP: Deep Retrosynthesis Reaction Prediction Based on Byproducts

Tags: single-step-retrosynthesis, template-based

## Publication Overview

| **Title:**  | RPBP: Deep Retrosynthesis Reaction Prediction Based on Byproducts |
| --- | --- |
| **Authors:**  | Yingchao Yan, Yang Zhao, Huifeng Yao, Jie Feng, Li Liang, Weijie Han, Xiaohe Xu,
Chengtao Pu, Chengdong Zang, Lingfeng Chen, Yuanyuan Li, Haichun Liu, Tao Lu,
Yadong Chen, Yanmin Zhang |
| Publication Date**:**  | 2023/09/19 |
| Publication Links: | [**ACS JCIM**](https://pubs.acs.org/doi/10.1021/acs.jcim.3c00274) |
| Alternative Links: | **-** |
| Code Links: | [**Official GitHub Repository**](https://github.com/yyc776/RPBP) |

## Publication Abstract

<aside>
ℹ️ Retrosynthesis prediction is crucial in organic synthesis and drug discovery, aiding chemists in designing efficient synthetic routes for target molecules. Data-driven deep retrosynthesis prediction has gained importance due to new algorithms and enhanced computing power. Although existing models show certain predictive power on the USPTO-50K benchmark data set, no one considers the effects of byproducts during the prediction process, which may be due to the lack of byproduct information in the benchmark data set. Here, we propose a novel two-stage retrosynthesis reaction prediction framework based on byproducts called RPBP. First, RPBP predicts the byproduct involved in the reaction based on the product molecule. Then, it handles an end-to-end prediction problem based on the prediction of reactants by product and byproduct. Unlike other methods that first identify the potential reaction center and then predict reactant molecules, RPBP considers additional information from byproducts, such as reaction reagents, conditions, and sites. Interestingly, adding byproducts reduces model learning complexity in natural language processing (NLP). Our RPBP model achieves 54.7% and 66.6% top-1 retrosynthesis prediction accuracy when the reaction class is unknown and known, respectively. It outperforms existing methods for known-class reactions, thanks to the rich chemical information in byproducts. The prediction of four kinase drugs from the literature demonstrates the model’s practicality and potential to accelerate drug discovery.

</aside>