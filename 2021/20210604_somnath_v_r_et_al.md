# Overview
**Title:**
Learning Graph Models for Retrosynthesis Prediction

**Authors:**
Somnath, V.R., Bunne, C., Coley, C.W., Krause, A., and Barzilay, R.

**Publication Date:**
2021/06/04

**Publication Link:**
[arXiv](https://arxiv.org/abs/2006.07038)

**Alternative Publication Links:**
[NeurIPS](https://proceedings.neurips.cc/paper/2021/hash/4e2a6330465c8ffcaa696a5a16639176-Abstract.html) |
[Official GitHub Repository](https://github.com/vsomnath/graphretro)


# Abstract
Retrosynthesis prediction is a fundamental problem in organic synthesis, where the task is to identify precursor molecules that can be used to synthesize a target molecule. 
A key consideration in building neural models for this task is aligning model design with strategies adopted by chemists. 
Building on this viewpoint, this paper introduces a graph-based approach that capitalizes on the idea that the graph topology of precursor molecules is largely unaltered during a chemical reaction. 
The model first predicts the set of graph edits transforming the target into incomplete molecules called synthons. 
Next, the model learns to expand synthons into complete molecules by attaching relevant leaving groups. 
This decomposition simplifies the architecture, making its predictions more interpretable, and also amenable to manual correction. 
Our model achieves a top-1 accuracy of 53.7%, outperforming previous template-free and semi-template-based methods.


# Citation
```
@inproceedings {somnath2021,
  author       = { Vignesh Ram Somnath and Charlotte Bunne and Connor Coley and Andreas Krause and Regina Barzilay },
  title        = { Learning Graph Models for Retrosynthesis Prediction },
  booktitle    = { Advances in Neural Information Processing Systems },
  year         = { 2021 },
  volume       = { 34 },
  pages        = { 9405--9415 },
  publisher    = { Curran Associates, Inc. },
  editor       = { M. Ranzato and A. Beygelzimer and Y. Dauphin and P.S. Liang and J. Wortman Vaughan },
  url          = { https://proceedings.neurips.cc/paper_files/paper/2021/file/4e2a6330465c8ffcaa696a5a16639176-Paper.pdf }
}
```
