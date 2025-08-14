# Overview
**Title:**
AiZynthFinder: A Fast, Robust and Flexible Open-source Software for Retrosynthetic Planning

**Authors:**
Genheden, S., Thakkar, A., Chadimová, V., Reymond, J.L., Engkvist, O., and Bjerrum, E.

**Publication Date:**
2020/11/17

**Publication Link:**
[BMC Journal of Cheminformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-020-00472-1)

**Alternative Publication Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/60c74c60bdbb891499a39777) |
[Official GitHub Repository](https://github.com/MolecularAI/aizynthfinder)


# Abstract
We present the open-source AiZynthFinder software that can be readily used in retrosynthetic planning. 
The algorithm is based on a Monte Carlo tree search that recursively breaks down a molecule to purchasable precursors. 
The tree search is guided by an artificial neural network policy that suggests possible precursors by utilizing a library of known reaction templates. 
The software is fast and can typically find a solution in less than 10 s and perform a complete search in less than 1 min. 
Moreover, the development of the code was guided by a range of software engineering principles such as automatic testing, system design and continuous integration leading to robust software with high maintainability. 
Finally, the software is well documented to make it suitable for beginners. The software is available at http://www.github.com/MolecularAI/aizynthfinder.


# Citation
```
@article {genheden2020,
  author       = { Samuel Genheden and Amol Thakkar and Veronika Chadimov{\'a} and Jean-Louis Reymond and Ola Engkvist and Esben Bjerrum },
  title        = { {AiZynthFinder}: a fast, robust and flexible open-source software for retrosynthetic planning },
  journal      = { J. Cheminform. },
  year         = { 2020 },
  pages        = { 70 },
  month        = { nov },
  volume       = { 12 },
  number       = { 1 },
  publisher    = { Springer Science and Business Media LLC },
  keywords     = { CASP; Monte Carlo tree-search; Neural network; Retrosynthesis;
               Retrosynthesis planning software },
  copyright    = { http://creativecommons.org/licenses/by/4.0/ },
  language     = { en }
}
```
