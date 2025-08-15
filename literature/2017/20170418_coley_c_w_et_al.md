# Overview
**Title:**
Prediction of Organic Reaction Outcomes using Machine Learning

**Authors:**
Coley, C.W., Barzilay, R., Jaakkola, T.S., Green, W.H., and Jensen, K.F.

**Publication Date:**
2017/04/18

**Publication Link:**
[ACS Central Science](https://pubs.acs.org/doi/10.1021/acscentsci.7b00064)

**Alternative Links:**
[DSpace@MIT](https://dspace.mit.edu/handle/1721.1/110706) |
[GitHub](https://github.com/connorcoley/ochem_predict_nn) |
[GitHub - USPTO (15k)](https://github.com/wengong-jin/nips17-rexgen) |
[PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5445544) |
[ResearchGate](https://www.researchgate.net/publication/316354788_Prediction_of_Organic_Reaction_Outcomes_Using_Machine_Learning)

**Tags:**
single-step-synthesis, template-based, data-source, uspto-15k


# Abstract
Computer assistance in synthesis design has existed for over 40 years, yet retrosynthesis planning software has struggled to achieve widespread adoption.
One critical challenge in developing high-quality pathway suggestions is that proposed reaction steps often fail when attempted in the laboratory, despite initially seeming viable.
The true measure of success for any synthesis program is whether the predicted outcome matches what is observed experimentally.
We report a model framework for anticipating reaction outcomes that combines the traditional use of reaction templates with the flexibility in pattern recognition afforded by neural networks.
Using 15,000 experimental reaction records from granted United States patents, a model is trained to select the major (recorded) product by ranking a self-generated list of candidates where one candidate is known to be the major product.
Candidate reactions are represented using a unique edit-based representation that emphasizes the fundamental transformation from reactants to products, rather than the constituent molecules' overall structures.
In a 5-fold cross-validation, the trained model assigns the major product rank 1 in 71.8% of cases, rank ≤3 in 86.7% of cases, and rank ≤5 in 90.8% of cases.


# Citation
```
@article {coley2017a,
  author       = { Connor W. Coley and Regina Barzilay and Tommi S. Jaakkola and William H. Green and Klavs F. Jensen },
  title        = { Prediction of Organic Reaction Outcomes Using Machine Learning },
  journal      = { ACS Central Science },
  year         = { 2017 },
  note         = { PMID: 28573205 },
  pages        = { 434-443 },
  volume       = { 3 },
  number       = { 5 },
  doi          = { 10.1021/acscentsci.7b00064 },
  url          = { https://doi.org/10.1021/acscentsci.7b00064 },
  eprint       = { https://doi.org/10.1021/acscentsci.7b00064 }
}
```
