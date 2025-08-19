# Overview
**Title:**
A Generative Model For Electron Paths

**Authors:**
Bradshaw, J., Kusner, M.J., Paige, B., Segler, M.H.S., and Hernández-Lobato, M.J. |
Bradshaw, J. et al.

**Publication Date:**
2018/12/21

**Link:**
[OpenReview](https://openreview.net/forum?id=r1x4BnCqKX)

**Alternative Links:**
[arXiv](https://arxiv.org/abs/1805.10970) |
[GitHub](https://arxiv.org/abs/1805.10970) |
[University of Cambridge Apollo Repository](https://www.repository.cam.ac.uk/items/c0d8b48a-5e44-43e5-9a03-487fcadea456)

**Starred:**
False

**Tags:**
data-source, reaction, uspto-lef


# Abstract
Chemical reactions can be described as the stepwise redistribution of electrons in molecules.
As such, reactions are often depicted using "arrow-pushing" diagrams which show this movement as a sequence of arrows.
We propose an electron path prediction model (ELECTRO) to learn these sequences directly from raw reaction data.
Instead of predicting product molecules directly from reactant molecules in one shot, learning a model of electron movement has the benefits of (a) being easy for chemists to interpret, (b) incorporating constraints of chemistry, such as balanced atom counts before and after the reaction, and (c) naturally encoding the sparsity of chemical reactions, which usually involve changes in only a small number of atoms in the reactants.
We design a method to extract approximate reaction paths from any dataset of atom-mapped reaction SMILES strings.
Our model achieves excellent performance on an important subset of the USPTO reaction dataset, comparing favorably to the strongest baselines.
Furthermore, we show that our model recovers a basic knowledge of chemistry without being explicitly trained to do so.


# Citation
```
@inproceedings {bradshaw2018a,
  author       = { John Bradshaw and Matt J. Kusner and Brooks Paige and Marwin H. S. Segler and José Miguel Hernández-Lobato },
  title        = { A Generative Model For Electron Paths },
  booktitle    = { International Conference on Learning Representations },
  year         = { 2019 },
  url          = { https://openreview.net/forum?id=r1x4BnCqKX }
}
```
