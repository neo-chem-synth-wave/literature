# Overview
**Title:**
Models Matter: The Impact of Single-Step Retrosynthesis on Synthesis Planning

**Authors:**
Torren-Peraire, P., and Hassen, A.K., Genheden, S., Verhoeven, J., Clevert, D., Preuss, M., and Tetko, I.V. |
Torren-Peraire, P. et al.

**Publication Date:**
2024/02/14

**Link:**
[RSC Digital Discovery](https://pubs.rsc.org/en/content/articlelanding/2024/dd/d3dd00252g)

**Alternative Links:**
[GitHub](https://github.com/AlanHassen/modelsmatter) |
[ResearchGate](https://www.researchgate.net/publication/378228992_Models_Matter_The_Impact_of_Single-Step_Retrosynthesis_on_Synthesis_Planning)

**Tags:**
single-step-retrosynthesis, multi-step-retrosynthesis, evaluation


# Abstract
Retrosynthesis consists of breaking down a chemical compound recursively step-by-step into molecular precursors until a set of commercially available molecules is found with the goal to provide a synthesis route.
Its two primary research directions, single-step retrosynthesis prediction, which models the chemical reaction logic, and multi-step synthesis planning, which tries to find the correct sequence of reactions, are inherently intertwined.
Still, this connection is not reflected in contemporary research.
In this work, we combine these two major research directions by applying multiple single-step retrosynthesis models within multi-step synthesis planning and analyzing their impact using public and proprietary reaction data.
We find a disconnection between high single-step performance and potential route-finding success, suggesting that single-step models must be evaluated within synthesis planning in the future.
Furthermore, we show that the commonly used single-step retrosynthesis benchmark dataset USPTO-50k is insufficient as this evaluation task does not represent model scalability or performance on larger and more diverse datasets.
For multi-step synthesis planning, we show that the choice of the single-step model can improve the overall success rate of synthesis planning by up to +28% compared to the commonly used baseline model.
Finally, we show that each single-step model finds unique synthesis routes, and differs in aspects such as route-finding success, the number of found synthesis routes, and chemical validity.


# Citation
```
@article {20240214_torren_peraire_p_et_al,
  author       = { Paula Torren-Peraire and Alan Kai Hassen and Samuel Genheden and Jonas Verhoeven and Djork-Arné Clevert and Mike Preuss and Igor V. Tetko },
  title        = { Models Matter: the impact of single-step retrosynthesis on synthesis planning },
  journal      = { Digital Discovery },
  year         = { 2024 },
  pages        = { 558-572 },
  volume       = { 3 },
  issue        = { 3 },
  publisher    = { RSC },
  doi          = { 10.1039/D3DD00252G },
  url          = { https://dx.doi.org/10.1039/D3DD00252G }
}
```
