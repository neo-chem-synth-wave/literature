# Overview
**Title:**
Biocatalysed Synthesis Planning using Data-driven Learning

**Authors:**
Probst, D., Manica, M., Teukam, Y.G.N., Castrogiovanni, A., Paratore, F., and Laino, T.	

**Publication Date:**
2022/02/18

**Publication Link:**
[Nature Communications](https://www.nature.com/articles/s41467-022-28536-w)

**Alternative Publication Links:**
[ResearchGate](https://www.researchgate.net/publication/358713206_Biocatalysed_synthesis_planning_using_data-driven_learning) |
[Official GitHub Repository](https://github.com/rxn4chemistry/biocatalysis-model)


# Abstract
Enzyme catalysts are an integral part of green chemistry strategies towards a more sustainable and resource-efficient chemical synthesis. 
However, the use of biocatalysed reactions in retrosynthetic planning clashes with the difficulties in predicting the enzymatic activity on unreported substrates and enzyme-specific stereo- and regioselectivity. 
As of now, only rule-based systems support retrosynthetic planning using biocatalysis, while initial data-driven approaches are limited to forward predictions. 
Here, we extend the data-driven forward reaction as well as retrosynthetic pathway prediction models based on the Molecular Transformer architecture to biocatalysis. 
The enzymatic knowledge is learned from an extensive data set of publicly available biochemical reactions with the aid of a new class token scheme based on the enzyme commission classification number, which captures catalysis patterns among different enzymes belonging to the same hierarchy. 
The forward reaction prediction model (top-1 accuracy of 49.6%), the retrosynthetic pathway (top-1 single-step round-trip accuracy of 39.6%) and the curated data set are made publicly available to facilitate the adoption of enzymatic catalysis in the design of greener chemistry processes.


# Citation
```
@article {probst2022,
  author       = { Daniel Probst and Matteo Manica and Yves Gaetan Nana Teukam and Alessandro Castrogiovanni and Federico Paratore and Laino Teodoro },
  title        = { Biocatalysed synthesis planning using data-driven learning },
  journal      = { Nat. Commun. },
  year         = { 2022 },
  pages        = { 964 },
  month        = { feb },
  volume       = { 13 },
  number       = { 1 },
  publisher    = { Springer Science and Business Media LLC },
  copyright    = { https://creativecommons.org/licenses/by/4.0 },
  language     = { en }
}
```
