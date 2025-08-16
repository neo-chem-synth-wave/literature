# Overview
**Title:**
Chemformer: A Pre-trained Transformer for Computational Chemistry

**Authors:**
Irwin, R., Dimitriadis, S., He, J., and Bjerrum, E.J.

**Publication Date:**
2022/01/31

**Publication Link:**
[IOP Science Machine Learning: Science and Technology](https://validate.perfdrive.com/fb803c746e9148689b3984a31fccd902/?ssa=63b5888b-9827-4de2-80a9-1dec9c08a769&ssb=27597288119&ssc=https%3A%2F%2Fiopscience.iop.org%2Farticle%2F10.1088%2F2632-2153%2Fac3ffb&ssi=5dca0433-cnvj-4227-90ea-77ca9a74883b&ssk=botmanager_support@radware.com&ssm=37057038649420255101952277635850&ssn=e8c675195b30cf488087498a56dab6f1603974349e5e-9dee-4e0b-a9db6a&sso=dcd69121-1601af328f87588c3e0381c7cf9bb80899cb670d0379b820&ssp=22180214251755236813175528401038626&ssq=61091157179414485138471794943747141370958&ssr=MTA5LjE3NS40OS4xMzE=&sst=Mozilla/5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/137.0.0.0%20Safari/537.36&ssu=&ssv=&ssw=&ssx=eyJyZCI6ImlvcC5vcmciLCJ1em14IjoiN2Y5MDAwNDc0NmRjN2UtNTRjNy00OWI2LWE1NzgtOTQ0MWY2OGZhMmJhMS0xNzU1MjcxNzk0ODIzMC0xNTk0NmU3YjFlMGM2ZTQ2MTAiLCJfX3V6bWYiOiI3ZjkwMDA3NDM0OWU1ZS05ZGVlLTRlMGItYTEyMS0xNjAxYWYzMjhmODcxLTE3NTUyNzE3OTQ4MjMwLTAwMGI5MmNhZDZiZjFiZGY1NzExMCJ9)

**Alternative Publication Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/60ee8a3eb95bdd06d062074b) |
[Official GitHub Repository](https://github.com/MolecularAI/Chemformer)


# Abstract
Transformer models coupled with a simplified molecular line entry system (SMILES) have recently proven to be a powerful combination for solving challenges in cheminformatics. 
These models, however, are often developed specifically for a single application and can be very resource-intensive to train. 
In this work we present the Chemformer model - a Transformer-based model which can be quickly applied to both sequence-to-sequence and discriminative cheminformatics tasks. 
Additionally, we show that self-supervised pre-training can improve performance and significantly speed up convergence on downstream tasks. 
On direct synthesis and retrosynthesis prediction benchmark datasets we publish state-of-the-art results for top-1 accuracy. 
We also improve on existing approaches for a molecular optimisation task and show that Chemformer can optimise on multiple discriminative tasks simultaneously. 
Models, datasets and code will be made available after publication.


# Citation
```
@article {irwin2022,
  author       = { Ross Irwin and Spyridon Dimitriadis and Jiazhen He and Esben Jannik Bjerrum },
  title        = { Chemformer: a pre-trained transformer for computational chemistry },
  journal      = { Machine Learning: Science and Technology },
  year         = { 2022 },
  pages        = { 015022 },
  month        = { jan },
  volume       = { 3 },
  number       = { 1 },
  doi          = { 10.1088/2632-2153/ac3ffb },
  url          = { https://dx.doi.org/10.1088/2632-2153/ac3ffb },
  publisher    = { IOP Publishing }
}
```
