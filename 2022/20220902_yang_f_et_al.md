# Overview
**Title:**
CNN-based Two-branch Multi-scale Feature Extraction Network for Retrosynthesis Prediction

**Authors:**
Yang, F., Liu, J., Zhang, Q., Yang, Z., and Zhang, X.

**Publication Date:**
2022/09/02

**Publication Link:**
[BMC Bioinformatics](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-022-04904-7)

**Alternative Publication Links:**
[ResearchGate](https://www.researchgate.net/publication/363245099_CNN-based_two-branch_multi-scale_feature_extraction_network_for_retrosynthesis_prediction)



# Abstract
***Background*** Retrosynthesis prediction is the task of deducing reactants from reaction products, which is of great importance for designing the synthesis routes of the target products. 
The product molecules are generally represented with some descriptors such as simplified molecular input line entry specification (SMILES) or molecular fingerprints in order to build the prediction models. 
However, most of the existing models utilize only one molecular descriptor and simply consider the molecular descriptors in a whole rather than further mining multi-scale features, which cannot fully and finely utilizes molecules and molecular descriptors features.

***Results*** We propose a novel model to address the above concerns. 
Firstly, we build a new convolutional neural network (CNN) based feature extraction network to extract multi-scale features from the molecular descriptors by utilizing several filters with different sizes. 
Then, we utilize a two-branch feature extraction layer to fusion the multi-scale features of several molecular descriptors to perform the retrosynthesis prediction without expert knowledge. 
The comparing result with other models on the benchmark USPTO-50k chemical dataset shows that our model surpasses the state-of-the-art model by 7.4%, 10.8%, 11.7% and 12.2% in terms of the top-1, top-3, top-5 and top-10 accuracies. 
Since there is no related work in the field of bioretrosynthesis prediction due to the fact that compounds in metabolic reactions are much more difficult to be featured than those in chemical reactions, we further test the feasibility of our model in task of bioretrosynthesis prediction by using the well-known MetaNetX metabolic dataset, and achieve top-1, top-3, top-5 and top-10 accuracies of 45.2%, 67.0%, 73.6% and 82.2%, respectively.

***Conclusion*** The comparison result on USPTO-50k indicates that our proposed model surpasses the existing state-of-the-art model. 
The evaluation result on MetaNetX dataset indicates that the models used for retrosynthesis prediction can also be used for bioretrosynthesis prediction.


# Citation
```
@article {yang2022,
  author       = { Feng Yang and Juan Liu and Qiang Zhang and Zhihui Yang and Xiaolei Zhang },
  title        = { {CNN-based} two-branch multi-scale feature extraction network for retrosynthesis prediction },
  journal      = { BMC Bioinformatics },
  year         = { 2022 },
  pages        = { 362 },
  month        = { sep },
  volume       = { 23 },
  number       = { 1 },
  publisher    = { Springer Science and Business Media LLC },
  copyright    = { https://creativecommons.org/licenses/by/4.0 },
}
```
