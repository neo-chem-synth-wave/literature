# Overview
**Title:**
Do Chemformers Dream of Organic Matter? Evaluating a Transformer Model for Multistep Retrosynthesis

**Authors:**
Westerlund, A.M., Koki, S.M., Kancharla, S., Tibo, A., Saigiridharan, L., Kabeshov, M., Mercado, R., and Genheden, S. |
Westerlund, A.M. et al.

**Publication Date:**
2024/04/11

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.3c01685)

**Alternative Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/650c0ffced7d0eccc3f32d7f)

**Starred:**
False

**Tags:**
single-step-retrosynthesis, multi-step-retrosynthesis, template-free, chemformer


# Abstract
Synthesis planning of new pharmaceutical compounds is a well-known bottleneck in modern drug design.
Template-free methods, such as transformers, have recently been proposed as an alternative to template-based methods for single-step retrosynthetic predictions.
Here, we trained and evaluated a transformer model, called the Chemformer, for retrosynthesis predictions within drug discovery.
The proprietary data set used for training comprised ∼18 M reactions from literature, patents, and electronic lab notebooks.
Chemformer was evaluated for the purpose of both single-step and multistep retrosynthesis.
We found that the single-step performance of Chemformer was especially good on reaction classes common in drug discovery, with most reaction classes showing a top-10 round-trip accuracy above 0.97.
Moreover, Chemformer reached a higher round-trip accuracy compared to that of a template-based model.
By analyzing multistep retrosynthesis experiments, we observed that Chemformer found synthetic routes, leading to commercial starting materials for 95% of the target compounds, an increase of more than 20% compared to the template-based model on a proprietary compound data set.
In addition to this, we discovered that Chemformer suggested novel disconnections corresponding to reaction templates, which are not included in the template-based model.
These findings were further supported by a publicly available ChEMBL compound data set.
The conclusions drawn from this work allow for the design of a synthesis planning tool where template-based and template-free models work in harmony to optimize retrosynthetic recommendations.


# Citation
```
@article {westerlund2024a,
  author       = { Annie M. Westerlund and Siva Manohar Koki and Supriya Kancharla and Alessandro Tibo and Lakshidaa Saigiridharan and Mikhail Kabeshov and Rocío Mercado and Samuel Genheden },
  title        = { Do Chemformers Dream of Organic Matter? Evaluating a Transformer Model for Multistep Retrosynthesis },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2024 },
  note         = { PMID: 38602390 },
  pages        = { 3021-3033 },
  volume       = { 64 },
  number       = { 8 },
  doi          = { 10.1021/acs.jcim.3c01685 },
  url          = { https://doi.org/10.1021/acs.jcim.3c01685 },
  eprint       = { https://doi.org/10.1021/acs.jcim.3c01685 }
}
```
