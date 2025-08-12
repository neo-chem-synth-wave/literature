# Overview
**Title:**
A Generative Model For Electron Paths

**Authors:**
Bradshaw, J., Kusner, M.J., Paige, B., Segler, M.H.S., and Hernández-Lobato, M.J.

**Publication Date:**
2019/03/20

**Publication Link:**
[arXiv](https://arxiv.org/abs/1805.10970)

**Alternative Publication Links:**
Copy the alternative publication links here using the | symbol as a delimiter.
This is important because a lot of official publications cannot be accessed for free, but the pre-prints or, in some cases, complete manuscripts can be found elsewhere online.
The best way of checking for alternative publication links is by Googling the exact title.
If there are no alternative links to be found, omit this section altogether.
Even if the official publication is open source, it is still useful to add two to three alternative publication links.
Please avoid any posting any illegal sources.
(_e.g._, `[arXiv](https://pubs.acs.org/journal/jcisd8)` | `[PubMed Central](https://pmc.ncbi.nlm.nih.gov)` | `[ResearchGate](https://researchgate.net)`)


# Abstract
Chemical reactions can be described as the stepwise redistribution of electrons in molecules. 
As such, reactions are often depicted using 'arrow-pushing' diagrams which show this movement as a sequence of arrows. 
We propose an electron path prediction model (ELECTRO) to learn these sequences directly from raw reaction data. 
Instead of predicting product molecules directly from reactant molecules in one shot, learning a model of electron movement has the benefits of (a) being easy for chemists to interpret, (b) incorporating constraints of chemistry, such as balanced atom counts before and after the reaction, and (c) naturally encoding the sparsity of chemical reactions, which usually involve changes in only a small number of atoms in the this http URL design a method to extract approximate reaction paths from any dataset of atom-mapped reaction SMILES strings. 
Our model achieves excellent performance on an important subset of the USPTO reaction dataset, comparing favorably to the strongest baselines. 
Furthermore, we show that our model recovers a basic knowledge of chemistry without being explicitly trained to do so.


# Citation
```
@misc{bradshaw2019,
title="A Generative Model For Electron Paths", 
author="John Bradshaw and Matt J. Kusner and Brooks Paige and Marwin H. S. Segler and José Miguel Hernández-Lobato",
year="2019",
eprint="1805.10970",
archivePrefix="arXiv",
primaryClass="physics.chem-ph",
url="https://arxiv.org/abs/1805.10970", 
}
```

