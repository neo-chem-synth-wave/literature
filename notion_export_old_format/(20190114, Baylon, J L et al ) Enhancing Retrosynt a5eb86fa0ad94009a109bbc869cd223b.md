# (20190114, Baylon, J.L. et al.) Enhancing Retrosynthetic Reaction Prediction with Deep Learning using Multiscale Reaction Classification

Tags: enhancement, single-step-retrosynthesis, template-based

## Publication Overview

| **Title:**  | Enhancing Retrosynthetic Reaction Prediction with Deep Learning using Multiscale
Reaction Classification |
| --- | --- |
| **Authors:**  | Javier L. Baylon, Nicholas A. Cilfone, Jeffrey R. Gulcher, Thomas W. Chittenden |
| Publication Date**:**  | 2019/01/14 |
| Publication Links: | [**ACS JCIM**](https://pubs.acs.org/doi/10.1021/acs.jcim.8b00801) |
| Alternative Links: | - |
| Code Links: | - |

## Publication Abstract

<aside>
ℹ️ Chemical synthesis planning is a key aspect in many fields of chemistry, especially drug discovery. Recent implementations of machine learning and artificial intelligence techniques for retrosynthetic analysis have shown great potential to improve computational methods for synthesis planning. Herein, we present a multiscale, data-driven approach for retrosynthetic analysis with deep highway networks (DHN). We automatically extracted reaction rules (i.e., ways in which a molecule is produced) from a data set consisting of chemical reactions derived from U.S. patents. We performed the retrosynthetic reaction prediction task in two steps: first, we built a DHN model to predict which group of reactions (consisting of chemically similar reaction rules) was employed to produce a molecule. Once a reaction group was identified, a DHN trained on the subset of reactions within the identified reaction group, was employed to predict the transformation rule used to produce a molecule. To validate our approach, we predicted the first retrosynthetic reaction step for 40 approved drugs using our multiscale model and compared its predictive performance with a conventional model trained on all machine-extracted reaction rules employed as a control. Our multiscale approach showed a success rate of 82.9% at generating valid reactants from retrosynthetic reaction predictions. Comparatively, the control model trained on all machine-extracted reaction rules yielded a success rate of 58.5% on the validation set of 40 pharmaceutical molecules, indicating a significant statistical improvement with our approach to match known first synthetic reaction of the tested drugs in this study. While our multiscale approach was unable to outperform state-of-the-art rule-based systems curated by expert chemists, multiscale classification represents a marked enhancement in retrosynthetic analysis and can be easily adapted for use in a range of artificial intelligence strategies.

</aside>