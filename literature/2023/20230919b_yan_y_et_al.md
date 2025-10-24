# Overview
**Title:**
RPBP: Deep Retrosynthesis Reaction Prediction Based on Byproducts

**Authors:**
Yan, Y., Zhao, Y., Yao, H., Feng, J., Liang, L., Han, W., Xu, X., Pu, C., Zang, C., Chen, L., Li, Y., Liu, H., Lu, T., Chen, Y., and Zhang, Y. |
Yan, Y. et al.

**Publication Date:**
2023/09/19

**Publication Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.3c00274)

**Alternative Links:**
[GitHub](https://github.com/yyc776/RPBP)

**Tags:**
single-step-retrosynthesis, template-free, rbpb


# Abstract
Retrosynthesis prediction is crucial in organic synthesis and drug discovery, aiding chemists in designing efficient synthetic routes for target molecules.
Data-driven deep retrosynthesis prediction has gained importance due to new algorithms and enhanced computing power.
Although existing models show certain predictive power on the USPTO-50K benchmark data set, no one considers the effects of byproducts during the prediction process, which may be due to the lack of byproduct information in the benchmark data set.
Here, we propose a novel two-stage retrosynthesis reaction prediction framework based on byproducts called RPBP.
First, RPBP predicts the byproduct involved in the reaction based on the product molecule.
Then, it handles an end-to-end prediction problem based on the prediction of reactants by product and byproduct.
Unlike other methods that first identify the potential reaction center and then predict reactant molecules, RPBP considers additional information from byproducts, such as reaction reagents, conditions, and sites.
Interestingly, adding byproducts reduces model learning complexity in natural language processing (NLP).
Our RPBP model achieves 54.7% and 66.6% top-1 retrosynthesis prediction accuracy when the reaction class is unknown and known, respectively.
It outperforms existing methods for known-class reactions, thanks to the rich chemical information in byproducts.
The prediction of four kinase drugs from the literature demonstrates the model's practicality and potential to accelerate drug discovery.


# Citation
```
@article {20230919b_yan_y_et_al,
  author       = { Yingchao Yan and Yang Zhao and Huifeng Yao and Jie Feng and Li Liang and Weijie Han and Xiaohe Xu and Chengtao Pu and Chengdong Zang and Lingfeng Chen and Yuanyuan Li and Haichun Liu and Tao Lu and Yadong Chen and Yanmin Zhang },
  title        = { RPBP: Deep Retrosynthesis Reaction Prediction Based on Byproducts },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2023 },
  note         = { PMID: 37724339 },
  pages        = { 5956-5970 },
  volume       = { 63 },
  number       = { 19 },
  doi          = { 10.1021/acs.jcim.3c00274 },
  url          = { https://doi.org/10.1021/acs.jcim.3c00274 },
  eprint       = { https://doi.org/10.1021/acs.jcim.3c00274 }
}
```
