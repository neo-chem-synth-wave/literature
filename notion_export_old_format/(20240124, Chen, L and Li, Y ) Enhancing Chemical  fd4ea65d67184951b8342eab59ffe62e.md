# (20240124, Chen, L. and Li, Y.) Enhancing Chemical Synthesis: A Two-stage Deep Neural Network for Predicting Feasible Reaction Conditions

Tags: chemical-data, off-topic

## Publication Overview

| **Title:**  | Enhancing Chemical Synthesis: A Two-stage Deep Neural Network for Predicting
Feasible Reaction Conditions |
| --- | --- |
| **Authors:**  | Lung-Yi Chen, Yi-Pei Li |
| Publication Date**:**  | 2024/01/24 |
| Publication Links: | [**BMC Journal of Chemoinformatics**](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-024-00805-4) |
| Alternative Links: | [**ResearchGate**](https://www.researchgate.net/publication/377662292_Enhancing_chemical_synthesis_a_two-stage_deep_neural_network_for_predicting_feasible_reaction_conditions) |
| Code Links: | [**Official GitHub Repository**](https://github.com/Lung-Yi/rxn_yield_context) |

## Publication Abstract

<aside>
ℹ️ In the field of chemical synthesis planning, the accurate recommendation of reaction conditions is essential for achieving successful outcomes. This work introduces an innovative deep learning approach designed to address the complex task of predicting appropriate reagents, solvents, and reaction temperatures for chemical reactions. Our proposed methodology combines a multi-label classification model with a ranking model to offer tailored reaction condition recommendations based on relevance scores derived from anticipated product yields. To tackle the challenge of limited data for unfavorable reaction contexts, we employed the technique of hard negative sampling to generate reaction conditions that might be mistakenly classified as suitable, forcing the model to refine its decision boundaries, especially in challenging cases. Our developed model excels in proposing conditions where an exact match to the recorded solvents and reagents is found within the top-10 predictions 73% of the time. It also predicts temperatures within ± 20 of the recorded temperature in 89% of test cases. Notably, the model demonstrates its capacity to recommend multiple viable reaction conditions, with accuracy varying based on the availability of condition records associated with each reaction. What sets this model apart is its ability to suggest alternative reaction conditions beyond the constraints of the dataset. This underscores its potential to inspire innovative approaches in chemical research, presenting a compelling opportunity for advancing chemical synthesis planning and elevating the field of reaction engineering. Scientific contribution: The combination of multi-label classification and ranking models provides tailored recommendations for reaction conditions based on the reaction yields. A novel approach is presented to address the issue of data scarcity in negative reaction conditions through data augmentation.

</aside>