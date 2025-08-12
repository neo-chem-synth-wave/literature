# (20201123, Mo, Y. et al.) Evaluating and Clustering Retrosynthesis Pathways with Learned Strategy

Tags: enhancement, synthesis-route-planning, template-based

## Publication Overview

| **Title:**  | Evaluating and Clustering Retrosynthesis Pathways with Learned Strategy |
| --- | --- |
| **Authors:**  | Yiming Mo, Yanfei Guan, Pritha Verma, Jiang Guo, Mike E. Fortunato, Zhaohong Lu,
Connor W. Coley, Klavs F. Jensen |
| Publication Date**:**  | 2020/11/23 |
| Publication Links: | [**RSC Chemical Science**](https://pubs.rsc.org/en/content/articlelanding/2021/sc/d0sc05078d) |
| Alternative Links: | [**ResearchGate**](https://www.researchgate.net/publication/347850498_Evaluating_and_clustering_retrosynthesis_pathways_with_learned_strategy) |
| Code Links: | [**Official GitHub Repository**](https://github.com/moyiming1/Retrosynthesis-pathway-ranking) |

## Publication Abstract

<aside>
ℹ️ With recent advances in the computer-aided synthesis planning (CASP) powered by data science and machine learning, modern CASP programs can rapidly identify thousands of potential pathways for a given target molecule. However, the lack of a holistic pathway evaluation mechanism makes it challenging to systematically prioritize strategic pathways except for using some simple heuristics. Herein, we introduce a data-driven approach to evaluate the relative strategic levels of retrosynthesis pathways using a dynamic tree-structured long short-term memory (tree-LSTM) model. We first curated a retrosynthesis pathway database, containing 238k patent-extracted pathways along with ∼55 M artificial pathways generated from an open-source CASP program, ASKCOS. The tree-LSTM model was trained to differentiate patent-extracted and artificial pathways with the same target molecule in order to learn the strategic relationship among single-step reactions within the patent-extracted pathways. The model achieved a top-1 ranking accuracy of 79.1% to recognize patent-extracted pathways. In addition, the trained tree-LSTM model learned to encode pathway-level information into a representative latent vector, which can facilitate clustering similar pathways to help illustrate strategically diverse pathways generated from CASP programs.

</aside>