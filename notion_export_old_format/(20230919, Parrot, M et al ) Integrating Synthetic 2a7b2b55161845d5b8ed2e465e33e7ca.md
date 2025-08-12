# (20230919, Parrot, M. et al.) Integrating Synthetic Accessibility with AI-based Generative Drug Design

Tags: enhancement, synthetic-accessibility

## Publication Overview

| **Title:**  | Integrating Synthetic Accessibility with AI-based Generative Drug Design |
| --- | --- |
| **Authors:**  | Maud Parrot, Hamza Tajmouati, Vinicius B.R. da Silva, Brian R. Atwood, Robin Fourcade,
Yann Gaston-Mathé, Nicolas D. Huu, Quentin Perron |
| Publication Date**:**  | 2023/09/19 |
| Publication Links: | [**BMC Journal of Chemoinformatics**](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-023-00742-8) |
| Alternative Links: | [**ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/61c19ee67f367e034f5adb11) | [ResearchGate](https://www.researchgate.net/publication/357221238_Integrating_Synthetic_Accessibility_with_AI-based_Generative_Drug_Design)** |
| Code Links: | [**Official GitHub Repository**](https://github.com/iktos/generation-under-synthetic-constraint) |

## Publication Abstract

<aside>
ℹ️ Generative models are frequently used for de novo design in drug discovery projects to propose new molecules. However, the question of whether or not the generated molecules can be synthesized is not systematically taken into account during generation, even though being able to synthesize the generated molecules is a fundamental requirement for such methods to be useful in practice. Methods have been developed to estimate molecule “synthesizability”, but, so far, there is no consensus on whether or not a molecule is synthesizable. In this paper we introduce the Retro-Score (RScore), which computes a synthetic accessibility score of molecules by performing a full retrosynthetic analysis through our data-driven synthetic planning software Spaya, and its dedicated API: Spaya-API (https://spaya.ai). We start by comparing several synthetic accessibility scores to a binary “chemist score” as estimated by chemists on a bench of generated molecules, as a first experimental validation that the RScore is a reliable synthetic accessibility score. We then describe a pipeline to generate molecules that validate a list of targets while still being easy to synthesize. We further this idea by performing experiments comparing molecular generator outputs across a range of constraints and conditions. We show that the RScore can be learned by a Neural Network, which leads to a new score: RSPred. We demonstrate that using the RScore or RSPred as a constraint during molecular generation enables our molecular generators to produce more synthesizable solutions, with higher diversity. The open-source Python code containing all the scores and the experiments can be found on (https://github.com/iktos/generation-under-synthetic-constraint).

</aside>