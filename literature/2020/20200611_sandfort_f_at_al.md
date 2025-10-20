# Overview
**Title:**
A Structure-Based Platform for Predicting Chemical Reactivity

**Authors:**
Sandfort, F., Strieth-Kalthoff, F., Kühnemund, M., Beecks, C., and Glorius, F. |
Sandfort, F. et al.

**Publication Date:**
2020/06/11

**Link:**
[Cell Press Chem](https://www.cell.com/chem/fulltext/S2451-9294(20)30085-1)

**Alternative Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/60c7453a0f50db42ad396203) |
[Elsevier ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2451929420300851) |
[GitLab](https://zivgitlab.uni-muenster.de/m_kueh11/fp-dm-tool)

**Tags:**
single-step-synthesis, reaction-yield


# Abstract
The Bigger Picture

Statistical data-based prediction models have found widespread application in nearly all areas of science, including chemistry.
In this context, the prediction of molecular properties or biological activities for a target molecule (quantitative structure-property relationships [QSPRs]) has been widely investigated, with great focus on developing new and general molecular representations.
However, the underlying fundamentals have not been transferred to the prediction of chemical reactivity.
In contrast, although recent progress in high-throughput data generation has enabled the generation of uniform reaction-based datasets, current prediction models suggest that complex parameterization is required for each individual case to achieve good results.
Applying universal (structure-based) molecular representations to the prediction of chemical reactivity could provide a readily applicable model, which could potentially decrease the barriers to apply machine learning techniques in organic synthesis.

Highlights

- Quantitative modeling of reaction outcomes via machine learning.
- Prediction of properties, yields, stereoselectivities, and relative conversion.
- Multiple fingerprint features as a versatile and robust molecular representation.
- Readily applicable machine learning tool, directly starting from molecular structures.

Summary

Despite their enormous potential, machine learning methods have only found limited application in predicting reaction outcomes, because current models are often highly complex and, most importantly, are not transferable to different problem sets.
Here, we present a structure-based machine learning platform for diverse applications in organic chemistry.
Therefore, an input based on multiple fingerprint features (MFFs) as a versatile molecular representation was developed that was shown to be applicable over a range of diverse problem sets.
First, molecular properties across a diverse array of molecules could be predicted accurately.
Next, reaction outcomes such as stereoselectivities and yields were predicted for experimental datasets that were previously evaluated using (complex) problem-oriented descriptor models.
As a final application, a systematic high-throughput dataset was investigated as a "real-world problem," and good correlation was observed when using the structure-based model.


# Citation
```
@article {20200611_sandfort_f_at_al,
  author       = { Frederik Sandfort and Felix Strieth-Kalthoff and Marius Kühnemund and Christian Beecks and Frank Glorius },
  title        = { A Structure-Based Platform for Predicting Chemical Reactivity },
  journal      = { Chem },
  year         = { 2020 },
  pages        = { 1379-1390 },
  month        = { Jun },
  volume       = { 6 },
  number       = { 6 },
  day          = { 11 },
  publisher    = { Elsevier },
  issn         = { 2451-9294 },
  doi          = { 10.1016/j.chempr.2020.02.017 },
  url          = { https://doi.org/10.1016/j.chempr.2020.02.017 }
}
```
